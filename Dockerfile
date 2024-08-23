FROM python:3.11-slim

ADD * .

CMD [ "python", "./pre_commit_hook.py" ]