import time
from snap7.server import Server as S7Server

# -- This Package -- #
from utils import (
    DEFAULT_TCP_PORT,
)


def main():
    print(f"Server 1 starting...")

    # Creating a S7 instance
    s7_server = S7Server()

    # Start the server
    s7_server.start(tcpport=DEFAULT_TCP_PORT)

    while True:
        event = s7_server.pick_event()
        if event:
            print(s7_server.event_text(event))
        time.sleep(1)


if __name__ == "__main__":
    main()
