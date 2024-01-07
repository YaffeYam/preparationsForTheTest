print ("Successful function executes: ")
def successful_function():
    try:
        # Try to execute the code inside this block
        print("First function executed successfully")
        return True
    except Exception as e:
        # Handle any exceptions that might occur
        print(f"Error in first_function: {e}")
        return False

def second_function():
    try:
        # Try to execute the code inside this block
        print("Second function executed successfully")
    except Exception as e:
        # Handle any exceptions that might occur
        print(f"Error in second_function: {e}")

# Call the first function and check if it executed successfully
if successful_function():
    # If first_function was successful, call the second function
    second_function()
else:
    # If there was an error in first_function, print a message
    print("Skipping second_function due to an error in first_function")

print ("--------------------------------------")
