def multiply_numbers_1_to_100():
  """
  Multiplies numbers from 1 to 100.

  Returns:
    int: The product of numbers from 1 to 100.
  """
  product = 1
  for i in range(1, 101):
    product *= i
  return product

if __name__ == "__main__":
  result = multiply_numbers_1_to_100()
  print(f"The product of numbers from 1 to 100 is: {result}")
