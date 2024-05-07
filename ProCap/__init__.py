import requests
import time
class Task:
    def __init__(self, response: dict) -> None:
        self.id = response.get("taskId")
        self.time = response.get("time")
        self.success = response.get("success")
        self.token = response["solution"].get("generated_pass_uuid")
        self.error = response.get("error")
        self.challengeKey = response["solution"].get("challenge_key")
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
    def get_balance(self):
        request = requests.get("https://api.procap.wtf/user")
        return User(request.json())
    def createTask(self, url, sitekey, proxy=None, userAgent=None, rqdata=None, isEnterprise=False, type="hCaptchaTask"):
        payload = {
            "clientKey": self.apikey,
            "task": {
                "type": type,
                "href":url,
                "sitekey": sitekey,
                "proxy": proxy,
                "useragent": userAgent,
                "rqdata": rqdata,
            }
        }
        if "hcaptcha" in type:
            payload.update({"isEnterprise": isEnterprise})
        request = requests.post("https://api.procap.wtf/createTask", json=payload)
        return Task(request.json())
    def checkTask(self, id):
        request = requests.get("https://api.procap.wtf/checkTask", json={
            "clientKey": self.apikey,
            "taskId": id
        })
        return Task(request.json())
    def solve(self, url, sitekey, proxy=None, userAgent=None, rqdata=None, isEnterprise=False):
        task = self.createTask(url, sitekey, proxy, userAgent, rqdata, isEnterprise)
        if not task.error:
            return task.error
        while True:
            captcha_challenge = self.checkTask(task.id)
            if not captcha_challenge.success:
                return None
            if captcha_challenge.success:
                return captcha_challenge.token
            time.sleep(0.5)
