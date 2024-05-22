from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Users will wait between 1 and 5 seconds between tasks

    @task
    def load_test(self):
        self.client.get("/get_user?user_id=123")  # Replace with the endpoint you want to test

# Run the test