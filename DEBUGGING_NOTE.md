# Debugging Note

## The error
While cloning the repository in Git GUI, I got this message:
"Location C:/Users/MY LAPTOP/Downloads already exists."

## What caused it
I typed the Downloads folder as the Target Directory. Git GUI needs a
folder that does not exist yet, because it creates that folder itself.
Downloads already existed, so the clone stopped.

## How I fixed it
Before: C:/Users/MY LAPTOP/Downloads
After:  C:/Users/MY LAPTOP/Downloads/python-practice

## What I do now
I always end the Target Directory with a new folder name.