import requests
import json

res = "filepath"                                                                                                                                                                                                                                                      
with open("links.txt") as f:
	listy = f.readlines()
	for line in listy:
		response = requests.post(
    		"http://citron.virt.ch.bbc.co.uk/quotes",
    		headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
    		data={"text": line}
			)
	if response is not None:
		with open(res, "a", encoding="utf-8") as outfile:
			json.dump(response.json(), outfile, ensure_ascii=False, indent=4)