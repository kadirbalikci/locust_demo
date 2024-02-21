from locust import task, between, HttpUser


class MyUser(HttpUser):

  wait_time = between(1,2)
  host = "http://newtours.demoaut.com/"

  @task
  def login_URL(self):
      print("I am logging into URL")
