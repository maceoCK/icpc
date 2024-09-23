def calculate_disguises(test_cases):
    results = []
    for attributes in test_cases:
        category_count = {}
        
        # Count attributes in each category
        for name, category in attributes:
            if category in category_count:
                category_count[category] += 1
            else:
                category_count[category] = 1
        
        # Calculate the number of possible disguises
        total_combinations = 1
        for count in category_count.values():
            total_combinations *= (count + 1)  # (count + 1) includes not choosing from this category
        
        # Subtract the case where no attribute is chosen at all
        distinct_disguises = total_combinations - 1
        results.append(distinct_disguises)
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

# Number of test cases
t = int(data[0])
index = 1

test_cases = []
for _ in range(t):
    n = int(data[index])
    index += 1
    attributes = []
    for _ in range(n):
        name, category = data[index].split()
        attributes.append((name, category))
        index += 1
    test_cases.append(attributes)

results = calculate_disguises(test_cases)
for result in results:
    print(result)
