print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: Jules Rafael J. Mag-isa")
print(' ')
print("Problem: Create python program that displays all prime numbers within a range:")
print(' ')
print("RULES TO CONSIDER:")
print("[1] If number[start] is a negative number. The program will prompt a message:", """ "Enter a non-negative number" """)
print("[2] If number[end] is less than number[start]. The program will prompt a message:", """ "Enter a number greater than number[start]" """)
print("[3] If the user enter a number"""" "0", """"the program will terminate.")
print('')

def prime(x, y):
    prime_list = []
    for i in range(x, y ):
        if i <= 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0 or i < 1:
                    break
            else:
                prime_list.append(i)
    return prime_list

start = int(input("Enter a number [start]:"))
end = int(input("Enter a number [end]:"))
print(' ')
first = prime(start, end)
if len(first) >= 1:
    print("Prime numbers between", start, "and", end, "are:", first)
elif start > end:
    print("Enter a number greater than", start)
elif start < 0 and end >= 1:
    print("Enter a non-negative number.")
else:
    print("Program terminated.")