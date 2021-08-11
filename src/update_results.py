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
    #make list of official names
    official_name_list = [0]*len(dirs)
    for i_lang,lang_name in enumerate(dirs): #loop over language directories (alphabetical language names)
        lang_dir = os.path.join(root,lang_name) # ../src/lang_dir
        #get official name
        official_name_file_name = os.path.join(lang_dir,'official_name')
        with open(official_name_file_name,'r') as f:
            official_name_list[i_lang] = (f.readlines()[0]).strip()

    #sort official names alphabetically and get sort indices
    name_index_list = sorted((official_name,index) for index, official_name in enumerate(official_name_list)) #[ (name, ind), ..., (name, ind) ] sorted by name
    sorted_indices=[tup[1] for tup in name_index_list] #pull out only sorted indices

    #sort dirs (alphabetical language names) by indices used to sort official language names
    sorted_dirs = [0]*len(dirs)
    for i,i_sorted in enumerate(sorted_indices):
        sorted_dirs[i] = dirs[i_sorted]
        
    #access results and store them in formatted lines
    for lang_name in sorted_dirs: #loop over *sorted* alphabetical language dirs
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
            line_split = line.split()
            text = line_split[0] #test name
            num_float = float(line_split[1]) #test result (number)
            text_formatted = '- `' + text + '`: '
            num_formatted =  f'{num_float:.2f}'
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
        
    
