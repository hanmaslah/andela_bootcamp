def data_type(n):
  if isinstance (n , str):
    return len(n)
  elif n is None:
    return 'no value'
  elif isinstance (n, bool):
    return n
  elif isinstance (n , int):
    if n < 100:
      return 'less than 100'
    elif n > 100:
      return 'more than 100'
    else:
      return 'equal to 100'
  else:
    if len(n)>2:
      return n[2]
    else:
      return None
  
