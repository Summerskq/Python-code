# Alt + Insert  ==== Create New file
# Ctrl + Alt + S  ===== seetings
# python package: itchat
import itchat

# 1. Login weixin
itchat.auto_login(hotReload=True)

# 2. get friends information, return friends List [1, 2, 3, 4, .....]
# Every friend information saved as dict.
friends = itchat.get_friends()

# First friend information is yours
mine = friends[0]
name = mine['NickName']
Signature = mine['Signature']

# init male, female, other = 0
male = female = other = 0
for friend in friends[1:]:
    sex = friend['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
# Ctrl + D : Quick copy one line
print("""
*******************************weixin INformation***********************
        Name: %s
        Signature: %s
        Male friends count: %d 
        Female friends count: %d
        Unknown sex friends count: %d 

""" %(name, Signature, male, female, other))
