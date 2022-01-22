import re

file_path = 'MOCK_DATA.txt'
results_file_path = 'result.txt'

file_reader = open(file_path, mode='r', encoding='latin-1')
result_file = open(results_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_search = r'[A-Z]+[A-z]+\w+\s+[A-z\W]+\w(!?a-z'
result = re.findall(what_search, my_text_file)

for items in result:
    print(items)
    result_file.write(items + '\n')

    print(f'{len(result)}')
    # print(result)
