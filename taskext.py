for num in range(100,1000):
    s = 0 
    temporary = num
  
    while temporary > 0:
       diginum = temporary % 10
       s += diginum ** 3
       temporary //= 10
  
    if num == s:
       print('These numbers are equal to their cubes sum: ', num)
