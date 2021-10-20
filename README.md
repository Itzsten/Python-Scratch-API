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
