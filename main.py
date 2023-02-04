#reverse string
first_name,last_name,r_f_name,r_l_name='','','',''

first_name=input("Please enter first name:  ")
last_name=input("Please enter last name:  ")

r_f_name=first_name[::-1]
r_l_name=last_name[::-1]


print(f'Your reversed name is: {r_l_name}  {r_f_name}')







