FROM python:3.6-alpine
ADD . /app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk update && apk add curl 
HEALTHCHECK --interval=3s --timeout=1s CMD curl -f http://localhost:5000 || exit 1
CMD ["flask", "run"]


