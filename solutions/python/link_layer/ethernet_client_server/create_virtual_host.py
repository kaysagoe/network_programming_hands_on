import re
import subprocess


def create_net_ns(name: str) -> None:
    subprocess.run(["ip", "netns", "add", name], check=True)
    subprocess.run(
        ["ip", "netns", "exec", name, "ip", "link", "set", "dev", "lo", "up"],
        check=True,
    )
    print(f"Virtual host ({name} created")


def main() -> None:
    # Check for the last namespace created or if any has previously been created
    existing_ns = sorted(
        subprocess.run(
            ["ip", "netns"], capture_output=True, encoding="utf-8"
        ).stdout.splitlines(),
        reverse=True,
    )
    last_created_host = None

    index = 0
    while not last_created_host and index < len(existing_ns):
        if re.match(r"^vhost\d+", existing_ns[index]):
            last_created_host = existing_ns[index]

    # Create namespace host(n+1)
    if last_created_host:
        last_created_host_id = int(last_created_host[5:])
        next_host_id = last_created_host_id + 1
    else:
        next_host_id = 1

    create_net_ns(f"vhost{next_host_id}")


if __name__ == "__main__":
    main()
