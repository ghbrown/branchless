
CC = gcc
CF = -O3
CPPC = g++
CPPF = -O3
FC = gfortran
FF = -O3 -w
PY = python3

all:
	@echo " "
	@echo "Running tests:"
	@$(MAKE) -s c
	@$(MAKE) -s cpp
	@$(MAKE) -s fortran
	@$(MAKE) -s python
	@echo "Finished testing."
	@$(MAKE) -s results

results:
	@echo " "
	@echo "Updating results..."
	@$(PY) src/update_results.py
	@echo "...finished."
	@echo " "

c:
	@echo "  ...C"
	@$(CC) $(CF) -o build/c src/languages/c/tests.c
	@./build/c

cpp:
	@echo "  ...C++"
	@$(CPPC) $(CPPF) -o build/cpp src/languages/cpp/tests.cpp
	@./build/cpp

fortran:
	@echo "  ...Fortran"
	@gfortran $(FF) -o build/fortran src/languages/fortran/tests.f90
	@./build/fortran
python:
	@echo "  ...Python"
	@$(PY) src/languages/python/tests.py
