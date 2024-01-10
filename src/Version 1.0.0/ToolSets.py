# Imports
from Modules import *

# Convert_Text - Converts a string to an array of integers that correspond to the ascii code for a given value
# Input:
#   _string - String that is to be converted to an array of ascii integers
# Algorithm:
#   * Create an empty array where the ascii digits are supposed to be appended to
#   * Iterate over the string and append the corresponding ascii value to integer_list
#       * Append the ascii code to integer_list
#   * Return the array
# Output:
#   integer_list - Array of integer values pertaining to the ascii of a letter or character
def Convert_Text(_string):
    integer_list = []
    for i in _string:
        integer_list.append(ord(i))
    return integer_list

# Convert_Num - Converts an array of numbers representing ascii numbers for a given character
# Input:
#   _list - Array of integers that represent ascii codes for a given character
# Algorithm:
#   * Create an empty string where characters are to be appended to the string
#   * Iterate over the array and append the characters to the string
#       * Append the character in _list to _string
#   * Return the string
# Output:
#   _string - String that represents the converted array to string
def Convert_Num(_list):
    _string = ''
    for i in _list:
        _string += chr(i)
    return _string

# Convert_Binary_String - Converts a decimal number to binary
# Input:
#   _int - Integer value that is to represent a number in decimal that is to be converted to binary
# Algorithm:
#   * Create an empty string that will represent the binary number
#   * While _int is greater than 0
#       * Calculate the binary digit by taking the modulo of _int and 2
#       * Update the string value with this digit
#       * Update _int by calculating the floor of _int divided by 2
#   * Reverse the order of the string
#   * Return the string
# Output:
#   _string - String value that is equal to the binary number of the original integer _int
def Convert_Binary_String(_int):
    _string = ''
    while(_int > 0):
        bindig = _int % 2
        _string += str(bindig)
        _int = _int // 2
    _string = _string[::-1]
    return _string

# FME - A function to calculate Fast Modular Exponentiation (b^n mod m)
# Input:
#   b - Integer value that represents the base of of the FME (b) in (b^n mod m)
#   n - Integer value that represents the exponent value in FME (n) in (b^n mod m)
#   m - Integer value that represents the value that is being modulo'd against in FME (m) in (b^n mod m)
# Algorithm:
#   * Calculate the binary representation of n with Convert_Binary_String
#   * Reverse the binary number so that the last digit appears first in the array
#   * Set the return value (x) to 1
#   * Calculate power by taking the modulo of b and m
#   * Traverse the string of binary digits up to the length of the binary number
#       * Convert the string to an integer and store it in binVal
#       * If the current digit is a one, calculate x with (x * power) % m
#       * Update the power variable with (power * power) % m
#   * Return x after the for loop finishes completion
# Output:
#   x - Integer value that is returned from the expression of (b^n mod m)
def FME(b,n,m):
    DecInBin = Convert_Binary_String(n)
    DecInBin = DecInBin[::-1]
    x = 1
    power = b % m
    for i in DecInBin:
        binVal = int(i)
        if (binVal == 1):
            x = (x * power) % m
        power = (power * power) % m
    return x

# Euclidean_Alg - Greatest Common Divisor or Euclidean algorithm for two numbers a and b
# Input:
#   a - Integer value that represents the larger of the two values in the EEA calculation
#   b - Integer value that represents the smaller of the two values in the EEA calculation
# Algorithm:
#   * Assign values to the initial of a and b with m_0 and b_0
#   * Assign values to the initial Bezout coefficients s_1,t_1 with 1 and 0
#   * Assign values to the updated Bezout coefficients s_2,t_2 with 0 and 1
#   * Execute the while loop until b is less than or equal to 0 (usually equal to 0)
#       * Calculate the modulo of a and b and assign it to k
#       * Calculate the integer division of a and b and assign it to q
#       * Update a to the current value of b and b to to the current value of k
#       * Calculate new values for the Bezout coefficients S_1,T_1 with s_2,t_2
#       * Calculate the new updated Bezout coefficients S_2,T_2 with s_1 - q * s_2, t_1 - q * t_2
#       * Update the Bezout coefficients (which will eventually be returned) s_1,t_1 with S_1,T_1
#       * Update the updated Bezout coefficients s_2,t_2 with S_2,T_2
#   * Return the GCD (a) and the Bezout coefficients (s_1,t_1) as an array after the loop
# Output:
#   This algorithm returns an array of values related to the Extended Euclidean Algorithm
#   a - This is the GCD of the two original numbers a and b
#   s_1 - This is the first Bezout coefficient (s) that is returned
#   t_1 - This is the second Bezout coefficient (t) that is returned
def Euclidean_Alg(a,b):
    a_0,b_0 = a,b
    s_1,t_1 = 1,0
    s_2,t_2 = 0,1
    while (b > 0):
        k = a % b
        q = a // b
        a = b
        b = k
        S_1,T_1 = s_2,t_2
        S_2,T_2 = s_1 - q * s_2, t_1 - q * t_2
        s_1,t_1 = S_1,T_1
        s_2,t_2 = S_2,T_2
    return [a,s_1,t_1]

