# We import the numpy library
import numpy as np

# Sub-question (a) i):
# Construct a NumPy array named ---> crypto_prices <--- containing the daily prices. (Thus, prices for 30 days).
crypto_prices = np.array([34.5, 36.2, 37.1, 35.8, 38.0, 39.5, 40.2, 38.7, 37.9, 36.5,
                          35.2, 34.8, 36.0, 37.3, 38.1, 39.9, 41.0, 42.5, 41.8, 40.7,
                          39.4, 38.2, 37.0, 36.8, 35.6, 34.9, 33.7, 34.1, 35.3, 36.6])

# Sub-question (a) ii):
# Construct a NumPy array named quantity containing the quantities traded each day. (Thus, for 30 days).
quantity = np.array([1520, 1678, 1580, 1745, 1603, 1820, 1901, 1778, 1690, 1800,
                     1850, 1923, 1789, 1700, 1625, 1598, 1750, 1830, 1890, 1950,
                     2000, 1875, 1790, 1650, 1587, 1523, 1675, 1720, 1810, 1880])

# Sub-question (a) iii):
# Construct a NumPy array named prices_by_ten.
# Convert the one-dimensional array into a two-dimensional array with 3 rows and 10 columns.
prices_by_ten = crypto_prices.reshape(3,10)

print("The presentation of data on a ten-day basis is:")
print(prices_by_ten)


# Sub-question (b):
# Calculate the total number of cryptocurrencies traded within the month.
# We calculate the total quantity of cryptocurrencies traded during the month by summing the quantity array.
total_quantity = np.sum(quantity)
print(f"A total of {total_quantity} cryptocurrencies were traded in the market")

# Sub-question (c):
# Print the total trading volume of the month in dollars.
total_volume = np.sum(crypto_prices * quantity)
print(f"The total cost is {total_volume:.2f}")

# Sub-question (d):
# Print the minimum and maximum price per ten-day period using the prices_by_ten array.
for i, ten_day_prices in enumerate(prices_by_ten, start=1):
    print(f"For the {i}th ten-day period, the minimum price is {np.min(ten_day_prices):.2f}")
    print(f"For the {i}th ten-day period, the maximum price is {np.max(ten_day_prices):.2f}")

# Sub-question (e):
# Print the average price of the last 5 days for the last 7 days of the month using the crypto_prices array.
for i in range(-7, 0):
    moving_average = np.mean(crypto_prices[i-5 if i-5 >= -30 else None:i])
    print(f"On day {30 + i + 1}, the average price of the last five days is {moving_average:.2f}")

# Sub-question (f):
sorted_prices_numpy = np.sort(crypto_prices)
print("The sorted prices are:", sorted_prices_numpy)

# Manual sorting implementation without NumPy
def bubble_sort(arr):
    arr = arr.copy()  # To avoid modifying the original array
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_prices_manual = bubble_sort(crypto_prices)
print("The sorted prices without using NumPy are:", sorted_prices_manual)
