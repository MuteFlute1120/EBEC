"""
Author: Warren Groscost, wgroscos@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 09/01/2022

Description:
    Program asks for how many cookies you want to make and then gives you back the required amount of butter, sugar, and flour for that quantity.

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
    cookies = int((input('How many cookies do you want to make? '))) #Asks user for how many cookies they want to make
    butter = (1.25 / 48) * cookies #Calculates amount of butter
    sugar = (1.5 / 48) * cookies #Calculates amount of sugar
    flour = (2.5 / 48) * cookies #Calculates amount of flour
    print('To make {} cookies, you will need:'.format(format(cookies, ',')))
    print('      {} cups of butter'.format(format(butter, ',.2f')))
    print('      {} cups of sugar'.format(format(sugar, ',.2f')))
    print('      {} cups of flour'.format(format(flour, ',.2f')))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
