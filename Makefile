
#these compiler variables and flag are in alphabetical order by official language name
#the order of runs in make all follows this ordering
#C
CC = gcc
CF = -O3

#C++
CPPC = g++
CPPF = -O3

#Chapel
CHPLC = chpl
CHPLF = --fast

#Fortran
FC = gfortran
FF = -O3 -w

#Go
GOC = go
#GOF = FLAGS?

#Java
JC = javac
JR = java

#JavaScript
JS = node

#Python
PY = python3

all:
	@echo " "
	@echo "Running tests:"
	@$(MAKE) -s c
	@$(MAKE) -s cpp
	@$(MAKE) -s chapel
	@$(MAKE) -s fortran
	@$(MAKE) -s go
	@$(MAKE) -s java
	@$(MAKE) -s javascript
	@$(MAKE) -s python
	@echo "Finished testing."
	@$(MAKE) -s results

results:
	@echo " "
	@echo "Updating results..."
	@$(PY) src/update_results.py
	@echo "...finished."
	@echo " "

clean:
	@echo " "
	@echo "Cleaning build artifacts..."
	@rm -r build/*
	@mkdir build/java
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

chapel: 
	@echo "  ...Chapel"
	@$(CHPLC) $(CHPLF) -o build/chapel src/languages/chapel/tests.chpl
	@./build/chapel

fortran:
	@echo "  ...Fortran"
	@$(FC) $(FF) -o build/fortran src/languages/fortran/tests.f90
	@./build/fortran

go:
	@echo "  ...Go"
	@$(GOC) build -o build/go src/languages/go/tests.go
	@./build/go

java:
	@echo "  ...Java"
	@$(JC) -d build/java src/languages/java/tests.java
	@$(JR) -cp build/java tests

javascript:
	@echo "  ...JavaScript"
	@$(JS) src/languages/javascript/tests.js

python:
	@echo "  ...Python"
	@$(PY) src/languages/python/tests.py
