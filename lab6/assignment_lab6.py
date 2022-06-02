"""
Student Name: {irfan teh}
ID: {364211760046}
Grop: {MIT212}
"""

"""
object ไว้ใน list ชื่อ mybook_store แสดงผลข้อมูลหนังสือทั้งหมดทางหน้าจอภาพ

ัตัวอย่างนำเข้าข้อมูล เช่น
คุณมีหนังสือท้ังหมดกี่เล่ม: 1 
ชื่อหนังสือ: OOP
ราคา: 200
ผู้แต่ง: ภูริวัฒน์ เลิศไกร
สำนักพิมพ์: MT

ตัวอย่างแสดงผล เช่น
Book name: OOP | Price: 200.0 THB | Auther: Puriwat Lertkrai
"""


from book import Book

book_store = []
num = int(input('คุณมีหนังสือทั้งหมดกี่เล่ม! :'))

for x in range(num):
    bookname = input('ชื่อหนังสือ')
    price = float(input('ราคา :'))
    auther = input('ชื่อผู้เเต่ง :')
    publisher = input('สำนักพิมพ์ :')
    #1
    b = Book(bookname,price,auther,publisher)
    book_store.append(b)

def display_book(book):
    print('จำนวนหนังสือทั้งหมด:',len(book))
    for x in  book:
        x.book_detail()

display_book(book_store)



