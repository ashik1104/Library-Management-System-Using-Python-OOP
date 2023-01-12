class User:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_list = []
        self.return_list = []
        self.my_donation = []


class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def borrow_book(self, book_name, user):
        if book_name in self.book_list:
            if book_name in user.borrow_list:
                print('Age ferot dao')
                return
            if self.book_list[book_name] == 0:
                print('boi shesh')
                return
            self.book_list[book_name] -= 1
            user.borrow_list.append(book_name)
            print('You have borrowed this book')
            return
        else:
            print('Book not available')

    def return_book(self, book_name, user):
        if book_name in self.book_list and book_name in user.borrow_list:
            self.book_list[book_name] += 1
            user.borrow_list.remove(book_name)
            user.return_list.append(book_name)
            print('Book returned successfully')
            return
        else:
            print('Kar boi ferot dite ashco mia??')

    def donate(self, book_name, amount, user):
        if book_name in self.book_list:
            self.book_list[book_name] += amount
            user.my_donation.append(book_name)
            print('Thanks for donation')
        else:
            self.book_list[book_name] = amount
            print('Thanks for donation')

    def availability(self):
        available_books = []
        for book in self.book_list:
            if self.book_list[book] > 0:
                available_books.append(book)
        print(available_books)


library = Library({'English': 2, 'Bangla': 5, 'Math': 4})
all_users = []
current_user = None

while True:
    if current_user is None:
        print('Not logged in\nPlease login or create account(l/c)')
        option = input()
        if option == 'l':
            roll = int(input('Roll : '))
            password = input('Password : ')
            match = False
            for user in all_users:
                if user.roll == roll and user.password == password:
                    current_user = user
                    match = True
                    break

            if not match:
                print('No user found')
        else:
            name = input('Name : ')
            roll = int(input('Roll : '))
            password = input('Password : ')
            found = False
            for user in all_users:
                if user.roll == roll:
                    found = True
                    break

            if found:
                print('This account is already exists')
                continue

            user = User(name, roll, password)
            all_users.append(user)
            current_user = user
        print("\n")

    else:
        print('Options : ')
        print('---------')
        print('1. Borrow a book')
        print('2. Return book')
        print('3. Borrowed book list')
        print('4. Returned book list')
        print('5. check availability')
        print('6. Donate a book')
        print('7. logout')

        x = int(input('Give option : '))
        if x == 1:
            book_name = input('Book name : ')
            library.borrow_book(book_name, current_user)
        elif x == 2:
            book_name = input('Book name : ')
            library.return_book(book_name, current_user)
        elif x == 3:
            print(current_user.borrow_list)
        elif x == 4:
            print(current_user.return_list)
        elif x == 5:
            library.availability()
        elif x == 6:
            book_name = input('Book name : ')
            amount = int(input('Amount : '))
            library.donate(book_name, amount, current_user)
        elif x == 7:
            print('Successfully log out')
            current_user = None

    print("\n")
