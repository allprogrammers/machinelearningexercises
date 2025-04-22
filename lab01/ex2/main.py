import sys

class Buses:
    def __init__(self, busid, route, x, y, checking_time):
        self.busid = busid
        self.route = route
        self.x = x
        self.y = y
        self.checking_time = checking_time

def read_file(filename):
    buses = []
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
                
                busid = parts[0]
                route = parts[1]
                x = parts[2]
                y = parts[3]
                checking_time = parts[4]
                buses.append(Buses(busid, route, x, y, checking_time))
    return buses
                
def main():
    # Check if the file name is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    # Get the file name from the command-line arguments
    filename = sys.argv[1]

    buses = read_file(filename)

    

if __name__ == "__main__":
    main()