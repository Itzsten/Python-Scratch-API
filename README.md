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
