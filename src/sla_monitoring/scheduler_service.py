from apscheduler.schedulers.asyncio import AsyncIOScheduler


class SchedulerService:
    def job_simple(self):
        print("simple job run")

    def start(self):
        self.scheduler = AsyncIOScheduler()
        self.scheduler.add_job(self.job_simple, "interval", seconds=5)
        self.scheduler.start()

    def shutdown(self):
        self.scheduler.shutdown()
