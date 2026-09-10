# # # # # # def student(name,rolno,marks):
# # # # # #     return name,rolno, marks
# # # # # # print(student("Lokesh",1,54))
# # # # # # print(student("Poori",2,23))
# # # # # # print(student("Sandeep",3,45))
# # # # # # print(student("Bhanu",4,23))

# # # # # # def add(a,b):
# # # # # #     return a+b
# # # # # #     #print("My name is Lokesh")
# # # # # # print(add(5,4))
# # # # # # print(add(3,2))
# # # # # # print(add(3,4))


# # # # # d={"ravi":12,"ramya":124,"karthik":1234}
# # # # # def login(username,password):
# # # # #     if(username in d.keys()and password in d.values()):
# # # # #         print("login succ")
# # # # #     else:
# # # # #         print("check your cred")
        
# # # # # u=input("Enter a name=")
# # # # # p=int(input("Enter a pass="))
# # # # # login(u,p)


# # # # s="python Lokesh"
# # # # reverse=""
# # # # for i in s:
# # # #     reverse=i+reverse
# # # # print(reverse)

# # # # s="python Lokesh"
# # # # a=s.split()
# # # # reverse=""
# # # # for i in a:
# # # #     reverse=reverse+i[::-1]+" "
# # # # print(reverse) 


# # # num=int(input("Enter a prime number:"))
# # # if num==1:
# # #     print("not a prime number")
    
# # # else:
# # #     for i in range(2,num):
# # #         if num%i==0:
# # #             print("not a prime number")
# # #             break
# # #     else:
# # #         print("Prime number")


# # #sum of digits  #123

a=123
b=str(a)
sum=0
for i in b:
    sum=sum+int(i)
print(sum)

# nums = [10, 20, 4, 45, 99]
# largest=nums[0]
# for i in nums:
#     if i>largest:
#         largest=i
# print("Largest number is" ,largest)    


