import time
import requests
def timeit(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        result =f(*args, **kwargs)
        end = time.time()
        print("函数%s执行使用的时间是%.3fs" %(f.__name__, end-start))
        return result
    return wrapper

"""
@timeit
def download_music():
    url = "http://m10.music.126.net/20200720151105/c12bde0cb40318003ad8a663bfd5393f/ymusic/8f48/c552/df0f/30b8555244d5dbada66cddbefcdd7e1a.mp3"
    response = requests.get(url)
    #music_content = response.content
    with open("music.mp3", 'wb') as f:
        f.write(response.content)
    print("music.mp3下载完成.......")
download_music()
"""
@timeit
def add(num1,num2):
    time.sleep(0.3)
    return num1 + num2
print(add(10,20))