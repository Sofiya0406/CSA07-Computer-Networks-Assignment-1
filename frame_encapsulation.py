"""Illustrative layer-by-layer encapsulation exercise."""
LAYERS = [("Application", "HTTP"), ("Transport", "TCP"),
          ("Network", "IP"), ("Data link", "ETH")]

def send(message):
    pdu = message
    for layer, tag in LAYERS:
        if tag == "ETH":
            pdu = f"[{tag}|{pdu}|FCS]"
        else:
            pdu = f"[{tag}|{pdu}]"
        print(f"{layer:<14} adds {tag:<4} -> {len(pdu)} bytes")
    return pdu

def receive(frame):
    pdu = frame
    for layer, tag in reversed(LAYERS):
        head = "[" + tag + "|"
        tail = "|FCS]" if tag == "ETH" else "]"
        assert pdu.startswith(head) and pdu.endswith(tail), f"{layer}: bad header"
        pdu = pdu[len(head):-len(tail)]
    return pdu

if __name__ == "__main__":
    frame = send("GET /results")
    print("on the wire:", frame)
    print("delivered :", receive(frame))
    print(f"overhead   : {len(frame) - len('GET /results')} bytes for 12 bytes of data")
