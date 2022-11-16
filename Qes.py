
# # Q1 WAP to find the force ?? 
# # (force = mass * accelaration)

# mass=int(input("enter mass"))
# acc=int(input("enter accelaration"))
# force=mass*acc
# print("apllyed force is = ",force) 


# #  Q2 WAP to find a distance between two points ???

# a=int(input("enter point A"))
# b=int(input("enter point b"))
# c=b-a
# print(c) 

# # Q3 write a python programme which accepts the radius of a circle 
# # and compute the area ?
# #  ( pie*r*r)
# r=float(input("enter radius :  "))
# area=3.14*r*r
# print("area of circle ",area)

# # Q4 write a python programme which accepts 
# # the user's first and last name and print them in reverse 
# # order with a space between them 

# fname=input("en ter first name  ")
# lname=input("enter last name ")
# print("hello " + lname ,fname)




#  Q5 write a python programme which accepts 
# a sequence of comma-separated numbers frome 
# user and generate a list and tuple with thosse numbers 

# num=input("enter a list") 
# list=num.split(",")
# tuple=tuple(list)
# print("list is : ",list)
# print("tuple  : ",tuple)



# Q6 write python programme to accept a file name 
# frome user and print the extention
#
# f_name=input("enter file name  ")  
# f_extns= f_name.split(".")
# print('EXtantion of file is  '+str(f_extns[1])) 
                            
                            
  # Q7 write a python programme to display the first and 
  #last colors from the following list 
 #  color_list = ["Red","Green","White" ,"Black"]
 #
# list=["Red","Green","White",'black']
# print(list[0],list[3])
 
 
# Q8  Write a Python program to display the examination schedule. 
# #  (extract the date from exam)
# exam=(11,12,2022) 
# print("examination will start from : %i / %i / %i "%exam) 


'''Q9 WAP that accepts an integer (n) and computes the 
value of n+nn+nnn.'''

n=int(input("enter a number"))
a=int(n)
b=int(n,n)
c=int(n,n,n)
print((a+b+c))
                          
                                 