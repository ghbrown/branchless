
import os

#get directory and official language names from languages.included file in src
with open('src/tested_languages.info','r') as f:
    languages_included_lines_stripped=f.readlines()

#lists of src/language/ directory names and corresponding "official" language names
dir_names = (languages_included_lines_stripped[3].strip()).split() #only these names will have their results pulled and used in the README
official_names = (languages_included_lines_stripped[6].strip()).split()

relative_readme_path='README.md'
cwd = os.getcwd() #current working directory
lang_dir = cwd + '/src/languages'
results_start_text = '<results start here>'
results_end_text = '<results end here>'

#collect results from each language directory and generate lines for README
results_lines=[] #empty list to hold lines that will generate results section of README
results_lines.append(results_start_text + '\n\n') #add markdown comment to easily find start of results
for root, dirs, files in os.walk(lang_dir):
    for i_lang, lang_name in enumerate(dir_names):
        if lang_name in dirs:
            lang_results = os.path.join(root,lang_name)
            results_file_name = lang_results + '/results.data'
            with open(results_file_name,'r') as f:
                lines = f.readlines()
            
            results_lines.append('**' + official_names[i_lang] + '**\n\n') #language name
            for line in lines:
                line_split = line.split(': ')
                text = line_split[0]
                num_float = float(line_split[1])
                num_formatted =  f'{num_float:.2f}'
                text_formatted = '- `'+text+'`: '
                test_line_formatted = text_formatted + num_formatted + '\n'
                results_lines.append(test_line_formatted) #test name and speedup factor
            results_lines.append('\n') #blank line for markdown
results_lines.append(results_end_text + '\n') #add markdown comment to easily find end of results

#update source material of README.md
with open(relative_readme_path,'r') as f: #read in existing README
    old_lines = f.readlines()

for i_line, line in enumerate(old_lines): #deterimine where results section begins and ends
    if results_start_text in line:
        first_line = i_line
    elif results_end_text in line:
        last_line = i_line

preresults_lines = old_lines[:first_line] #duplicate non-results lines
postresults_lines = old_lines[(last_line+1):]

readme_lines = preresults_lines + results_lines + postresults_lines
with open(relative_readme_path,'w') as f:
    f.writelines(readme_lines)
        
    
