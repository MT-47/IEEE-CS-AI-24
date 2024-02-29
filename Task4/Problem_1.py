def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")

        # if 'done' entered
        if user_input.lower() == 'done':
            if len(numbers) == 0:  # empty case
                print("At least one number is required.")
                continue  # ask again for input
            else:
                return numbers

        # if number entered
        try:
            # validation for numbers only (floats and integers)
            num_input = float(user_input)
            if num_input.is_integer():
                num_input = int(num_input)

            numbers.append(num_input)
        except ValueError:
            print("Please enter a numerical value.")


def find_min(numbers):
    numbers.sort()
    return numbers[0]


def find_max(numbers):
    numbers.sort()
    return numbers[-1]


def find_mean(numbers):
    total_sum = sum(numbers)
    return total_sum / len(numbers)


def find_mode(numbers):
    frequency = {}
    max_frequency = 0
    mode = []

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
        # max frequency
        if frequency[num] > max_frequency:
            max_frequency = frequency[num]

    # Find mode (numbers with max freq)
    mode = [num for num, freq in frequency.items() if freq == max_frequency]

    if max_frequency == 1:
        return None  # No mode if all numbers have frequency 1
    else:
        return mode


def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    # case even
    if n % 2 == 0:
        return (numbers[n//2] + numbers[n//2 - 1]) / 2
    # case odd
    else:
        return numbers[n//2]


def find_range(numbers):
    return find_max(numbers) - find_min(numbers)


def find_variance(numbers):
    n = len(numbers)
    if n < 2:
        return None  # Variance is undefined for less than 2 elements
    mean = find_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (n - 1)
    return variance


def find_std_deviation(numbers):
    return find_variance(numbers) ** 0.5


def find_quartiles(numbers):
    numbers.sort()
    n = len(numbers)
    quartiles = []

    # Q2 is the median
    Q2 = find_median(numbers)

    # Q1 is the median from 0 to (n/2) not including
    Q1 = find_median(numbers[:n//2])

    # Q3 is the median from (n/2) to n
    if n % 2 == 0:
        Q3 = find_median(numbers[n//2:])
    else:
        # skip the median element
        Q3 = find_median(numbers[n//2 + 1:])

    quartiles.extend([Q1, Q2, Q3])
    return quartiles


def find_iqr(numbers):
    quartiles = find_quartiles(numbers)
    return quartiles[2] - quartiles[0]


if __name__ == "__main__":
    numbers = get_numbers()

    print("Min:", find_min(numbers))
    print("Max:", find_max(numbers))
    print("Mean:", find_mean(numbers))
    print("Mode:", find_mode(numbers))
    print("Median:", find_median(numbers))
    print("Range:", find_range(numbers))
    print("Variance:", find_variance(numbers))
    print("Standard Deviation:", find_std_deviation(numbers))
    print("Quartiles:", find_quartiles(numbers))
    print("Interquartile Range (IQR):", find_iqr(numbers))