from typing import Dict, List, Tuple
from collections import defaultdict
from datetime import datetime

def read_file(filename: str) -> List[str]:
    """Reads the file and returns a list of lines."""
    with open(filename, 'r') as file:
        return file.readlines()

def process_transactions(lines: List[str]) -> None:
    """Processes the transactions and computes the required statistics."""
    available_copies: Dict[str, int] = defaultdict(int)
    sold_copies: Dict[str, int] = defaultdict(int)
    sold_books_per_month: Dict[str, int] = defaultdict(int)
    gains_per_book: Dict[str, Tuple[float, int]] = defaultdict(lambda: (0.0, 0))  # (total gain, total sold)

    for line in lines:
        # Parse the line
        parts = line.strip().split()
        if len(parts) != 5:
            print(f"Invalid line format: {line}")
            continue
        
        isbn, transaction_type, date, num_copies, price_per_copy = parts
        num_copies = int(num_copies)
        price_per_copy = float(price_per_copy)
        date_obj = datetime.strptime(date, "%d/%m/%Y")
        month_year = date_obj.strftime("%B, %Y")

        if transaction_type == "B":  # Books bought
            available_copies[isbn] += num_copies
        elif transaction_type == "S":  # Books sold
            if available_copies[isbn] >= num_copies:
                available_copies[isbn] -= num_copies
                sold_copies[isbn] += num_copies
                sold_books_per_month[month_year] += num_copies
                total_gain, total_sold = gains_per_book[isbn]
                gains_per_book[isbn] = (total_gain + num_copies * price_per_copy, total_sold + num_copies)
            else:
                print(f"Error: Not enough copies of {isbn} to sell {num_copies} copies.")

    # Output results
    print("Available copies:")
    for isbn, count in available_copies.items():
        print(f"{isbn}: {count}")

    print("\nSold books per month:")
    for month_year, count in sold_books_per_month.items():
        print(f"{month_year}: {count}")

    print("\nGain per book:")
    for isbn, (total_gain, total_sold) in gains_per_book.items():
        avg_gain = total_gain / total_sold if total_sold > 0 else 0
        print(f"{isbn}: {total_gain:.1f} (avg {avg_gain:.1f}, sold {total_sold})")

def main() -> None:
    filename = "books.txt"
    lines = read_file(filename)
    process_transactions(lines)

if __name__ == "__main__":
    main()