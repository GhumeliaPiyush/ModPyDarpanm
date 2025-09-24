# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget,QProgressBar,QPushButton,QFileDialog,QMessageBox,QLineEdit,QDateEdit,
                               QTableWidgetItem, QVBoxLayout, QWidget, QLabel,QLCDNumber,QHBoxLayout,QGroupBox,QStackedWidget,QSizePolicy,
                               QScrollArea,QCheckBox,QGridLayout,QFrame)
from PySide6.QtCore import QThreadPool, QRunnable, Signal, QObject, QTimer,QThread,Slot,Qt,QTimer,QRect,QSize,QCoreApplication,QDate,QEvent
from PySide6.QtGui import QIcon,QFont
from PySide6.QtGui import QScreen


from pymodbus.client.sync import ModbusSerialClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.framer.rtu_framer import ModbusRtuFramer
from pymodbus.constants import Defaults
from pymodbus.exceptions import ModbusException, ConnectionException
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer

import numpy as np
import threading
import time
from views.ui_DashBoard import Ui_MainWindow
from views.ui_Protocol_SettingDia import Ui_Dialog


class ScrollingAlarms(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(35)  # Adjust height as needed

        # Dictionary to hold active alarms
        self.connection_error = {}
        self.slave_error = {}

        # Scrolling label
        self.error_label = QLabel("", self)
        self.error_label.setAlignment(Qt.AlignVCenter)
        # self.error_label.setStyleSheet("color: red; font-size: 20px; font-weight:bold;")  # Customize appearance

        layout = QVBoxLayout(self)
        layout.addWidget(self.error_label)
        layout.setContentsMargins(0, 0, 0, 0)

        # Timer for scrolling effect
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scroll_error_messages)
        self.timer.start(40)  # Adjust speed if needed

        # Initial position
        self.x_position = self.width()
        # self.x_position = self.width() 

    def update_alarms(self, slave_errors):
        """Update active alarms dynamically"""
        self.slave_error = slave_errors
        self.refresh_display()

    def refresh_display(self):
        """Update text content based on active alarms"""

        self.error_label.setText(self.slave_error)
        # self.x_position = self.width()  # Reset position

    def scroll_error_messages(self):
        """Scroll the error messages continuously"""
        self.x_position -= 2  # Adjust speed
        self.error_label.move(self.x_position, 5)

        # Reset position when out of view
        if self.x_position + self.error_label.width() < 0:
            self.x_position = self.width()


# Signal Class for Thread Communication
class WorkerSignals(QObject):
    result = Signal(object)
    
