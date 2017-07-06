def is_prime(x):
  if x < 2:
    print False
    return False
  elif x == 2:
    print True
    return True
  else:
      print x%2
      if(x % 2) == 0:
        print False
        return False
      else:
        print True
        return True


is_prime(9)
