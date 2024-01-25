from django_cron import CronJobBase, Schedule
from .views import fetch_news

class UpdateNewsCronJob(CronJobBase):
    schedule = Schedule(run_every_mins=15)
    code = 'news_api_proxy.update_news'

    def do(self):
        fetch_news(None)
