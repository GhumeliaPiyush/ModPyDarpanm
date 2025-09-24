import pytest
from unittest.mock import MagicMock
from app.core.modbus_client import ModbusClient


def test_read_registers_mocked():
    client = ModbusClient(protocol="rtu")

    # Mock the pymodbus client
    client._client = MagicMock()

    # Create a fake response object with .registers and .isError()
    fake_response = MagicMock()
    fake_response.isError.return_value = False
    fake_response.registers = [123, 456]

    # Make the client return our fake response
    client._client.read_holding_registers.return_value = fake_response

    result = client.read_registers(1, 2)

    assert result == [123, 456]
