
# Question 1 - Ask for number and check if odd or even. Print out appropriate message

num = int(input("Enter a number."))
mod = num % 2
if mod > 0:
    print("This is an odd number")
else:
    print("This is an even number")

# Question 2 - Check if string is palindrome

# Palindrome function

def isPalindrome(x):
    if x == x[::-1]:
        print(x, " is a palindrome")
    else:
        print(x, " is not a palindrome")


s = input("Please enter a word.")

isPalindrome(s)

# Question 3 - Take list of numbers and output the list ordered

listSize = int(input("Enter the size of the list."))

numList = list(int(num) for num in input("Enter a list of numbers, separated by spaces and equal to the length specified.").strip().split())[:listSize]
print("List Provided: ", numList)
newList = sorted(numList)
print("The list in ascending order is ", newList)

# Question 4 - Check if number is in input
value = int(input("Please provide a number to check if it is in the list generated above in Q3."))
value in newList

# Question 5 - Loop given list print all prime numbers.

a = [8, 9, 10, 11, 13, 81, 101, 100, 94]
answer = []

for num in a:
    if all(num % i != 0 for i in range(2, num)):
        print(num)

for num in a:
    if all(num % i != 0 for i in range(2, num)):
        answer.append(num)

print(answer)
