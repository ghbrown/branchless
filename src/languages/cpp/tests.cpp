#include <iostream>
#include <fstream>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
  using std::chrono::high_resolution_clock;

  int rand_max = 32767;
  int n_trial = 3;
  string results_file_name = "src/languages/cpp/results.data";
  float t_branched, t_branchless;

  //--------------num_thresh-------------
  int n = 1e9;
  float thresh = 0.5;
  int n_gt_branched, n_gt_branchless;
  float *v = new float[n];

  srand(time(NULL)); //random seed
  for (int i=0; i<n; i++) { //set random elements of v
    v[i] = ((float)(rand() % rand_max)) / ((float)(rand_max));
  }

  //branched
  auto t0 = high_resolution_clock::now();
  for (int i_trial=0; i_trial<n_trial; i_trial++) {
    n_gt_branched=0;
    for (int i=0; i<n; i++) {
	if (v[i] > thresh) {
	n_gt_branched += 1;
	}
    }
  }
  auto t1 = high_resolution_clock::now();
  t_branched = std::chrono::duration<float>(t1 - t0).count();

  //branchless
  t0 = high_resolution_clock::now();
  for (int i_trial=0; i_trial<n_trial; i_trial++) {
    n_gt_branchless=0;
    for (int i=0; i<n; i++) {
      n_gt_branchless += (v[i] > thresh);
    }
  }
  t1 = high_resolution_clock::now();
  t_branchless = std::chrono::duration<float>(t1 - t0).count();
  
  delete[] v;

  if (n_gt_branched != n_gt_branchless){
    cout << "ERROR: branched and branchless implementations give different results\n";
  }

  //write test result to file
  ofstream f;
  f.open(results_file_name);
  f << "num_thresh  " << (t_branchless/t_branched) << "\n";
  f.close();
  //-------------------------------------

  return 0;
}
