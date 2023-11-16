# Function to find the GCD of two numbers
def gcd(a, b):
    while b != 0:
        remainder = a % b  
        a = b 
        b = remainder  
    return a  


# Function to find the extended GCD of two numbers
def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1 
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - quotient * x1
        y0, y1 = y1, y0 - quotient * y1
    return a, x0, y0  


if __name__ == "__main__":
    while True:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        gcd_result = gcd(num1, num2)
        extended_gcd_result = extended_gcd(num1, num2)
        print(f"GCD({num1}, {num2}) = {gcd_result}.")
        print(f"Bezout's coefficients for {num1}x and {num2}y are: x = {extended_gcd_result[1]}, y = {extended_gcd_result[2]}.")