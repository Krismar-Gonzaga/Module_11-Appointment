from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class FacultyEditSchedulePage_ui(QWidget):
    back = QtCore.pyqtSignal()

    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self._setupEditSchedulePage()


    def _setupEditSchedulePage(self):
        self.setObjectName("Editschedule")
        
        # Main layout
        edit_layout = QtWidgets.QVBoxLayout(self)
        edit_layout.setContentsMargins(0, 0, 0, 0)
        edit_layout.setSpacing(10)
        
        # Header
        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        self.RequestPage = QtWidgets.QLabel("Edit Schedule")
        font = QtGui.QFont("Poppins", 24)
        self.RequestPage.setFont(font)
        self.RequestPage.setStyleSheet("color: #084924;")
        
        header_layout.addWidget(self.RequestPage)
        header_layout.addStretch(1)

        self.backbutton = QtWidgets.QPushButton("<- Back")
        self.backbutton.clicked.connect(self.back)
        header_layout.addWidget(self.backbutton)

        self.backButton_3 = QtWidgets.QLabel()
        self.backButton_3.setFixedSize(40, 40)
        self.backButton_3.setPixmap(QtGui.QPixmap(":/assets/back_button.png"))
        self.backButton_3.setScaledContents(True)
        
        header_layout.addWidget(self.backButton_3)
        edit_layout.addWidget(header_widget)
        
        # White container with rounded corners
        self.widget_26 = QtWidgets.QWidget()
        self.widget_26.setStyleSheet("background-color: #FFFFFF; border-radius: 20px;")
        
        widget_layout = QtWidgets.QVBoxLayout(self.widget_26)
        widget_layout.setContentsMargins(20, 20, 20, 20)
        widget_layout.setSpacing(15)
        
        # Controls row
        controls_widget = QtWidgets.QWidget()
        controls_layout = QtWidgets.QHBoxLayout(controls_widget)
        controls_layout.setContentsMargins(0, 0, 0, 0)
        
        self.label_93 = QtWidgets.QLabel("Set Available Slots")
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_93.setFont(font)
        
        controls_layout.addWidget(self.label_93)
        controls_layout.addStretch(1)
        
        self.cancelButton = QtWidgets.QPushButton("Cancel")
        self.cancelButton.setFixedSize(80, 35)
        self.cancelButton.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 6px;
                font: 600 10pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        
        self.createButton = QtWidgets.QPushButton("Create")
        self.createButton.setFixedSize(80, 35)
        self.createButton.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 6px;
                font: 600 10pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #0a5a2f;
            }
        """)
        
        self.comboBox_3 = QtWidgets.QComboBox()
        self.comboBox_3.setFixedSize(200, 35)
        self.comboBox_3.setStyleSheet("""
            QComboBox {
                border: 2px solid #064420;
                border-radius: 6px;
                padding: 4px 8px;
                font: 10pt 'Poppins';
                color: #064420;
                background: white;
            }
        """)
        self.comboBox_3.addItems([
            "1st Semester 2025 - 2026",
            "2nd Semester 2025 - 2026",
            "Summer 2026"
        ])
        
        controls_layout.addWidget(self.cancelButton)
        controls_layout.addWidget(self.createButton)
        controls_layout.addWidget(self.comboBox_3)
        
        widget_layout.addWidget(controls_widget)
        
        # Now use the weekly grid with plus buttons
        self._setupEditWeeklyGrid(widget_layout)
        
        edit_layout.addWidget(self.widget_26, 1)


    def _setupDraggableScheduleArea(self, parent_layout):
        """Setup a draggable schedule area similar to Google Calendar"""
        # Main container for draggable schedule
        schedule_container = QtWidgets.QWidget()
        schedule_layout = QtWidgets.QVBoxLayout(schedule_container)
        schedule_layout.setContentsMargins(0, 0, 0, 0)
        schedule_layout.setSpacing(0)
        
        # Day headers
        day_headers = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        headers_widget = QtWidgets.QWidget()
        headers_layout = QtWidgets.QHBoxLayout(headers_widget)
        headers_layout.setContentsMargins(50, 0, 0, 0)  # Offset for time column
        headers_layout.setSpacing(1)
        
        for day in day_headers:
            day_label = QtWidgets.QLabel(day)
            day_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            day_label.setFixedHeight(40)
            day_label.setStyleSheet("""
                QLabel {
                    background-color: #f8f9fa;
                    color: #666666;
                    font: 600 11pt 'Poppins';
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    margin: 1px;
                }
            """)
            day_label.setMinimumWidth(120)
            headers_layout.addWidget(day_label)
        
        schedule_layout.addWidget(headers_widget)
        
        # Scroll area for the schedule
        self.schedule_scroll = QtWidgets.QScrollArea()
        self.schedule_scroll.setWidgetResizable(True)
        self.schedule_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.schedule_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.schedule_scroll.setStyleSheet("QScrollArea { border: none; background: white; }")
        
        # Schedule widget
        self.schedule_widget = QtWidgets.QWidget()
        self.schedule_widget.setObjectName("schedule_widget")
        self.schedule_layout = QtWidgets.QHBoxLayout(self.schedule_widget)
        self.schedule_layout.setContentsMargins(0, 0, 0, 0)
        self.schedule_layout.setSpacing(1)
        
        # Time column
        time_column = QtWidgets.QWidget()
        time_column.setFixedWidth(50)
        time_layout = QtWidgets.QVBoxLayout(time_column)
        time_layout.setContentsMargins(0, 0, 0, 0)
        time_layout.setSpacing(0)
        
        # Create time labels (7 AM to 10 PM)
        for hour in range(7, 23):
            for minute in [0, 30]:
                time_str = f"{hour}:{minute:02d}"
                period = "AM" if hour < 12 else "PM"
                display_hour = hour if hour <= 12 else hour - 12
                time_label = QtWidgets.QLabel(f"{display_hour}:{minute:02d} {period}")
                time_label.setFixedHeight(60)
                time_label.setStyleSheet("""
                    QLabel {
                        color: #666666;
                        font: 9pt 'Poppins';
                        background: transparent;
                        padding: 2px;
                        border-right: 1px solid #e0e0e0;
                    }
                """)
                time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTop)
                time_layout.addWidget(time_label)
        
        self.schedule_layout.addWidget(time_column)
        
        # Days container
        self.days_container = QtWidgets.QWidget()
        self.days_layout = QtWidgets.QHBoxLayout(self.days_container)
        self.days_layout.setContentsMargins(0, 0, 0, 0)
        self.days_layout.setSpacing(1)
        
        # Create day columns
        self.day_columns = []
        for i in range(7):
            day_column = DraggableDayColumn(i, day_headers[i])
            day_column.timeBlockCreated.connect(self._onTimeBlockCreated)
            day_column.timeBlockMoved.connect(self._onTimeBlockMoved)
            day_column.timeBlockDeleted.connect(self._onTimeBlockDeleted)
            self.days_layout.addWidget(day_column)
            self.day_columns.append(day_column)
        
        self.schedule_layout.addWidget(self.days_container, 1)
        
        self.schedule_scroll.setWidget(self.schedule_widget)
        schedule_layout.addWidget(self.schedule_scroll, 1)
        
        parent_layout.addWidget(schedule_container, 1)

    def _showCreateTimeBlockDialog(self):
        """Show dialog to create a new draggable time block"""
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Create New Time Block")
        dialog.setModal(True)
        dialog.setFixedSize(400, 500)
        dialog.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 10px;
            }
        """)
        
        layout = QtWidgets.QVBoxLayout(dialog)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(20)
        
        title_label = QtWidgets.QLabel("Create New Time Block")
        title_label.setStyleSheet("""
            QLabel {
                color: #084924;
                font: 600 16pt 'Poppins';
            }
        """)
        layout.addWidget(title_label)
        
        # Form layout
        form_layout = QtWidgets.QFormLayout()
        form_layout.setVerticalSpacing(15)
        form_layout.setHorizontalSpacing(20)
        
        # Day selection
        day_label = QtWidgets.QLabel("Day:")
        day_label.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #333; }")
        day_combo = QtWidgets.QComboBox()
        day_combo.addItems(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        day_combo.setStyleSheet("""
            QComboBox {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px;
                font: 10pt 'Poppins';
                background: white;
            }
        """)
        form_layout.addRow(day_label, day_combo)
        
        # Start time
        start_label = QtWidgets.QLabel("Start Time:")
        start_label.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #333; }")
        start_time = QtWidgets.QTimeEdit()
        start_time.setTime(QtCore.QTime(9, 0))
        start_time.setStyleSheet("""
            QTimeEdit {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px;
                font: 10pt 'Poppins';
                background: white;
            }
        """)
        form_layout.addRow(start_label, start_time)
        
        # End time
        end_label = QtWidgets.QLabel("End Time:")
        end_label.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #333; }")
        end_time = QtWidgets.QTimeEdit()
        end_time.setTime(QtCore.QTime(10, 0))
        end_time.setStyleSheet("""
            QTimeEdit {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px;
                font: 10pt 'Poppins';
                background: white;
            }
        """)
        form_layout.addRow(end_label, end_time)
        
        # Title
        title_label = QtWidgets.QLabel("Title:")
        title_label.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #333; }")
        title_edit = QtWidgets.QLineEdit()
        title_edit.setPlaceholderText("Office Hours, Consultation, etc.")
        title_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px;
                font: 10pt 'Poppins';
                background: white;
            }
        """)
        form_layout.addRow(title_label, title_edit)
        
        layout.addLayout(form_layout)
        layout.addStretch(1)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        
        cancel_btn = QtWidgets.QPushButton("Cancel")
        cancel_btn.setFixedHeight(40)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 6px;
                font: 600 11pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        cancel_btn.clicked.connect(dialog.reject)
        
        create_btn = QtWidgets.QPushButton("Create Block")
        create_btn.setFixedHeight(40)
        create_btn.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 6px;
                font: 600 11pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #0a5a2f;
            }
        """)
        
        def createTimeBlock():
            day_index = day_combo.currentIndex()
            start = start_time.time()
            end = end_time.time()
            title = title_edit.text().strip() or "Available"
            
            # Create the time block
            self.day_columns[day_index].createTimeBlock(start, end, title)
            dialog.accept()
            self._showScheduleUpdatedDialog()
        
        create_btn.clicked.connect(createTimeBlock)
        
        button_layout.addWidget(cancel_btn)
        button_layout.addStretch(1)
        button_layout.addWidget(create_btn)
        
        layout.addLayout(button_layout)
        
        dialog.exec()

    def _onTimeBlockCreated(self, day_index, start_time, end_time, title):
        """Handle when a new time block is created"""
        print(f"Time block created: Day {day_index}, {start_time.toString('h:mm AP')} - {end_time.toString('h:mm AP')}, {title}")

    def _onTimeBlockMoved(self, day_index, old_start, new_start, new_end, title):
        """Handle when a time block is moved"""
        print(f"Time block moved: Day {day_index}, {old_start.toString('h:mm AP')} -> {new_start.toString('h:mm AP')} - {new_end.toString('h:mm AP')}, {title}")

    def _onTimeBlockDeleted(self, day_index, start_time, title):
        """Handle when a time block is deleted"""
        print(f"Time block deleted: Day {day_index}, {start_time.toString('h:mm AP')}, {title}")

    

    def _setupEditWeeklyGrid(self, parent_layout):
        # Weekly grid container
        grid_container = QtWidgets.QWidget()
        grid_container.setObjectName("grid_container")
        
        grid_layout = QtWidgets.QVBoxLayout(grid_container)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)
        
        # Weekly grid table
        self.weeklyGridEdit = QtWidgets.QTableWidget()
        self.weeklyGridEdit.setColumnCount(8)  # Time + Mon..Sun
        self.weeklyGridEdit.setRowCount(24)    # 24 hours from 7:00 AM to 6:30 AM next day
        self.weeklyGridEdit.setShowGrid(False)
        self.weeklyGridEdit.verticalHeader().setVisible(False)
        self.weeklyGridEdit.horizontalHeader().setVisible(True)
        self.weeklyGridEdit.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.weeklyGridEdit.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.weeklyGridEdit.setStyleSheet(
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
            self.weeklyGridEdit.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(h))
        
        self.weeklyGridEdit.setColumnWidth(0, 100)
        header = self.weeklyGridEdit.horizontalHeader()
        try:
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Fixed)
            for c in range(1, 8):
                header.setSectionResizeMode(c, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception:
            pass
        
        # Time labels (30-minute intervals from 7:00 AM to 6:30 AM next day)
        times = []
        for hour in range(7, 31):  # 7 AM to 6 AM next day (24 hours)
            actual_hour = hour % 24
            period = "AM" if actual_hour < 12 else "PM"
            display_hour = actual_hour if actual_hour <= 12 else actual_hour - 12
            times.append(f"{display_hour}:00 {period}")
            times.append(f"{display_hour}:30 {period}")
            
        # Only show first 24 rows (7:00 AM to 6:30 AM next day)
        times = times[:24]
        
        for r, t in enumerate(times):
            item = QtWidgets.QTableWidgetItem(t)
            item.setForeground(QtGui.QBrush(QtGui.QColor("#6b6b6b")))
            self.weeklyGridEdit.setItem(r, 0, item)

                
            
            # Add plus buttons to all time slots
            for c in range(1, 8):
                self._addPlusCell(r, c)
                if c != 0:
                    self.weeklyGridEdit.setRowHeight(r, 100)
        
        grid_layout.addWidget(self.weeklyGridEdit, 1)
        parent_layout.addWidget(grid_container, 1)

    def _addPlusCell(self, row, col):
        """Add a clickable plus button cell to the schedule grid"""
        container = QtWidgets.QWidget()
        container.setStyleSheet("QWidget { border: 1px dashed #cfd8dc; border-radius: 4px; background: transparent; }")
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(0)
        
        # Create clickable plus button
        plus_btn = QtWidgets.QPushButton("+")
        plus_btn.setFixedSize(24, 24)
        plus_btn.setStyleSheet("""
            QPushButton {
                background-color: #e8f5e8;
                color: #084924;
                border: 1px solid #084924;
                border-radius: 12px;
                font: bold 12pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #d4edda;
                border: 2px solid #084924;
            }
            QPushButton:pressed {
                background-color: #c8e6c9;
            }
        """)
        
        # Connect click event to show make available dialog
        plus_btn.clicked.connect(lambda checked, r=row, c=col: self._showMakeAvailableDialog(r, c))
        
        layout.addWidget(plus_btn, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.weeklyGridEdit.setCellWidget(row, col, container)

    def _showMakeAvailableDialog(self, row, col):
        """Show dialog to make a time slot available"""
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Make Time Slot Available")
        dialog.setModal(True)
        dialog.setFixedSize(400, 200)
        dialog.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 10px;
            }
        """)
        
        # Main layout
        layout = QtWidgets.QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Get time information
        time_item = self.weeklyGridEdit.item(row, 0)
        time_text = time_item.text() if time_item else "Unknown Time"
        
        day_header = self.weeklyGridEdit.horizontalHeaderItem(col)
        day_text = day_header.text() if day_header else "Unknown Day"
        
        # Title
        title_label = QtWidgets.QLabel(f"Make this slot available")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: #2b2b2b;
                font: 600 14pt 'Poppins';
            }
        """)
        layout.addWidget(title_label)
        
        # Time slot info
        time_info = QtWidgets.QLabel(f"{day_text}  {time_text}")
        time_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        time_info.setStyleSheet("""
            QLabel {
                color: #6b6b6b;
                font: 11pt 'Poppins';
                background-color: #f8f9fa;
                padding: 8px;
                border-radius: 6px;
            }
        """)
        layout.addWidget(time_info)
        
        layout.addStretch(1)
        
        # Buttons row
        button_layout = QtWidgets.QHBoxLayout()
        
        cancel_btn = QtWidgets.QPushButton("Cancel")
        cancel_btn.setFixedHeight(35)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 6px;
                font: 600 11pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        cancel_btn.clicked.connect(dialog.reject)
        
        make_available_btn = QtWidgets.QPushButton("Make Available")
        make_available_btn.setFixedHeight(35)
        make_available_btn.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 6px;
                font: 600 11pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #0a5a2f;
            }
        """)
        make_available_btn.clicked.connect(dialog.accept)
        
        button_layout.addWidget(cancel_btn)
        button_layout.addStretch(1)
        button_layout.addWidget(make_available_btn)
        
        layout.addLayout(button_layout)
        
        # Show dialog and handle result
        result = dialog.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted:
            self._convertToAvailableSlot(row, col, time_text, day_text)

    def _convertToAvailableSlot(self, row, col, time_text, day_text):
        """Convert the plus button cell to an available time slot"""
        container = QtWidgets.QWidget()
        container.setStyleSheet("QWidget { background: transparent; }")
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(0)
        
        # Create available slot indicator
        slot_widget = QtWidgets.QWidget()
        slot_widget.setStyleSheet("""
            QWidget {
                background: #ffc000;
                border-radius: 6px;
                border: 1px solid #e6ac00;
            }
        """)
        slot_widget.setMinimumHeight(36)
        
        slot_layout = QtWidgets.QVBoxLayout(slot_widget)
        slot_layout.setContentsMargins(8, 4, 8, 4)
        slot_layout.setSpacing(2)
        
        # Time label
        time_label = QtWidgets.QLabel(time_text)
        time_label.setStyleSheet("""
            QLabel {
                color: #2b2b2b;
                font: 600 9pt 'Poppins';
                background: transparent;
            }
        """)
        time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        # Status label
        status_label = QtWidgets.QLabel("Available")
        status_label.setStyleSheet("""
            QLabel {
                color: #2b2b2b;
                font: 8pt 'Poppins';
                background: transparent;
            }
        """)
        status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        slot_layout.addWidget(time_label)
        slot_layout.addWidget(status_label)
        
        layout.addWidget(slot_widget)
        self.weeklyGridEdit.setCellWidget(row, col, container)
        
        # Show success message
        self._showScheduleUpdatedDialog()

    def _showScheduleUpdatedDialog(self):
        """Show a success dialog when schedule is updated"""
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Success")
        dialog.setModal(True)
        dialog.setFixedSize(300, 150)
        dialog.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 10px;
            }
        """)
        
        # Main layout
        layout = QtWidgets.QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Success message
        message_label = QtWidgets.QLabel("Schedule Updated!")
        message_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        message_label.setStyleSheet("""
            QLabel {
                color: #084924;
                font: 600 14pt 'Poppins';
            }
        """)
        layout.addWidget(message_label)
        
        # OK button
        ok_button = QtWidgets.QPushButton("OK")
        ok_button.setFixedHeight(40)
        ok_button.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 8px;
                font: 600 12pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #0a5a2f;
            }
        """)
        ok_button.clicked.connect(dialog.accept)
        layout.addWidget(ok_button)
        
        # Show the dialog
        dialog.exec()
    
class DraggableDayColumn(QtWidgets.QWidget):
    """A column representing one day with draggable time blocks"""
    
    timeBlockCreated = QtCore.pyqtSignal(int, QtCore.QTime, QtCore.QTime, str)
    timeBlockMoved = QtCore.pyqtSignal(int, QtCore.QTime, QtCore.QTime, QtCore.QTime, str)
    timeBlockDeleted = QtCore.pyqtSignal(int, QtCore.QTime, str)
    
    def __init__(self, day_index, day_name):
        super().__init__()
        self.day_index = day_index
        self.day_name = day_name
        self.dragged_block = None
        self.drag_start_pos = None
        self.time_blocks = []  # Track created time blocks
        self.setAcceptDrops(True)
        self._setupUI()
    
    def _setupUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Day column background (time slots)
        self.setFixedWidth(120)
        self.setStyleSheet("""
            DraggableDayColumn {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
            }
        """)
        
        # Create time slot areas (7 AM to 10 PM)
        self.time_slots = []
        for hour in range(7, 23):
            for minute in [0, 30]:
                time_slot = TimeSlotArea(hour, minute)
                time_slot.setFixedHeight(60)
                layout.addWidget(time_slot)
                self.time_slots.append(time_slot)
    
    def createTimeBlock(self, start_time, end_time, title):
        """Create a new draggable time block"""
        block = DraggableTimeBlock(start_time, end_time, title, self.day_index)
        block.setParent(self)
        block.show()
        
        # Position the block
        self._positionTimeBlock(block)
        
        # Connect signals
        block.timeBlockMoved.connect(self._onTimeBlockMoved)
        block.timeBlockDeleted.connect(self._onTimeBlockDeleted)
        
        # Add to tracking list
        self.time_blocks.append(block)
        
        self.timeBlockCreated.emit(self.day_index, start_time, end_time, title)
    
    def _positionTimeBlock(self, block):
        """Position a time block based on its start and end times"""
        start_minutes = block.start_time.hour() * 60 + block.start_time.minute()
        end_minutes = block.end_time.hour() * 60 + block.end_time.minute()
        
        # Calculate position (7 AM = 0 position)
        start_pos = (start_minutes - 7*60) / 30 * 60  # 60px per 30 minutes
        height = (end_minutes - start_minutes) / 30 * 60
        
        block.setGeometry(2, start_pos, self.width() - 4, max(height, 30))  # Minimum height of 30px
    
    def _onTimeBlockMoved(self, block, old_start, new_start, new_end):
        """Handle when a time block is moved within this column"""
        # Update the block's time
        block.start_time = new_start
        block.end_time = new_end
        
        # Reposition the block
        self._positionTimeBlock(block)
        self.timeBlockMoved.emit(self.day_index, old_start, new_start, new_end, block.title)
    
    def _onTimeBlockDeleted(self, block):
        """Handle when a time block is deleted"""
        # Remove from tracking list
        if block in self.time_blocks:
            self.time_blocks.remove(block)
        
        self.timeBlockDeleted.emit(self.day_index, block.start_time, block.title)
        block.deleteLater()

class TimeSlotArea(QtWidgets.QWidget):
    """Individual time slot area that can accept draggable blocks"""
    
    def __init__(self, hour, minute):
        super().__init__()
        self.hour = hour
        self.minute = minute
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-timeblock"):
            event.acceptProposedAction()
    
    def dropEvent(self, event):
        if event.mimeData().hasFormat("application/x-timeblock"):
            # Handle drop to move time block to this position
            event.acceptProposedAction()

class DraggableTimeBlock(QtWidgets.QWidget):
    """A draggable time block that can be moved within and between days"""
    
    timeBlockMoved = QtCore.pyqtSignal(object, QtCore.QTime, QtCore.QTime, QtCore.QTime)
    timeBlockDeleted = QtCore.pyqtSignal(object)
    
    def __init__(self, start_time, end_time, title, day_index):
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.title = title
        self.day_index = day_index
        self.old_start_time = start_time
        self.drag_start_pos = None
        
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self._setupUI()
    
    def _setupUI(self):
        # Calculate duration for display
        duration_minutes = (self.end_time.hour() * 60 + self.end_time.minute() - 
                        (self.start_time.hour() * 60 + self.start_time.minute()))
        
        self.setStyleSheet(f"""
            DraggableTimeBlock {{
                background-color: #ffc000;
                border: 1px solid #e6ac00;
                border-radius: 6px;
                padding: 4px;
            }}
        """)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(4, 2, 4, 2)
        layout.setSpacing(2)
        
        # Time label
        time_label = QtWidgets.QLabel(
            f"{self.start_time.toString('h:mm AP')} - {self.end_time.toString('h:mm AP')}"
        )
        time_label.setStyleSheet("""
            QLabel {
                color: #2b2b2b;
                font: 600 8pt 'Poppins';
                background: transparent;
            }
        """)
        time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        # Title label
        title_label = QtWidgets.QLabel(self.title)
        title_label.setStyleSheet("""
            QLabel {
                color: #2b2b2b;
                font: 9pt 'Poppins';
                background: transparent;
            }
        """)
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setWordWrap(True)
        
        layout.addWidget(time_label)
        layout.addWidget(title_label)
        
        # Add context menu for deletion
        self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._showContextMenu)
    
    def _showContextMenu(self, position):
        """Show context menu for the time block"""
        menu = QtWidgets.QMenu(self)
        
        delete_action = QtGui.QAction("Delete Time Block", self)
        delete_action.triggered.connect(self._deleteTimeBlock)
        menu.addAction(delete_action)
        
        menu.exec(self.mapToGlobal(position))
    
    def _deleteTimeBlock(self):
        """Delete this time block"""
        self.timeBlockDeleted.emit(self)
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.drag_start_pos = event.pos()
            self.old_start_time = self.start_time
    
    def mouseMoveEvent(self, event):
        if not (event.buttons() & QtCore.Qt.MouseButton.LeftButton) or not self.drag_start_pos:
            return
        
        # Start drag operation
        drag = QtGui.QDrag(self)
        mime_data = QtCore.QMimeData()
        mime_data.setData("application/x-timeblock", f"{self.day_index}".encode())
        drag.setMimeData(mime_data)
        
        # Create drag pixmap
        pixmap = self.grab()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        
        drag.exec(QtCore.Qt.DropAction.MoveAction)
    
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.drag_start_pos = None
            
            # If position changed, emit moved signal
            if self.start_time != self.old_start_time:
                self.timeBlockMoved.emit(self, self.old_start_time, self.start_time, self.end_time)
