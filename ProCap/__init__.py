import requests
import time
class Task:
    def __init__(self, response: dict) -> None:
        self.id = response.get("ID")
        self.time = response.get("Time")
        self.message = response.get("Message")
        self.success = response.get("Success")
        self.token = response["Results"].get("Pass")
        self.challengeKey = response["Results"].get("ChallengeKey")
        self.response = response
class User:
    def __init__(self, response: dict) -> None:
        self.balance = response.get("balance")
        self.daily_limit = response.get("daily_limit")
        self.next_reset = response.get("next_reset")
        self.daily_used = response.get("daily_used")
        self.daily_remaining = response.get("daily_remaining")
        self.plan_expire = response.get("plan_expire")
        self.response = response
class ProCap:
    def __init__(self, apikey) -> None:
        self.apikey = apikey
        self.headers = {"apikey": apikey}
    def get_balance(self):
        request = requests.get("https://api.procap.wtf/user", headers=self.headers)
        return User(request.json())
    def createTask(self, url, sitekey, proxy=None, userAgent=None, rqdata=None):
        payload = {
            "url": url,
            "sitekey": sitekey,
            "proxy": proxy,
            "userAgent": userAgent,
            "rqdata": rqdata
        }
        request = requests.post("https://api.procap.wtf/createTask", json=payload, headers=self.headers)
        return Task(request.json())
    def checkTask(self, id):
        request = requests.get("https://api.procap.wtf/checkTask/"+id)
        return Task(request.json())
    def solve(self, url, sitekey, proxy=None, userAgent=None, rqdata=None):
        while True:
            task = self.createTask(url, sitekey, proxy, userAgent, rqdata)
            if "busy" not in task.message:
                break
            else:
                time.sleep(5)
        if not task.success:
            return task.message
        while True:
            captcha_challenge = self.checkTask(task.id)
            if captcha_challenge.message != "solving" and captcha_challenge.message != "solved":
                return None
            if captcha_challenge.message == "solved":
                return captcha_challenge.token
            time.sleep(1)
