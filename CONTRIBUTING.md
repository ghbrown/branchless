
To add a new language with alphabetical name `new_lang` (e.g. cpp) and official name `official_lang` (e.g. C++):

   - create the new folder `src/languages/new_lang`
   - create the file `src/languages/new_lang/official_name` containing a single line with the language's official name (note: this file's name is literally `official_name`)
   - implement the tests in `src/languages/new_lang/tests.new_lang_extension`
   - these tests should write the results to `src/languages/new_lang/results.data`, in the format below, and with tests in alphabetical order
   ```
   test_name  t_branchless/t_branched
   ...more tests (in alphabetical order)...
   ```
   - add a `make` rule called `new_lang` that compiles `tests.new_lang_exension` (if necessary, the executable should be name `new_lang` and goes in `build/`) and runs the tests; don't forget the `@echo "  ...official_lang"`
   - add a call of `new_lang`'s `make` rule in the `all` rule (in alphabetical order) 