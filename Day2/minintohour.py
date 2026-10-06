def convert_minutes(total_minutes):
    # Calculate total hours using integer division
    hours = total_minutes // 60
    
    # Calculate remaining minutes using modulo
    remaining_minutes = total_minutes % 60
    
    return hours, remaining_minutes

# Get input from the user
try:
    minutes = int(input("Enter the number of minutes: "))
    
    # Convert and print the result
    hours, remaining_minutes = convert_minutes(minutes)
    
    if hours == 0:
        print(f"{minutes} minutes is equal to {remaining_minutes} minutes.")
    else:
        print(f"{minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")
        
except ValueError:
    print("Please enter a valid integer number.")
