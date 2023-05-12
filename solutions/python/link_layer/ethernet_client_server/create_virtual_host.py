from utils import create_net_ns, get_virtual_hosts


def main() -> None:
    # Check for the last namespace created or if any has previously been created
    existing_ns = get_virtual_hosts()

    next_host_id = existing_ns[0].id + 1 if existing_ns else 1
    create_net_ns(f"vhost{next_host_id}")


if __name__ == "__main__":
    main()
