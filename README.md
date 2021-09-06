
A comparison of the relative speedup achieved by [branchless programming](https://dev.to/jobinrjohnson/branchless-programming-does-it-really-matter-20j4) techniques in a variety of languages.


## Speedups by langauge

For each language and test pair, the ratio `t_branchless/t_branched` is computed. Here `t_branchless` is the CPU time taken by the branchless implementation, and `t_branched` is the time taken by the branched implementation.


**Numbers less than 1.0 imply branchless techniques result in a speedup, while numbers greater than one imply they result in a slowdown.**
For example, 0.23 implies the branchless version ran in 23% of the time the branched version took.

Results are organized by programming language, under which the relative speedup is given for each test (see more about the tests below).
**Based on the fluctuations observed, these results have a relative uncertainty of about 10% (rough estimate).**

---

<results start here>

**C**

- `num_thresh`: 0.99

**C++**

- `num_thresh`: 1.01

**Chapel**

- `num_thresh`: 1.11

**Fortran**

- `num_thresh`: 1.01

**Go**

- `num_thresh`: 1.11

**Java**

- `num_thresh`: 0.48

**JavaScript**

- `num_thresh`: 1.03

**Python**

- `num_thresh`: 11.46

<results end here>

---

<you should autogenerate a plot on run>
<bar plot with up and down bars around ratio=1>
<generate plot, capture as file, then link to file name in README>


## Tests

`num_thresh`: given an array of random numbers, how many of them are above some threshold?


## Extra information

This project uses GNU Make to run the tests.
A Python script is used to collect all testing results and automatically update the [`README.md`](https://github.com/ghbrown/branchless/blob/main/README.md).

Compiler optimizations are generally set to the maximum level, but look in the [`Makefile`](https://github.com/ghbrown/branchless/blob/main/Makefile) for the exact flags.
The level of optimizations can change the results drastically. For example, without compiler optimizations the branchless to branched time ratio for `num_thresh` is about 0.25 (compared to about 1.00 for `-O3` optimization).


## Contributing

If you would like to contribute tests for an open source language or suggest new kinds of tests, feel free to open an issue. Instructions for adding a new language are in [`CONTRIBUTING.md`](https://github.com/ghbrown/branchless/blob/main/CONTRIBUTING.md).

If you want to contribute and are looking for language suggestions please consider:
- Rust
- C#
- R
- Julia
- Pascal
- Lisp
- Perl
