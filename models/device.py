# Modbus device abstraction
class Device:
    def __init__(self, name, unit_id):
        self.name = name
        self.unit_id = unit_id
