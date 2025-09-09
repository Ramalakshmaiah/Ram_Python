from can_decoder import decode_battery_status

def test_battery_status():
    data = [80, 65]   # SOC=80%, Temp=65-40=25°C
    status = decode_battery_status(data)
    assert status["soc"] == 80
    assert status["temperature"] == 25

