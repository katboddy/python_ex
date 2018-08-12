from sympy import FiniteSet


def probability(space,event):
    return len(event)/len(space)



# find the probability of a prime number
# appearing when a 20-sided die is rolled

def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

# if __name__ == '__main__':
#     space = FiniteSet(*range(1,21))
#     primes = []
#     for num in space:
#         if check_prime(num):
#             primes.append(num)
#     event = FiniteSet(*primes)
#     p = probability(space,event)
#     print('Sample space: {0}'.format(space))
#     print('Event: {0}'.format(event))
#     print('Probability of rolling a prime: {0:.5f}'.format(p))


# if __name__ == '__main__':
#     space = range(1, 21)
#     primes = []
#     for num in space:
#         if check_prime(num):
#             primes.append(num)
#     p = probability(space, primes)
#     print('Probability of rolling a prime: {0:.5f}'.format(p))


# Simulating a Die Roll
import matplotlib.pyplot as plt
import random

target_score = 20
def roll():
    return random.randint(1,6)

if __name__ == '__main__':
    score = 0
    num_rolls = 0
    while score < target_score:
        die_roll = roll()
        num_rolls += 1
        print('Rolled: {0}'.format(die_roll))
        score += die_roll
    print('Score of {0} reached in {1} rolls'.format(score, num_rolls))


# whether a certain target score is reachable within a maximum number of rolls
def find_prob(target_score, max_rolls):
    die_sides = FiniteSet(1,2,3,4,5,6)
    # Sample space
    s = die_sides**max_rolls
    # Find the event set
    if max_rolls > 0:
        success_rolls = []
        for elem in s:
            if sum(elem) >= target_score:
                success_rolls.append(elem)
    else:
        if target_score > 6:
            success_rolls = []
        else:
            success_rolls = []
            for roll in die_sides:
                if roll >= target_score:
                    success_rolls.append(roll)
    e = FiniteSet(*success_rolls)
    # Calculate the probability of reaching target score
    return len(e)/len(s)


# if __name__ == '__main__':
#     target_score = int(input('Enter target score: '))
#     max_rolls = int(input('Enter maximum number of rolls allowed: '))
#     p = find_prob(target_score, max_rolls)
#     print('Probability {0:.5f}'.format(p))


# unequal probability of heads or tails appearing
def toss():
    # 0 -> Heads, 1 -> Tails
    if random.random() < 2/3:
        return 0
    else:
        return 1


# Simulate a fictional ATM that dispenses dollar bills
# of various denominations with varying probability
def get_index(probability):
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    r = random.random()
    for index, sp in enumerate(sum_probability):
        if r <= sp:
            return index
    return len(probability) - 1


def dispense():
    dolar_bills = [5,10,20,50]
    probability = [1/6, 1/6, 1/3, 1/3]
    bill_index = get_index(probability)
    return dolar_bills[bill_index]


if __name__ == '__main__':
    for i in range(1, 100):
        print(dispense())



