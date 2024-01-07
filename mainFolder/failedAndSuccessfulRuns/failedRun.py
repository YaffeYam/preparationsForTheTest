print ("--------------------------------------")
print ("Failing function executes: ")
def failing_function():
    try:
        # Raise a ValueError intentionally to simulate an error
        raise ValueError("Intentional error in first_function")
        
        # This line won't be reached if the ValueError is raised
        print ("First function executed successfully")
        
        # If no error occurs, return True
        return True
    except Exception as e:
        # Handle any exception that occurs during the try block
        print(f"Error in first_function: {e}")
        
        # If an error occurs, return False
        return False

def second_function():
    try:
        # Print a success message if no error occurs
        print("Second function executed successfully")
    except Exception as e:
        # Handle any exception that occurs during the try block
        print(f"Error in second_function: {e}")

# Call the first function and check its return value
if failing_function():
    # If the first function succeeds, call the second function
    second_function()
else:
    # If the first function fails, print a message
    print("Skipping second_function due to an error in first_function")

print ("--------------------------------------")