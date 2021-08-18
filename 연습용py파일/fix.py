import os
import csv
import html

text_file_path = './templates/file.html'
new_text_content = ''
target_word = '<html>'
new_word = '{% extends "index.html" %}'
# f = open('./templates/file1.html', mode='r', encoding='utf-8')
# lines = f.readlines()
# lines.replace('html','WKd')
# f.close()

with open('./templates/file.html', 'a') as html_file:
    html_file.replace('html','dd')


# html_file = open('./templates/file1.html', 'w')
# html_file.replace('html','dd')
# html_file.close()

# with open(text_file_path,'r') as f:
#     lines = f.readlines()
#     print(lines)
#     for line in lines:
#         # 조건에 따라 원하는 대로 line을 수정
#         if '<html>' in line:
#             edited_lines.append('{% extends "index.html" %}')
#         else:
#             edited_lines.append(line)

# with open(text_file_path, 'w') as f:
#     f.writelines(edited_lines)