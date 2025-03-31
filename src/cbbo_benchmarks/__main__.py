"""Main entry point for package."""

import argparse
from .runner import Runner
from .plotter import Plotter


def main():
    """here."""
    parser = argparse.ArgumentParser(description="C-BBO benchmarks tool")
    parser.add_argument("config", help="configuration file")
    parser.add_argument("-p", "--plot", action="store_true", help="plot benchmarks")

    args = parser.parse_args()

    if args.plot:
        print("Plot benchmark results")
        plotter = Plotter(args.config)
        plotter.plot()
    else:
        runner = Runner(args.config)
        runner.run()


if __name__ == "__main__":
    main()
