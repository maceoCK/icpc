def solve_ghost_leg(N, K, legs):
    # Initialize the board
    board = list(range(N))
    
    # Sort legs by their vertical position (Bi)
    legs.sort(key=lambda x: x[1])
    
    # Process each leg
    for Ai, _ in legs:
        # Swap the characters at positions Ai and Ai+1
        board[Ai], board[Ai+1] = board[Ai+1], board[Ai]
    
    # Create the result array
    result = [0] * N
    for i, char in enumerate(board):
        result[char] = i
    
    return result

# Read input
N, K = map(int, input().split())
legs = [tuple(map(int, input().split())) for _ in range(K)]

# Solve and print the result
result = solve_ghost_leg(N, K, legs)
print(*result)