'''
samp1 = [6,5,4,4]
samp2 = [5,15,20,10]
'''
'''
if 2nd no > 1st no
increasing monotonic
flag decrease = false
for loop--3rd no < 2nd no :-break, return flag- false

if 2nd no < 1st no
decreasing monotonic
flag decrease = true
for loop-- 3rd no > 2nd no:- break , return flag- false

[2,3,3,5]

flag operator - string (increasing/decreasing/flat)
for loop starting from 1st number to last number -
    if condition - 1st number == next number ?
        set operator to flat
    else condition -
        if condition - compare with next number (is 1st number > next number)
            set operator to decreasing
        else condition - 1st number < next number ?
            set operator to increasing

---------------------------------------
2,2,2,2,2,2,4,5,1
operator initialize to flat
monotonic = True
for loop -
    until operator becomes increasing/decreasing
        break
operator = increasing/decreasing
if operator is not flat
    for loop -
        if operator == increasing
            if current element is not less than the next element
                set monotonic = False
                break
        else if operator == decreasing
            if current element is not greater than the next element
                set monotonic = False
                break
        else 
            print undesired operator value
            fail the execution with message - undesired operator value

'''


samp1 = [4,4,4,4,4,4,4]
operator = 'flat'
monotonic = True
for ind in range(0, len(samp1)-1):
    if samp1[ind] < samp1[ind + 1]:
        operator = 'increasing'
        break
    elif samp1[ind] > samp1[ind + 1]:
        operator = 'decreasing'
        break
if operator is not 'flat':
    for ind in range(0, len(samp1)-1):
        if operator is 'increasing':
            if samp1[ind] > samp1[ind + 1]:
                monotonic = False
                break
        elif operator is 'decreasing':
            if samp1[ind] < samp1[ind + 1]:
                monotonic = False
                break
        else:
            print('Undesired operator value')
            raise Exception('Undesired operator value')
if monotonic is True:
    print('MONOTONIC!')
else:
    print('NOT MONOTONIC!')
