import functools
from abc import ABC, abstractmethod
from deephyper.hpo import HpProblem
from cbbo_benchmarks.scorer import HPOScorer


class HPOBenchmark(ABC):
    """Base class for Hyperparameter optimization benchmarks."""

    @property
    @abstractmethod
    def problem(self) -> HpProblem:
        """The benchmark hyperparameter problem."""
        pass

    @property
    @abstractmethod
    def run_function(self) -> functools.partial:
        """The benchmark hyperparameter run_function."""
        pass

    @property
    @abstractmethod
    def scorer(self) -> HPOScorer:
        """The benchmark hyperparameter scorer."""
        pass
