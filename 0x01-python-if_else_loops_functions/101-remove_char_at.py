#!/usr/bin/python3

def remove_char_at(str, n):
    j = 0
    arr = []
    for i in str:
        if j == n:
            arr.remove(arr[j])
            j += 1
        else:
            arr.append(i)
    print(arr)
    return arr

remove_char_at("hello", 3)