# Find_Public_Key_e - This function finds a public key e such that it is relatively prime to (p-1)(q-1)
# Input:
#   p - First prime number
#   q - Second prime number
# Algorithm:
#   * Calculate both (p-1) and (q-1) and store them as P and Q
#   * Calculate the product of p and q and store it as n
#   * Initialize e to be 2
#   * While the gcd(e,P*Q) is not 1 and e is not equal to both p and q
#       * Increment e by 1
#   * Return e and n in an array
# Output:
#   This function returns the public key e and n
def Find_Public_Key_e(p, q):
    P = p - 1
    Q = q - 1
    n = p * q
    e = 2
    while (Euclidean_Alg(e,P*Q)[0] != 1 and e != p and e != q):
        e += 1
    return [e,n]

# Find_Private_Key_d - This function returns the private key d from a public key e and two prime numbers p and q
# Input:
#   e - Public key that is calculated with Find_Public_Key_e
#   p - First prime number
#   q - Second prime number
# Algorithm:
#   * Calculate (p-1) and (q-1) and store them as P and Q respectively
#   * Calculate the modular inverse (the Bezout coefficient) of e and P*Q and store it as d
#   * If d is negative, add the modulo to it until it is positive
#   * Return d
# Output:
#   This function returns the public key d
def Find_Private_Key_d(e, p, q):
    P = p - 1
    Q = q - 1
    d = Euclidean_Alg(e,P*Q)[1]
    if (d < 0):
        while(d < 0):
            d += P*Q
    return d

# Encode - Encodes a string of text from a public key e and number n
# Input:
#   n - Integer value that is calculated with Find_Public_Key_e
#   e - Integer value that is calculated with Find_Public_Key_e
#   message - Message that is fed into the algorithm to by encoded
# Algorithm:
#   * Create an empty array called cipher_text
#   * Iterate over the characters in the message
#       * Calculate the integer value of char from Convert_Text
#       * Encode charNum with the use of FME and the value of e and n with charNum
#       * Append this value to cipher_text
#   * Return cipher_text
# Output:
#   This function returns an array of integers that represent encoded values from message
def Encode(n,e,message):
    cipher_text = []
    for char in message:
        charNum = Convert_Text(char)[0]
        encoded = FME(charNum,e,n)
        cipher_text.append(encoded)
    return cipher_text

# Decode - Decodes a message from an array of integers with private key d, n, and cipher_text
# Input:
#   n - Integer value that is calculated with Find_Public_Key_e
#   d - Integer value that is calculated with Find_Private_Key_d
#   cipher_text - Array of integers that represents an encoded message
# Algorithm:
#   * Create an empty container for the message that is to be returned
#   * Create an empty array to store the converted integers to strings in
#   * Iterate over the cipher_text array
#       * Calculate the ascii code for the given string with FME
#       * Append this ascii code to empty
#   * Decode the ascii values with Convert_Num and assign the result to message
#   * Return message
# Output:
#   This function returns the decoded message from cipher_text with private key d and n
def Decode(n,d,cipher_text):
    message = ''
    empty = []
    for num in cipher_text:
        numVal = FME(num,d,n)
        empty.append(numVal)
    message = Convert_Num(empty)
    return message

# IsPrime - Checks if a number is prime
# Input:
#   n - Integer that is being checked if it is a prime number
# Algorithm:
#   * Index from 2 up to the square root of n + 1
#       * If the modulo of n and i is zero, then the number is not prime
#       * Return False
#   * Return True if False is not returned
# Output:
#   This function returns a boolean value depending on whether or not an integer is prime
def IsPrime(n):
    for i in range(2,int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True

# GeneratePrime - Generates a prime number between two values a and b
# Input:
#   a - Integer value that represents the lower bound of the two integers
#   b - Integer value that represents the upper bound of the two integers
# Algorithm:
#   * Generate a random number in the range of a and b and assign it to start
#   * While the number that is generated is not prime
#       * Increment start by one
#       * If start reaches the upper bound equal to b
#           * Double b
#           * Set start back to a and continue the loop
#   * Return the prime number start after the loop ends execution
# Output:
#   start - Random prime number that is generated between a and b
def GeneratePrime(a,b):
    start = random.randrange(a,b)
    while (IsPrime(start) == False):
        start += 1
        if (start > b):
            b *= 2
            start = a
    return start