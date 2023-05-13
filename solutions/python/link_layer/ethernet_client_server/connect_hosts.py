import subprocess
from argparse import ArgumentParser
from utils import interface_exists, get_virtual_hosts, Host, get_connecting_interfaces


def main(host1: str, host2: str) -> None:
    # Check if both hosts exist
    existing_hosts = get_virtual_hosts()
    host1_cls = Host(name=host1)
    host2_cls = Host(name=host2)
    for host in [host1_cls, host2_cls]:
        if host not in existing_hosts:
            print(f"Virtual host ({host.name}) does not exist")

    interfaces = get_connecting_interfaces(host1_cls, host2_cls)

    # Check if a connection already exists
    if interface_exists(interfaces[host1_cls.id]) and interface_exists(
        interfaces[host2_cls.id]
    ):
        print(
            f"A connection between {host1_cls.name} and {host2_cls.name} already exists"
        )
        return

    # Create new connection
    create_connect_cmds = [
        f"ip link add {interfaces[host1_cls.id]} type veth peer name {interfaces[host2_cls.id]}",
        f"ip link set {interfaces[host1_cls.id]} netns {host1_cls.name}",
        f"ip link set {interfaces[host2_cls.id]} netns {host2_cls.name}",
        f"ip netns exec {host1_cls.name} ip link set dev {interfaces[host1_cls.id]} up",
        f"ip netns exec {host2_cls.name} ip link set dev {interfaces[host2_cls.id]} up",
    ]
    for cmd in create_connect_cmds:
        subprocess.run(cmd.split(), check=True)
    print(
        f"Connection established between {interfaces[host1_cls.id]} on {host1_cls.name} "
        f"and {interfaces[host2_cls.id]} on {host2_cls.name}"
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("host1")
    parser.add_argument("host2")
    args = parser.parse_args()
    main(args.host1, args.host2)
