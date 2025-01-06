def is_palindrome(input_string):
    input_string = input_string.lower() # Convert to lowercase
    input_string = input_string.replace(' ','') # Remove spaces
    return input_string == input_string[::-1] # Check if the string is the samr backward as forward