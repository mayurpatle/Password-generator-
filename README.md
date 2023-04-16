# Password-generator-

In this program, we use Python's random module to generate a random password.
The string module provides a set of characters that we can use for the password, including ASCII letters, digits, and punctuation marks.

The generate_password() function takes an optional argument length, which specifies the length of the password to generate.
If no length is specified, the function defaults to generating an 8-character password.

To generate the password, we use a list comprehension to choose a random character from the character set chars for each position in the password.
The resulting list of characters is joined together into a single string using the join() method.

Finally, we print the generated password to the console.
