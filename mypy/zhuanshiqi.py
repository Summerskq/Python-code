import time
import requests
def timeit(f):
    def wrapper():
        start = time.time()
        result = f()
        end = time.time()
        print("time is%.3fs" %(f.__name__, end-start))
        return result
    return wrapper
@timeit
def download_music():
    url = "http://m10.music.126.net/20200719114251/ef8f31068c2a1921edca918f9d211dd3/ymusic/5152/5552/030c/f860fa842eb8201274264f2d9eda6139.mp3"
    # 模拟浏览器访问mp3的网址，获取服务器端给我们的响应(response)
    response = requests.get(url)
    # 获取mp3音乐的内容
    # music_content = response.content
    # 打开文件，存储音乐的内容到文件中
    with open("你是人间四月天解忧邵帅.mp3", 'wb') as f:
        f.write(response.content)
    print("你是人间四月天解忧邵帅.mp3下载完成.......")

download_music()