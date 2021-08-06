
A comparison of the relative speedup achieved by [branchless programming](https://dev.to/jobinrjohnson/branchless-programming-does-it-really-matter-20j4) techniques in a variety of languages.

## Speedups by langauge
For each language and test pair, the ratio `t_branchless/t_branched` is computed. Here `t_branchless` is the CPU time taken by the branchless implementation, and `t_branched` is the time taken by the branched implementation.

**Numbers less than 1.0 imply branchless techniques result in a speedup, while numbers greater than one imply they result in a slowdown.
** For example, 0.23 implies the branchless version ran in 23% of the time the branched version took.

Results are organized by programming language, under which the relative speedup is given for each test (see more about the tests below).

---
<results start here>

**C**

- `num_thresh`: 1.02

**Fortran**

- ` num_thresh`: 1.01

**Python**

- `num_thresh`: 11.13

<results end here>
---

<you should autogenerate a plot on run>
<bar plot with up and down bars around ratio=1>
<generate plot, capture as file, then link to file name in README>

## The tests
`num_thresh`: given a random array of numbers, how many of them are above some threshold?

