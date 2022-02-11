from flask import Flask
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

from send_data import tweet_data

app = Flask(__name__)

@app.route('/')
def job():
    tweet_data()

scheduler = BackgroundScheduler()
#send tweets every 24hrs
scheduler.add_job(func=job, trigger="interval", day=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    app.run(port=5000, debug=True)
