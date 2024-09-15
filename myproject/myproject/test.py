import os

# Check if the file exists
path = "myapp/credentials/credentials.json"
if not os.path.exists(path):
    print(f"File not found: {path}")
else:
    print(f"File found: {path}")
