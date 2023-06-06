def freq_of_word(str): 
  str2_list = str.split()
  words = set(str2_list)
  for word in words:
    print('Frequency of ' , word ,'is : ', str2_list.count(word) ) 

### Driver Code
print("**************************************** Test Case 1 *****************************************************")
str2 = "if Teacher wants the students in the class to get every student good score compare to other college students in the city and not only that the teacher wants their students to compete with the students presented in the district and the state students also."
freq_of_word(str2)

print("**************************************** Test Case 2 *****************************************************")
str3 = " Physics Maths Social Physics Telugu Maths Physics Social Maths Science Physics Telugu Physics Maths Science Maths"
freq_of_word(str3)

print("**************************************** Test Case 3 *****************************************************")
str4 = "PC Laptop Ipad Laptop Mac Desktop Laptop Ipad PC Mouse Laptop"
freq_of_word(str4)
