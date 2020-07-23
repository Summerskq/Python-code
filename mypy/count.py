from collections import  Counter
string = 'hello world hello python hello java hello c hello c'

string_dict = {}
for c in string:
    if c in string_dict:
        string_dict[c] = string_dict[c] + 1
    else:
        string_dict[c] = 1
print(string_dict)
counter = Counter(string)
top_3_string = counter.most_common(3)
print(top_3_string)
