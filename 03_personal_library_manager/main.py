import json

def load_library(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library(library, filename):
    with open(filename, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    try:
        year = int(input("Enter publication year: ").strip())
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
    genre = input("Enter genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == 'yes' else False

    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(book)
    print(f"Book '{title}' added successfully.")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed successfully.")
            return
    print(f"No book found with title '{title}'.")

def search_books(library):
    keyword = input("Enter a keyword to search (title/author): ").strip().lower()
    results = [book for book in library if keyword in book['title'].lower() or keyword in book['author'].lower()]
    if results:
        print(f"Found {len(results)} book(s):")
        for book in results:
            print_book(book)
    else:
        print("No matching books found.")

def display_books(library):
    if not library:
        print("Library is empty.")
        return
    print(f"Displaying all {len(library)} book(s):")
    for book in library:
        print_book(book)

def print_book(book):
    read_status = 'Read' if book['read'] else 'Unread'
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {read_status}")

def display_statistics(library):
    total = len(library)
    if total == 0:
        print("Library is empty.")
        return
    read_count = sum(1 for book in library if book['read'])
    read_percentage = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Books read: {read_count} ({read_percentage:.2f}%)")

def main():
    filename = 'library.json'
    library = load_library(filename)

    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Save library")
        print("7. Load library")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library, filename)
            print("Library saved successfully.")
        elif choice == '7':
            library = load_library(filename)
            print("Library loaded successfully.")
        elif choice == '8':
            save_library(library, filename)
            print("Library saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
