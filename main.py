import random

def main():
    total = 0
    numbers = []

    while True:
        num = random.randint(1, 10)
        if total + num > 100:
            break
        numbers.append(num)
        total += num

    # Now add the last number that caused the sum to exceed 100 to the list
    numbers.append(num)

    print(' '.join(str(n) for n in numbers))  # Print random values on one line
    print(f'The total sum is {total}')        # Sum excluding last number

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
