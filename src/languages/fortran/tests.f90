
program tests
  implicit none
  integer :: n_trial = 3
  character(len=50) :: results_file_name = 'src/languages/fortran/results.data'
  real :: t0, t1, t_branched, t_branchless


  !--------------num_thresh-------------
  integer :: n = 1e9
  real :: thresh = 0.5
  integer :: n_gt_branched, n_gt_branchless
  integer :: i_trial, i
  integer :: log_int !intermediate variable for logical to int conversion
  real, allocatable, dimension(:) :: v
  allocate(v(n))
  call random_number(v) !fill v with random numbers

  !branched
  call cpu_time(t0)
  do i_trial=1,n_trial !run n_trial trials
    n_gt_branched = 0
    do i=1,n
        if (v(i) > thresh) then
            n_gt_branched = n_gt_branched + 1
        end if
    end do
  end do
  call cpu_time(t1)
  t_branched = t1 - t0

  !branchless
  call cpu_time(t0)
  do i_trial=1,n_trial !run n_trial trials
    n_gt_branchless = 0
    do i=1,n
        log_int = (v(i) > thresh)
        n_gt_branchless = n_gt_branchless + log_int
    end do
  end do
  call cpu_time(t1)
  t_branchless = t1 - t0

  if (n_gt_branched /= n_gt_branchless) then
     print *, 'ERROR: branched and branchless implementations give different results'
  end if
  !-------------------------------------

  open (unit = 9, file = results_file_name)
  write(9,*) 'num_thresh: ', t_branchless/t_branched
  close(unit = 9)
end program tests

 
