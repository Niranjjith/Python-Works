def print_pyramid(rows):
    spaces = rows - 1
    stars = 1
    while spaces >= 0:
        print(" " * spaces + "*" * stars)
        spaces -= 1
        stars += 2

rows = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(rows)