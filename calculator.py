def calc(a, b):
  calc_sum = a + b
  diff = a - b
  multiple = a * b
  quotient = None
  if b != 0:
    quotient = a / b
  nums = {
    "sum": calc_sum,
    "diff": diff,
    "multiple": multiple,
    "quotient": quotient
  }
  return nums