# 16.3
text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960 ... Perdido Street Station,China Miéville,2000 ... Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books2.csv', 'wt') as file:
    file.write(text)

# 16.4
import sqlite3
database = sqlite3.connect('books.db')
cursor = database.cursor()
cursor.execute('''create table book (title text, author text, year int)''')
database.commit()

# 16.5
import csv
import sqlite3
book_values = 'insert into book values(?, ?, ?)'
with open('books2.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        cursor.execute(book_values, (book['title'], book['author'], book['year']))