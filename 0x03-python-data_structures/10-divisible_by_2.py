#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    partylist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            partylist[count] = True
        else:
            partylist[count] = False
            return (partylist)
