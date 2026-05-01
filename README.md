services:
  - type: web
    name: vote-detector
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_SECRET_KEY
        generateValue: true
      - key: VOTING_PEPPER
        generateValue: true
