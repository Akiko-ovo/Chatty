import time
birthday = time.strptime("2024-11-30 00:00:00", "%Y-%m-%d %H:%M:%S")

while True:
    now = time.localtime()
    if now >= birthday:
        print("=" * 30)
        print(" Happy Birthday! ChatGPT ")
        print("Wishing you a wonderful year filled with joy and love!")
        print("=" * 30)
        break
    time.sleep(1)
