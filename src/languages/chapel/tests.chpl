
use IO;
use Random;
use Time;

var n_trial : int = 3;
var results_file_name : string = 'src/languages/chapel/results.data'; //path to results file RELATIVE TO MAKEFILE
var t : Timer;
var t_branched : real;
var t_branchless : real;

//---------num_thresh----------
var n : int = 1e9 : int ; //problem size
var thresh : real = 0.5; //threshold
var n_gt_branched : int;
var n_gt_branchless : int;
var v : [0..#n] real;
fillRandom(v);

//branched
t.start();
for trial in [0..#n_trial] {
  for val in v {
    if (val > thresh) {
      n_gt_branched += 1;
    }
  }
} //end for (trial)
t.stop();
t_branched = t.elapsed();

//branchless
t.start();
for trial in [0..#n_trial] {
  for val in v {
    n_gt_branchless += (val > thresh);
  }
} //end for (trial)
t.stop();
t_branchless = t.elapsed();

if (n_gt_branched != n_gt_branchless) {
  writeln("ERROR: branched and branchless implementations give different results");
}

//write test result to file
var f = open(results_file_name,iomode.cw);
var chan = f.writer();
chan.write("num_thresh  ", (t_branchless : real)/(t_branched : real));
chan.close();
f.close();
//-----------------------------

