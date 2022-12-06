# чтение файла

import os
current = os.getcwd()
folder = 'folder_text'
full_path = os.path.join(current, folder)
 
result = {} # избавиться от лишних символов....

# записываем новый список и словарь

for file_name in os.listdir(full_path):
    with open(os.path.join(full_path, file_name), 'r', encoding='utf-8') as f :
        file_content = []   # записываем новый список
        for line in f :
            file_content.append(line)   
        result[file_name] = len(file_content), file_content   # записываем новый словарь

# Сортируем словарь

sorted_dict = {}
sorted_keys = sorted(result, key=result.get)
for sort in sorted_keys:
    sorted_dict[sort] = result[sort]

#print(sorted_dict) 

with open('result.txt', 'w', encoding='utf-8') as f:
      
    for key, value in sorted_dict.items():
        f.write(f'{key}\n')
        f.write(f'{value[0]}\n')
        f.write(f'{value[1]}\n')
       
print (result)