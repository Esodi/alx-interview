#!/usr/bin/python3
''' the module itself'''


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        ''' function iswinner'''
        if n < 2:
            return []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    def simulate_game(n):
        '''simulate the game'''
        if n < 2:
            return "Ben"
        is_prime = sieve_of_eratosthenes(n)
        numbers = [True] * (n + 1)
        maria_turn = True
        while True:
            prime_found = False
            for i in range(2, n + 1):
                if is_prime[i] and numbers[i]:
                    prime_found = True
                    for j in range(i, n + 1, i):
                        numbers[j] = False
                    break
            if not prime_found:
                return "Maria" if not maria_turn else "Ben"
            maria_turn = not maria_turn
    maria_wins = ben_wins = 0
    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
