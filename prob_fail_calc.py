def calculate_failure_probability(success_probability, attempts):
    """
    Calculate the probability of failing all attempts.

    :param success_probability: Probability of success per attempt (e.g., 0.005 for 0.5%).
    :param attempts: Number of attempts made.
    :return: Probability of failing all attempts as a percentage.
    """
    failure_probability = 1 - success_probability
    total_failure_probability = failure_probability ** attempts
    return total_failure_probability * 100

# Input from the user
success_prob = float(input("Enter the probability of success for one attempt (e.g., 0.005 for 0.5%): "))
attempts = int(input("Enter the number of attempts: "))

# Calculate failure probability
failure_chance = calculate_failure_probability(success_prob, attempts)

# Output the result
print(f"The probability of failing all {attempts} attempts is approximately {failure_chance:.2f}%.")
