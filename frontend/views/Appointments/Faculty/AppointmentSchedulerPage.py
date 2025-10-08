from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QDialog, QVBoxLayout, QFormLayout, QPushButton, QDateEdit
from .appointment_crud import appointment_crud
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class AppointmentSchedulerPage_ui(QWidget):
    go_to_EditSchedulePage = QtCore.pyqtSignal()
    back = QtCore.pyqtSignal()

    def convert_time(self, time_str):
        """Convert 24-hour format to 12-hour format with AM/PM."""
        if ":" in time_str:
            hour, minute = map(int, time_str.split(":"))
            period = "AM" if hour < 12 else "PM"
            hour = hour % 12 if hour != 0 else 12
            return f"{hour}:{minute:02d} {period}"
        return time_str

    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self.crud = appointment_crud()
        self.faculty_id = self._get_faculty_id()
        logging.debug(f"Initialized AppointmentSchedulerPage_ui with username: {self.username}, faculty_id: {self.faculty_id}")
        self._setupAppointmentSchedulerPage()
        self.retranslateUi()

    def _get_faculty_id(self):
        faculty_list = self.crud.list_faculty()
        logging.debug(f"Faculty list: {faculty_list}")
        for faculty in faculty_list:
            if faculty["email"] == "Kim":
                logging.debug(f"Found faculty: {faculty['name']} with ID: {faculty['id']}")
                return faculty["id"]
        logging.warning(f"No faculty found for username: Kim, using fallback ID: 1")
        return 1

    def _setupAppointmentSchedulerPage(self):
        self.setObjectName("AppointmentScheduler")
        scheduler_layout = QtWidgets.QVBoxLayout(self)
        scheduler_layout.setContentsMargins(10, 10, 10, 10)
        scheduler_layout.setSpacing(10)

        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(10)

        self.Academics_5 = QtWidgets.QLabel()
        font = QtGui.QFont("Poppins", 24)
        self.Academics_5.setFont(font)
        self.Academics_5.setStyleSheet("QLabel { color: #084924; }")
        header_layout.addWidget(self.Academics_5)
        header_layout.addStretch(1)

        self.backButton_7 = QtWidgets.QPushButton()
        self.backButton_7.setFixedSize(40, 40)
        self.backButton_7.setStyleSheet("border: none; background: transparent;")
        self.backButton_7.setIcon(QtGui.QIcon(":/assets/back_button.png"))
        self.backButton_7.setIconSize(QtCore.QSize(40, 40))
        self.backButton_7.clicked.connect(self.back.emit)
        header_layout.addWidget(self.backButton_7)

        scheduler_layout.addWidget(header_widget)

        self.widget_25 = QtWidgets.QWidget()
        self.widget_25.setStyleSheet("QWidget#widget_25 { background-color: #FFFFFF; border-radius: 20px; }")
        widget_layout = QtWidgets.QVBoxLayout(self.widget_25)
        widget_layout.setContentsMargins(20, 20, 20, 20)
        widget_layout.setSpacing(15)

        controls_widget = QtWidgets.QWidget()
        controls_layout = QtWidgets.QHBoxLayout(controls_widget)
        controls_layout.setContentsMargins(0, 0, 0, 0)

        self.label_92 = QtWidgets.QLabel()
        font = QtGui.QFont("Poppins", 18, QtGui.QFont.Weight.Bold)
        self.label_92.setFont(font)
        controls_layout.addWidget(self.label_92)
        controls_layout.addStretch(1)

        self.delete_3 = QtWidgets.QPushButton()
        self.delete_3.setFixedSize(80, 30)
        self.delete_3.setStyleSheet("""
            QPushButton { background-color: #EB5757; color: white; border-radius: 4px; font: 10pt 'Poppins'; }
            QPushButton:hover { background-color: #d43f3f; }
        """)
        self.delete_3.clicked.connect(self._deleteSelectedSlots)
        controls_layout.addWidget(self.delete_3)

        self.createschedule_2 = QtWidgets.QPushButton()
        self.createschedule_2.setFixedSize(120, 30)
        self.createschedule_2.setStyleSheet("""
            QPushButton { background-color: #084924; color: white; border-radius: 8px; font: 10pt 'Poppins'; }
            QPushButton:hover { background-color: #0a5a2f; }
        """)
        self.createschedule_2.clicked.connect(self.go_to_EditSchedulePage.emit)
        controls_layout.addWidget(self.createschedule_2)

        self.comboBox_2 = QtWidgets.QComboBox()
        self.comboBox_2.setFixedSize(200, 30)
        self.comboBox_2.setStyleSheet("""
            QComboBox { border: 2px solid #064420; border-radius: 6px; padding: 4px 8px; font: 10pt 'Poppins'; color: #064420; background: white; }
        """)
        self.comboBox_2.addItems(["1st Semester 2025 - 2026", "2nd Semester 2025 - 2026", "Summer 2026"])
        self.comboBox_2.currentTextChanged.connect(self._populateWeeklySchedule)
        controls_layout.addWidget(self.comboBox_2)

        # Date selection controls
        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setStyleSheet("""
            QDateEdit { border: 2px solid #064420; border-radius: 6px; padding: 4px 8px; font: 10pt 'Poppins'; color: #064420; background: white; }
        """)
        self.dateEdit.dateChanged.connect(self._updateWeek)
        controls_layout.addWidget(self.dateEdit)

        self.prevWeekButton = QPushButton("Previous Week")
        self.prevWeekButton.setFixedSize(100, 30)
        self.prevWeekButton.setStyleSheet("""
            QPushButton { background-color: #084924; color: white; border-radius: 4px; font: 10pt 'Poppins'; }
            QPushButton:hover { background-color: #0a5a2f; }
        """)
        self.prevWeekButton.clicked.connect(self._prevWeek)
        controls_layout.addWidget(self.prevWeekButton)

        self.nextWeekButton = QPushButton("Next Week")
        self.nextWeekButton.setFixedSize(100, 30)
        self.nextWeekButton.setStyleSheet("""
            QPushButton { background-color: #084924; color: white; border-radius: 4px; font: 10pt 'Poppins'; }
            QPushButton:hover { background-color: #0a5a2f; }
        """)
        self.nextWeekButton.clicked.connect(self._nextWeek)
        controls_layout.addWidget(self.nextWeekButton)

        self.prevMonthButton = QPushButton("Previous Month")
        self.prevMonthButton.setFixedSize(120, 30)
        self.prevMonthButton.setStyleSheet("""
            QPushButton { background-color: #084924; color: white; border-radius: 4px; font: 10pt 'Poppins'; }
            QPushButton:hover { background-color: #0a5a2f; }
        """)
        self.prevMonthButton.clicked.connect(self._prevMonth)
        controls_layout.addWidget(self.prevMonthButton)

        self.nextMonthButton = QPushButton("Next Month")
        self.nextMonthButton.setFixedSize(120, 30)
        self.nextMonthButton.setStyleSheet("""
            QPushButton { background-color: #084924; color: white; border-radius: 4px; font: 10pt 'Poppins'; }
            QPushButton:hover { background-color: #0a5a2f; }
        """)
        self.nextMonthButton.clicked.connect(self._nextMonth)
        controls_layout.addWidget(self.nextMonthButton)

        widget_layout.addWidget(controls_widget)
        self._setupWeeklySchedule(widget_layout)
        scheduler_layout.addWidget(self.widget_25, 1)

    def _setupWeeklySchedule(self, parent_layout):
        grid_container = QtWidgets.QWidget()
        grid_layout = QtWidgets.QVBoxLayout(grid_container)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)

        self.weeklyGrid = QtWidgets.QTableWidget()
        self.weeklyGrid.setColumnCount(8)
        self.weeklyGrid.setRowCount(25)  # 12:00 AM to 12:00 PM with 30-min increments
        self.weeklyGrid.setShowGrid(True)
        self.weeklyGrid.verticalHeader().setVisible(True)
        self.weeklyGrid.horizontalHeader().setVisible(True)
        self.weeklyGrid.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.weeklyGrid.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.weeklyGrid.setStyleSheet("""
            QTableWidget { background: #f9f9f9; font: 10pt 'Poppins'; border: 1px solid #e0e0e0; }
            QTableWidget::item { padding: 5px; border: 1px solid #e0e0e0; }
            QHeaderView::section { background-color: #0a5a2f; color: white; border: 0; padding: 10px; font: 600 11pt 'Poppins'; }
        """)
        headers = ["Time", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, h in enumerate(headers):
            self.weeklyGrid.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(h))

        self.weeklyGrid.setColumnWidth(0, 80)
        header = self.weeklyGrid.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Fixed)
        for c in range(1, 8):
            header.setSectionResizeMode(c, QtWidgets.QHeaderView.ResizeMode.Stretch)

        times = []
        for hour in range(0, 13):  # 12:00 AM to 12:00 PM
            times.append(f"{hour % 12 or 12}:00 {'AM' if hour < 12 else 'PM'}")
            times.append(f"{hour % 12 or 12}:30 {'AM' if hour < 12 else 'PM'}")
        for r, t in enumerate(times):
            item = QtWidgets.QTableWidgetItem(t)
            item.setForeground(QtGui.QBrush(QtGui.QColor("#6b6b6b")))
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.weeklyGrid.setItem(r, 0, item)
            self.weeklyGrid.setRowHeight(r, 40)
            for c in range(1, 8):
                w = QtWidgets.QWidget()
                w.setStyleSheet("QWidget { background: white; }")
                self.weeklyGrid.setCellWidget(r, c, w)

        grid_layout.addWidget(self.weeklyGrid, 1)
        parent_layout.addWidget(grid_container, 1)
        self._populateWeeklySchedule()

    def _addWeeklySlot(self, row, col, title="Available", appt_id=None):
        slot = QtWidgets.QLabel(title)
        slot.setStyleSheet("QLabel { background: #ffc000; border-radius: 4px; font: 9pt 'Poppins'; text-align: center; padding: 2px; }")
        slot.mousePressEvent = lambda event: self._showAppointmentDetails(row, col, appt_id) if appt_id else None
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.addWidget(slot, 1)
        self.weeklyGrid.setCellWidget(row, col, container)

    def _populateWeeklySchedule(self):
        for r in range(self.weeklyGrid.rowCount()):
            for c in range(1, self.weeklyGrid.columnCount()):
                self.weeklyGrid.removeCellWidget(r, c)
                w = QtWidgets.QWidget()
                w.setStyleSheet("QWidget { background: white; border: 1px solid #e0e0e0; }")
                self.weeklyGrid.setCellWidget(r, c, w)

        block = self.crud.get_active_block(self.faculty_id)
        logging.debug(f"Active block: {block}")
        if "error" in block:
            logging.warning("No active block found")
            return

        entries = self.crud.get_block_entries(block["id"])
        logging.debug(f"Block entries: {entries}")
        appointments = self.crud.get_faculty_appointments(self.faculty_id)
        logging.debug(f"Faculty appointments: {appointments}")
        day_map = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
        time_map = {f"{h % 12 or 12}:{m:02d} {'AM' if h < 12 else 'PM'}": i for i, (h, m) in enumerate([(h, m) for h in range(0, 13) for m in [0, 30]])}

        # Get the selected week (Monday to Sunday based on dateEdit)
        selected_date = self.dateEdit.date()
        start_of_week = selected_date.addDays(-(selected_date.dayOfWeek() - 1))  # First day of the week (Monday)
        end_of_week = start_of_week.addDays(6)  # Last day of the week (Sunday)
        logging.debug(f"Selected week: {start_of_week.toString('yyyy-MM-dd')} to {end_of_week.toString('yyyy-MM-dd')}")

        # Populate available slots
        for entry in entries:
            col = day_map.get(entry["day_of_week"])
            start_time = self.convert_time(entry["start_time"])
            logging.debug(f"Checking entry: {entry}, converted time: {start_time}")
            if start_time in time_map and col:
                row = time_map[start_time]
                self._addWeeklySlot(row, col)

        # Populate booked appointments for the selected week
        for appt in appointments:
            appt_date = QtCore.QDate.fromString(appt["appointment_date"], "yyyy-MM-dd")
            logging.debug(f"Checking appointment: {appt}, date: {appt_date.toString('yyyy-MM-dd')}")
            if start_of_week <= appt_date <= end_of_week:
                entry = next((e for e in entries if e["id"] == appt.get("appointment_schedule_entry_id")), {})
                if entry:
                    col = day_map.get(entry["day_of_week"])
                    start_time = self.convert_time(entry["start_time"])
                    if start_time in time_map and col:
                        row = time_map[start_time]
                        title = f"{appt.get('status', 'Booked')}: {next((s['name'] for s in self.crud.list_students() if s['id'] == appt['student_id']), 'Unknown')}"
                        self._addWeeklySlot(row, col, title, appt["id"])

    def _updateWeek(self):
        self._populateWeeklySchedule()

    def _prevWeek(self):
        current_date = self.dateEdit.date()
        self.dateEdit.setDate(current_date.addDays(-7))
        self._populateWeeklySchedule()

    def _nextWeek(self):
        current_date = self.dateEdit.date()
        self.dateEdit.setDate(current_date.addDays(7))
        self._populateWeeklySchedule()

    def _prevMonth(self):
        current_date = self.dateEdit.date()
        self.dateEdit.setDate(current_date.addMonths(-1))
        self._populateWeeklySchedule()

    def _nextMonth(self):
        current_date = self.dateEdit.date()
        self.dateEdit.setDate(current_date.addMonths(1))
        self._populateWeeklySchedule()

    def _showAppointmentDetails(self, row, col, appt_id):
        if appt_id is None:
            logging.info("No appointment details available for this slot")
            return

        appt = next((a for a in self.crud.get_faculty_appointments(self.faculty_id) if a["id"] == appt_id), {})
        if not appt:
            logging.warning(f"No appointment found for ID: {appt_id}")
            return

        entry = next((e for e in self.crud.entries_db.read_all() if e["id"] == appt.get("appointment_schedule_entry_id", -1)), {})
        student = next((s for s in self.crud.list_students() if s["id"] == appt.get("student_id", -1)), {})
        details = [
            ("Student:", student.get("name", "Unknown")),
            ("Time:", f"{entry.get('start_time', '')} - {entry.get('end_time', '')}"),
            ("Purpose:", appt.get("additional_details", "N/A")),
            ("Status:", appt.get("status", "Pending").capitalize()),
            ("Location:", appt.get("address", "N/A"))
        ]
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Appointment Details - ID: {appt_id}")
        dialog.setModal(True)
        dialog.setMinimumSize(400, 300)
        dialog.setStyleSheet("QDialog { background-color: white; border-radius: 12px; }")

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        group = QtWidgets.QGroupBox(f"Appointment ID: {appt_id}")
        group.setStyleSheet("""
            QGroupBox { font: 600 12pt 'Poppins'; color: #084924; border: 1px solid #e0e0e0; border-radius: 8px; margin-bottom: 10px; }
            QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 8px; }
        """)
        form_layout = QFormLayout(group)
        for label, value in details:
            label_widget = QLabel(label)
            label_widget.setStyleSheet("QLabel { font: 600 11pt 'Poppins'; color: #333; }")
            value_widget = QLabel(value)
            value_widget.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #666; }")
            form_layout.addRow(label_widget, value_widget)
        layout.addWidget(group)

        close_button = QPushButton("Close")
        close_button.setFixedSize(120, 40)
        close_button.setStyleSheet("""
            QPushButton { background-color: #084924; color: white; border-radius: 8px; font: 600 12pt 'Poppins'; }
            QPushButton:hover { background-color: #0a5a2f; }
        """)
        close_button.clicked.connect(dialog.accept)
        layout.addWidget(close_button, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        dialog.exec()

    def _deleteSelectedSlots(self):
        selected = self.weeklyGrid.selectedIndexes()
        if not selected:
            logging.info("No slots selected for deletion")
            return

        block = self.crud.get_active_block(self.faculty_id)
        if "error" in block:
            logging.warning("No active block found")
            return

        appointments = self.crud.get_faculty_appointments(self.faculty_id)
        day_map = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
        time_map = {i: f"{h % 12 or 12}:{m:02d} {'AM' if h < 12 else 'PM'}" for i, (h, m) in enumerate([(h, m) for h in range(0, 13) for m in [0, 30]])}

        for index in selected:
            row, col = index.row(), index.column()
            if col == 0:
                continue
            start_time = time_map.get(row)
            day = day_map.get(col)
            for appt in appointments:
                entry = next((e for e in self.crud.entries_db.read_all() if e["id"] == appt.get("appointment_schedule_entry_id")), {})
                if entry and entry["day_of_week"] == day and self.convert_time(entry["start_time"]) == start_time:
                    logging.debug(f"Deleting appointment: {appt}")
                    self.crud.delete_appointment(appt["id"])
                    self.weeklyGrid.removeCellWidget(row, col)
                    w = QtWidgets.QWidget()
                    w.setStyleSheet("QWidget { background: white; border: 1px solid #e0e0e0; }")
                    self.weeklyGrid.setCellWidget(row, col, w)

        self._populateWeeklySchedule()  # Refresh schedule

    def retranslateUi(self):
        self.Academics_5.setText("Appointment Scheduler")
        self.label_92.setText("Weekly Schedule")
        self.createschedule_2.setText("Create Schedule")
        self.delete_3.setText("Delete")
        self.comboBox_2.setItemText(0, "1st Semester 2025 - 2026")
        self.comboBox_2.setItemText(1, "2nd Semester 2025 - 2026")
        self.comboBox_2.setItemText(2, "Summer 2026")