from pymodbus.client import sync
from pymodbus.framer.rtu_framer import ModbusRtuFramer
from pymodbus.exceptions import ModbusException, ConnectionException


class ModbusClient:
    def __init__(self, protocol="rtu", port=None, baudrate=9600, ip=None, tcp_port=502, unit_id=1):
        """
        Wrapper for pymodbus Modbus client.

        :param protocol: "rtu" or "tcp"
        :param port: COM port for RTU (e.g., "COM3" or "/dev/ttyUSB0")
        :param baudrate: Baudrate for RTU
        :param ip: IP for TCP
        :param tcp_port: TCP port (default 502)
        :param unit_id: Modbus slave unit id
        """
        self.protocol = protocol
        self.port = port
        self.baudrate = baudrate
        self.ip = ip
        self.tcp_port = tcp_port
        self.unit_id = unit_id
        self._client = None

    def connect(self):
        """Establish connection."""
        if self.protocol == "rtu":
            self._client = sync.ModbusSerialClient(
                method="rtu",
                port=self.port,
                baudrate=self.baudrate,
                timeout=1,
                framer=ModbusRtuFramer,
            )
        elif self.protocol == "tcp":
            self._client = sync.ModbusTcpClient(
                host=self.ip,
                port=self.tcp_port,
                timeout=1,
            )
        else:
            raise ValueError("Unsupported protocol: choose 'rtu' or 'tcp'")

        if not self._client.connect():
            raise ConnectionException("Unable to connect to Modbus device")

    def disconnect(self):
        """Close connection."""
        if self._client:
            self._client.close()

    def read_registers(self, address, count=1):
        """Read holding registers."""
        if not self._client:
            raise ModbusException("Not connected")

        response = self._client.read_holding_registers(address, count, unit=self.unit_id)
        if response.isError():
            raise ModbusException(f"Read failed: {response}")
        return response.registers

    def write_register(self, address, value):
        """Write single register."""
        if not self._client:
            raise ModbusException("Not connected")

        response = self._client.write_register(address, value, unit=self.unit_id)
        if response.isError():
            raise ModbusException(f"Write failed: {response}")
        return True
