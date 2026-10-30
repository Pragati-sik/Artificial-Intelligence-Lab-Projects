
from collections import deque

# Function to check whether a state is valid
def is_valid(m, c, total_m, total_c):

    # Condition 1: Number cannot be negative
    # or greater than the total population
    if m < 0 or c < 0 or m > total_m or c > total_c:
        return False

    # Calculate people on the right bank
    rm = total_m - m
    rc = total_c - c

    # Condition 2: Cannibals should not outnumber
    # missionaries on the left bank
    if m > 0 and c > m:
        return False

    # Condition 3: Cannibals should not outnumber
    # missionaries on the right bank
    if rm > 0 and rc > rm:
        return False

    return True


# BFS function
def bfs(total_m, total_c):

    # Initial state
    # (Missionaries, Cannibals, Boat Position)
    start = (total_m, total_c, 0)

    # Goal state
    goal = (0, 0, 1)

    # Possible boat movements
    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    # Create queue and visited set
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:

        state, path = queue.popleft()

        # Check goal condition
        if state == goal:
            return path

        m, c, boat = state

        # Try all possible boat movements
        for dm, dc in moves:

            # Boat is on left bank
            if boat == 0:
                new_state = (m - dm, c - dc, 1)

            # Boat is on right bank
            else:
                new_state = (m + dm, c + dc, 0)

            # Check valid state and boat movement
            if (is_valid(new_state[0], new_state[1],
                         total_m, total_c)
                and new_state not in visited):

                visited.add(new_state)

                queue.append(
                    (new_state, path + [new_state])
                )

    return None


# Main program
print("MISSIONARIES AND CANNIBALS PROBLEM")
print("----------------------------------")

# Take input from user
M = int(input("Enter number of Missionaries: "))
C = int(input("Enter number of Cannibals: "))

# Check input conditions
if M < 0 or C < 0:
    print("Invalid input! Numbers cannot be negative.")

elif M == 0 and C == 0:
    print("Please enter at least one person.")

else:
    # Find solution using BFS
    solution = bfs(M, C)

    if solution:

        print("\nSOLUTION FOUND!")
        print("Total Crossings:", len(solution) - 1)
        print("----------------------------------")

        for i, state in enumerate(solution):

            m, c, boat = state

            # Calculate right bank members
            rm = M - m
            rc = C - c

            print("\nStep:", i)

            print("Left Bank :",
                  m, "Missionaries,",
                  c, "Cannibals")

            print("Right Bank:",
                  rm, "Missionaries,",
                  rc, "Cannibals")

            if boat == 0:
                print("Boat Position: LEFT")
            else:
                print("Boat Position: RIGHT")

            print("----------------------------------")

    else:
        print("\nNo solution exists for these numbers.")
