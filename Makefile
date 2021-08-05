
PY = python3
FC = gfortran
FF = -O3 -w
CC = gcc

all:
	@echo " "
	@echo "Running tests:"
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

fortran:
	@echo "  ...Fortran"
	@gfortran $(FF) -o build/fortran src/languages/fortran/tests.f90
	@./build/fortran
python:
	@echo "  ...Python"
	@$(PY) src/languages/python/tests.py
