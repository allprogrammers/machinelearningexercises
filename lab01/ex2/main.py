import sys
import math
from datetime import datetime

class Buses:
    def __init__(self, busid, route):
        self.busid = busid
        self.route = route
        self.checkpoints = [] #x, y, checking_time
        self.distance = 0

    def add_checkpoint(self, x, y, checking_time):
        self.checkpoints.append((x, y, checking_time))
        if len(self.checkpoints) > 1:
            self.distance += self.calculate_distance(
                self.checkpoints[-2][0], self.checkpoints[-2][1],
                x, y
            )

    def calculate_distance(self,x1, y1, x2, y2):
        """Calculate the Pythagorean distance between two points."""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def calculate_speed(self):
        """Calculate the speed of the bus based on its distance and time between first and last checkpoints."""
        if len(self.checkpoints) < 2:
            return 0
        timediff = self.checkpoints[-1][2] - self.checkpoints[0][2]
        return self.distance / timediff if timediff > 0 else 0

def read_file(filename):
    buses = {}
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
                x = float(parts[2])
                y = float(parts[3])
                checking_time = parts[4]
                if busid not in buses:
                    buses[busid] = Buses(busid, route)
                buses[busid].add_checkpoint(x, y, checking_time)
    return buses



def calculate_speed(distance, time1, time2):
    """Calculate speed given distance and time difference."""
    time_format = "%H:%M:%S"  # Assuming time is in HH:MM:SS format
    t1 = datetime.strptime(time1, time_format)
    t2 = datetime.strptime(time2, time_format)
    time_diff = (t2 - t1).total_seconds() / 3600  # Convert seconds to hours
    return distance / time_diff if time_diff > 0 else 0


def handle_route(buses, route):
    """Handle the -l flag: Calculate average speed for a specific route."""
    route_buses = [bus for bus in buses if bus.route == route]
    if not route_buses:
        print(f"No buses found for route {route}.")
        return

    bus_ids = set(bus.busid for bus in route_buses)
    total_speed = 0
    valid_buses = 0

    for busid in bus_ids:
        bus_points = [bus for bus in route_buses if bus.busid == busid]
        if len(bus_points) < 2:
            continue

        total_distance = 0
        for i in range(len(bus_points) - 1):
            total_distance += calculate_distance(
                bus_points[i].x, bus_points[i].y,
                bus_points[i + 1].x, bus_points[i + 1].y
            )

        speed = calculate_speed(
            total_distance,
            bus_points[0].checking_time,
            bus_points[-1].checking_time
        )
        if speed > 0:
            total_speed += speed
            valid_buses += 1

    if valid_buses > 0:
        average_speed = total_speed / valid_buses
        print(f"Average speed for route {route}: {average_speed:.2f}")
    else:
        print(f"Not enough data to calculate average speed for route {route}.")

def main():
    # Check if the file name is provided as a command-line argument
    if len(sys.argv) < 3:
        print("Usage: python main.py <filename> [-b <busid> | -l <routenumber>]")
        sys.exit(1)

    # Get the file name from the command-line arguments
    filename = sys.argv[1]
    flag = sys.argv[2]

    buses = read_file(filename)

    if flag == "-b" and len(sys.argv) == 4:
        busid = sys.argv[3]
        print(f"{busid} - Total Distance: {buses[busid].distance:.1f}")
    elif flag == "-l" and len(sys.argv) == 4:
        route = sys.argv[3]
        handle_route(buses, route)
    else:
        print("Invalid arguments. Usage: python main.py <filename> [-b <busid> | -l <routenumber>]")

if __name__ == "__main__":
    main()