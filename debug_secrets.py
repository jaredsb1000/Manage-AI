import os

print("--- DEBUGGING SECRETS ---")

# 1. Check if we can see the target secret
target = "GUMROAD_ACCESS_TOKEN"
value = os.getenv(target)

print(f"Looking for: {target}")
print(f"Value Found: {value}")
print("-" * 20)

# 2. List ALL environment variables that start with "GUM"
# This will show us if GitHub is loading the secrets at all
found = False
for key in os.environ.keys():
    if key.startswith("GUM"):
        print(f"Found Key: {key}")
        found = True

if not found:
    print("ERROR: No keys starting with 'GUM' found at all.")
    print("       This means GitHub isn't loading the secrets.")
else:
    print("INFO: Gumroad keys are loaded. Check the value above.")
