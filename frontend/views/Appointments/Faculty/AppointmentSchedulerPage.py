from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AppointmentSchedulerPage_ui(QWidget):

    go_to_EditSchedulePage = QtCore.pyqtSignal()
    back = QtCore.pyqtSignal()

    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self.setWindowTitle("Appointment Scheduler")
        self._setupAppointmentSchedulerPage()
       
        
    
    def _setupAppointmentSchedulerPage(self):
    
        self.setObjectName("AppointmentScheduler")
        
        # Main layout
        scheduler_layout = QtWidgets.QVBoxLayout(self)
        scheduler_layout.setContentsMargins(0, 0, 0, 0)
        scheduler_layout.setSpacing(10)
        
        # Header
        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        self.Academics_5 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        self.Academics_5.setFont(font)
        self.Academics_5.setStyleSheet("QLabel { color: #084924; }")
        self.Academics_5.setObjectName("Academics_5")
        
        header_layout.addWidget(self.Academics_5)
        header_layout.addStretch(1)

        self.backbutton = QtWidgets.QPushButton("<- Back")
        self.backbutton.setIcon(QtGui.QIcon(":assets/images/back_button.png"))
        self.backbutton.clicked.connect(self.back)
        header_layout.addWidget(self.backbutton)
        
        self.backButton_7 = QtWidgets.QLabel()
        self.backButton_7.setFixedSize(40, 40)
        self.backButton_7.setText("")
        self.backButton_7.setPixmap(QtGui.QPixmap(":assets/back_button.png"))
        self.backButton_7.setScaledContents(True)
        self.backButton_7.setObjectName("backButton_7")
        
        header_layout.addWidget(self.backButton_7)
        
        scheduler_layout.addWidget(header_widget)
        
        # Content widget
        self.widget_25 = QtWidgets.QWidget()
        self.widget_25.setStyleSheet("QWidget#widget_25 { background-color: #FFFFFF; border-radius: 20px; }")
        self.widget_25.setObjectName("widget_25")
        
        widget_layout = QtWidgets.QVBoxLayout(self.widget_25)
        widget_layout.setContentsMargins(20, 20, 20, 20)
        widget_layout.setSpacing(15)
        
        # Controls section
        controls_widget = QtWidgets.QWidget()
        controls_layout = QtWidgets.QHBoxLayout(controls_widget)
        controls_layout.setContentsMargins(0, 0, 0, 0)
        
        self.label_92 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_92.setFont(font)
        self.label_92.setObjectName("label_92")
        
        controls_layout.addWidget(self.label_92)
        controls_layout.addStretch(1)
        
        self.delete_3 = QtWidgets.QPushButton()
        self.delete_3.setFixedSize(80, 30)
        self.delete_3.setStyleSheet("""
            QPushButton {
                background-color: #EB5757;
                color: white;
                border-radius: 4px;
                font: 10pt 'Poppins';
            }
        """)
        self.delete_3.setObjectName("delete_3")
        
        self.createschedule_2 = QtWidgets.QPushButton()
        self.createschedule_2.setFixedSize(120, 30)
        self.createschedule_2.clicked.connect(self.go_to_EditSchedulePage.emit)
        self.createschedule_2.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 8px;
                font: 10pt 'Poppins';
            }
        """)
        self.createschedule_2.setObjectName("createschedule_2")
        
        self.comboBox_2 = QtWidgets.QComboBox()
        self.comboBox_2.setFixedSize(200, 30)
        self.comboBox_2.setStyleSheet("""
            QComboBox {
                border: 2px solid #064420;
                border-radius: 6px;
                padding: 4px 8px;
                font-size: 12px;
                color: #064420;
                background: white;
            }
        """)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        
        controls_layout.addWidget(self.delete_3)
        controls_layout.addWidget(self.createschedule_2)
        controls_layout.addWidget(self.comboBox_2)
        
        widget_layout.addWidget(controls_widget)
        
        # Weekly grid
        self._setupWeeklyGrid(widget_layout)
        
        scheduler_layout.addWidget(self.widget_25, 1)
        
        self.retranslateUi()  # Added missing call to retranslateUi

    def _setupWeeklyGrid(self, parent_layout):
        # Weekly grid container
        grid_container = QtWidgets.QWidget()
        grid_container.setObjectName("grid_container")
        
        grid_layout = QtWidgets.QVBoxLayout(grid_container)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)
        
        # Weekly grid table
        self.weeklyGrid = QtWidgets.QTableWidget()
        self.weeklyGrid.setColumnCount(8)  # Time + Mon..Sun
        self.weeklyGrid.setRowCount(10)
        self.weeklyGrid.setShowGrid(False)
        self.weeklyGrid.verticalHeader().setVisible(False)
        self.weeklyGrid.horizontalHeader().setVisible(True)
        self.weeklyGrid.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.weeklyGrid.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.weeklyGrid.setStyleSheet(
            """
            QTableWidget { 
                background: white; 
                font: 10pt 'Poppins'; 
                border: none;
            }
            QHeaderView::section { 
                background-color: #0a5a2f; 
                color: white; 
                border: 0; 
                padding: 12px 8px; 
                font: 600 11pt 'Poppins';
            }
            """
        )
        
        # Headers
        headers = ["", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, h in enumerate(headers):
            item = QtWidgets.QTableWidgetItem(h)
            self.weeklyGrid.setHorizontalHeaderItem(i, item)
        
        # Configure column widths
        self.weeklyGrid.setColumnWidth(0, 100)
        header = self.weeklyGrid.horizontalHeader()
        try:
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Fixed)
            for c in range(1, 8):
                header.setSectionResizeMode(c, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception:
            pass

        # Time labels and dashed separators
        base_times = ["7:00 AM", "7:30 AM", "8:00 AM", "8:30 AM", "9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM"]
        for r, t in enumerate(base_times):
            item = QtWidgets.QTableWidgetItem(t)
            item.setForeground(QtGui.QBrush(QtGui.QColor("#6b6b6b")))
            self.weeklyGrid.setItem(r, 0, item)
            self.weeklyGrid.setRowHeight(r, 60)
            
            # Create dashed line effect
            for c in range(1, 8):
                w = QtWidgets.QWidget()
                w.setStyleSheet("QWidget { border-bottom: 1px dashed #cfcfcf; }")
                self.weeklyGrid.setCellWidget(r, c, w)

        # Add sample yellow slot blocks
        sample_slots = [
            (0, 1), (0, 2), (0, 4), (0, 5),
            (2, 3),
            (4, 4),
            (6, 2),
        ]
        for r, c in sample_slots:
            self._addWeeklySlot(r, c)
        
        grid_layout.addWidget(self.weeklyGrid, 1)
        parent_layout.addWidget(grid_container, 1)  # FIXED: Added this missing line

    def _addWeeklySlot(self, row, col):
        slot = QtWidgets.QLabel()
        slot.setMinimumHeight(50)
        slot.setStyleSheet("QLabel { background: #ffc000; border-radius: 8px; }")
        slot.setText("")
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(5, 2, 5, 2)
        layout.addWidget(slot, 1)
        self.weeklyGrid.setCellWidget(row, col, container)

    def _onPlusButtonClicked(self, time_slot, day_name):
        """Handle plus button clicks"""
        print(f"Plus button clicked: {day_name} at {time_slot}")
        # Here you can add logic to create a time slot
        # For example: open a dialog, add to database, etc.

    def retranslateUi(self):
        
        # Appointment Scheduler page
        self.Academics_5.setText("Appointment Scheduler")
        self.label_92.setText("Weekly Available Slot")
        self.createschedule_2.setText("Create Schedule")
        self.delete_3.setText("Delete")
        self.comboBox_2.setItemText(0, "1st Semester 2025 - 2026")
        self.comboBox_2.setItemText(1, "2nd Semester 2025 - 2026")
        self.comboBox_2.setItemText(2,  "Summer 2026")