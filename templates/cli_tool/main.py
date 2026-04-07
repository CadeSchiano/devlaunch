import argparse

def main():
    parser = argparse.ArgumentParser(description="My CLI Tool")

    parser.add_argument("name", help="Name to greet")
    parser.add_argument("--uppercase", action="store_true", help="Uppercase output")

    args = parser.parse_args()

    message = f"Hello, {args.name}!"

    if args.uppercase:
        message = message.upper()

    print(message)


if __name__ == "__main__":
    main()