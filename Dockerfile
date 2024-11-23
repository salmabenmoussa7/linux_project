FROM python:3.10-buster
RUN mkdir -p /dashboard_app
WORKDIR /dashboard_app
COPY . .
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

CMD bash -c "cd bin && . run.sh"