#!/usr/bin/python3

""" The prime game model between Ben and Maria """


def isWinner(x, nums):
    """ Function to get the winner """

    def isPrime(num):
        """this method check if the number is a prime number"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def getPrimes(n):
        """get prime number of an integer"""
        primes = []
        for i in range(2, n + 1):
            if isPrime(i):
                primes.append(i)
        return primes

    def playGame(n):
        """play the game"""
        primes = getPrimes(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = [playGame(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
