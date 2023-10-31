for i in range (3,101):
    is_Prime=True
    for j in range(2, i):
        if (i%j==0):
            is_Prime=False
            break
    if (is_Prime):
        print("This number is prime: " + str(i))
    if (is_Prime==False):
        print("This number is not prime: " + str(i))
  