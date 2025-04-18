"""Main module for the package."""

import argparse
from .runner import Runner
from .plotter import Plotter


def main():
    """Command line interface for package."""
    parser = argparse.ArgumentParser(description="C-BBO benchmarks tool")
    parser.add_argument("config", help="configuration file")
    parser.add_argument("-p", "--plot", action="store_true", help="plot benchmarks")

    args = parser.parse_args()

    if args.plot:
        plotter = Plotter(args.config)
        plotter.plot()
    else:
        runner = Runner(args.config)
        runner.run()


if __name__ == "__main__":
    main()
