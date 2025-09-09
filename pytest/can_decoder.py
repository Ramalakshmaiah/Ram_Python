
# can_decoder.py
def decode_battery_status(data):
    # Example: first byte = SOC (%), second byte = Temperature (°C)
    return {
        "soc": data[0],
        "temperature": data[1] - 40   # offset
    }
