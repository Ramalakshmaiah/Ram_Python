import pytest

from uds import diagnostic_session_control,ecu_reset,read_data_by_identifier,write_data_by_identifier

# ---------- Test Diagnostic Session Control (0x10) ----------

@pytest.mark.parametrize("subfunction,expected",[
    (0x01,"Positive Response"), # Default Session
    (0x02,"Positive Response"), # Programming Session
    (0x03,"Positive Response"), # Exteded Session
    (0x99,"Negative Response"), # Unsupported Subfunction
])

def test_diagnostic_session_control(subfunction,expected):
    assert diagnostic_session_control(subfunction) == expected

 # ---------- Test ECU Reset (0x11) ----------

@pytest.mark.parametrize("subfunction,expected", [
    (0x01,"Positive Response"), # Hard Reset
    (0x02,"Positive Response"), # Key off on Reset
    (0x03,"Positive Response"), # Soft Reset
    (0xFF,"Negative Response"), # Invalid Reset type
])

def test_ecu_reset(subfunction,expected):
    assert ecu_reset(subfunction) == expected  

# ---------- Test ReadDataByIdentifier (0x22) ----------
@pytest.mark.parametrize("did,expected", [
    (0xF190, "VIN123456789"),       # Vehicle Identification Number
    (0xF187, "SW_VERSION_1.0"),     # Software Version
    (0x1234, "Negative Response"),  # Unsupported DID
])
def test_read_data_by_identifier(did, expected):
    assert read_data_by_identifier(did) == expected


# ---------- Test WriteDataByIdentifier (0x2E) ----------
@pytest.mark.parametrize("did,value,expected", [
    (0xF187, "NEW_SW", "Write Successful"),     # Valid DID + data length OK
    (0xF187, "TOO_LONG_VERSION_STRING", "Negative Response"),  # Invalid length
    (0x9999, "ANY", "Negative Response"),       # Unsupported DID
])
def test_write_data_by_identifier(did, value, expected):
    assert write_data_by_identifier(did, value) == expected