FROM python:3.12

COPY ./src/requirements.txt /usr/src/siemens/src/requirements.txt
RUN python3 -m pip install -r /usr/src/siemens1/src/requirements.txt

# Configuring timezone
ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/timezone

EXPOSE 102

WORKDIR /usr/src

ENTRYPOINT ["python", "siemens1/src/main.py"]
