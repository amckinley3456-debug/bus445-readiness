def mean_and_max(numbers):
    mean_value = sum(numbers) / len(numbers)
    max_value = max(numbers)
    return mean_value, max_value

print("Hello, I am Aidan McKinley, and my student ID is R08882231.")

my_numbers = [4, 8, 15, 16, 23, 42]
avg, top = mean_and_max(my_numbers)
print(f"Mean: {avg}, Max: {top}")
