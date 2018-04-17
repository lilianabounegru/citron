import requests
import json

res = "filepath" 
out_list = []                                                                                                                                                                                                                                                     
with open("links.txt") as f:
	listy = f.readlines()
	for line in listy:
		print(line)
		response = requests.post(
    		"http://citron.virt.ch.bbc.co.uk/quotes",
    		headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
    		data={"text": line}
			)
		if response is not None:
			out_list.append(response.json())
			print(out_list)
		with open(res, "w", encoding="utf-8") as outfile:
			json.dump(out_list, outfile, ensure_ascii=False, indent=4)
