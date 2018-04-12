import requests
import json

res = "filepath"                                                                                                                                                                                                                                                      
fhand = open("links.txt")
for line in fhand:
	response = requests.post(
    	"http://citron.virt.ch.bbc.co.uk/quotes",
    	headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
    	data={"text": fhand}
	)
	if response is not None:
		with open(res, "w", encoding="utf-8") as outfile:
			json.dump(response.json(), outfile, ensure_ascii=False, indent=4)