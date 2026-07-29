import time

BLOCKS = [
    {
        "type": "print",
        "entry": True,
        "numeric": False,
        "color": "green"
    },
    {
        "type": "wait",
        "entry": True,
        "numeric": True,
        "color": "green"
    }
]


def Play(code):

    print("Play")

    for block_info, entry in code:
        value = entry.get() if entry else ""

        if block_info["type"] == "print":
            print(value)

        elif block_info["type"] == "wait":
            time.sleep(float(value or 0))