def anagrams(s1, s2):
  pass # todo
  result=True
  my_dict_1 = {}
  my_dict_2 = {}
  
  
  for i in range (len(s1)):
      my_dict_1[s1[i]]=s1.count(s1[i])
      
  for i in range (len(s2)):
      my_dict_2[s2[i]]=s2.count(s2[i])
  
  print (my_dict_1)
  
  print (my_dict_2)

  if (my_dict_1 != my_dict_2):
         result= False
  return result

print(anagrams('cats','tocs'))