import sys

class BinaryIndexedTree:
    def __init__(self, size):
        self.N = size + 2  # Extra space to handle 1-based indexing
        self.tree = [0] * (self.N)

    def update(self, idx, delta):
        """
        Increment the value at position 'idx' by 'delta'.
        """
        while idx < self.N:
            self.tree[idx] += delta
            idx += idx & -idx  # Move to the next responsible node

    def query(self, idx):
        """
        Compute the prefix sum from index 1 to 'idx'.
        """
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx  # Move to the parent node
        return res

def simulate_movie_collection(m, r, requests):
    """
    Simulates the movie collection process.

    Parameters:
    - m (int): Number of movies initially in the stack.
    - r (int): Number of locate requests.
    - requests (List[int]): List of movie IDs to locate and move to the top.

    Returns:
    - List[int]: Number of movies above each requested movie before it was moved.
    """
    # Total positions needed: initial movies + all possible new top positions
    total_positions = m + r + 1
    bit = BinaryIndexedTree(total_positions)

    # Initialize movie positions. Assign initial positions from (r + 1) to (r + m)
    positions = {}
    for movie in range(1, m + 1):
        positions[movie] = r + movie
        bit.update(r + movie, 1)  # Mark the presence of the movie in BIT

    current_top = r  # Next available top position
    results = []

    for movie in requests:
        pos = positions[movie]
        # Query how many movies are above the current movie
        res = bit.query(pos - 1)
        results.append(res)

        # Move the movie to the top:
        bit.update(pos, -1)        # Remove the movie from its current position
        bit.update(current_top, 1) # Place the movie at the new top position
        positions[movie] = current_top  # Update the movie's position mapping
        current_top -= 1  # Update the next available top position

    return results

input = sys.stdin.read().split()
idx = 0
n = int(input[idx])
idx += 1
for _ in range(n):
    m = int(input[idx])
    r = int(input[idx + 1])
    idx += 2
    requests = list(map(int, input[idx:idx + r]))
    idx += r
    results = simulate_movie_collection(m, r, requests)
    print(' '.join(map(str, results)))
