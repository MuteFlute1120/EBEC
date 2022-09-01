"""
Author: Warren Groscost, wgroscos@purdue.edu
Assignment: 01.2 - Interest
Date: 09/01/2022

Description:
    Determins the final value of a bank account after a given number of years, average interest, initial deposit, and number of times the account receives interest.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():
    print('Enter the following parameters.')
    deposit = float(input('  The initial deposit? ')) #Asks user to provide initial deposit amount.
    avg_interest = float(input('  The annual interest rate in percent? ')) #Asks user to provide the average interest
    time = float(input('  The number of years the account earn interest? ')) #Asks user to provide the time the account will be earning interest in years
    compounds = float(input('  The number of times interest is compounded each year: ')) #Asks user to provide the number of times the money compounds per year
    final_value = deposit * (1 + ((avg_interest / 100) / compounds)) ** (compounds * time) #Calculates the final value of the account given these conditions.
    print('The balance of this account will be ${} after {} years.'.format(format(final_value, ',.2f'), time))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
