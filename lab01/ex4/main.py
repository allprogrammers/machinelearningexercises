import sys
from typing import List, Dict, Tuple

month = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]

class Book:
    def __init__(self, isbn: str):
        self.isbn = isbn
        self.transactions = []
        self.bought = 0
        self.sold = 0
        self.average_buy_price = 0.0
        self.average_sell_price = 0.0

    def add_transaction(self, action: str, date: str, quantity: int, price: float) -> None:
        """Adds a transaction for the book."""
        if action == "S":
            self.average_sell_price = (quantity*price + self.average_sell_price * self.sold) / (self.sold + quantity)
            self.sold += quantity
        elif action == "B":
            self.average_buy_price = (quantity*price + self.average_buy_price * self.bought) / (self.bought + quantity)
            self.bought += quantity
        
        if action == "S":
            quantity = -quantity
        self.transactions.append((date,quantity,price))

    def calculate_gain(self) -> float:
        """Calculates the gain from the transactions."""
        gain = self.average_sell_price * self.sold - self.average_buy_price * self.sold
        return gain

def read_file(filename: str) -> Dict[str, Book]:
    books: Dict[str, Book] = {}
    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace
            line = line.strip()
            if line:
                # Split the line into components
                parts = line.split()
                
                # Validate the format
                if len(parts) != 5:
                    print(f"Invalid format in line: {line}")
                    continue
                
                isbn: str = parts[0]
                if isbn not in books:
                    books[isbn] = Book(isbn)

                books[isbn].add_transaction(parts[1], parts[2], int(parts[3]), float(parts[4]))
    return books

def main() -> None:
    # Check if the file name is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    books = read_file(sys.argv[1])

    # strings can be constructed in a single loop instead of running the loop n times
    # for each book calculate the final inventory
    print("Available copies:")
    for key,value in books.items():
        print(f"\t{key}: {value.bought - value.sold}")

    print("")

    # for each month-year calculate the number of books sold
    monthly_sales: Dict[str, int] = {}
    for book in books.values():
        for transaction in book.transactions:
            month_year = transaction[0][3:10]
            if month_year not in monthly_sales:
                monthly_sales[month_year] = 0
            if transaction[1] < 0:
                monthly_sales[month_year] += abs(transaction[1])

    print("Sold books per month:")
    for month_year, sold in monthly_sales.items():
        if sold==0:
            continue
        print(f"\t{month[int(month_year[:2])-1]}, {month_year[3:]}: {sold}")
    
    print("")
    # for each book calculate the gain
    print("Gain per book:")
    for key, value in books.items():
        gain = value.calculate_gain()
        print(f"\t{key}: {gain:.1f} (avg: {(gain)/value.sold:.1f}, sold: {value.sold})")
    
    

if __name__ == "__main__":
    main()