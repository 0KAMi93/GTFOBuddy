import requests, re

banner = '''
   ____ _____ _____ ___  ____            _     _       
  / ___|_   _|  ___/ _ \| __ ) _   _  __| | __| |_   _ 
 | |  _  | | | |_ | | | |  _ \| | | |/ _` |/ _` | | | |
 | |_| | | | |  _|| |_| | |_) | |_| | (_| | (_| | |_| |
  \____| |_| |_|   \___/|____/ \__,_|\__,_|\__,_|\__, |
                                                 |___/ 
'''                                                

bin_list = "https://github.com/GTFOBins/GTFOBins.github.io/tree/master/_gtfobins"
first_req = requests.get(bin_list)

response = first_req.text
results = re.findall("\w+\.md", response)

bin_names = []

# Get binary names...
for i in results:
	if i not in bin_names:
		bin_names.append(i)

bin_names = [item.replace('.md', '') for item in bin_names]


#list = ["ab", "bash", "dash", "nano", "screen", "nice"]

m_functions = ["command:", "reverse-shell:", "non-interactive-reverse-shell:", "bind-shell:", "non-interactive-bind-shell:", "file-upload:", "file-download:", "file-write:", "file-read:", "library-load:", "sudo:", "capabilities:", "limited-suid:", "shell:","suid:"]
removed_strings = ["functions:", "---", "- code:", "code: |", "|"]

print(banner)
print("[   Welcome to GTFOBuddy! - Please note: This tool is CASE-SENSITIVE   ]\n")
print("• Type 'exit' or 'quit' to quit or type Ctrl + C\n• Type 'list' to list all binaries\n")
def lookup():
	z = 1
	while z:
		func = input("[  Search for a vulnerable function  ]\n>  ")
		if func in bin_names:
			print("[  Available Options:  ]")
			url_to_request = "https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/" + func + ".md"
			request = requests.get(url_to_request)
			formatted = request.text
			formatted.strip()
			for i in removed_strings:
				formatted = formatted.replace(i, "")
			formatted = formatted.replace("- description:", "- Description")
			for i in m_functions:
				word = " " + i
				if word in formatted:
					i.lstrip()
					formatted = formatted.replace(i, "\n" + "   [  " + i.upper() + "  ]")
			print(formatted)
		elif func == "quit" or func == "exit":
			print("[  Goodbye!  ]")
			exit()
		elif func == "list":
			print("\n")
			for name in range(len(bin_names)):
				print("• ",bin_names[name])
			print("\n")
		else:
			print("Could not find binary:","[", func,"]", "on GTFOBins - Please try another\n")
try:
	lookup()
except KeyboardInterrupt:
	print("[  Goodbye!  ]")