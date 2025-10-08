from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox
from .appointment_crud import appointment_crud
from datetime import datetime

class StudentRequestPage_ui(QWidget):
    back = QtCore.pyqtSignal()
    backrefreshdata = QtCore.pyqtSignal()
    
    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self.Appointment_crud = appointment_crud()
        self.selected_faculty = None
        self.selected_schedule_entry = None
        self.selected_date = None
        self.slot_buttons = []
        self.slots_container = None
        self.available_days = set()  # Store available days for highlighting
        self.setFixedSize(1000, 550)
        self._setupStudentRequestPage()
        self.retranslateUi()

    def set_faculty_data(self, faculty_data):
        """Set the faculty data when navigating from browse page"""
        self.selected_faculty = faculty_data
        self._updateFacultyInfo()
        self._loadAvailableSlots()
        self._updateCalendarHighlighting()  # Update calendar highlighting
        self._onDateSelected()

    def _updateFacultyInfo(self):
        """Update the UI with faculty information"""
        if self.selected_faculty:
            self.label_29.setText(self.selected_faculty["name"])
            self.label_30.setText(f"Select Date & Time with {self.selected_faculty['name']}")
            current_date = datetime.now()
            self.month_header.setText(current_date.strftime("%B %Y"))

    def _loadAvailableSlots(self):
        """Load available time slots for the selected faculty based on their schedule"""
        if not self.selected_faculty:
            return
            
        try:
            # Get active block and entries
            active_block = self.Appointment_crud.get_active_block(self.selected_faculty["id"])
            
            if active_block and "error" not in active_block:
                self.block_entries = self.Appointment_crud.get_block_entries(active_block["id"])
                
                # Extract available days from block entries
                self._extractAvailableDays()
                
        except Exception as e:
            print(f"Error loading available slots: {e}")
            QMessageBox.warning(self, "Error", f"Failed to load available slots: {str(e)}")
            self._showNoSlotsMessage()

    def _extractAvailableDays(self):
        """Extract available days from block entries for calendar highlighting"""
        self.available_days.clear()
        
        if not hasattr(self, 'block_entries') or not self.block_entries:
            return
            
        # Map day names to numbers (Monday=1, Sunday=7)
        day_mapping = {
            "Monday": 1, "Tuesday": 2, "Wednesday": 3, 
            "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7
        }
        
        for entry in self.block_entries:
            day_name = entry.get('day_of_week', '')
            if day_name in day_mapping:
                self.available_days.add(day_mapping[day_name])
        
        print(f"Available days: {self.available_days}")

    def _updateCalendarHighlighting(self):
        """Update calendar to highlight available days"""
        if not self.available_days:
            return
            
        # Create a text char format for available days
        available_format = QtGui.QTextCharFormat()
        available_format.setBackground(QtGui.QBrush(QtGui.QColor("#FFF9C4")))  # Light yellow
        available_format.setForeground(QtGui.QBrush(QtGui.QColor("#000000")))  # Black text
        
        # Apply the format to available days
        for day_number in self.available_days:
            self.calendarWidget.setWeekdayTextFormat(
                QtCore.Qt.DayOfWeek(day_number), 
                available_format
            )

    def _showNoSlotsMessage(self):
        """Show message when no slots are available"""
        no_slots_label = QtWidgets.QLabel("No available time slots\nfor this faculty")
        no_slots_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        no_slots_label.setStyleSheet("""
            QLabel {
                font: 12pt 'Poppins';
                color: #666666;
                background: #f8f9fa;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        no_slots_label.setWordWrap(True)
        
        # Clear existing scroll area
        old_widget = self.availableSlot.layout().itemAt(0)
        if old_widget and old_widget.widget():
            old_widget.widget().deleteLater()
        
        self.availableSlot.layout().insertWidget(0, no_slots_label)
        self.selected_schedule_entry = None
        if hasattr(self, 'button_4') and self.button_4:
            self.button_4.setEnabled(False)

    def _updateCalendarForSelectedDay(self, day_of_week):
        """Update calendar to highlight the selected day"""
        try:
            day_mapping = {
                "Monday": 1, "Tuesday": 2, "Wednesday": 3, 
                "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7
            }
            
            if day_of_week in day_mapping:
                target_day = day_mapping[day_of_week]
                current_date = self.calendarWidget.selectedDate()
                
                days_to_add = (target_day - current_date.dayOfWeek()) % 7
                if days_to_add == 0:
                    days_to_add = 7
                
                new_date = current_date.addDays(days_to_add)
                self.calendarWidget.setSelectedDate(new_date)
                self.selected_date = new_date.toString('yyyy-MM-dd')
                
        except Exception as e:
            print(f"Error updating calendar: {e}")

    def _loadTheEntries(self, day):
        """Load available entries for the selected day"""
        day_entries = []
        unavailble_entry_index = []

        for i in range(len(self.block_entries)):
            entry = self.block_entries[i]
            if entry.get('day_of_week') == day:
                day_entries.append(entry)
        
        for i in range(len(day_entries)):
            date_appointments = self.Appointment_crud.get_appointments_by_entry_and_date(day_entries[i].get('id'), self.selected_date)
            if date_appointments:
                unavailble_entry_index.append(i)
        
        try: 
            for btn in self.slot_buttons:
                btn.deleteLater()
            self.slot_buttons.clear()
                
            # Clear the slots container content
            if hasattr(self, "slots_container") and self.slots_container is not None:
                self.slots_container.deleteLater()
                self.slots_container = None
                self.slots_layout = None

            if day_entries:
                # Ensure slots_container and slots_layout exist
                if not self.slots_container:
                    self.slots_container = QtWidgets.QWidget()
                    self.slots_layout = QtWidgets.QVBoxLayout(self.slots_container)
                    self.slots_layout.setContentsMargins(5, 5, 5, 5)
                    self.slots_layout.setSpacing(8)
                        
                    slots_scroll = QtWidgets.QScrollArea()
                    slots_scroll.setWidgetResizable(True)
                    slots_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
                    slots_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                    slots_scroll.setStyleSheet("""
                            QScrollArea {
                                border: none;
                                background: transparent;
                            }
                            QScrollBar:vertical {
                                background: #f0f0f0;
                                width: 8px;
                                margin: 0px;
                                border-radius: 4px;
                            }
                            QScrollBar::handle:vertical {
                                background: #c0c0c0;
                                border-radius: 4px;
                                min-height: 20px;
                            }
                        """)
                    slots_scroll.setWidget(self.slots_container)
                        
                    # Replace old scroll area with new one
                    old_widget = self.availableSlot.layout().itemAt(0)
                    if old_widget and old_widget.widget():
                        old_widget.widget().deleteLater()
                    self.availableSlot.layout().insertWidget(0, slots_scroll)
                    
                # Populate slot buttons
                for i in range(len(day_entries)):
                    entry = day_entries[i]
                    start_time = entry.get('start_time', '')
                    end_time = entry.get('end_time', '')
                        
                    slot_text = f"{start_time} - {end_time}"
                    
                    self.button_4.setEnabled(False)
                    btn = QtWidgets.QPushButton(slot_text)
                    btn.setFixedHeight(45)
                    btn.setCheckable(True)
                    btn.setProperty("schedule_entry_id", entry["id"])
                    btn.setProperty("start_time", start_time)
                    btn.setProperty("end_time", end_time)
                    btn.setStyleSheet(self.slot_style(default=True))
                    btn.clicked.connect(lambda checked, b=btn, e=entry: self.select_slot(b, e))
                    
                    if (i in unavailble_entry_index):      
                        print("U")
                        btn.setEnabled(False)
                    
                    self.slots_layout.addWidget(btn)
                    self.slot_buttons.append(btn)
                    
                self.slots_layout.addStretch(1)
                    
                if self.slot_buttons:
                    self.slot_buttons[0].setChecked(True)
                    self.slot_buttons[0].setStyleSheet(self.slot_style(selected=True))
                    self.selected_schedule_entry = day_entries[0]
                else:
                    self.selected_schedule_entry = None
                    self._showNoSlotsMessage()
            else:
                self._showNoSlotsMessage()
                
        except Exception as e:
            print(f"Error loading available slots: {e}")
            QMessageBox.warning(self, "Error", f"Failed to load available slots: {str(e)}")
            self._showNoSlotsMessage()

    def _setupStudentRequestPage(self):
        self.setObjectName("facultyreschedule")
        
        reschedule_layout = QtWidgets.QVBoxLayout(self)
        reschedule_layout.setContentsMargins(0, 0, 0, 0)
        reschedule_layout.setSpacing(10)
        
        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(30, 0, 30, 0)
        
        self.FacultyListPage = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        self.FacultyListPage.setFont(font)
        self.FacultyListPage.setStyleSheet("QLabel { color: #084924; }")
        self.FacultyListPage.setObjectName("FacultyListPage")
        
        header_layout.addWidget(self.FacultyListPage)
        header_layout.addStretch(1)

        self.backbutton = QtWidgets.QPushButton("<- Back")
        self.backbutton.clicked.connect(self._handleBackButton)
        header_layout.addWidget(self.backbutton)
        
        self.backButton = QtWidgets.QLabel()
        self.backButton.setFixedSize(40, 40)
        self.backButton.setText("")
        self.backButton.setPixmap(QtGui.QPixmap(":/assets/back_button.png"))
        self.backButton.setScaledContents(True)
        self.backButton.setObjectName("backButton")
        
        header_layout.addWidget(self.backButton)
        
        reschedule_layout.addWidget(header_widget)
        
        self.widget_3 = QtWidgets.QWidget()
        self.widget_3.setStyleSheet("QWidget#widget_3 { background-color: #FFFFFF; border-radius: 20px; }")
        self.widget_3.setObjectName("widget_3")
        
        widget_layout = QtWidgets.QVBoxLayout(self.widget_3)
        widget_layout.setContentsMargins(10, 0, 10, 0)
        widget_layout.setSpacing(5)
        
        self.nameheader = QtWidgets.QFrame()
        self.nameheader.setContentsMargins(30, 0, 30, 0)
        self.nameheader.setStyleSheet("""
            QFrame#nameheader {
                background: #ffffff;
                border-radius: 12px;
            }
        """)
        self.nameheader.setObjectName("nameheader")
        self.nameheader.setFixedHeight(80)
        
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 3)
        shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.nameheader.setGraphicsEffect(shadow)

        nameheader_layout = QtWidgets.QHBoxLayout(self.nameheader)
        nameheader_layout.setContentsMargins(20, 0, 20, 0)
        nameheader_layout.setSpacing(12)
        nameheader_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.label_32 = QtWidgets.QLabel()
        self.label_32.setFixedSize(50, 50)
        self.label_32.setPixmap(QtGui.QPixmap(":/assets/profile_icon.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setStyleSheet("""
            QLabel {
                background: #4285F4;
                border-radius: 25px;
                border: 2px solid white;
            }
        """)
        
        self.label_29 = QtWidgets.QLabel("Select a Faculty")
        font = QtGui.QFont("Poppins", 18, QtGui.QFont.Weight.Bold)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: #084924;")
        self.label_29.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)

        nameheader_layout.addWidget(self.label_32)
        nameheader_layout.addWidget(self.label_29, 1)

        center_layout = QtWidgets.QHBoxLayout()
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.addStretch()
        center_layout.addWidget(self.nameheader)
        center_layout.addStretch()

        widget_layout.addLayout(center_layout)

        self.subtitle = QtWidgets.QLabel("Select Date & Time")
        subtitle_font = QtGui.QFont("Poppins", 14, QtGui.QFont.Weight.Medium)
        self.subtitle.setFont(subtitle_font)
        self.subtitle.setStyleSheet("color: #084924;")
        self.subtitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        widget_layout.addWidget(self.subtitle)

        content_widget = QtWidgets.QWidget()
        content_layout = QtWidgets.QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(20)
        
        left_widget = QtWidgets.QWidget()
        left_layout = QtWidgets.QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)
        
        calendar_header = QtWidgets.QWidget()
        calendar_header_layout = QtWidgets.QHBoxLayout(calendar_header)
        calendar_header_layout.setContentsMargins(0, 0, 0, 0)
        
        self.label_30 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel#label_30 { color: #084924; }")
        self.label_30.setObjectName("label_30")
        
        calendar_header_layout.addWidget(self.label_30)
        calendar_header_layout.addStretch(1)
        
        left_layout.addWidget(calendar_header)
        
        self.month_header = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.month_header.setFont(font)
        self.month_header.setStyleSheet("QLabel { color: #084924; background: transparent; }")
        self.month_header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.month_header.setText(datetime.now().strftime("%B %Y"))
        left_layout.addWidget(self.month_header)
        
        days_widget = QtWidgets.QWidget()
        days_layout = QtWidgets.QHBoxLayout(days_widget)
        days_layout.setContentsMargins(0, 0, 0, 0)
        days_layout.setSpacing(0)
        
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for day in days:
            day_label = QtWidgets.QLabel(day)
            day_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            day_label.setStyleSheet("""
                QLabel {
                    color: #666666;
                    font: 600 10pt 'Poppins';
                    background: transparent;
                    padding: 8px 0px;
                }
            """)
            days_layout.addWidget(day_label)
        
        left_layout.addWidget(days_widget)

        self.calendarCard = QtWidgets.QWidget()
        self.calendarCard.setStyleSheet("""
            QWidget#calendarCard {
                background: #ffffff;
                border-radius: 12px;
                border: 1px solid #e0e0e0;
            }
        """)
        self.calendarCard.setObjectName("calendarCard")

        calendar_layout = QtWidgets.QVBoxLayout(self.calendarCard)
        calendar_layout.setContentsMargins(10, 10, 10, 10)
        
        self.calendarWidget = QtWidgets.QCalendarWidget()
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader)
        self.calendarWidget.setStyleSheet("""
            QCalendarWidget {
                background: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 10px;
                font: 10pt 'Poppins';
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background: transparent;
                border: none;
                margin: 10px;
            }
            QCalendarWidget QToolButton {
                background: transparent;
                color: #084924;
                font: bold 12pt 'Poppins';
                border: none;
                padding: 5px;
            }
            QCalendarWidget QToolButton:hover {
                color: #0a5a2f;
            }
            QCalendarWidget QToolButton#qt_calendar_prevmonth {
                qproperty-icon: url(:/assets/arrow_left.png);
                icon-size: 16px;
            }
            QCalendarWidget QToolButton#qt_calendar_nextmonth {
                qproperty-icon: url(:/assets/arrow_right.png);
                icon-size: 16px;
            }
            QCalendarWidget QToolButton#qt_calendar_monthbutton,
            QCalendarWidget QToolButton#qt_calendar_yearbutton {
                font: bold 12pt 'Poppins';
                color: #084924;
            }
            QCalendarWidget QTableView {
                selection-background-color: transparent;
                selection-color: black;
            }
            QCalendarWidget QHeaderView::section {
                background: transparent;
                color: #084924;
                font: 600 10pt 'Poppins';
                border: none;
                padding: 6px 0;
            }
            QCalendarWidget QAbstractItemView:enabled {
                color: #084924;
                font: 10pt 'Poppins';
                background: white;
                selection-background-color: #084924;
                selection-color: white;
                border-radius: 20px;
                outline: none;
            }
            QCalendarWidget QAbstractItemView:disabled {
                color: #cccccc;
            }
        """)
        self.calendarWidget.selectionChanged.connect(self._onDateSelected)
        
        calendar_layout.addWidget(self.calendarWidget)
        left_layout.addWidget(self.calendarCard, 1)
        
        right_widget = QtWidgets.QWidget()
        right_layout = QtWidgets.QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(5)

        self.label_31 = QtWidgets.QLabel("Available Slots")
        font = QtGui.QFont("Poppins", 16, QtGui.QFont.Weight.Bold)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: #084924;")
        right_layout.addWidget(self.label_31)

        self.availableSlot = QtWidgets.QFrame()
        self.availableSlot.setStyleSheet("""
            QFrame#availableSlot {
                background: #ffffff; 
                border: 1px solid #e0e0e0; 
                border-radius: 10px;
            }
        """)
        self.availableSlot.setObjectName("availableSlot")
        available_layout = QtWidgets.QVBoxLayout(self.availableSlot)
        available_layout.setContentsMargins(15, 15, 15, 15)
        available_layout.setSpacing(10)

        initial_message = QtWidgets.QLabel("Please select a faculty first")
        initial_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        initial_message.setStyleSheet("""
            QLabel {
                font: 12pt 'Poppins';
                color: #666666;
                background: #f8f9fa;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        available_layout.addWidget(initial_message)

        self.button_4 = QtWidgets.QPushButton("Request Appointment")
        self.button_4.setFixedHeight(50)
        self.button_4.setContentsMargins(0, 20, 0, 0)
        self.button_4.clicked.connect(self._showRequestDialog)
        self.button_4.setFont(QtGui.QFont("Poppins", 14, QtGui.QFont.Weight.Bold))
        self.button_4.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                border-radius: 8px;
                color: white;
                font: 600 14pt 'Poppins';
            }
            QPushButton:hover { background-color: #0a5a2f; }
            QPushButton:pressed { background-color: #06381b; }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        self.button_4.setEnabled(False)
        available_layout.addWidget(self.button_4)

        right_layout.addWidget(self.availableSlot, 1)

        content_layout.addWidget(left_widget, 1)
        content_layout.addWidget(right_widget, 1)

        widget_layout.addWidget(content_widget, 1)
        reschedule_layout.addWidget(self.widget_3, 1)

    def _handleBackButton(self):
        """Handle back button click - emit both signals"""
        print("Back button clicked - emitting signals")
        self.back.emit()  # Signal to go back to previous page
        self.backrefreshdata.emit()  # Signal to refresh data

    def _onDateSelected(self):
        """Handle date selection from calendar"""
        self.selected_date = self.calendarWidget.selectedDate().toString('yyyy-MM-dd')
        selected_day = self.calendarWidget.selectedDate().toString('dddd')
        self._loadTheEntries(selected_day)

    def slot_style(self, default=False, selected=False):
        if selected:
            return """
            QPushButton {
                background-color: #084924;
                color: white;
                border: 2px solid #084924;
                border-radius: 8px;
                padding: 10px 20px;
                font: 600 11pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #0a5a2f;
            }
            QPushButton:disabled {
                background-color: #bfbfbf;
                color: #6f6f6f;
                border: 2px solid #a0a0a0;
            }
            """
        else:
            return """
            QPushButton {
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #084924;
                border-radius: 8px;
                padding: 10px 20px;
                font: 600 11pt 'Poppins';
            }
            QPushButton:hover { 
                background-color: #f0f7f3; 
            }
            QPushButton:pressed { 
                background-color: #e0f0e8; 
            }
            QPushButton:disabled {
                background-color: #bfbfbf;
                color: #6f6f6f;
                border: 2px solid #a0a0a0;
            }
            """

    def select_slot(self, button, schedule_entry):
        """Handle slot selection"""
        for btn in self.slot_buttons:
            btn.setChecked(False)
            btn.setStyleSheet(self.slot_style(default=True))
        button.setChecked(True)
        button.setStyleSheet(self.slot_style(selected=True))
        self.selected_schedule_entry = schedule_entry
        
        if hasattr(self, 'button_4') and self.button_4 and not self.button_4.isHidden():
            self.button_4.setEnabled(True)

    def _showRequestDialog(self):
        """Show request dialog to collect appointment details"""
        if not self.selected_faculty:
            QMessageBox.warning(self, "Warning", "Please select a faculty first.")
            return
            
        if not self.selected_schedule_entry:
            QMessageBox.warning(self, "Warning", "Please select a time slot.")
            return
            
        if not self.selected_date:
            QMessageBox.warning(self, "Warning", "Please select a date.")
            return

        self._showAppointmentDetailsDialog()

    def _showAppointmentDetailsDialog(self):
        """Show dialog with appointment details and purpose form"""
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Appointment Request")
        dialog.setModal(True)
        dialog.setFixedSize(500, 600)
        dialog.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 12px;
            }
        """)
        
        layout = QtWidgets.QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        title_label = QtWidgets.QLabel("Appointment Request Details")
        title_label.setStyleSheet("""
            QLabel {
                color: #084924;
                font: 600 18pt 'Poppins';
            }
        """)
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        summary_group = QtWidgets.QGroupBox("Appointment Summary")
        summary_group.setStyleSheet("""
            QGroupBox {
                font: 600 12pt 'Poppins';
                color: #084924;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 12px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 8px 0 8px;
            }
        """)
        
        summary_layout = QtWidgets.QFormLayout(summary_group)
        summary_layout.setVerticalSpacing(8)
        summary_layout.setHorizontalSpacing(20)
        
        faculty_name = self.selected_faculty["name"]
        day_of_week = self.selected_schedule_entry.get('day_of_week', '')
        start_time = self.selected_schedule_entry.get('start_time', '')
        end_time = self.selected_schedule_entry.get('end_time', '')
        date = self.selected_date
        
        summary_data = [
            ("Faculty:", faculty_name),
            ("Date:", f"{day_of_week}, {date}"),
            ("Time:", f"{start_time} - {end_time}"),
        ]
        
        for label, value in summary_data:
            label_widget = QtWidgets.QLabel(label)
            label_widget.setStyleSheet("QLabel { font: 600 11pt 'Poppins'; color: #333; }")
            value_widget = QtWidgets.QLabel(value)
            value_widget.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #666; }")
            summary_layout.addRow(label_widget, value_widget)
        
        layout.addWidget(summary_group)
        
        reason_group = QtWidgets.QGroupBox("Appointment Purpose")
        reason_group.setStyleSheet("""
            QGroupBox {
                font: 600 12pt 'Poppins';
                color: #084924;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 12px;
            }
        """)
        
        reason_layout = QtWidgets.QVBoxLayout(reason_group)
        
        self.reason_text_edit = QtWidgets.QTextEdit()
        self.reason_text_edit.setPlaceholderText("Please describe the purpose of your appointment...")
        self.reason_text_edit.setFixedHeight(120)
        self.reason_text_edit.setStyleSheet("""
            QTextEdit {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px;
                font: 11pt 'Poppins';
                background-color: #fafafa;
            }
            QTextEdit:focus {
                border: 1px solid #084924;
                background-color: white;
            }
        """)
        reason_layout.addWidget(self.reason_text_edit)
        layout.addWidget(reason_group)
        
        location_group = QtWidgets.QGroupBox("Meeting Location")
        location_group.setStyleSheet("""
            QGroupBox {
                font: 600 12pt 'Poppins';
                color: #084924;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 12px;
            }
        """)
        
        location_layout = QtWidgets.QVBoxLayout(location_group)
        
        self.location_combo = QtWidgets.QComboBox()
        self.location_combo.addItems([
            "Faculty Office",
            "Online Meeting",
            "Classroom",
            "Laboratory",
            "Other (specify in purpose)"
        ])
        self.location_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px;
                font: 11pt 'Poppins';
                background-color: #fafafa;
            }
        """)
        location_layout.addWidget(self.location_combo)
        layout.addWidget(location_group)
        
        layout.addStretch(1)
        
        button_layout = QtWidgets.QHBoxLayout()
        
        cancel_button = QtWidgets.QPushButton("Cancel")
        cancel_button.setFixedSize(120, 40)
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 8px;
                font: 600 12pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        cancel_button.clicked.connect(dialog.reject)
        
        submit_button = QtWidgets.QPushButton("Submit Request")
        submit_button.setFixedSize(140, 40)
        submit_button.setStyleSheet("""
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
        submit_button.clicked.connect(lambda: self._handleSubmitRequest(dialog))
        
        button_layout.addStretch(1)
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(submit_button)
        
        layout.addLayout(button_layout)
        
        dialog.exec()

    def _handleSubmitRequest(self, dialog):
        """Handle the appointment request submission"""
        reason_text = self.reason_text_edit.toPlainText().strip()
        location = self.location_combo.currentText()
        
        if not reason_text:
            QMessageBox.warning(
                dialog,
                "Missing Information",
                "Please enter the purpose of your appointment before submitting."
            )
            return
        
        try:
            student_id = self._get_current_student_id()
            if not student_id:
                QMessageBox.warning(dialog, "Error", "Student profile not found.")
                return
                
            result = self.Appointment_crud.create_appointment(
                student_id=student_id,
                schedule_entry_id=self.selected_schedule_entry["id"],
                details=reason_text,
                address=location,
                date_str=self.selected_date,
                image_path=""
            )
            
            if result:
                dialog.accept()
                self._showSuccessDialog()
            else:
                QMessageBox.warning(dialog, "Error", "Failed to create appointment request.")
                
        except Exception as e:
            print(f"Error creating appointment: {e}")
            QMessageBox.warning(dialog, "Error", f"Failed to create appointment: {str(e)}")

    def _get_current_student_id(self):
        """Get the current student's ID"""
        students = self.Appointment_crud.list_students()
        for student in students:
            if student.get('email') == self.username or student.get('name') == self.username:
                return student.get('id')
        
        try:
            student_id = self.Appointment_crud.create_student(
                name=self.username,
                email=self.username,
                course="Unknown",
                year_level="Unknown"
            )
            return student_id
        except Exception as e:
            print(f"Error creating student: {e}")
            return None

    def _showSuccessDialog(self):
        """Show success dialog"""
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Success")
        dialog.setModal(True)
        dialog.setFixedSize(350, 200)
        dialog.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 10px;
            }
        """)
        
        layout = QtWidgets.QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        icon_label = QtWidgets.QLabel()
        icon_label.setFixedSize(64, 64)
        icon_label.setStyleSheet("""
            QLabel {
                background-color: #4CAF50;
                border-radius: 32px;
                color: white;
                font: bold 24pt 'Poppins';
                qproperty-alignment: AlignCenter;
            }
        """)
        icon_label.setText("✓")
        layout.addWidget(icon_label, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        
        message_label = QtWidgets.QLabel("Appointment Request Submitted!")
        message_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        message_label.setStyleSheet("""
            QLabel {
                color: #084924;
                font: 600 14pt 'Poppins';
            }
        """)
        layout.addWidget(message_label)
        
        info_label = QtWidgets.QLabel("Your request is pending faculty approval.\nYou will be notified once it's processed.")
        info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        info_label.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #666; }")
        info_label.setWordWrap(True)
        layout.addWidget(info_label)
        
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
        ok_button.clicked.connect(lambda: self._handleSuccessDialogClose(dialog))
        
        layout.addWidget(ok_button)
        
        dialog.exec()

    def _handleSuccessDialogClose(self, dialog):
        """Handle success dialog close - emit refresh signal and close"""
        print("Success dialog closed - emitting refresh signal")
        self.backrefreshdata.emit()  # Emit refresh signal
        dialog.accept()
        self.back.emit()  # Also emit back signal to navigate back

    def retranslateUi(self):
        self.label_29.setText("Select a Faculty")
        self.label_30.setText("Select Date & Time")
        self.label_31.setText("Available Slots")
        self.button_4.setText("Request Appointment")
        self.FacultyListPage.setText("Request Appointment")