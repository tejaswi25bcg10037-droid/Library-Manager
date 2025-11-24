from datetime import datetime, timedelta

books = {
    'B101': {'title': 'Python Basics', 'author': 'Smith', 'borrower': 'Alice', 'due_date': '2025-11-20'},
    'B102': {'title': 'Physics 101', 'author': 'Doe', 'borrower': None, 'due_date': None},
    'B103': {'title': 'Chemistry 202', 'author': 'Lee', 'borrower': 'Bob', 'due_date': '2025-11-18'},
    'B104': {'title': 'Sunrise on the Reaping', 'author': 'Suzanne Collins', 'borrower': 'Eve', 'due_date': '2025-11-25'},
    'B105': {'title': 'Onyx Storm', 'author': 'Rebecca Yarros', 'borrower': None, 'due_date': None},
    'B106': {'title': 'The Widow', 'author': 'John Grisham', 'borrower': 'Mike', 'due_date': '2025-12-01'},
    'B107': {'title': 'The Intruder', 'author': 'Freida McFadden', 'borrower': None, 'due_date': None},
    'B108': {'title': 'Great Big Beautiful Life', 'author': 'Emily Henry', 'borrower': 'Sara', 'due_date': '2025-12-03'},
    'B109': {'title': 'The Secret of Secrets', 'author': 'Dan Brown', 'borrower': None, 'due_date': None},
    'B110': {'title': 'Lights Out', 'author': 'Navessa Allen', 'borrower': None, 'due_date': None},
    'B111': {'title': 'The Tenant', 'author': 'Freida McFadden', 'borrower': 'Tom', 'due_date': '2025-11-28'},
    'B112': {'title': 'My Friends', 'author': 'Fredrik Backman', 'borrower': 'Nina', 'due_date': '2025-12-10'},
    'B113': {'title': 'Nightshade', 'author': 'Michael Connelly', 'borrower': None, 'due_date': None},
    'B114': {'title': 'Atmosphere: A Love Story', 'author': 'Taylor Jenkins Reid', 'borrower': 'Zoe', 'due_date': '2025-11-22'},
}


fine_per_day = 10

def check_borrowed_books():
    now = datetime.now()
    for book_id, details in books.items():
        if details['borrower']:
            due = datetime.strptime(details['due_date'], '%Y-%m-%d')
            if now > due:
                overdue_days = (now - due).days
                fine = overdue_days * fine_per_day
                print(f"Book '{details['title']}' (ID: {book_id}) is overdue by {overdue_days} days.")
                print(f"Notify {details['borrower']} to return the book. Fine: {fine}")
            else:
                print(f"Book '{details['title']}' (ID: {book_id}) borrowed by {details['borrower']} is not overdue.")
        else:
            print(f"Book '{details['title']}' (ID: {book_id}) is available.")

check_borrowed_books()
