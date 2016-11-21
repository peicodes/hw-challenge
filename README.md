# Wealthsimple Lightning Challenge

### Background

The simplest model of an investment account is a `snapshot`. A `snapshot` represents an account's market liquidation value and the cash flow going in or out of that account for a given time period. It is assumed that all market values are calculated at the end of the time period, while cash flows occur during the time period.

##### Example Snapshots

{ year: 0, cash_flow: 1000.00, market_value: 1000.00 }  
{ year: 1, cash_flow: 0.00, market_value: 1020.00 }  
{ year: 2, cash_flow: 500.00, market_value: 1535.00 }  
{ year: 3, cash_flow: -1000.00, market_value: 540.00 }

One of the most important things our clients want to see is the return rate of their account. The Canadian government mandates investment managers to use Money Weighted Return, also know as MWR.


### Introduction

Some basic finance definitions:  
1. Cash Flow - Money going in or out of an account. Positive cash flows are deposits.  
2. Annualized MWR - The 'per-year' MWR. Using this value, you can calculate the total MWR for any length of time. You can also calculate the annualized MWR if you are given the MWR for a period of time.  

##### Example 1

If the MWR after 2 years is 21%, then the annualized MWR is 10%. This is known by solving the following equation:

`(1 + x) ^ 2 = 1 + 0.21`

Where `x` is the unknown annualized MWR.

##### Example 2

Let's say an account had a single cash flow of $1000.00 at year 0. After 5 years, the account is worth $1610.51. The annualized MWR required to make this happen is again, 10%. This is known by solving the following equation:

`1000 * (1 + x) ^ 5 = 1610.51`

##### Example 3

What if there are two cash flows? Let's say an account had the following snapshots:

{ year: 0, cash_flow: 1000.00, market_value: 1000.00 }  
{ year: 1, cash_flow: 1500.00, market_value: 2600.00 }  
{ year: 2, cash_flow: 0.00, market_value: 2700.00 }  
{ year: 3, cash_flow: 0.00, market_value: 3000.00 }  
{ year: 4, cash_flow: 0.00, market_value: 3400.00 }  
{ year: 5, cash_flow: 0.00, market_value: 3806.66 }  

At year 5, the account is worth $3806.66. The annualized MWR require to make this happen is also 10%. This is known by solving the following equation:

`1000 * (1 + x) ^ 5 + 1500 * (1 + x) ^ 4 = 3806.66`

Notice how the second cash flow only compounds for 4 years, since it was deposited 1 year after the first cash flow.


### Problem

Given n snapshots, you must calculate the annualized MWR. In general, the problem looks like this:

`snapshot[0].cash_flow * (1 + x) ^ (n - 1) + snapshot[1].cash_flow * (1 + x) ^ (n - 2) + ... + snapshot[n-2].cash_flow * (1 + x) ^ 1 = snapshot[n-1].market_value`

Two assumptions you can always make:  
1. In the first snapshot, cash_flow = market_value  
2. In the last snapshot, cash_flow = 0  


### Requirements

Your code should read from a file called test.csv, and output the result on the console. An example of such a file is provided. Your submission should run on console without any additional configuration; For example, `python3 your_solution.py` or `ruby your_solution.rb`.

The return rate you output should be a raw decimal. For example, 12.2% is 0.122.

Your answer is considered correct if it's within 0.001 of the actual answer.


### Submission

Fork this repo and make a pull request with your code before the deadline.
TESTaaa
