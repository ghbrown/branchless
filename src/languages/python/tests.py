import time
import numpy as np

n_trial = 3 #number of times to repeat each test
results_file_name='src/languages/python/results.data' #path of results file RELATIVE TO MAKEFILE

#---------num_thresh----------
n = int(1e6) #problem size
thresh = 0.5 #threshold
v = np.random.rand(n) #random vector with values between 0 and 1

#branched
t0 = time.perf_counter()
for trial in range(n_trial):
    n_gt_branched = 0 #accumulator for number of value in v greater than thresh
    for val in v:
        if (val > thresh):
            n_gt_branched += 1
t1 = time.perf_counter()
t_branched = t1 - t0

#branchless
t0 = time.perf_counter()
for trial in range(n_trial):
    n_gt_branchless = 0 #accumulator for number of value in v greater than thresh
    for val in v:
        n_gt_branchless += 1*(val > thresh)
t1 = time.perf_counter()
t_branchless = t1 - t0

if (n_gt_branched != n_gt_branchless):
    print('ERROR: branched and branchless implementations give different results')

num_thresh_time_frac = t_branchless/t_branched #relative speedup of branchless techniques

#-----------------------------

with open(results_file_name,'w') as f:
    f.write('num_thresh  ' + str(num_thresh_time_frac) + '\n')
