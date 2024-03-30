FROM python:3.12

COPY ./ /usr/backend
RUN python3 -m pip install -r /usr/backend/requirements.txt

# -- Configuring timezone -- #
ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/timezone

EXPOSE 8000

WORKDIR /usr/backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
