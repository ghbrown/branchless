
all:
	@echo " "
	@echo "Beginning tests:"
	@$(MAKE) -s python
	@echo "Finished testing."
	@echo " "
	@echo "Updating results..."
	@$(MAKE) -s results
	@echo "...finished."

results:
	@python3 update_results.py

python:
	@echo "...testing python"
	@python3 languages/python/tests.py
