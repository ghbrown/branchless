var fs = require('fs'); //file system module

var n_trial = 3; //number of times to repeat each test
var results_file_name = 'src/languages/javascript/results.data'; //path of results file RELATIVE TO MAKEFILE
var t0, t1;

//---------num_thresh----------
var n = 1e7; //problem size
var thresh = 0.5; //threshold
const v = new Array(n); //random vector with values between 0 and 1
for (var i=0; i<v.length; i++) {
    v[i] = Math.random();
}

//branched
var n_gt_branched; //accumulator for number of value in v greater than thresh
t0 = performance.now();
for (var trial=0; trial<n_trial; trial++) {
    n_gt_branched = 0; 
    for (const i_v in v) {
	if (v[i_v] > thresh) {
	    n_gt_branched += 1;
	} //end if
    } //end for (elements)
} //end for (trials)
t1 = performance.now();
var t_branched = t1 - t0;

//branchless
var n_gt_branchless; //accumulator for number of value in v greater than thresh
t0 = performance.now();
for (var trial=0; trial<n_trial; trial++) {
    n_gt_branchless = 0; 
    for (const i_v in v) {
	n_gt_branchless += (v[i_v] > thresh);
    } //end for (elements)
} //end for (trials)
t1 = performance.now();
var t_branchless = t1 - t0;

if (n_gt_branched != n_gt_branchless) {
    console.log('ERROR: branched and branchless implementations give different results');
}

//write num_thresh result to file
fs.writeFile(results_file_name,'num_thresh  '+(t_branchless/t_branched),function(err){});
//-----------------------------

