import locust as loc


class Quicktest(loc.HttpUser):
    wait_time = loc.between(2, 6)

    @loc.task
    def getAPI(self):
        self.client.get()
