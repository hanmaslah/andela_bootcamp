def words(n):
  words=n.split()
  counts =dict()
  
  for word in words:
    if word.isdigit():
      word=int(word)
    if word in counts:  
      counts[word] += 1  
    else:  
      counts[word] = 1  
  
  return counts  
  
  