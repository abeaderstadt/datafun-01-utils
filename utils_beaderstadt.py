"""
Module: utils_beaderstadt

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Alissa Beaderstadt

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_international_clients: bool = True
is_pet_friendly: bool = True
# declare an integer variable 
# TODO: Add or replace this with your own integer variable
years_in_operation: int = 10
number_of_deliveries: int = 75
# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_client_satisfaction: float = 4.7
average_daily_sales: float = 3.9
# declare a list of strings
# TODO: Add or replace this with your own list  
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
tools_used: list = ["SQL", "GitHub", "Python"]
# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
recent_scores_on_skills_drills: list = [5.5, 2.2, 6.6, 9.0]
# Calculate basic statistics using built-in Python functions and the statistics module
# Recent Scores on Skills Drills Statistics
min_score: float = min(recent_scores_on_skills_drills)  
max_score: float = max(recent_scores_on_skills_drills)  
mean_score: float = statistics.mean(recent_scores_on_skills_drills)  
stdev_score: float = statistics.stdev(recent_scores_on_skills_drills)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Is Pet Friendly:                          {is_pet_friendly}
Number Of Deliveries:                     {number_of_deliveries}
Tools Used:                               {tools_used}
Recent Scores On Skills Drills:           {recent_scores_on_skills_drills}
Minimum Skill Drill Score:                {min_score}
Maximum Skill Drill Score:                {max_score}
Mean Skill Drill Score:                   {mean_score:.2f}
Standard Deviation of Skill Drill Scores: {stdev_score:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
