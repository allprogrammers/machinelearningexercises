import sys
import math
from datetime import datetime
from typing import List, Dict, Tuple
from bisect import insort

class Buses:
    def __init__(self, busid: str, route: str) -> None:
        self.busid: str = busid
        self.route: str = route
        self.checkpoints: List[Tuple[float, float, int]] = []  # List of (x, y, checking_time)
        self.distance: float = 0.0

    def add_checkpoint(self, x: float, y: float, checking_time: int) -> None:
        """Add a checkpoint in sorted order based on checking_time."""
        # Insert the checkpoint in the correct position to maintain order
        insort(self.checkpoints, (x, y, checking_time))
    
    def update_distance(self) -> None:
        self.distance = 0.0
        for i in range(1, len(self.checkpoints)):
            self.distance += self.calculate_distance(
                self.checkpoints[i - 1][0], self.checkpoints[i - 1][1],
                self.checkpoints[i][0], self.checkpoints[i][1]
            )

    def calculate_distance(self, x1: float, y1: float, x2: float, y2: float) -> float:
        """Calculate the Pythagorean distance between two points."""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def calculate_speed(self) -> float:
        """Calculate the speed of the bus based on its distance and time between first and last checkpoints."""
        if len(self.checkpoints) < 2:
            return 0.0
        timediff = self.checkpoints[-1][2] - self.checkpoints[0][2]
        return self.distance / timediff if timediff > 0 else 0.0

def read_file(filename: str) -> Dict[str, Buses]:
    buses: Dict[str, Buses] = {}
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
                
                busid: str = parts[0]
                route: str = parts[1]
                x: float = float(parts[2])
                y: float = float(parts[3])
                checking_time: int = int(parts[4])
                if busid not in buses:
                    buses[busid] = Buses(busid, route)
                buses[busid].add_checkpoint(x, y, checking_time)
    return buses

def handle_route(buses: Dict[str, Buses], route: str) -> None:
    """Handle the -l flag: Calculate average speed for a specific route."""
    route_buses: List[Buses] = [bus for bus in buses.values() if bus.route == route]
    if not route_buses:
        print(f"No buses found for route {route}.")
        return
    
    speeds_sum = 0
    for bus in route_buses:
        speed = bus.calculate_speed()
        speeds_sum += speed
    average_speed = speeds_sum / len(route_buses) if route_buses else 0
    print(f"{route} - Avg speed: {average_speed:.2f}")

def main() -> None:
    # Check if the file name is provided as a command-line argument
    if len(sys.argv) < 3:
        print("Usage: python main.py <filename> [-b <busid> | -l <routenumber>]")
        sys.exit(1)

    # Get the file name from the command-line arguments
    filename: str = sys.argv[1]
    flag: str = sys.argv[2]

    buses: Dict[str, Buses] = read_file(filename)

    for key,value in buses.items():
        value.update_distance()

    if flag == "-b" and len(sys.argv) == 4:
        busid: str = sys.argv[3]
        print(f"{busid} - Total Distance: {buses[busid].distance:.1f}")
    elif flag == "-l" and len(sys.argv) == 4:
        route: str = sys.argv[3]
        handle_route(buses, route)
    else:
        print("Invalid arguments. Usage: python main.py <filename> [-b <busid> | -l <routenumber>]")

if __name__ == "__main__":
    main()