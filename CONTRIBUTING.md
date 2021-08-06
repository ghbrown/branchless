
To add a new language with alphabetical name `new_lang` (e.g. cpp) and official name 'official_lang` (e.g. C++):

   - create the new folder `src/languages/new_lang`
   - implement the tests in `src/languages/new_lang/tests.new_lang_extension`
   - these tests should write the results to `src/languages/new_lang/results.data`, in the format below, and with tests in alphabetical order
   ```
   test_name: t_branchless/t_branched
   ...more tests...
   ```
   - add a `make` rule called `new_lang` that executes the tests (the executable should be name `new_lang` and goes in `build/` (if `new_lang` is compiled)) and don't forget the `@echo "  ...new_lang"`
   - add a call of `new_lang`'s `make` rule in the `all` rule (in alphabetical order) 
   - add `new_lang` entry to the first uncommented line of `src/tested_languages.info` (in alphabetical order)
   - add the language's official name `official_name` to the second uncommented line of `src/tested_languages.info` (in alphabetical order)