# Worker Thread for Modbus Communication
class ModbusWorker(QRunnable):
    def __init__(self, master):
        super().__init__()
      
        
        self.master = master
        
        self.signals = WorkerSignals()
        self.is_running = True
        
        self.read_process = {}
        try:
            match self.master.readingArea:
                    case "Input Registers":
                        area_add =30000
                    case "Holding Registers":
                        area_add =40000
            match self.master.DataType:
                    case "INT":
                        for i in range(self.master.Range):
                            add = self.master.StartAdd+i+area_add
                            self.read_process[f'{add}'] = 0
                    case "UINT":
                        for i in range(self.master.Range):
                            add = self.master.StartAdd+i+area_add
                            self.read_process[f'{add}'] = 0
                    case "LONG":
                        for i in range(0,self.master.Range,2):
                            add = self.master.StartAdd+i+area_add
                            self.read_process[f'{add}'] = 0
                    case "ULONG":
                        for i in range(0,self.master.Range,2):
                            add = self.master.StartAdd+i+area_add
                            self.read_process[f'{add}'] = 0
                    case "FLOAT":
                        for i in range(0,self.master.Range,2):
                            add = self.master.StartAdd+i+area_add
                            self.read_process[f'{add}'] = 0.00
        except Exception as e:
            pass
        
        
        
    def decode_response(self,registers,datatype='INT',endiancod = 'Big Endian',word_swap=False):
        regs = np.array(registers, dtype=np.uint16)
        
        # Handle word swap for 32-bit types
        if datatype in ("LONG", "ULONG", "FLOAT") and word_swap:
            regs = regs.reshape(-1, 2)[:, ::-1].ravel()
        
        # Convert to bytes
        raw = regs.tobytes(order="C")
        
        # Dtype map
        dtype_map = {
            "INT": ">i2" if endiancod == "Big Endian" else "<i2",
            "UINT": ">u2" if endiancod == "Big Endian" else "<u2",
            "LONG": ">i4" if endiancod == "Big Endian" else "<i4",
            "ULONG": ">u4" if endiancod == "Big Endian" else "<u4",
            "FLOAT": ">f4" if endiancod == "Big Endian" else "<f4",
        }
        
        dtype = np.dtype(dtype_map[datatype])
        
        # Cast to NumPy array
        values = np.frombuffer(raw, dtype=dtype)

        return values.tolist()

    def stop(self):
        self.is_running = False

    @Slot()
    def run(self):

        """ self.SlaveId = 1
            self.StartAdd = 0
            self.Range = 0
            self.Protocol = "MODBUS-RTU"
            
            self.readingArea = self.RegisterCombo.currentText()
            self.DataEndcod = self.EndienCombo.currentText()
            self.DataType = self.DataTypeCombo.currentText()
            self.FrmtDisp.setText(f"{self.DataType}")
            
            # Communication Variable Iteration:
            self.BaudRate = 9600
            self.DataBits = 8
            self.StopBit = 1
            self.PariTy = "N"
            self.ComAdd = "COM1"
            self.IpAdd = None
            self.IpProt = None
            self.LinkFlag = False
                
        """

        
        while self.is_running:
            match self.master.Protocol:
                case "MODBUS-RTU":
                    ''' Define modbus rtu para maters and client'''
                    port = self.master.ComAdd
                    baudRate = self.master.BaudRate
                    databits = self.master.DataBits
                    stopBit = self.master.StopBit
                    pari = self.master.PariTy
                    client = ModbusSerialClient(method='rtu',port =port,baudrate=baudRate,bytesize=databits,
                                                parity=pari,stopbits=stopBit,timeout=1,handle_local_echo=1,retry_on_empty=True)

                case "MODBUS-TCP":
                    ''' Define modbus tcp para maters and client'''
                    # get the ip address and port number:
                    port_add =int(self.master.IpProt)
                    ip_add = self.master.IpAdd
                    
                    # defining the the modbustcp client:
                    client = ModbusTcpClient(ip_add, port=port_add,framer=ModbusFramer)
                    Defaults.Timeout = 5
            
            if client.connect():
                try:
                    # self.master.scroll_alarm.update_alarms(slave_errors='')
                    start = int(self.master.StartAdd)
                    count = int(self.master.Range)
                    unit = int(self.master.SlaveId)
                    
                    self.error_flage = False
                    match self.master.readingArea:
                        case "Input Registers":
                            response = client.read_input_registers(start,count=count,unit=unit)
                        case "Holding Registers":
                            response = client.read_holding_registers(start,count=count,unit=unit)
                            
                    read_response = response.registers if not response.isError() else ["--err--"] * count
                    if '--err--' not in read_response:
                        read_vals = self.decode_response(registers=read_response,datatype=self.master.DataType,endiancod=self.master.DataEndcod,word_swap=False)
                        self.master.scroll_alarm.update_alarms(slave_errors='')
                    else:
                        read_vals = read_response
                        self.master.scroll_alarm.update_alarms(slave_errors='Error while reading the slave please check connection and parameters')
                    for i,(key,val) in enumerate(self.read_process.items()):
                        self.read_process[key]=read_vals[i]
                   
                    
                except Exception as e:
                    self.master.scroll_alarm.update_alarms(slave_errors='Error while reading the slave please check connection and parameters')
                    
            
                client.close()                                                 
            self.signals.result.emit(self.read_process)
            time.sleep(0.1)  # Poll every 200 milisecond



