# Python-Scratch-API
A Python script to interact with the Scratch API.

Start by downloading the Scratch.py file, and make sure you have the library requests installed on your device.

# Users
Let's start by setting a User variable!

```python
from scratch import *
user = User('griffpatch')
```
Now, let's say we wanted the profile picture.
```python
link = user.profilepicture()
```
This gives us the following:
```
https://cdn2.scratch.mit.edu/get_image/user/1882674_90x90.png?v=
```
Which represents a link to the users profile picture!

So, how do we check if a user is in Scratchteam?
Well, we can do that by using the following:
```python
print(User('griffpatch').scratchteam()) # False
print(User('Za-Chary').scratchteam())   # True
```
Get User ID:
```python
print(User('griffpatch').id()) # 1882674 (User ID of griffpatch)
```
You can also get users from links:
```python
linkuser = User('https://scratch.mit.edu/griffpatch/')
normal = User('griffpatch')
# These to work exactly the same.
```
Get exact username:
```python
user = User('GrIfFpAtCh')
print(user.exactUsername()) # griffpatch
```
Get joindate of user:
```python
user = User('griffpatch')
print(user.joindate()) # 2012-10-24T12:59:31.000Z
```
Get status of user:
```python
print(User('mref').status())
```
Get bio of user:
```python
print(User('mref').bio())
```
Get country of user:
```python
print(User('griffpatch').country())
```
Get a list of usernames that the user follows:
```python
print(User('mref').following())
```
Get the amount of users the user follows:
```python
print(User('mref').followingCount())
```
Get a list of usernames that follows the user:
```python
print(User('mref').followers())
```
Get follower count:
```python
print(User('mref').followersCount())
```
Get list of Project ID's that the user made:
```python
print(User('griffpatch').projects())
```
Get the amounts of projects the user made:
```python
print(User('griffpatch').projectsCount())
```
Get link of user
```python
print(User('griffpatch').link())
```
# Projects
Let's start by setting a project variable! We can use both links and ID's.
```python
project = Project('https://scratch.mit.edu/projects/501406149/') # You can use links or the last number (Project ID (501406149 in this case))
```
Let's get the title!
```python
print(project.title()) # In the Sky - Platformer
```
Let's get the description!
```python
print(project.description()) # ...
```
Get link of project
```python
print(Project('501406149').link())
```
Let's get the instructions!
```python
print(project.instructions()) # ...
```
Let's see if a project is visible!
```python
print(project.visibility()) # True
```
Check if a project is public!
```python
print(project.public()) # True
```
Check if comments is allowed on a project!
```python
print(project.commentsAllowed()) # True
```
Let's see who made the project!
```python
print(project.author()) # Geometrysten2
```
Let's get the projects thumbnail!
```python
print(project.thumbnail()) # (link to thumbnail)
```
Let's see when the project was created!
```python
print(project.created())
```
Let's see when the project was shared publicly!
```python
print(project.shared())
```
Let's see when the last time that the project was modified!
```python
print(project.modified())
```
Let's get the projects amount of views!
```python
print(project.views())
```
Let's get the projects amount of favorites!
```python
print(project.favorites())
```
Let's get the projects amount of loves!
```python
print(project.loves())
```
Let's get the projects amount of remixes!
```python
print(project.remixesCount())
```
Let's get the remixes projects ID's!
```python
print(project.remixes())
```
Let's check if a project exists!
```python
print(Project.exists(50305)) # False
```
Let's check the latest projects posted!
```python
print(Project.latestprojects())
```
# Scratch Main
Get Scratch website:
```python
print(Scratch.website())
```
Get Scratch API:
```python
print(Scratch.api())
```
Get Scratch help E-Mail:
```python
print(Scratch.help())
```
