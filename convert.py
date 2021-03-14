from requests.structures import CaseInsensitiveDict

raw =  "id=12345&quantity=1"

keyvals = raw.split("&")

payload = CaseInsensitiveDict()

for pair in keyvals:
    split = pair.split("=")
    key = split[0]
    value = split[1]
    payload[key] = value.replace("+", " ")

print(payload)
