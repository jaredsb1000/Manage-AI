name: Run Manage AI

on:
  # Runs every day at 9:00 AM UTC
  schedule:
    - cron: '0 9 * * *'
  
  # Allows you to run her manually
  workflow_dispatch:

jobs:
  run_script:
    runs-on: ubuntu-latest
    
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install Tools
        run: pip install requests

      - name: Execute Manage
        run: python manage.py
