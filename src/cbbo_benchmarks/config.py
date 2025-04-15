"""Module for configuration functions."""

import inspect
import tomllib
from . import benchmarks


def get_config(path: str) -> dict:
    """Get benchmark configuration from TOML file."""

    with open(path, "rb") as f:
        config = tomllib.load(f)

    return config


def get_benchmark(config: dict) -> object:
    """Get benchmark class using configuration dictionary."""

    name = config["name"]

    # Get benchmark class associated with the name
    class_name = name + "Benchmark"
    bench_class = getattr(benchmarks, class_name)

    # Inspect class constructor and create dict of input arguments
    sig = inspect.signature(bench_class)
    kwargs = {k: config[k] for k in sig.parameters if k in config}

    # Init benchmark class using input args from config
    bench = bench_class(**kwargs)

    return bench
