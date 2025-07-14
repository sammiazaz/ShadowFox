#Task 1
"""1. Create a variable named pi and store the value 22/7 in it.
Now check the data type of this variable."""

pi = 22 / 7
print("value of pi : ", pi)
print("data type of pi : ", type(pi))


#Task 2
"""2. Create a variable called for and assign it a value 4. See what
happens and find out the reason behind the behavior that you
see."""

# for  = 5  -> This will raise a SyntaxError because 'for' is a reserved keyword in Python.


#Task 3
""" 3. Store the principal amount, rate of interest, and time in
different variables and then calculate the Simple Interest for 3
years. Formula: Simple Interest = P x R x T / 100"""

P = float (input("Enter the principal amount : "))
R = float(input("Enter the Rate of intrest per year: "))
T = 3  # 3 Years

SI = (P * R * T) / 100


print(f"Principal (P): {P}")
print(f"Rate (R): {R}")
print(f"Time (T): {T}")
print(f"Simple Interest: {SI}")