try:
    list = [1,3,4,5]
    print(list[6])
except IndexError as e:
    print(list[-1])
else:
    print("zhngechang")
finally:
    print("ssss")