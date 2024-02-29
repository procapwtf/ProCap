import requests
class Task:
    def __init__(self, response: dict) -> None:
        self.id = response.get("ID")
        self.time = response.get("Time")
        self.message = response.get("Message")
        self.success = response.get("Success")
        self.token = response["Results"].get("Pass")
        self.challengeKey = response["Results"].get("ChallengeKey")
class ProCap:
    def __init__(self, apikey) -> None:
        self.apikey = apikey
        self.headers = {"apikey": apikey}
    def get_balance(self):
        request = requests.get("https://api.procap.wtf/balance", headers=self.headers)
        js = request.json()
        balance = js.get("balance")
        return balance if balance != None else js.get("error")
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
