# Monthly expenses
monthly_expenses = {
    'rent': 1200,
    'utilities': 300,
    'transport': 450,
    'food': 600,
    'entertainment': 110,
    'clothing': 220,
    'health': 30,
    'internet': 60,
    'education': 200,
    'other': 100
}

# Calculate the total expenses
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    sum = 0
    
    for key in monthly_expenses:
        sum += monthly_expenses[key]

    return sum

print(total_expenses(monthly_expenses))

# Find the least expensive expense
def least_expensive(monthly_expenses: dict) -> str:
    """
    Find the least expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        least_expensive: least expensive expense
    """
    sum = list(monthly_expenses.values())
    min = sum[0]
    for value in sum[1:]:
        if min > value:
            min = value
    return min

print(least_expensive(monthly_expenses))

# Find the most expensive expense
def most_expensive(monthly_expenses: dict) -> str:
    """
    Find the most expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        most_expensive: most expensive expense
    """
    sum = list(monthly_expenses.values())
    max = sum[0]
    for value in sum[1:]:
        if max < value:
            max = value
    return max

print(most_expensive(monthly_expenses))