from __future__ import print_function
from __future__ import division
import itertools
import math



#------start of input area---------


#total number of applicants
people_num = 10


#------end of input area---------



N = math.factorial(people_num)

count = 0
n=[]
test_list = []
value = 0
choice = 0
get_max_num = 0
iter_list =[]
flag = 0

for i in range(1,people_num+1):
    n.append(i)

for x in range(0,people_num):
    get_max_num = 0

    for i in itertools.permutations(n,len(n)):
        iter_list = []
        iter_list = list(i)
        #print('iter_list =',iter_list)
        test_list = []
        value = 0
        choice = 0

        #print('i = ',list(i))
        for k in range(0,x+1):
            test_list.append(iter_list[k])
        value = max(test_list)
        #print('value =',value)

        flag = 0
        for v in range(x+1,len(iter_list)):
            if iter_list[v] > value:
                #print('v =',v)
                choice = iter_list[v]
                flag = 1
                break

        if flag == 0:
            choice = iter_list[len(iter_list) - 1]


        #print('choice =',choice)
        if choice == people_num:
            get_max_num = get_max_num +1
            #print('x = ',x+1,'iter_list =',iter_list,'get_max_num =',get_max_num)

    p = (get_max_num/N)*100


    print('when the interviewer rejects the first',x+1,'people,','the probability that the best applicant is selected is',p,'%')
    print('')














