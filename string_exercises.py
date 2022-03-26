"""
1. Write a Python program to calculate the length of a string.
"""
def isLength(str):
    return len(str)
    
"""
2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""

def isCount(str):
    hashMap={}
    for i in str:
        if i not in hashMap.keys():
            hashMap[i]=1
        else:
            hashMap[i]+=1 
    return hashMap


"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

def isLastEnd(str):
    if str is None or len(str)==0:
        return ""
    else:
        return str[:2]+str[-2:]


"""
4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

Sample String : 'restart'
Expected Result : 'resta$t'
"""
# lets first get the first character
# for loop idx str[1:n]
# if i ==first character then str[i]==first_character 
# return the str

def stringOnstring(str):
    first_ch = str[0]
    new_str = str[1:]
    for idx in range(len(new_str)):
        if new_str[idx] == first_ch:
            str[idx-1] = "$"
    return str

######## Proposed solution #######
def change_char(str):
    first_ch = str[0]
    str = str.replace(first_ch, "$")

    return first_ch + str[1:]


"""
5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

"""
# get str1[0] and get str2[0]
# replace str1[0] =str2[0] and the same for str2
# return the concat: str1 +" "+str2

def swapString(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    return new_str1 + " " + new_str2

"""
6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

# python has a built in method called endwith: str.endwith("strng") -> bool 
# if str[-3:] = "ing" then str[-3:]="ly"
# else: str[-3] = "ing"

def addChartoString(strng):
    if len(strng)<3:
        return strng
    if strng[-3:] == "ing":
        strng[-3:]="ly"
    else:
        strng[-3:]="ing"

    return strng 


"""
7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'
 ...'poor' substring with 'good'. Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""

def replaceWord(strng):
    def isMatch():
        return



