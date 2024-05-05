# Open a file in write mode ('w')
# The 'with' statement ensures that the file is properly closed after its suite finishes,
# even if an exception is raised during the execution
with open('output.txt', 'w') as file:
    # Write some text to the file using the 'write()' method
    file.write("Hello, world!\n")  # Writing the string "Hello, world!" followed by a newline
    file.write("This is a test file.\n")  # Writing the string "This is a test file." followed by a newline
    file.write("Writing to a file in Python is easy!")  # Writing the string "Writing to a file in Python is easy!"

# References:
# Python documentation on file input/output operations:
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
