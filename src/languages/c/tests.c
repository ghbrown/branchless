#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

int main() {
  int rand_max = 32767;
  float cpu_freq = CLOCKS_PER_SEC;
  FILE *fp;
  int n_trial = 3;
  char results_file_name[] = "src/languages/c/results.data";
  clock_t t0, t1;
  float t_branched, t_branchless;
  
  //--------------num_thresh-------------
  int n = 1e9; //change back to 1e9
  float thresh = 0.5;
  int n_gt_branched, n_gt_branchless;
  float *v;
  v = malloc(sizeof(float)*n); //use heap memory for large array to avoid stack overflow

  srand(time(NULL)); //random seed
  for (int i=0; i<n; i++) { //set random elements of v
    v[i] = ((float)(rand() % rand_max)) / ((float)(rand_max));
  }

  //branched
  t0 = clock();
  for (int i_trial=0; i_trial<n_trial; i_trial++) {
    n_gt_branched=0;
    for (int i=0; i<n; i++) {
	if (v[i] > thresh) {
	n_gt_branched += 1;
	}
    }
  }
  t1 = clock();
  t_branched = ((float)(t0 - t1))/cpu_freq;
  

  //branchless
  t0 = clock();
  for (int i_trial=0; i_trial<n_trial; i_trial++) {
    n_gt_branchless=0;
    for (int i=0; i<n; i++) {
      n_gt_branchless += (v[i] > thresh);
    }
  }
  t1 = clock();
  t_branchless = ((float)(t0 - t1))/cpu_freq;

  if (n_gt_branched != n_gt_branchless){
    printf("ERROR: branched and branchless implementations give different results\n");
  }
  //-------------------------------------

  //write results to file
  fp = fopen(results_file_name,"w+");
  fprintf(fp, "num_thresh: %f\n", (t_branchless/t_branched));
  fclose(fp);

} //end main()
