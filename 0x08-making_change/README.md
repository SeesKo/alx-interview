#  0x08. Making Change

## Project Overview

The Coin Change Problem is a classic algorithmic challenge where the goal is to find the minimum number of coins required to make up a given total amount using a specified set of coin denominations. This project demonstrates the implementation of two approaches to solve this problem: the Greedy Algorithm and Dynamic Programming.

## Introduction

Given a list of coin denominations and a target amount, the objective is to determine the minimum number of coins required to make up that amount. The problem can be tackled using different algorithmic strategies, each with its own trade-offs in terms of correctness and efficiency.

## Approaches

### Greedy Algorithm

The Greedy Algorithm makes the most immediate optimal choice at each step, attempting to use the highest denomination coin as much as possible. While this method is simple and efficient for certain coin systems (like standard US coins), it does not guarantee an optimal solution for all possible coin sets.

**Steps:**

    1. Sort the coin denominations in descending order.
    2. Start with the largest denomination and subtract it from the amount until the remainder is smaller than the denomination.
    3. Move to the next largest denomination and repeat until the amount is zero.

**Limitations:** The Greedy Algorithm may fail to find the minimum number of coins for some coin denominations.

### Dynamic Programming

Dynamic Programming (DP) is used to find the minimum number of coins required for any set of coin denominations by solving smaller subproblems and building up to the solution of the larger problem.

**Steps:**

    1. Initialize a list dp where dp[i] represents the minimum number of coins needed to make up amount i.
    2. Iterate through each coin, updating the dp list by considering the minimum coins needed for each amount.
    3. The solution for the original amount will be found at dp[amount].

**Advantages:** This approach guarantees an optimal solution and handles all possible coin sets.

## Project Requirements

- Ubuntu 20.04 LTS
- Python (version 3.4.3)
- Code should adhere to `PEP 8` style guidelines.
- The scripts should be executable.
