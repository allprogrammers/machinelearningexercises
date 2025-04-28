import sys
import numpy as np

def main():
    players = []
    scores = np.empty((5,0), dtype=float)
    print(scores.shape)
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            players.append((parts[0], parts[1],parts[2]))
            #append the score to the scores array 
            score = np.array(parts[3:8],dtype=float).reshape(5,1)
            scores = np.append(scores, score, axis=1)


    print(scores)
    # sum all the scores except the min and the max
    sumscores = scores.sum(axis=0)
    print(sumscores)
    sumscores = sumscores - scores.max(axis=0) - scores.min(axis=0)
    print(sumscores)



if __name__ == "__main__":
    main()