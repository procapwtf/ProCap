# ProCap
ProCap is a captcha solving service that handle help you to bypass various type of captchas

# Installation
```
pip install procap
```

### ⚠️ Requirements
* Apikey : **Join [ProCap](https://procap.wtf/), to get api key**

### 💡 Examples

* 1 - Example (Solve)

```python
from procap import ProCap
apikey = "" # Api key (required)
url = "" # Link to captcha (required)
sitekey = "" # Sitekey (required)
proxy = "" # Proxy (optional)
userAgent = "" # User agent (optional)
rqdata = "" # RQData (optional)
solver = ProCap(apikey)
captchaToken = solver.solve(url=url, sitekey=sitekey, proxy=proxy, userAgent=userAgent, rqdata=rqdata)
```

* 2 - Example 2 (Create task)

```python
from procap import ProCap
apikey = "" # Api key (required)
url = "" # Link to captcha (required)
sitekey = "" # Sitekey (required)
proxy = "" # Proxy (optional)
userAgent = "" # User agent (optional)
rqdata = "" # RQData (optional)
solver = ProCap(apikey)
captchaTask = solver.createTask(url=url, sitekey=sitekey, proxy=proxy, userAgent=userAgent, rqdata=rqdata)
captchaTask.id # Task id
captchaTask.time # Time taken
captchaTask.message # Message
captchaTask.success # Success [True or False]
captchaTask.token # Captcha Token (if solved)
captchaTask.challengeKey # Captcha challenge key
```

* 3 - Example (Get Task Result)
  ```python
from procap import ProCap
solver = ProCap(apikey)
id = "Challenge ID" 
captchaTask = solver.checkTask(id)
captchaTask.id # Task id
captchaTask.time # Time taken
captchaTask.message # Message
captchaTask.success # Success [True or False]
captchaTask.token # Captcha Token (if solved)
captchaTask.challengeKey # Captcha challenge key
```
