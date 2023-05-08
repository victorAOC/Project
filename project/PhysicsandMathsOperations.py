
# Ask the user if they want to perform math or physics calculations
print("Do you want to perform a math or physics calculation?")
calculation_type = input().lower()

if calculation_type == "math":
    # Create an instance of the Math class
    math = Math()

    # Ask the user what operation they want to perform
    print("What operation do you want to perform? (add, subtract, multiply, divide, power)")
    operation = input().lower()

    # Ask for the two numbers to perform the calculation on
    print("Enter the first number:")
    a = float(input())
    print("Enter the second number:")
    b = float(input())

    # Perform the requested operation and print the result
    if operation == "add":
        result = math.add(a, b)
    elif operation == "subtract":
        result = math.subtract(a, b)
    elif operation == "multiply":
        result = math.multiply(a, b)
    elif operation == "divide":
        result = math.divide(a, b)
    elif operation == "power":
        result = math.power(a, b)
    else:
        print("Invalid operation")
        result = None

    if result is not None:
        print("Result:", result)

elif calculation_type == "physics":
    # Create an instance of the Physics class
    physics = Physics()

    # Ask the user what operation they want to perform
    print("What operation do you want to perform? (distance, velocity, acceleration, force, work)")
    operation = input().lower()

    # Ask for the input values required by the operation
    if operation == "distance":
        print("Enter velocity:")
        v = float(input())
        print("Enter time:")
        t = float(input())
        result = physics.distance(v, t)
    elif operation == "velocity":
        print("Enter distance:")
        d = float(input())
        print("Enter time:")
        t = float(input())
        result = physics.velocity(d, t)
    elif operation == "acceleration":
        print("Enter final velocity:")
        v = float(input())
        print("Enter initial velocity:")
        u = float(input())
        print("Enter time:")
        t = float(input())
        result = physics.acceleration(v, u, t)
    elif operation == "force":
        print("Enter mass:")
        m = float(input())
        print("Enter acceleration:")
        a = float(input())
        result = physics.force(m, a)
    elif operation == "work":
        print("Enter force:")
        f = float(input())
        print("Enter distance:")
        d = float(input())
        result = physics.work(f, d)
    else:
        print("Invalid")





