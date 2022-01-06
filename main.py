import requests
import json

auth_key = 'auth_key'
auth_email = 'auth_email'

headers = {'X-Auth-Email': auth_email, 'X-Auth-Key': auth_key,
           'Content-Type': 'application/json'}


r = requests.get(
    "https://api.cloudflare.com/client/v4/user/firewall/access_rules/rules", headers=headers)

rjs = json.loads(r.text)


cnt = 0
"""with open("ips.txt", "r+") as f:
    for i in rjs:
        for ids in rjs["result"]:
            cnt = cnt + 1
            f.write(ids["configuration"]["value"] + "\n")
            print(ids["configuration"]["value"])

print("Total {0}".format(cnt))"""

cnt = 0
for i in rjs:
    for ids in rjs["result"]:
        cnt = cnt + 1
        print(ids["id"])
        delreq = requests.delete(
            "https://api.cloudflare.com/client/v4/user/firewall/access_rules/rules/{0}".format(ids["id"]), headers=headers)
        print(delreq.text)

print("Total {0}".format(cnt))

# delreq = requests.delete("https://api.cloudflare.com/client/v4/user/firewall/access_rules/rules/YOUR_ZONE_ID", headers = headers)

# print(delreq.text)
