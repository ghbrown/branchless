
A comparison of the relative speedup achieved by [branchless programming](https://dev.to/jobinrjohnson/branchless-programming-does-it-really-matter-20j4) techniques in a variety of languages.

## Speedups by langauge
For each language and test pair, the relative speedup is given as `t_branched/t_branchless`, where `t_branched` is the CPU time taken by the branched implementation, and `t_branchless` is the time taken by the branchless implementation.

**Numbers greater than 1.0 imply branchless techniques result in a speedup, while numbers less than one imply that they result in a slowdown.**

Results are organized by programming language, under which the relative speedup is given for each test (see more about the tests below).

<results start here>

**Python**

- `num_thresh`: 0.10

<results end here>

<you should autogenerate a plot on run>
<bar plot with up and down bars around ratio=1>
<generate plot, capture as file, then link to file name in README>

## The tests
`num_thresh`: given a random array of numbers, how many of them are above some threshold

