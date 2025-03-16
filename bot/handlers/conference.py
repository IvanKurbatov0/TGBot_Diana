import datetime

class Conference:
    def __init__(self):
        self.date = None
        self.time = None
        self.description = None
        self.key = None
        self.url = None

    async def create(self, time, date, description):
        self.time = datetime.datetime(year=int(date.split('.')[2]), month=int(date.split('.')[1]), day=int(date.split('.')[0]), hour=int(time.split(':')[0]), minute=int(time.split(':')[1]))
        self.date = datetime.date(year=int(date.split('.')[2]), month=int(date.split('.')[1]), day=int(date.split('.')[0]))
        self.description = description

    async def clear(self):
        self.date = None
        self.time = None
        self.description = None
        self.key = None
        self.url = None

