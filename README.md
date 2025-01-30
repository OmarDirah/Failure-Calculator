# Failure-Calculator
Probability Failure Calculator 
Function calculate_failure_probability:

Takes two inputs: success_probability (the chance of success for a single attempt, e.g., 0.005 for 0.5%) and attempts (the total number of attempts).

Computes the probability of failing a single attempt as 1 - success_probability.

Raises the failure probability to the power of the number of attempts to determine the probability of failing all attempts.

Returns the result as a percentage.

User Input:

The script prompts the user to input the success probability and the number of attempts.

Calculation and Output:

The script calls the calculate_failure_probability function with the user-provided inputs.

It then prints the probability of failing all attempts, formatted to two decimal places.
