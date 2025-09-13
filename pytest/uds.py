# Simulated UDS functions for practice

def diagnostic_session_control(subfunction:int) ->str:
    # Service ID: 0x10
    if subfunction in [0x01,0x02,0x03]:
        return "Positive Response"
    return "Negative Response"

def ecu_reset(subfunction:int) -> str:
    # Service ID: 0x11

    if subfunction in [0x01,0x02,0x03]:
        return "Positive Response"
    return "Negative Response"

def read_data_by_identifier(did: int) -> str:
    #Service ID: 0x22
    supported_dids ={0xF190: "VIN123456789",
                    0XF187:"SW_VERSION_1.0"}
    return supported_dids.get(did,"Negative Response")

def write_data_by_identifier(did: int,value: str) ->str:
    # Srvice ID:0x2E
    if did == 0xF187 and len(value) <=10:
        return "write Successful"
    return "Negative Response"