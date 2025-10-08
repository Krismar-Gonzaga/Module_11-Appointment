from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QFormLayout, QCheckBox, QLineEdit, QPushButton
from .appointment_crud import appointment_crud
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class FacultyReschedulePage_ui(QWidget):
    back = QtCore.pyqtSignal()

    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self.crud = appointment_crud()
        self.faculty_id = self._get_faculty_id()
        self.selected_appointment_id = None  # To be set externally
        self._setupFacultyReschedulePage()
        self.retranslateUi()
        self._load_appointment_details()
        self.setFixedSize(1000, 550)

    def _get_faculty_id(self):
        faculty_list = self.crud.list_faculty()
        logging.debug(f"Faculty list: {faculty_list}")
        for faculty in faculty_list:
            if faculty["email"] == self.username:
                logging.debug(f"Found faculty: {faculty['name']} with ID: {faculty['id']}")
                return faculty["id"]
        logging.warning(f"No faculty found for username: {self.username}, using fallback ID: 1")
        return 1

    def _load_appointment_details(self):
        """Load and display details of the selected appointment."""
        if not self.selected_appointment_id:
            logging.warning("No selected appointment ID")
            return
        appointments = self.crud.get_faculty_appointments(self.faculty_id)
        appointment = next((a for a in appointments if a["id"] == self.selected_appointment_id), None)
        if appointment:
            logging.debug(f"Loaded appointment: {appointment}")
            # Update UI with appointment details if needed (e.g., display in a label)
            self.subtitle.setText(f"Reschedule Appointment - {appointment.get('appointment_date', 'N/A')}")

    def _setupFacultyReschedulePage(self):
        self.setObjectName("facultyreschedule")
        reschedule_layout = QtWidgets.QVBoxLayout(self)
        reschedule_layout.setContentsMargins(10, 10, 10, 10)
        reschedule_layout.setSpacing(10)

        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(30, 0, 30, 0)

        self.FacultyListPage = QtWidgets.QLabel()
        font = QtGui.QFont("Poppins", 24)
        self.FacultyListPage.setFont(font)
        self.FacultyListPage.setStyleSheet("QLabel { color: #084924; }")
        header_layout.addWidget(self.FacultyListPage)
        header_layout.addStretch(1)

        self.backButton = QtWidgets.QPushButton()
        self.backButton.setFixedSize(40, 40)
        self.backButton.setStyleSheet("border: none; background: transparent;")
        self.backButton.setIcon(QtGui.QIcon(":/assets/back_button.png"))
        self.backButton.setIconSize(QtCore.QSize(40, 40))
        self.backButton.clicked.connect(self.back.emit)
        header_layout.addWidget(self.backButton)

        reschedule_layout.addWidget(header_widget)

        self.widget_3 = QtWidgets.QWidget()
        self.widget_3.setStyleSheet("QWidget#widget_3 { background-color: #FFFFFF; border-radius: 20px; }")
        widget_layout = QtWidgets.QVBoxLayout(self.widget_3)
        widget_layout.setContentsMargins(10, 0, 10, 0)
        widget_layout.setSpacing(5)

        self.nameheader = QtWidgets.QFrame()
        self.nameheader.setStyleSheet("QFrame#nameheader { background: #ffffff; border-radius: 12px; }")
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 3)
        shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.nameheader.setGraphicsEffect(shadow)
        nameheader_layout = QtWidgets.QHBoxLayout(self.nameheader)
        nameheader_layout.setContentsMargins(20, 0, 20, 0)
        nameheader_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.label_32 = QtWidgets.QLabel()
        self.label_32.setFixedSize(50, 50)
        self.label_32.setStyleSheet("QLabel { background: #4285F4; border-radius: 25px; border: 2px solid white; }")
        self.label_29 = QtWidgets.QLabel("Shapi Dot Com")
        font = QtGui.QFont("Poppins", 18, QtGui.QFont.Weight.Bold)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: #084924;")
        nameheader_layout.addWidget(self.label_32)
        nameheader_layout.addWidget(self.label_29, 1)

        center_layout = QtWidgets.QHBoxLayout()
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
        self.label_30 = QtWidgets.QLabel()
        font = QtGui.QFont("Poppins", 16, QtGui.QFont.Weight.Bold)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel { color: #084924; }")
        calendar_header_layout.addWidget(self.label_30)
        calendar_header_layout.addStretch(1)
        left_layout.addWidget(calendar_header)

        month_header = QtWidgets.QLabel()
        font = QtGui.QFont("Poppins", 14, QtGui.QFont.Weight.Bold)
        month_header.setFont(font)
        month_header.setStyleSheet("QLabel { color: #084924; }")
        month_header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        month_header.setText("October 2025")  # Updated to current month
        left_layout.addWidget(month_header)

        days_widget = QtWidgets.QWidget()
        days_layout = QtWidgets.QHBoxLayout(days_widget)
        days_layout.setContentsMargins(0, 0, 0, 0)
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for day in days:
            day_label = QtWidgets.QLabel(day)
            day_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            day_label.setStyleSheet("QLabel { color: #666666; font: 600 10pt 'Poppins'; padding: 8px 0px; }")
            days_layout.addWidget(day_label)
        left_layout.addWidget(days_widget)

        self.calendarCard = QtWidgets.QWidget()
        self.calendarCard.setStyleSheet("QWidget#calendarCard { background: #ffffff; border-radius: 12px; border: 1px solid #e0e0e0; }")
        calendar_layout = QtWidgets.QVBoxLayout(self.calendarCard)
        calendar_layout.setContentsMargins(10, 10, 10, 10)
        self.calendarWidget = QtWidgets.QCalendarWidget()
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader)
        self.calendarWidget.setSelectedDate(QtCore.QDate.currentDate())  # Set to today: 2025-10-08
        self.calendarWidget.setStyleSheet("""
            QCalendarWidget { background: #ffffff; border: none; font: 10pt 'Poppins'; }
            QCalendarWidget QWidget#qt_calendar_navigationbar { background: transparent; border: none; margin: 10px; }
            QCalendarWidget QToolButton { background: transparent; color: #084924; font: bold 12pt 'Poppins'; border: none; padding: 5px; }
            QCalendarWidget QToolButton:hover { color: #0a5a2f; }
            QCalendarWidget QToolButton#qt_calendar_prevmonth { qproperty-icon: url(:/assets/arrow_left.png); icon-size: 16px; }
            QCalendarWidget QToolButton#qt_calendar_nextmonth { qproperty-icon: url(:/assets/arrow_right.png); icon-size: 16px; }
            QCalendarWidget QAbstractItemView:enabled { color: #084924; selection-background-color: #084924; selection-color: white; }
            QCalendarWidget QAbstractItemView:disabled { color: #cccccc; }
        """)
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
        self.availableSlot.setStyleSheet("background: #ffffff; border: 1px solid #e0e0e0; border-radius: 10px;")
        available_layout = QtWidgets.QVBoxLayout(self.availableSlot)
        available_layout.setContentsMargins(0, 0, 0, 0)
        available_layout.setSpacing(10)

        self.slots_layout = QtWidgets.QHBoxLayout()
        self.slots_layout.setSpacing(12)
        self.slot_buttons = []
        available_layout.addLayout(self.slots_layout)

        self.button_4 = QtWidgets.QPushButton("Reschedule")
        self.button_4.setFixedHeight(50)
        self.button_4.setFont(QtGui.QFont("Poppins", 14, QtGui.QFont.Weight.Bold))
        self.button_4.setStyleSheet("""
            QPushButton { background-color: #084924; border-radius: 8px; color: white; font: 600 14pt 'Poppins'; }
            QPushButton:hover { background-color: #0a5a2f; }
        """)
        self.button_4.clicked.connect(self._openRescheduleDialog)
        available_layout.addWidget(self.button_4)

        right_layout.addWidget(self.availableSlot, 1)
        content_layout.addWidget(left_widget, 1)
        content_layout.addWidget(right_widget, 1)
        widget_layout.addWidget(content_widget, 1)
        reschedule_layout.addWidget(self.widget_3, 1)
        self.calendarWidget.selectionChanged.connect(self._updateAvailableSlots)

    def resizeEvent(self, event):
        """Adjust slot buttons and calendar size dynamically."""
        width = self.availableSlot.width()
        num_slots = max(1, len(self.slot_buttons))
        for btn in self.slot_buttons:
            btn.setFixedWidth(int(width / min(num_slots, 3)) - 12)
        self.calendarWidget.setMinimumSize(int(self.widget_3.width() * 0.45), 300)
        super().resizeEvent(event)

    def _updateAvailableSlots(self):
        date = self.calendarWidget.selectedDate()
        for btn in self.slot_buttons:
            btn.deleteLater()
        self.slot_buttons.clear()
        block = self.crud.get_active_block(self.faculty_id)
        if "error" in block:
            logging.warning("No active block found")
            return
        entries = self.crud.get_block_entries(block["id"])
        day_name = date.toString("dddd")
        slots = [e for e in entries if e["day_of_week"] == day_name]
        for slot in slots:
            time_text = f"{slot['start_time']} - {slot['end_time']}"
            btn = QtWidgets.QPushButton(time_text)
            btn.setFixedHeight(45)
            btn.setCheckable(True)
            btn.setStyleSheet(self.slot_style(default=True))
            btn.clicked.connect(lambda checked, b=btn: self.select_slot(b))
            self.slots_layout.addWidget(btn)
            self.slot_buttons.append(btn)
        if self.slot_buttons:
            self.slot_buttons[0].setChecked(True)
            self.slot_buttons[0].setStyleSheet(self.slot_style(selected=True))

    def slot_style(self, default=False, selected=False):
        """Style for slot buttons."""
        if selected:
            return """
            QPushButton { background-color: #084924; color: white; border: 2px solid #084924; border-radius: 8px; padding: 10px 20px; font: 600 11pt 'Poppins'; }
            """
        return """
        QPushButton { background-color: #ffffff; color: #333333; border: 2px solid #084924; border-radius: 8px; padding: 10px 20px; font: 600 11pt 'Poppins'; }
        QPushButton:hover { background-color: #f0f7f3; }
        QPushButton:pressed { background-color: #e0f0e8; }
        """

    def select_slot(self, button):
        """Handle slot button selection."""
        for btn in self.slot_buttons:
            btn.setChecked(False)
            btn.setStyleSheet(self.slot_style(default=True))
        button.setChecked(True)
        button.setStyleSheet(self.slot_style(selected=True))

    def _openRescheduleDialog(self):
        """Open dialog to confirm rescheduling."""
        if not self.selected_appointment_id:
            logging.warning("No selected appointment ID for rescheduling")
            return
        selected_slot = next((btn.text() for btn in self.slot_buttons if btn.isChecked()), None)
        if not selected_slot:
            logging.warning("No slot selected for rescheduling")
            return
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Reschedule Appointment")
        dlg.setModal(True)
        dlg.setMinimumSize(420, 210)
        root = QtWidgets.QVBoxLayout(dlg)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(14)

        title = QtWidgets.QLabel(f"Reschedule to {selected_slot} on {self.calendarWidget.selectedDate().toString('yyyy-MM-dd')}?")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        title.setStyleSheet("QLabel { color: #2b2b2b; font: 600 12pt 'Poppins'; }")
        root.addWidget(title)
        root.addStretch(1)

        btn_row = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_confirm = QtWidgets.QPushButton("Confirm")
        btn_cancel.setStyleSheet("QPushButton { background: #e0e0e0; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: #2b2b2b; }")
        btn_confirm.setStyleSheet("QPushButton { background: #084924; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: white; }")
        btn_cancel.clicked.connect(dlg.reject)
        def _confirm_clicked():
            block = self.crud.get_active_block(self.faculty_id)
            if "error" not in block:
                entries = self.crud.get_block_entries(block["id"])
                day_name = self.calendarWidget.selectedDate().toString("dddd")
                entry = next((e for e in entries if e["day_of_week"] == day_name and f"{e['start_time']} - {e['end_time']}" == selected_slot), None)
                if entry:
                    appointments = self.crud.get_faculty_appointments(self.faculty_id)
                    current_appointment = next((a for a in appointments if a["id"] == self.selected_appointment_id), None)
                    if current_appointment and current_appointment.get("status") in ["pending", "approved"]:
                        self.crud.update_appointment(self.selected_appointment_id, {
                            "appointment_schedule_entry_id": entry["id"],
                            "appointment_date": self.calendarWidget.selectedDate().toString("yyyy-MM-dd"),
                            "status": "rescheduled"
                        })
                        self._showSuccessDialog()
                        dlg.accept()
                    else:
                        logging.warning(f"Cannot reschedule appointment {self.selected_appointment_id}: Invalid status")
        btn_confirm.clicked.connect(_confirm_clicked)
        btn_row.addWidget(btn_cancel)
        btn_row.addStretch(1)
        btn_row.addWidget(btn_confirm)
        root.addLayout(btn_row)
        dlg.exec()

    def _openDenyDialog(self):
        """Open dialog to confirm denying reschedule request."""
        if not self.selected_appointment_id:
            logging.warning("No selected appointment ID for denying")
            return
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Deny Reschedule")
        dlg.setModal(True)
        dlg.setMinimumSize(420, 210)
        root = QtWidgets.QVBoxLayout(dlg)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(14)

        title = QtWidgets.QLabel("Are you sure you want to deny this reschedule request?")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        title.setStyleSheet("QLabel { color: #2b2b2b; font: 600 12pt 'Poppins'; }")
        root.addWidget(title)
        root.addStretch(1)

        btn_row = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_deny = QtWidgets.QPushButton("Deny")
        btn_cancel.setStyleSheet("QPushButton { background: #e0e0e0; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: #2b2b2b; }")
        btn_deny.setStyleSheet("QPushButton { background: #EB5757; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: white; }")
        btn_cancel.clicked.connect(dlg.reject)
        def _confirm_clicked():
            appointments = self.crud.get_faculty_appointments(self.faculty_id)
            current_appointment = next((a for a in appointments if a["id"] == self.selected_appointment_id), None)
            if current_appointment and current_appointment.get("status") in ["pending", "approved"]:
                self.crud.update_appointment(self.selected_appointment_id, {"status": "denied"})
                self._showSuccessDialog(message="Reschedule request denied!")
                dlg.accept()
            else:
                logging.warning(f"Cannot deny appointment {self.selected_appointment_id}: Invalid status")
        btn_deny.clicked.connect(_confirm_clicked)
        btn_row.addWidget(btn_cancel)
        btn_row.addStretch(1)
        btn_row.addWidget(btn_deny)
        root.addLayout(btn_row)
        dlg.exec()

    def _showSuccessDialog(self, message="Appointment rescheduled successfully!"):
        """Show success dialog after rescheduling or denying."""
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Success")
        dialog.setModal(True)
        dialog.setMinimumSize(300, 150)
        dialog.setStyleSheet("QDialog { background-color: white; border-radius: 10px; }")
        layout = QtWidgets.QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        message_label = QtWidgets.QLabel(message)
        message_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        message_label.setStyleSheet("QLabel { color: #084924; font: 600 14pt 'Poppins'; }")
        layout.addWidget(message_label)
        ok_button = QtWidgets.QPushButton("OK")
        ok_button.setFixedHeight(40)
        ok_button.setStyleSheet("""
            QPushButton { background-color: #084924; color: white; border-radius: 8px; font: 600 12pt 'Poppins'; }
            QPushButton:hover { background-color: #0a5a2f; }
        """)
        ok_button.clicked.connect(dialog.accept)
        layout.addWidget(ok_button)
        dialog.exec()

    def retranslateUi(self):
        """Set text for UI elements."""
        self.FacultyListPage.setText("Reschedule Appointment")
        self.label_30.setText("Pick a Date")
        self.label_31.setText("Available Slots")
        self.button_4.setText("Reschedule")