#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_next_prime(n):
        while True:
            n += 1
            if is_prime(n):
                return n

    def get_winner(n):
        if n == 0:
            return "Ben"
        if n == 1:
            return "Maria"
        if n == 2:
            return "Maria"
        if n % 2 == 0:
            return "Ben"
        return "Maria"

    winners = []
    for n in nums:
        winner = "Maria"
        while n > 1:
            prime = get_next_prime(1)
            if prime > n:
                break
            n -= prime
            winner = get_winner(n)
        winners.append(winner)

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None