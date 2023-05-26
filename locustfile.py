from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def my_task(self):
        self.client.get("/")

    @task(2)
    def get_request(self):
        headers = {"Content-Type": "text/plain"}
        body = "Duis posuere augue vel cursus pharetra. In luctus a ex nec pretium."
        self.client.post("/post", headers=headers, data=body)

    @task(3)
    def put_request(self):
        headers = {"Content-Type": "text/plain"}
        body = "Etiam mi lacus, cursus vitae felis et, blandit pellentesque neque"
        self.client.put("/put", headers=headers, data=body)

    @task(4)
    def get_status(self):
        self.client.get("/status/200")

    @task(5)
    def set_cookies(self):
        params = {
            'foo1': 'bar1',
            'foo2': 'bar2'
        }
        self.client.get("/cookies/set", params=params)

    @task(6)
    def patch_request(self):
        headers = {"Content-Type": "text/plain"}
        body = "Curabitur auctor, elit nec pulvinar porttitor, ex augue condimentum enim"
        self.client.patch("/patch", headers=headers, data=body)

    @task(7)
    def delete_request(self):
        headers = {"Content-Type": "text/plain"}
        body = "Donec fermentum, nisi sed cursus eleifend"
        self.client.delete("/delete", headers=headers, data=body)
