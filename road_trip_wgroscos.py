"""
Author: Warren Groscost, wgroscos@purdue.edu
Assignment: 01.1 - Road Trip
Date: 09/01/2022

Description:
    Programs asks for a distance, average price per gallon of fuel, and the fuel efficiency of your vehichle
    and gives you an approximate fuel cost for the trip both ways.

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
    print('Road trip fuel cost estimator:')
    distance = float(input('  How far away is your destination (miles)? ')) #Asks user to input the distance to the destination
    avg_price = float(input('  What is the average price of gas (dollars per gallon)? ')) #Asks user for the average per gallon price of fuel
    mpg = float(input('  What is the fuel efficiency of your vehicle (mpg)? ')) #Aks user for the fuel efficiency of their vehicle in mpg
    cost = int((2 * distance) * (avg_price / mpg)) #Calculates total approximate cost
    print('\nThe fuel cost for this trip is approximately ${}.'.format(cost))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
