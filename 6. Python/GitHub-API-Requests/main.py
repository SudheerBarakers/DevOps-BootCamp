import requests

response = requests.get("https://api.github.com/users/SudheerBarakers")
my_projects = response.json()

print(my_projects)

print("Login Name:", my_projects['login'])
print("URL:", my_projects['html_url'])
