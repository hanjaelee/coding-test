def parse(n):
  numbers = n.split(',')
  result = 0

  for x in numbers:
    result += 1

  return result

n = input()
result = parse(n)
print(result)
