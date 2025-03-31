"""Main entry point for package."""

from .runner import Runner


def main():
    """here."""
    print("Hello there!")

    runner = Runner("cbbo.toml")
    runner.run()


if __name__ == "__main__":
    main()
