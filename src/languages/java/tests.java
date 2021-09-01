
import java.util.Random;
import java.io.FileWriter;
import java.io.IOException;
    
public class tests {
    public static void main(String args[]){
	int n_trial = 3;
	String results_file_name = "src/languages/java/results.data";
	long t0, t1;
	long t_branched, t_branchless;

	//---------num_thresh----------
	int n = (int) 1e9;
	float thresh = (float) 0.5;
	int n_gt_branched, n_gt_branchless;
	float[] v;
	v = new float[n];
	Random rand = new Random(); //create instance of random class
	for (int i=0; i<n; i++) {
	    v[i] = rand.nextFloat();
	}

	//branched
	n_gt_branched = 0; //to get around compiler error about uninitialized varaible
	t0 = System.currentTimeMillis();
	for (int i_trial=0; i_trial<n_trial; i_trial++) {
	    n_gt_branched = 0;
	    for (int i=0; i<n; i++) {
		if (v[i] > thresh) {
		    n_gt_branched += 1;
		}
	    }
	}
	t1 = System.currentTimeMillis();
	t_branched = t1 - t0;

	//branchless
	n_gt_branchless = 0; //to get around compiler error about uninitialized varaible
	t0 = System.currentTimeMillis();
	for (int i_trial=0; i_trial<n_trial; i_trial++) {
	    n_gt_branchless = 0;
	    for (int i=0; i<n; i++) {
		n_gt_branchless += (v[i] > thresh) ? 1 : 0;
	    }
	}
	t1 = System.currentTimeMillis();
	t_branchless = t1 - t0;

	
	if (n_gt_branched != n_gt_branchless){
	    System.out.println("ERROR: branched and brancless implementations give different results\n");
	}

	//write test result to file
	try {
	    FileWriter w = new FileWriter(results_file_name);
	    w.write("num_thresh  " + ((float) t_branchless)/((float) t_branched));
	    w.close();
	} catch (IOException e) {
	    e.printStackTrace();
	}
	//-----------------------------

    } //end main()
}
