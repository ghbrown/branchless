
PY = python3
FC = gfortran
CC = gcc

all:
	@echo " "
	@echo "Running tests:"
	@$(MAKE) -s python
	@echo "Finished testing."
	@echo " "
	@echo "Updating results..."
	@$(MAKE) -s results
	@echo "...finished."

results:
	@$(PY) src/update_results.py

python:
	@echo "  ...python"
	@$(PY) src/languages/python/tests.py
