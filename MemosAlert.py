import time
from plyer import notification

msg = input("What should I remind you of? ")
tm = 3600 * float(input("Every how many hours should I remind you? "))

if __name__ == "__main__":
    notification.notify(
        title = "MemosAlerter",
        message = f"Alert for {msg} started, I will remind you in {tm} seconds.",
        timeout = 10
    )
    while True:
        time.sleep(tm)
        notification.notify(
            title = "MemosAlerter",
            message = msg,
            timeout = 10
        )