# Main Window Class::
class ModPyDarpanam(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("|| ModPyदरपणम् ||")
        
        self.readValues = {}
        # Iterating Communication Protocol Variables::
        self.SlaveId = 1
        self.StartAdd = 0
        self.Range = 0
        self.Protocol = "MODBUS-RTU"
        
        self.readingArea = self.RegisterCombo.currentText()
        self.DataEndcod = self.EndienCombo.currentText()
        self.DataType = self.DataTypeCombo.currentText()
        self.FrmtDisp.setText(f"{self.DataType}")
        
        # Communication Variable Iteration:
        self.BaudRate = 9600
        self.DataBits = 8
        self.StopBit = 1
        self.PariTy = "N"
        self.ComAdd = "COM1"
        self.IpAdd = None
        self.IpProt = None
        self.LinkFlag = False
        
        # Assign function to the SideBar buttons :
        
        self.Settings_btn.clicked.connect(self.Protocol_setting) 
        self.Connect_btn.toggled.connect(self.on_connection_toggle)
        
         # Assign function to the SideBar Combo Boxes :
        self.RegisterCombo.currentTextChanged.connect(self.ChangeReadingArea)
        self.EndienCombo.currentTextChanged.connect(self.ChangeDataEncoding)
        self.DataTypeCombo.currentTextChanged.connect(self.ChangeDataType)
        
        
        self.AddDisp.setText(str(self.StartAdd))
        self.RngDisp.setText(str(self.Range))
        self.PortDisp.setText("COM1")
        self.ChDisp.setText("MODBUS-RTU")
        self.SlaveDisp.setText("1")
        
        
        # Design settings and programing for ToolBar Display:
        self.AddDisp.installEventFilter(self)
        self.RngDisp.installEventFilter(self)
        self.editor = None  # placeholder for temporary field
        
        # setting scroll alarm window:
        self.scroll_alarm = ScrollingAlarms(self.AlarmWid)
        self.scroll_alarm.setGeometry(0, 0, self.AlarmWid.width(), self.AlarmWid.height())
        
        # declaing a QThreaPool for parallel operations
        self.threadpool = QThreadPool()
    
    def closeEvent(self, event):
        if hasattr(self, "worker") and self.worker.is_running:
            self.worker.stop()
            # Wait for all threads to finish
            super().closeEvent(event)
        
    def Protocol_setting(self,checked):
        if checked:
            self.Settings_btn.setChecked(False)
            self.update_protocol = Ui_Dialog()            
            self.update_protocol.SaveProtocol_button.clicked.connect(self.transfer_protocol)
            self.update_protocol.exec()
        
    def transfer_protocol(self):

        self.SlaveId = self.update_protocol.slaveId_combo.currentText()
        self.Protocol = self.update_protocol.chanelType_combo.currentText()
        self.SlaveDisp.setText(self.SlaveId)
        self.ChDisp.setText(self.Protocol)
        if self.Protocol == "MODBUS-RTU":
            self.BaudRate = int(self.update_protocol.baudRate_combo.currentText())
            self.ComAdd = self.update_protocol.comPort_combo.currentText()
            self.DataBits = int(self.update_protocol.dataBit_combo.currentText())
            self.StopBit = int(self.update_protocol.stopBit_combo.currentText())
            self.PariTy = self.update_protocol.parityCombo.currentText()
            self.PortDisp.setText(self.ComAdd)
        elif self.Protocol == "MODBUS-TCP":
            ipAd = self.update_protocol.IpEdit.text().split()
            self.PortDisp.setText(self.update_protocol.IpEdit.text())
            self.IpAdd = ipAd[0]
            self.IpProt = ipAd[1]
        self.update_protocol.close()
        
    # defing function to start and stop communiocation::
    def start_comm(self):
        if not hasattr(self, "worker") or not self.worker.is_running:
            self.worker = ModbusWorker(self)
            self.worker.signals.result.connect(self.update_ui)  # update GUI safely
            self.threadpool.start(self.worker)

    def stop_comm(self):
        if hasattr(self, "worker") and self.worker.is_running:
            self.worker.stop()

        
    
    
    
    def on_connection_toggle(self, checked):
        if checked:
            # Connection ON
            self.Connect_btn.setText("Link On")
            # self.Settings_btn.hide()   # or .setDisabled(True)
            self.Settings_btn.setDisabled(True)
            self.RegisterCombo.setDisabled(True)
            self.EndienCombo.setDisabled(True)
            self.DataTypeCombo.setDisabled(True)
            
            self.start_comm() # start the serial communication
            self.LinkFlag = True

        else:
            # Connection OFF
            self.Connect_btn.setText("Link Off")
            # self.Settings_btn.show()   # or .setDisabled(False)
            self.Settings_btn.setDisabled(False)
            self.RegisterCombo.setDisabled(False)
            self.EndienCombo.setDisabled(False)
            self.DataTypeCombo.setDisabled(False)
            self.stop_comm() # disconnect the slave
            self.LinkFlag = False
            
    # screen upadtion function:
    def update_ui(self,values: dict):
        # this is called in the main thread
        self.readings = values
        self.set_reading_area()
        time.sleep(0.1)

    
    def ChangeReadingArea(self,text):
        self.readingArea = text
        self.set_reading_area()
        
    
    def ChangeDataEncoding(self,text):
        self.DataEndcod = text
    
    def ChangeDataType(self,text):
        self.DataType = text
        self.FrmtDisp.setText(self.DataType)
        self.set_reading_area()
    

            
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.MouseButtonPress and watched in (self.AddDisp, self.RngDisp):
            self.show_editor(watched)
            return True
        return super().eventFilter(watched, event)

    def show_editor(self, label: QLabel):
        if self.editor:
            self.editor.deleteLater()

        # Create temporary input box over the label
        self.editor = QLineEdit(label.text(), self)
        self.editor.setGeometry(label.geometry())
        self.editor.setAlignment(Qt.AlignCenter)
        self.editor.setStyleSheet("QLineEdit { border: 1px solid #1976D2; padding: 6px; }")
        self.editor.setFocus()
        self.editor.returnPressed.connect(lambda: self.apply_text(label))
        self.editor.editingFinished.connect(lambda: self.apply_text(label))
        self.editor.show()

    def apply_text(self, label: QLabel):
        if self.editor:
            new_text = self.editor.text()
            st_ad = self.StartAdd
            rng = self.Range
            label.setText(new_text)
            # Save value to variable
            if label == self.AddDisp:
                self.StartAdd = int(new_text)
            elif label == self.RngDisp:
                self.Range = int(new_text)
            
            self.editor.deleteLater()
            self.editor = None
            
            if (st_ad != self.StartAdd) or (rng !=self.Range):
                self.set_reading_area()
    
    def set_reading_area(self):
        if self.Range !=0:
            if self.LinkFlag == False:
                self.readValues={}
                match self.readingArea:
                    case "Input Registers":
                        area_add =30000
                    case "Holding Registers":
                        area_add =40000
                match self.DataType:
                    case "INT":
                        for i in range(self.Range):
                            add = self.StartAdd+i+area_add
                            self.readValues[f'{add}'] = '0'
                    case "UINT":
                        for i in range(self.Range):
                            add = self.StartAdd+i+area_add
                            self.readValues[f'{add}'] = '0'
                    case "LONG":
                        for i in range(0,self.Range,2):
                            add = self.StartAdd+i+area_add
                            self.readValues[f'{add}'] = '0'
                    case "ULONG":
                        for i in range(0,self.Range,2):
                            add = self.StartAdd+i+area_add
                            self.readValues[f'{add}'] = '0'
                    case "FLOAT":
                        for i in range(0,self.Range,2):
                            add = self.StartAdd+i+area_add
                            self.readValues[f'{add}'] = '0.00'
            else:
                self.readValues= self.readings
                
                            
            grid = self.DispScrollWidget.layout()
            if grid is None:
                grid = QGridLayout(self.DispScrollWidget)
            self.clearLayout(grid)
            
            # Add "pairs" (Address, Value) in grid
            row = 0
            col = 0
            for i, (addr, val) in enumerate(self.readValues.items()):
                # Address
                addr_label = QLabel(str(f"Reading - {addr} : {val}"))
                addr_label.setStyleSheet("font: 12pt 'Consolas'; color: #000000;")
                
                grid.addWidget(addr_label, row, col) 

                row +=1
                if row==10:
                    row = 0
                    col += 1 
                
    def clearLayout(self,layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    # Nested layout
                    self.clearLayout(item.layout()) 
                        
                                        
            

if __name__ == "__main__":
    app = QApplication([])
    window = ModPyDarpanam()
    window.showMaximized()

    app.exec()