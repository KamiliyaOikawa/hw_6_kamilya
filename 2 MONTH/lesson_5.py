import re

my_text = 'Vasya, 1998, ramir@gmail.com,' \
          'Adilet, 1997, Adilet@gamil.ru,' \
          'Ramilita, 2000, Ramiliya@yandex.com'

file_path = 'demo_mock_data.txt'
results_file_path = 'results.txt'

file_reader = open(file_path, mode='r', encoding='latin-1')
results_file = open(results_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()

what_search = r'[@]+\w+\S\w+'
result = re.findall(what_search, my_text_file)

for items in result:
    print(items)
    results_file.write(items +'\n')

print(f'{len(result)}')
# print(result)
