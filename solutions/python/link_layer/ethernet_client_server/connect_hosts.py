import subprocess
from argparse import ArgumentParser
from utils import interface_exists


def main(host1: str, host2: str) -> None:
    # Check if both hosts exist
    existing_hosts = subprocess.run(
        ["ip", "netns"], capture_output=True, encoding="utf-8", check=True
    ).stdout

    for host in [host1, host2]:
        if host not in existing_hosts:
            print(f"Virtual host ({host}) does not exist")
    host1_id = host1[5:]
    host2_id = host2[5:]

    host1_host2_interface = f"veth_{host1_id}_{host2_id}"
    host2_host1_interface = f"veth_{host2_id}_{host1_id}"

    # Check if a connection already exists
    if interface_exists(host1_host2_interface) and interface_exists(
        host2_host1_interface
    ):
        print(f"A connection between {host1} and {host2} already exists")
        return

    # Create new connection
    create_connect_cmds = [
        f"ip link add {host1_host2_interface} type veth peer name {host1_host2_interface}",
        f"ip link set {host1_host2_interface} netns {host1}",
        f"ip link set {host2_host1_interface} netns {host2}",
        f"ip netns exec {host1} ip link set dev {host1_host2_interface} up",
        f"ip netns exec {host2} ip link set dev {host2_host1_interface} up",
    ]
    for cmd in create_connect_cmds:
        subprocess.run(cmd.split(), check=True)
    print(
        f"Connection established between {host1_host2_interface} on {host1} "
        f"and {host2_host1_interface} on {host2}"
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("host1")
    parser.add_argument("host2")
    args = parser.parse_args()
    main(args.host1, args.host2)
