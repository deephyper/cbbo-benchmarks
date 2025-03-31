# C-BBO benchmarks

Continuous Black-Box Optimization (C-BBO) benchmarks for DeepHyper.

| Function Name | Number of Dimensions  |                   Comment                   |
| ------------- | --------------------- | ------------------------------------------- |
| ackley        | $\infty$ (default 5)  | Many local minima and single global optimum |
| branin        | 2                     | Three global optimum                        |
| cossin        | 1                     | Many local minima, good for visualisation.  |
| easom         | 2                     | Almost flat everywhere                      |
| griewank      | $\infty$ (default 5)  |                                             |
| hartmann6D    | 6                     |                                             |
| levy          | $\infty$ (default 5)  |                                             |
| michal        | $\infty$ (default 2)  |                                             |
| rosen         | $\infty$ (default 5)  |                                             |
| schwefel      | $\infty$ (default 5)  |                                             |
| shekel        | 4                     | Many local minima with flat areas           |

## Installation

Python installation and dependency management is handled with uv. Clone this repository then create a Python environment with `uv sync`.

## Usage

Go to the `example` directory and run the benchmarks with `uv run benchmark cbbo.toml`. Plot the results of the benchmarks with `uv run benchmark cbbo.toml --plot`.
