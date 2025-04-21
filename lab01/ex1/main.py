import sys

def calculate_average_score(scores_list):
    """
    Calculate the average score by ignoring the max and min values
    and averaging the remaining three scores.
    """
    if len(scores_list) != 5:
        raise ValueError("Scores list must contain exactly 5 scores.")
    
    # Sort the scores and ignore the max and min
    min = scores_list[0]
    max = scores_list[0]
    sum = 0
    for score in scores_list:
        if score < min:
            min = score
        if score > max:
            max = score
        sum += score
    # Remove the min and max from the sum
    sum -= min + max
    average_score =  sum/ 3  # Average the middle three scores
    return average_score

def read_file(filename):
    scores = []
    try:
        # Open the file and read its content
        with open(filename, 'r') as file:
            for line in file:
                # Strip any leading/trailing whitespace
                line = line.strip()
                if line:
                    # Split the line into components
                    parts = line.split()
                    
                    # Validate the format
                    if len(parts) != 8:
                        print(f"Invalid format in line: {line}")
                        continue
                    
                    name = parts[0]
                    surname = parts[1]
                    country_code = parts[2]
                    try:
                        # Ensure the country code is 3 letters
                        if len(country_code) != 3 or not country_code.isalpha():
                            raise ValueError("Invalid country code")
                        
                        # Parse the 5 floating-point numbers
                        scores_list = [float(num) for num in parts[3:]]
                        
                        # Append the parsed data as a dictionary
                        scores.append({
                            "name": name,
                            "surname": surname,
                            "country_code": country_code,
                            "scores": scores_list,
                        })
                    except ValueError as ve:
                        print(f"Error parsing line: {line} - {ve}")
                        continue
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return scores

def main():
    # Check if the file name is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    # Get the file name from the command-line arguments
    filename = sys.argv[1]
    players = read_file(filename)
    # Print the top three players
    print("Final Ranking:")
    for player in players:
        player['average_score'] = calculate_average_score(player['scores'])
    

        # Sort players by average score in descending order
        players.sort(key=lambda x: x['average_score'], reverse=True)
        for i in range(3):
            if i < len(players):
                player = players[i]
                # Print the player's name, surname, and average score
                print(f"{i + 1}: {player['name']} {player['surname']} - Score: {player['average_score']:.2f}")
            else:
                break
        
        # Group scores by country and calculate total scores
        country_scores = {}
        max_country_score = 0
        max_country_name = ""
        for player in players:
            country = player["country_code"]
            country_scores[country] = country_scores.get(country, 0) + player["average_score"]
            if country_scores[country] > max_country_score:
                max_country_score = country_scores[country]
                max_country_name = country
        
        # Find the country with the highest total score
        print("\nBest Country:")
        print(f"{max_country_name} - Total score: {max_country_score:.2f}")

if __name__ == "__main__":
    main()