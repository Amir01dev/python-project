from speedtest import Speedtest

s = Speedtest()

print("Test Download Speed...")
download_res = s.download()/1024/1024
print(f"Your download speed is : {download_res:.2f} mb/s")

print("Test Upload Speed...")
upload_res = s.upload()/1024/1024
print(f"Your upload speed is : {upload_res:.2f} mb/s")

print("Test Ping...")
ping_res = s.ping()/1024/1024
print(f"Your ping is : {ping_res:.2f} mb/s")
