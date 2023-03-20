##########################1#################################

#my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']


#def modify_list(my_list):
    #new_list = []
    #for i in range(len(my_list)):
        #if i % 2 == 0:
            #new_list.append(my_list[i])
        #else:
            #new_list.append(my_list[i][::-1])
    #return new_list


#result = modify_list(my_list)
#print(result)

##########################2#################################

#my_list = ['dig', 'sick', 'big', 'apple']


#def filter_by_first_letter_a(my_list):
    #result_list = []
    #for item in my_list:
        #if item.startswith('a'):
            #result_list.append(item)
    #return result_list


#result = filter_by_first_letter_a(my_list)
#print(result)


##########################3#################################

#my_list = ['dig', 'sick', 'big', 'apple']


#def filter_by_letter_a(my_list):
    #result_list = []
    #for item in my_list:
        #if 'a' in item:
            #result_list.append(item)
    #return result_list


#result = filter_by_letter_a(my_list)
#print(result)

##########################4#################################


#def get_strings(my_list):
    #result_string = []
    #for item in my_list:
        #if isinstance(item, str):
            #result_string.append(item)
    #return result_string


#my_list = ['dig', 'sick', 'big', 'apple', 1]
#new_list = get_strings(my_list)
#print(new_list)


##########################5#################################


#def unique_chars(my_str):
    #result = []
    #for char in my_str:
        #if my_str.count(char) == 1:
            #result.append(char)
    #return result


#my_str = "abbcccdddd"
#result = unique_chars(my_str)
#print(result)

##########################6#################################
"""


def common_chars(str_1, str_2):
    result = []
    for char in str_1:
        if char in str_2 and char not in result:
            result.append(char)
    return result


str_1 = "hello"
str_2 = "world"
result = common_chars(str_1, str_2)
print(result)
"""

##########################7#################################
"""


def common_chars(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    common = list(set1.intersection(set2))

    return sorted(common)


str1 = "hello"
str2 = "world"
common = common_chars(str1, str2)
print(common)  # ['l', 'o']

"""

##########################8#################################
"""
import random
import string  #вообще импорті должни бить в начале


def create_email(domains, names):
    name = random.choice(names)
    domain = random.choice(domains)

    number = random.randint(100, 999)

    string_length = random.randint(5, 7)
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(string_length))

    email = name + "." + str(number) + "@" + random_string + "." + domain

    return email


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
"""





























