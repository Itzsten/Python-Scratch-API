# Python-Scratch-API
A Python script to interact with the Scratch API.

Start by downloading the Scratch.py file, and make sure you have the library requests installed on your device.

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
exactUsername gives us the exact name.
```python
user = User('GrIfFpAtCh')
print(user.exactUsername()) # griffpatch
```
