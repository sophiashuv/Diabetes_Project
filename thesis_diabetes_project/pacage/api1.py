#https://api.dexcom.com/v2/oauth2/login?client_id=ck8SjP0KHS5T3EWGmEvoYp6CNqUyMehS&redirect_uri=https://github.com/sophiashuv/Diabetes_Project&response_type=code&scope=offline_access

import http.client

conn = http.client.HTTPSConnection("api.dexcom.com")

code = "5bbc6d72ceeb49bd677ac14c64ab1765"

payload = "client_secret=lXd55eQ8YcwmnaO2&client_id=ck8SjP0KHS5T3EWGmEvoYp6CNqUyMehS&code={}&grant_type=authorization_code&redirect_uri=https://github.com/sophiashuv/Diabetes_Project".format(code)

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

conn.request("POST", "/v2/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))