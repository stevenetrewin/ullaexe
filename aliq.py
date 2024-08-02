# Example combining iterating over a list and accessing items in a dictionary
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]

for person in data:
    print(f"Name: {person['name']}, Age: {person['age']}")
