"""Module to run CBBO benchmarks."""

import argparse
import importlib
import logging
import os
import pathlib
import uuid

import tomllib
from deephyper.evaluator import Evaluator
from deephyper.evaluator.callback import TqdmCallback


def get_attr_from_package(path):
    """Performs a relative import."""
    path = path.split(".")
    package = ".".join(path[:-1])
    name = path[-1]
    attr = importlib.import_module(name, package)
    return attr


def create_parser():
    """Creates the parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--config")
    return parser


class Runner:
    """Runner class to run cbbo benchmarks.

    Args:
        config_path (str): path to configuration TOML file.
    """

    def __init__(self, config_path: str):
        with open(config_path, "rb") as f:
            self.config = tomllib.load(f)
        self.root_path = os.getcwd()
        self.runs_path = os.path.join(self.root_path, "runs")
        pathlib.Path(self.runs_path).mkdir(parents=False, exist_ok=True)

    def create_evaluator(self, run_function, tqdm_label):  # noqa: D102
        config = self.config["evaluator"]

        evaluator = Evaluator.create(
            run_function,
            method=config["method"],
            method_kwargs={
                "num_workers": config["num_workers"],
                "callbacks": [TqdmCallback(tqdm_label)],
            },
        )
        return evaluator

    def run_search_replica(self, bench, max_evals, label, config):  # noqa: D102
        search_kwargs = config.get("kwargs", {})

        Search = getattr(
            importlib.import_module(config["package"]),
            config["name"],
        )

        evaluator = self.create_evaluator(bench.run_function, tqdm_label=label)

        log_dir = os.path.join(self.runs_path, label)
        pathlib.Path(log_dir).mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            filename=os.path.join(log_dir, "deephyper.log"),
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s - %(message)s",
            force=True,
        )

        search = Search(bench.problem, evaluator, log_dir=log_dir, **search_kwargs)
        search.search(max_evals)

    def run_search(self, bench, label, config):
        """Runs all replications of a search."""
        num_replications = self.config["search"]["num_replications"]
        max_evals = self.config["search"]["max_evals"]

        for i in range(num_replications):
            replica_id = str(uuid.uuid4())
            print(f"Starting replica {i + 1}/{num_replications}: {label}")
            self.run_search_replica(bench, max_evals, f"{label}/{replica_id}", config)

    def run_benchmark(self, label, config):
        """Runs a benchmark instance."""
        print(f"Starting benchmark: {label}")

        Benchmark = getattr(
            importlib.import_module(config["package"]),
            config["name"],
        )
        bench = Benchmark()

        for search_label, search_config in self.config["search"]["method"].items():
            self.run_search(bench, f"{label}/{search_label}", search_config)

    def run(self):
        """Runs everything."""
        print(f"Running: {self.config['title']}")

        for benchmark_label, benchmark_config in self.config["benchmark"].items():
            self.run_benchmark(benchmark_label, benchmark_config)
