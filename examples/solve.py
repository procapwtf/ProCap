from ProCap import ProCap
apikey = "" # Api key (required)
url = "" # Link to captcha (required)
sitekey = "" # Sitekey (required)
proxy = "" # Proxy (optional)
userAgent = "" # User agent (optional)
rqdata = "" # RQData (optional)
solver = ProCap(apikey) # Replace "api" with your api key !!
captchaToken = solver.solve(url=url, sitekey=sitekey, proxy=proxy, userAgent=userAgent, rqdata=rqdata)
print(f"Captcha solved : {captchaToken}")
