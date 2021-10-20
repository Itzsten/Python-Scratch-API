import json
try:
    import requests
except:
    raise ImportError('Please open the cmd and type the following:\npip install requests')
class Scratch:
    def website(): return json.loads(requests.get('https://api.scratch.mit.edu').text)["website"]
    def api(): return json.loads(requests.get('https://api.scratch.mit.edu').text)["api"]
    def help(): return json.loads(requests.get('https://api.scratch.mit.edu').text)["help"]
class User(object):
    def __init__(self, user):
        if 'https://' in user: usp = user.split('/')[4]
        else: usp = user
        self.user = usp
    def id(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/users/' + self.user).text)["id"]
    def scratchteam(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/users/' + self.user).text)["scratchteam"]
    def exactUsername(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/users/' + self.user).text)["username"]
    def joindate(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/users/' + self.user).text)["history"]["joined"]
    def profilepicture(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/users/' + self.user).text)["profile"]["images"]["90x90"]
    def status(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/users/' + self.user).text)["profile"]["status"]
    def bio(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/users/' + self.user).text)["profile"]["bio"]
    def country(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/users/' + self.user).text)["profile"]["country"]
    def following(self):
        c = []
        for i in range(0, len(json.loads(requests.get(f'https://api.scratch.mit.edu/users/{self.user}/following').text))): c.append(json.loads(requests.get(f'https://api.scratch.mit.edu/users/{self.user}/following').text)[i]["username"])
        return c
    def followingCount(self):
        return len(json.loads(requests.get('https://api.scratch.mit.edu/users/'+ + self.user + '/following').text)) 
    def followers(self):
        c = []
        for i in range(0, len(json.loads(requests.get(f'https://api.scratch.mit.edu/users/{self.user}/followers').text))): c.append(json.loads(requests.get(f'https://api.scratch.mit.edu/users/{self.user}/followers').text)[i]["username"])
        return c
    def followersCount(self):
        return len(json.loads(requests.get('https://api.scratch.mit.edu/users/'+ self.user+'/followers').text))
    def projects(self):
        c = []
        for i in range(0, len(json.loads(requests.get(f'https://api.scratch.mit.edu/users/{self.user}/projects').text))): c.append(json.loads(requests.get(f'https://api.scratch.mit.edu/users/{self.user}/projects').text)[i]["id"])
        return c
    def projectsCount(self):
        return len(json.loads(requests.get('https://api.scratch.mit.edu/users/'+ self.user+'/projects').text))
    def link(self):
        return 'https://scratch.mit.edu/users/' + self.user + '/'
class Project(object):
    def __init__(self, project):
        if 'https://' in project: usp = project.split('/')[4]
        else: usp = project
        self.project = usp
    def link(self):
        return 'https://scratch.mit.edu/users/' + self.project + '/'
    def title(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/projects/' + self.project).text)["title"]
    def description(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/projects/' + self.project).text)["description"]
    def instructions(self):
        return json.loads(requests.get('https://api.scratch.mit.edu/projects/' + self.project).text)["instructions"]
