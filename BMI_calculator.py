def bmi_calculation():
    keep_running = True
    value = None
    msg = None
    while keep_running:
        mode = int(input("Choose Calculation Mode: \n1. kilograms in weight and meters in height\n2. pounds in weight and inches in height\nYour Choice: "))
        if mode == 1:
            weight_kg = float(input("What's your weight in kilograms: "))
            height_m = float(input("What's your height in meters: "))
            value = weight_kg/(height_m**2)
            keep_running = False
        elif mode == 2:
            weight_lbs = float(input("What's your weight in pounds: "))
            height_in = float(input("What's your height in inches: "))
            value = 703 * weight_lbs / (height_in**2)
            keep_running = False
        else:
            print("Please type 1 or 2")

        if value is None:
            msg = "None"
        elif value < 18.5:
            msg = "Underweight"
        elif 18.5 <= value < 25:
            msg = "Normal Weight"
        elif 25 <= value < 29.9:
            msg = "Overweight"
        else:
            msg = "Obese"

        print("Your BMI is {}".format(value))
        print("You are {}".format(msg))

bmi_calculation()