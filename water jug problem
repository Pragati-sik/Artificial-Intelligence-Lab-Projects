
# Goal: Get exactly 2 litres in Jug 1

from collections import deque
from math import gcd

# Take jug capacities from the user
jug1 = int(input("Enter capacity of Jug 1 (in litres): "))
jug2 = int(input("Enter capacity of Jug 2 (in litres): "))

TARGET = 2

# Check whether the input is valid
if jug1 <= 0 or jug2 <= 0:
    print("Jug capacities must be greater than zero.")

elif TARGET > max(jug1, jug2):
    print("It is impossible to get 2 litres in Jug 1.")

elif TARGET % gcd(jug1, jug2) != 0:
    print("It is impossible to measure exactly 2 litres.")

else:
    # Initial state: both jugs are empty
    initial_state = (0, 0)

    # Queue stores states that we need to explore
    queue = deque([(initial_state, [])])

    # Visited states prevent repeated work
    visited = {initial_state}

    solution = None

    # Search for a sequence of operations
    while queue:
        (x, y), path = queue.popleft()

        # Check whether Jug 1 contains exactly 2 litres
        if x == TARGET:
            solution = path + [(x, y, "Goal reached")]
            break

        # RULE 1: Fill Jug 1 completely
        next_states = [
            (jug1, y, "Rule 1: Fill Jug 1")
        ]

        # RULE 2: Fill Jug 2 completely
        next_states.append(
            (x, jug2, "Rule 2: Fill Jug 2")
        )

        # RULE 3: Empty Jug 1
        next_states.append(
            (0, y, "Rule 3: Empty Jug 1")
        )

        # RULE 4: Empty Jug 2
        next_states.append(
            (x, 0, "Rule 4: Empty Jug 2")
        )

        # RULE 5: Pour Jug 1 into Jug 2
        amount = min(x, jug2 - y)
        next_states.append(
            (x - amount, y + amount,
             "Rule 5: Pour Jug 1 into Jug 2")
        )

        # RULE 6: Pour Jug 2 into Jug 1
        amount = min(y, jug1 - x)
        next_states.append(
            (x + amount, y - amount,
             "Rule 6: Pour Jug 2 into Jug 1")
        )

        # RULE 7: Keep the current state if no new
        # operation is possible (no change)
        next_states.append(
            (x, y, "Rule 7: No change")
        )

        # Add valid, unexplored states to the queue
        for new_x, new_y, rule in next_states:
            state = (new_x, new_y)

            if state not in visited:
                visited.add(state)

                new_path = path + [
                    (new_x, new_y, rule)
                ]

                queue.append((state, new_path))

    # Display the solution
    if solution:
        print("\nSolution found!\n")
        print("Step\tJug 1\tJug 2\tOperation")
        print("-" * 65)

        print("0\t0\t0\tInitial State")

        for step, (x, y, operation) in enumerate(solution, 1):
            print(f"{step}\t{x}\t{y}\t{operation}")

        print("\nGoal: Exactly 2 litres in Jug 1.")
    else:
        print("No solution found.")
