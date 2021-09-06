package main
import(
	"os"
	"log"
	"strconv"
	"fmt"
	"math/rand"
	"time"
)

func main() {
    var n_trial int = 3 //number of times to repeat each test
	var results_file_name string = "src/languages/go/results.data" //path of results RELATIVE TO MAKEFILE
	var t0, t1 int64
	var t_branched, t_branchless int64
	rand.Seed(time.Now().Unix())

	//---------num_thresh----------
	const n int = int(5e8)
	var thresh float32 = 0.5
	var n_gt_branched, n_gt_branchless int
	var v[n] float32
	for i := range v {
		v[i] = rand.Float32()
	}

	//branched
	t0 = time.Now().UnixNano()
	for trial:=1; trial<=n_trial; trial++ {
		n_gt_branched = 0
		for i := range v {
			if (v[i] > thresh) {
				n_gt_branched += 1
			} //end if
		} //end for
	} //end for
	t1 = time.Now().UnixNano()
	t_branched = t1 - t0

	//branchless
	t0 = time.Now().UnixNano()
	for trial:=1; trial<=n_trial; trial++ {
		n_gt_branchless = 0
		for i := range v {
			n_gt_branchless += func() int {if(v[i] > thresh) {return 1} else {return 0}}()
		} //end for
	} //end for
	t1 = time.Now().UnixNano()
	t_branchless = t1 - t0

	if (n_gt_branched != n_gt_branchless) {
		fmt.Println("ERROR: branched and branchless implementations give different results")
	}

	//write test results to file
	f, err0 := os.Create(results_file_name)
	if err0 != nil {log.Fatal(err0)}
	defer f.Close()
	_, err1 := f.WriteString("num_thresh  "+strconv.FormatFloat(float64(t_branchless)/float64(t_branched),'E',-1,64))
	if err1 != nil {log.Fatal(err1)}
	//-----------------------------

} //end main()
