def validate_siteswap(pattern):
    try:
        n = len(pattern)
        throws = [int(x) for x in pattern]
        
        # Check if the number of balls is an integer
        num_balls = sum(throws) / n
        if not num_balls.is_integer():
            return f"{pattern}: invalid # of balls"
        
        # Check if the pattern is valid
        landing_times = set()
        for i, throw in enumerate(throws):
            landing_time = (i + throw) % n
            if landing_time in landing_times:
                return f"{pattern}: invalid pattern"
            landing_times.add(landing_time)
        
        return f"{pattern}: valid with {int(num_balls)} balls"
    except ValueError:
        return f"{pattern}: invalid input (non-integer throws)"

# Read input and process patterns
while True:
    try:
        pattern = input().strip()
        print(validate_siteswap(pattern))
    except EOFError:
        break