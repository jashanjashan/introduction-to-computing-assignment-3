#q1
input_string=input("Enter  string: ")
list_of_string=input_string.split()
#here we will  take a dictionary s whose key  represents words and  values represent no of times it occured
s=dict()
# here we have taken a dictionary l  whose key  represents characters and  values represent no of times it occured
l=dict()

if len(list_of_string)==1:
    for i in input_string:
        y=input_string.count(i)
        s[i]=y
    print(s)
elif len(list_of_string)>1:
    for i in list_of_string:
        x=list_of_string.count(i)
        l[i]=x
    print(l)
        
#q2
#q2
while True :
    date=int(input("enter date: "))
    month=int(input("input month: "))
    year=int(input("enter year: "))
    months_with_31=[1,3,5,7,8,10,12]
    months_with_30=[4,6,9,11]
    
    if month in months_with_30 :
        if date<30:
            date=date+1
            print(date,month,year)
            break
        elif date==30:
            date=1
            month=month+1
            print(date,month,year)
            break
        else:
            print("invalid enter again")
            continue
    if month in months_with_31:
        if date<31:
            date=date+1
            print(date,month,year)
            break
        if date==31:
            if month!=12:
                date=1
                month=month+1
                print(date,month,year)
                break
            if month==12:
                date=1
                month=1
                year=year+1
                print(date,month,year)
                break
            else:
                print("invalid enter again")
                continue
    if month==2 and year%4!=0:
            if date<28 :
                date=date+1
                print(date,month,year)
                break
            if date==28:
                date=1
                month=3
                print(date,month,year)
                break
            else:
                print("invalid enter again")
                continue
    if month==2 and year%4==0:
              if date<29:
                 date=date+1
                 print(date,month,year)
                 break
              if date==29:
                date=1
                month=3
                print(date,month,year)
                break
              else:
                print("invalid enter again")
                continue
    else:
        print("invalid enter again")
        continue          
        
            
#q(3)
list_of_numbers=[3,9,10]
list_of_tuples=[]
for i in list_of_numbers:
    list_of_tuples.append((i,i**2))
print(list_of_tuples)

#q4
Grade_point=int(input("enter the grade point:"))
if Grade_point==10:
    print("Your Grade is 'A+' and Outstanding performance")
elif Grade_point==9:
    print("Your Grade is 'A' and Excellent performance")
elif Grade_point==8:
    print("Your Grade is 'B+' and Very Good performance")
elif Grade_point==7:
    print("Your Grade is 'B' and  Good performance")
elif Grade_point==6:
    print("Your Grade is 'C+' and  Average performance")
elif Grade_point==5:
    print("Your Grade is 'C' and  Below Average performance")
elif Grade_point==4:
    print("Your Grade is 'D' and  Poor performance")
else:
    print("Error 404")

#q(5)
string_entered="ABCDEFGHIJK"
#now we will iterate in this string using iteration  variable i
# here i did nesting using the j as iterating variable
for i in range(int((len(string_entered)+1)/2)):
    for j in range(i+1):
        spaces=" "*j
    print(spaces+string_entered[0:11-j*2])

#q(6)
student_info=dict()
n="y"
alistsid=[]

#q6(a)
#here we keep  a while  loop that goes for infinite times
#hence it asks sid and names repeatedly and add them to dictionary
#here i have used the if statement so that i can exit the loop whenever i want
# i am making list along with the dictionary which will help us in further parts
print("a part")
while(n=="y"):
    sid=int(input("give me the sid:"))
    name=input("enter your name")
    student_info[sid]=name
    n=input("give a letter y or n:")
    alistsid.append((sid,name))
print("the required dictionary :",student_info)
print("the list will be used in further parts")
print("the required list:",alistsid)
print("Done!")
#q6(b)
#to sort our dictionary based to names we will iterate dict.items() twice each
#time inversing the key value pair and we will form a list which can be sorted
#and converted back to dictionary hence we get the required dictionary
print("  b part")
print("the dictionary we had:")
print(student_info)
#now we exchange key value pair and make a new dictionary and a new list
newdict=dict()
alistname=[]
for (k,v) in student_info.items():
    newdict[v]=k
    alistname.append((v,k))
print("now we have exchanged the key value pair but its not sorted")
#our dict and list are both not sorted
print(alistname)
alistname.sort()
#sorted.list
print("the sorted list:")
print(alistname)
#now we create a sorted  dictionary  from our sorted list
print("the sorted dictionary:")
sorted_dict=dict(alistname)
print(sorted_dict)
#now we just need to exchange the key value pair of sorted_dict to get
#our required dictionary
required_dict_name=dict()
for (k,v) in sorted_dict.items():
    required_dict_name[v]=k
print("this is dictionary sorted on basis of name")
print(required_dict_name)
print("Done!")

#(c)
print("c part")
print("the list we made before will be used now ")
print(alistsid)
alistsid.sort()
print("now list is sorted")
print(alistsid)
sorted_student_info_sid=dict(alistsid)
print("sorted dictionary based on sid",sorted_student_info_sid)
print("Done!")

#(D)
print("d part")
entered_sid=int(input("please enter on of the sids you entered before:"))
print("the name of student with this sid is:")
print(student_info[entered_sid])
print("Done")


                            


#q7
#q7
first_number_entered_by_user=int(input("enter first number:"))
second_number_entered_by_user=int(input("enter second number:"))
list_of_fibonaaci_series=[first_number_entered_by_user,second_number_entered_by_user]
n=int(input("number  of extra terms we want to add in fibonacci series apart from first two :"))
sum=first_number_entered_by_user + second_number_entered_by_user
for i in range(n):
       next_term_of_series=first_number_entered_by_user + second_number_entered_by_user
       first_number_entered_by_user=second_number_entered_by_user
       second_number_entered_by_user=next_term_of_series
       list_of_fibonaaci_series.append(next_term_of_series)
       sum=sum+next_term_of_series
print(list_of_fibonaaci_series,end=" ")
average_of_Series=sum/(n+2)
print("average_of_series",average_of_Series)

#q8(a)
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
#x denotes elements in Set1 and Set2 but not both
x=Set1^Set2
print(x)

#q8(b)
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17,}
#x denotes set consisting of elementd that are only one of three Set1,Ser2 and Set3
x=(Set2^Set1^Set3)-(Set1&Set2&Set3)
print(x)

#q8(c)
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17,}
#x denotes elements in exactly 2 of  Set1,Set2 and Set3 
x=(Set2&Set1)|(Set1&Set3)|(Set2&Set3)-(Set1&Set2&Set3)
print(x)

#q8(d)
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17,}
my_list=[]
# here what i have done is i created a list of elements in range(1,10) and then converted them to Set
for i in  range(1,10):
    my_list.append(i)
Set_of_elements_in_range1to10=set(my_list)
Set_required=Set_of_elements_in_range1to10-Set1
print(Set_required)

#q8(e)
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
my_list=[]
# here what I have done is Icreated a list of elements in range(1,10) and then converted it to Set
for i in  range(1,10):
    my_list.append(i)
Set_of_elements_in_range1to10=set(my_list)
set_required=Set_of_elements_in_range1to10-(Set1|Set2|Set3)
print(set_required)





       

    






                    
                    
    