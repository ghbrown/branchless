import os

relative_readme_path='README.md'
cwd = os.getcwd() #current working directory
lang_dir = cwd + '/src/languages'
results_start_text = '<results start here>'
results_end_text = '<results end here>'

#collect results from each language directory and generate lines for README
results_lines=[] #empty list to hold lines that will generate results section of README
results_lines.append(results_start_text + '\n\n') #add markdown comment to easily find start of results
for root, dirs, files in os.walk(lang_dir):
    for lang_name in dirs: #loop over language directories (lang_names)
        lang_dir = os.path.join(root,lang_name) # ../src/lang_dir
        #get official name
        official_name_file_name = os.path.join(lang_dir,'official_name')
        with open(official_name_file_name,'r') as f:
            official_name = (f.readlines()[0]).strip()
        results_lines.append('**' + official_name + '**\n\n') #language name
        #get results
        results_file_name = os.path.join(lang_dir,'results.data')
        with open(results_file_name,'r') as f:
            lines = f.readlines()
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
        
    
