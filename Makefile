
PY = python3
FC = gfortran
CC = gcc

all:
	@echo " "
	@echo "Running tests:"
	@$(MAKE) -s python
	@echo "Finished testing."
	@$(MAKE) -s results

results:
	@echo " "
	@echo "Updating results..."
	@$(PY) src/update_results.py
	@echo "...finished."
	@echo " "

python:
	@echo "  ...python"
	@$(PY) src/languages/python/tests.py
