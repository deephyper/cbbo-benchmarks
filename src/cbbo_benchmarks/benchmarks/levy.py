"""Module for Levy benchmark.

Description of the function: https://www.sfu.ca/~ssurjano/levy.html
"""

import functools
import numpy as np
from deephyper.hpo import HpProblem
from cbbo_benchmarks.benchmark import HPOBenchmark
from cbbo_benchmarks.scorer import HPOScorer
from cbbo_benchmarks.utils import run_func


def levy(x):
    """Levy benchmark function."""
    z = 1 + (x - 1) / 4
    y = (
        np.sin(np.pi * z[0]) ** 2
        + np.sum((z[:-1] - 1) ** 2 * (1 + 10 * np.sin(np.pi * z[:-1] + 1) ** 2))
        + (z[-1] - 1) ** 2 * (1 + np.sin(2 * np.pi * z[-1]) ** 2)
    )
    return -y


class LevyScorer(HPOScorer):
    """A class defining performance evaluators for the Levy problem."""

    def __init__(self, nparams: int = 5):
        self.nparams = nparams
        self.x_max = np.ones(self.nparams)
        self.y_max = 0.0


class LevyBenchmark(HPOBenchmark):
    """Levy benchmark."""

    def __init__(self, nparams=5):
        """Create a Levy benchmark."""
        self.nparams = nparams

    @property
    def problem(self):
        """Define the hyperparameter problem."""
        domain = (-10.0, 10.0)
        problem = HpProblem()
        for i in range(self.nparams):
            problem.add_hyperparameter(domain, f"x{i}")
        return problem

    @property
    def run_function(self):
        """Provide the run function for the hyperparameter benchmark."""
        return functools.partial(run_func, bb_func=levy)

    @property
    def scorer(self):
        """Provide the scorer for the hyperparameter benchmark."""
        return LevyScorer(self.nparams)
