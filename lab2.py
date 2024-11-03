import csv
import random

def read_csv(booksen):
  with open(booksen, 'r', encoding='ISO-8859-2') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')  
    data = list(reader)
    print("Titles:", reader.fieldnames)  
  return data


books = read_csv('books-en.csv')

def long_titles(data):
  # Счет по количеству длинных названий
  count = 0
  for book in data:
    if len(book['Book-Title']) > 30:  
      count += 1
  return count

def search_by_author(data, author, max_price):
  # Поиск по автору
  results = [book for book in data if book['Book-Author'] == author and float(book['Price'].replace(',', '.')) <= max_price]
  return results

def generate_bibliography(data, num_records):
  # Генерируем библиогрф ссылки
  if len(data) < num_records:
    num_records = len(data) 

  random_books = random.sample(data, num_records)
  with open('result.txt', 'w', encoding='utf-8') as f: 
    for i, book in enumerate(random_books, start=1):
      f.write(f"{i}. {book['Book-Author']}. {book['Book-Title']} - {book['Year-Of-Publication']}\n")


books = read_csv('books-en.csv')

# Считает количество книг с длинными названиями
long_titles_count = long_titles(books)
print(f"Amount of books with long titles {long_titles_count}")

# Вывод поиска по автору
results = search_by_author(books, 'Harper Lee', 150)
for book in results:
  print(book)


generate_bibliography(books, 20)
