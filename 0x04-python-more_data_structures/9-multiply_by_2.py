#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dic = {}
    for i in a_dictionary:
        nw_dic[i] = a_dictionary[i] * 2
    return nw_dic
