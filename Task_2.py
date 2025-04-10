def print_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces for formatting the pyramid
        for j in range(n - i):
            print(" ", end="")

        # Print numbers in the current row
        for k in range(1, i + 1):
            print(k, end=" ")

        # Move to the next line after each row
        print()

# Example usage
n = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(n)

#OUTPUT
'''
Enter the number of rows for the pyramid: 3
  1 
 1 2 
1 2 3 '''