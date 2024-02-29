# ProCap
ProCap is a captcha solving service that handle help you to bypass various type of captchas

# Installation
```
pip install procap
```

### ⚠️ Requirements
* Apikey : **Join [ProCap](https://procap.wtf/), to get api key**

### 💡 Examples

* 1 - Example :

```python
from procap import ProCap
apikey = "" # Api key (required)
url = "" # Link to captcha (required)
sitekey = "" # Sitekey (required)
proxy = "" # Proxy (optional)
userAgent = "" # User agent (optional)
rqdata = "" # RQData (optional)
solver = ProCap(apikey) # Replace "api" with your api key !!
captchaToken = solver.solve(url=url, sitekey=sitekey, proxy=proxy, userAgent=userAgent, rqdata=rqdata))
```
