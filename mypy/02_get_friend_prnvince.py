# 1. Analyse
# friend province
# "shanxi"-200  "beijing"-100  "shandong" 10 .........
# dict: {"province_name":people_num}

# 2.
import itchat
from collections import  Counter

# 3.
itchat.auto_login(hotReload=True)
# friends===List, friend===Dict {"NickName":"", "Sex":"", "Province":""}
# First Information is your info
friends = itchat.get_friends()

# First friend information is yours
mine = friends[0]
name = mine['NickName']
Signature = mine['Signature']


# 4.
# Save Province to dict
provinces = {}
for friend in friends[1:]:
    province = friend['Province']
    if province != '':
        # If province not in dict, set value=1
        # If province in dict, value += 1
        if province in provinces:
            # value = provinces[province]    # province people count
            # value += 1                     # value + 1
            # provinces[province] = value     # set new value
            provinces[province]  += 1
        else:
            provinces[province] = 1

# 5.
counter = Counter(provinces)
top_5_provinces = counter.most_common(5)

# 6.
print("""
*******************************weixin INformation***********************
        Name: %s
        Signature: %s
""" %(name, Signature))

print("*******************************weixin friends Province***********************")
for name, count in top_5_provinces:
    print("%s : %s" %(name, count))