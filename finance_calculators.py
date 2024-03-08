import math
# Present 2 option to users.
print("""This program can help you with 2 calculations:
Investment - calculate the amount of interest you'll earn on your investment
Bond       - calculate the amount you'll have to pay on a home loan""")

# Request users to select either 'investment' or 'bond'.
# If user does not input 'investment' or 'bond', program will repeat the input request.

while True: 
    calculation_type = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ")


    # If user selects 'investment', ask user to insert amount of money, interest rate, number of years they are investing.
    # Ask user if they want to calculate the simple or compound interest.
    # If user selects 'simple', insert details into the simple interest formula and print the total interest.
    # If user selects 'compound', insert details into the compound interest formula and print the total interest.

    if calculation_type.lower() == "investment":
        print("You have chosen to calculate your investment.")
        while True:
            try:
                amount_money = float(input("Insert the full amount of money you are depositing: "))
                interest_rate = float(input("Insert the interest rate as a percentage. Do not include the percentage sign: "))
                years = float(input("Insert the number of years to plan to invest: "))
                break
            except ValueError:
                print("You have not entered a number.")
        
        while True:
            interest = input("Insert which type of interest you would like to calculate: 'simple' or 'compound': ")

            if interest.lower() == "simple":
                r = interest_rate / 100     # Divide the percentage by 100
                simple_interest = amount_money *(1 + r*years)   # Formula for simple interest
                print(f"Your total amount once simple interest has been applied is £{simple_interest}.")
                break

            elif interest.lower() == "compound":
                r = interest_rate / 100      
                compound_interest = amount_money * math.pow((1+r),years)    # Formula for compound interest
                print(f"Your total amount once compound interest has been applied is £{round(compound_interest,2)}.")     
                break

            else:
                print("Error. You have not selected 'simple' or 'compound' interest.")
        break
    # If user selects 'bond', ask user to insert present value of house, interest rate, and number of months they are repaying loan.
    # Insert details into the bond formula and print the total repaid each month.

    elif calculation_type.lower() == "bond":
        print("You have chosen to have calculate your bonds.")
        present_value = float(input("Please insert the present value of the house. Do not include the currency."))
        interest_rate = float(input("Insert the interest rate as a percentage. Do not include the percentage sign: "))
        months = float(input("Please insert the number of months you plan you repay the loan over:"))

        r = interest_rate / 100
        i = r/12
        repayment = (i * present_value)/(1 - (1 + i)**(-months))    # Formula for bond repayment

        print(f"The total amount you will have to repay each month is £{repayment}.")
        break
    
    # If user did not select 'investment' or 'bond', print error code.     
    else:
        print("Error. You have not selected 'investment' or 'bond'.")





