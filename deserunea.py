def length_comparator(s):
    return len(s)

string_list = ["apple", "banana", "cherry"]
sorted_list = sorted(string_list, key=length_comparator)
