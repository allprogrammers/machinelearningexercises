from typing import Dict, List
from collections import defaultdict

def read_file(filename: str) -> List[str]:
    """Reads the file and returns a list of lines."""
    with open(filename, 'r') as file:
        return file.readlines()

def compute_statistics(lines: List[str]) -> None:
    """Computes and prints the required statistics."""
    births_per_city: Dict[str, int] = defaultdict(int)
    births_per_month: Dict[str, int] = defaultdict(int)
    month_names: List[str] = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    for line in lines:
        # Parse the line
        parts = line.strip().split()
        if len(parts) != 4:
            print(f"Invalid line format: {line}")
            continue
        
        name, surname, birthplace, birthdate = parts
        day, month, year = map(int, birthdate.split('/'))

        # Update statistics
        births_per_city[birthplace] += 1
        births_per_month[month_names[month - 1]] += 1

    # Compute average number of births per city
    total_births = sum(births_per_city.values())
    num_cities = len(births_per_city)
    average_births = total_births / num_cities if num_cities > 0 else 0

    # Print results
    print("Births per city:")
    for city, count in births_per_city.items():
        print(f"{city}: {count}")

    print("\nBirths per month:")
    for month, count in births_per_month.items():
        print(f"{month}: {count}")

    print(f"\nAverage number of births: {average_births:.2f}")

def main() -> None:
    filename = "people.txt"
    lines = read_file(filename)
    compute_statistics(lines)

if __name__ == "__main__":
    main()