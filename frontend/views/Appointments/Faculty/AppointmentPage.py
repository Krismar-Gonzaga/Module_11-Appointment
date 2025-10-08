from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from .appointment_crud import appointment_crud
from datetime import datetime
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class AppointmentPage_ui(QWidget):
    go_to_AppointmentSchedulerPage = QtCore.pyqtSignal()
    go_to_AppointmentReschedulePage = QtCore.pyqtSignal()
    back = QtCore.pyqtSignal()

    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self.crud = appointment_crud()
        self.faculty_id = self._get_faculty_id()
        logging.debug(f"Initialized AppointmentPage_ui with username: {self.username}, faculty_id: {self.faculty_id}")
        self._setupAppointmentsPage()
        self.retranslateUi()

    def _get_faculty_id(self):
        """Get faculty ID based on username."""
        faculty_list = self.crud.list_faculty()
        logging.debug(f"Faculty list from CRUD: {faculty_list}")
        print(f"Faculty list: {faculty_list}")
        for faculty in faculty_list:
            print(f"Checking faculty: {faculty}, username match: {faculty.get('name', '') == self.username or faculty.get('email', '') == self.username}")
            if faculty.get("name", "") == self.username or faculty.get("email", "") == self.username:
                logging.debug(f"Found faculty: {faculty['name']} with ID: {faculty['id']}")
                print(f"Found faculty: {faculty['name']} with ID: {faculty['id']}")
                return faculty["id"]
        logging.warning(f"No faculty found for username: {self.username}, using fallback ID: 1")
        print(f"No faculty found for username: {self.username}, using fallback ID: 1")
        return 1  # Fallback ID

    def _setupAppointmentsPage(self):
        self.setObjectName("Appointments_2")
        appointments_layout = QtWidgets.QVBoxLayout(self)
        appointments_layout.setContentsMargins(10, 10, 10, 10)
        appointments_layout.setSpacing(10)
        appointments_layout.setObjectName("appointments_layout")

        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(10)

        self.Academics_6 = QtWidgets.QLabel()
        font = QtGui.QFont("Poppins", 24)
        self.Academics_6.setFont(font)
        self.Academics_6.setStyleSheet("QLabel { color: #084924; }")
        self.Academics_6.setObjectName("Academics_6")
        self.Academics_6.setText("Appointments")
        header_layout.addWidget(self.Academics_6)
        header_layout.addStretch(1)

        self.refreshButton = QtWidgets.QPushButton()
        self.refreshButton.setFixedSize(40, 40)
        self.refreshButton.setStyleSheet("border: none; background: transparent;")
        self.refreshButton.setIcon(QtGui.QIcon(":/assets/refresh_icon.png"))
        self.refreshButton.setIconSize(QtCore.QSize(40, 40))
        self.refreshButton.clicked.connect(self._refreshAppointments)
        header_layout.addWidget(self.refreshButton)

        self.backButton_9 = QtWidgets.QPushButton()
        self.backButton_9.setFixedSize(40, 40)
        self.backButton_9.setStyleSheet("border: none; background: transparent;")
        self.backButton_9.setIcon(QtGui.QIcon(":/assets/back_button.png"))
        self.backButton_9.setIconSize(QtCore.QSize(40, 40))
        self.backButton_9.clicked.connect(self.goBackPage)
        header_layout.addWidget(self.backButton_9)

        appointments_layout.addWidget(header_widget)

        self.widget_27 = QtWidgets.QWidget()
        self.widget_27.setStyleSheet("""
            QWidget#widget_27 { 
                background-color: #FFFFFF; 
                border-radius: 20px;
                padding: 20px;
            }
        """)
        widget_layout = QtWidgets.QVBoxLayout(self.widget_27)
        widget_layout.setContentsMargins(20, 20, 20, 20)
        widget_layout.setSpacing(15)

        section_header = QtWidgets.QWidget()
        section_layout = QtWidgets.QHBoxLayout(section_header)
        section_layout.setContentsMargins(0, 0, 0, 0)

        self.label_94 = QtWidgets.QLabel()
        font = QtGui.QFont("Poppins", 20, QtGui.QFont.Weight.Bold)
        self.label_94.setFont(font)
        section_layout.addWidget(self.label_94)
        section_layout.addStretch(1)

        self.pushButton_13 = QtWidgets.QPushButton()
        font = QtGui.QFont("Poppins", 12)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0a5a2f;
            }
        """)
        self.pushButton_13.clicked.connect(self.go_to_AppointmentSchedulerPage.emit)
        section_layout.addWidget(self.pushButton_13)
        widget_layout.addWidget(section_header)

        self.tableWidget_8 = QtWidgets.QTableWidget()
        self.tableWidget_8.setAlternatingRowColors(True)
        self.tableWidget_8.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_8.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_8.setShowGrid(False)
        self.tableWidget_8.verticalHeader().setVisible(False)
        self.tableWidget_8.horizontalHeader().setVisible(True)
        self.tableWidget_8.setColumnCount(6)
        header = self.tableWidget_8.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #0a5a2f;
                color: white;
                padding: 12px 8px;
                border: 0px;
                font: 600 11pt 'Poppins';
            }
        """)
        self.tableWidget_8.setStyleSheet("""
            QTableWidget {
                background: white;
                gridline-color: transparent;
                border: none;
                font: 10pt 'Poppins';
            }
            QTableWidget::item { 
                padding: 10px 8px;
                border-bottom: 1px solid #f0f0f0;
            }
        """)
        headers = ["Time", "Student", "Slot", "Purpose", "Status", "Actions"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(QtGui.QFont("Poppins", 11))
            self.tableWidget_8.setHorizontalHeaderItem(i, item)
        widget_layout.addWidget(self.tableWidget_8, 1)
        appointments_layout.addWidget(self.widget_27, 1)
        self._populateAppointmentsTable()

    def resizeEvent(self, event):
        """Adjust table column widths on resize."""
        width = self.tableWidget_8.width()
        self.tableWidget_8.setColumnWidth(0, int(width * 0.15))  # Time
        self.tableWidget_8.setColumnWidth(1, int(width * 0.20))  # Student
        self.tableWidget_8.setColumnWidth(2, int(width * 0.20))  # Slot
        self.tableWidget_8.setColumnWidth(3, int(width * 0.25))  # Purpose
        self.tableWidget_8.setColumnWidth(4, int(width * 0.15))  # Status
        self.tableWidget_8.setColumnWidth(5, int(width * 0.15))  # Actions
        super().resizeEvent(event)

    def goBackPage(self):
        self.back.emit()

    def _refreshAppointments(self):
        """Refresh the appointments table."""
        logging.debug("Refreshing appointments table")
        self.tableWidget_8.setRowCount(0)  # Clear existing rows
        self._populateAppointmentsTable()

    def _makeStatusItem(self, text, color_hex):
        item = QtWidgets.QTableWidgetItem(text)
        item.setForeground(QtGui.QBrush(QtGui.QColor(color_hex)))
        item.setFont(QtGui.QFont("Poppins", 10, QtGui.QFont.Weight.DemiBold))
        return item

    def _makePurposeViewCell(self, appointment_id):
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        link = QtWidgets.QLabel("View")
        link.mousePressEvent = lambda event: self._showPurposeDetailsDialog(appointment_id)
        link.setFont(QtGui.QFont("Poppins", 10))
        link.setStyleSheet("QLabel { color: #2F80ED; text-decoration: underline; }")
        link.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        layout.addWidget(link, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        return container

    def _showPurposeDetailsDialog(self, appointment_id):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Appointment Details")
        dialog.setModal(True)
        dialog.setMinimumSize(550, 600)
        dialog.setStyleSheet("QDialog { background-color: white; border-radius: 12px; }")
        main_layout = QtWidgets.QVBoxLayout(dialog)
        main_layout.setContentsMargins(0, 0, 0, 0)
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea { border: none; background: white; }
            QScrollBar:vertical {
                background: #f0f0f0;
                width: 12px;
                margin: 0px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                border-radius: 6px;
                min-height: 20px;
            }
        """)
        scroll_content = QtWidgets.QWidget()
        content_layout = QtWidgets.QVBoxLayout(scroll_content)
        content_layout.setContentsMargins(24, 20, 24, 20)
        content_layout.setSpacing(20)

        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        icon_label = QtWidgets.QLabel()
        icon_label.setFixedSize(32, 32)
        icon_label.setStyleSheet("QLabel { background-color: #084924; border-radius: 8px; }")
        title_label = QtWidgets.QLabel("Appointment Purpose")
        title_label.setStyleSheet("QLabel { color: #084924; font: 600 20pt 'Poppins'; }")
        header_layout.addWidget(icon_label)
        header_layout.addSpacing(12)
        header_layout.addWidget(title_label)
        header_layout.addStretch(1)
        content_layout.addWidget(header_widget)

        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        separator.setStyleSheet("QFrame { background-color: #e0e0e0; }")
        content_layout.addWidget(separator)

        appointment = next((a for a in self.crud.get_faculty_appointments(self.faculty_id) if a["id"] == appointment_id), None)
        if appointment:
            student = next((s for s in self.crud.list_students() if s["id"] == appointment.get("student_id", -1)), {})
            entry = next((e for e in self.crud.entries_db.read_all() if e["id"] == appointment.get("appointment_schedule_entry_id", -1)), {})
            if not student:
                logging.warning(f"No student found for student_id: {appointment.get('student_id', 'unknown')}")
            if not entry:
                logging.warning(f"No entry found for appointment_schedule_entry_id: {appointment.get('appointment_schedule_entry_id', 'unknown')}")
            info_data = [
                ("Student:", student.get("name", "Unknown")),
                ("Date & Time:", f"{appointment.get('appointment_date', '')} {entry.get('start_time', '')}"),
                ("Duration:", "30 minutes"),
                ("Status:", appointment.get("status", "").capitalize()),
                ("Mode:", appointment.get("address", "").startswith("http") and "Online" or "In person"),
                ("Meeting Link:", appointment.get("address", "")),
                ("Contact Email:", student.get("email", ""))
            ]
            info_group = QtWidgets.QGroupBox("Appointment Information")
            info_group.setStyleSheet("""
                QGroupBox { font: 600 12pt 'Poppins'; color: #084924; border: 1px solid #e0e0e0; border-radius: 8px; margin-top: 12px; }
                QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 8px; }
            """)
            info_layout = QtWidgets.QFormLayout(info_group)
            for label, value in info_data:
                label_widget = QtWidgets.QLabel(label)
                label_widget.setStyleSheet("QLabel { font: 600 11pt 'Poppins'; color: #333; }")
                value_widget = QtWidgets.QLabel(value)
                value_widget.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #666; }")
                info_layout.addRow(label_widget, value_widget)
            content_layout.addWidget(info_group)

            purpose_group = QtWidgets.QGroupBox("Purpose Details")
            purpose_group.setStyleSheet("""
                QGroupBox { font: 600 12pt 'Poppins'; color: #084924; border: 1px solid #e0e0e0; border-radius: 8px; margin-top: 12px; }
                QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 8px; }
            """)
            purpose_layout = QtWidgets.QVBoxLayout(purpose_group)
            purpose_label = QtWidgets.QLabel(appointment.get("additional_details", ""))
            purpose_label.setWordWrap(True)
            purpose_label.setStyleSheet("QLabel { color: #2b2b2b; font: 11pt 'Poppins'; line-height: 1.5; }")
            purpose_scroll_area = QtWidgets.QScrollArea()
            purpose_scroll_area.setWidgetResizable(True)
            purpose_scroll_area.setStyleSheet("QScrollArea { border: 1px solid #f0f0f0; border-radius: 6px; background: #fafafa; }")
            purpose_scroll_area.setFixedHeight(200)
            purpose_scroll_content = QtWidgets.QWidget()
            purpose_scroll_layout = QtWidgets.QVBoxLayout(purpose_scroll_content)
            purpose_scroll_layout.setContentsMargins(12, 12, 12, 12)
            purpose_scroll_layout.addWidget(purpose_label)
            purpose_scroll_area.setWidget(purpose_scroll_content)
            purpose_layout.addWidget(purpose_scroll_area)
            content_layout.addWidget(purpose_group)
        else:
            logging.warning(f"No appointment found for appointment_id: {appointment_id}")
            content_layout.addWidget(QtWidgets.QLabel("No appointment details available"))

        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)
        close_button = QtWidgets.QPushButton("Close")
        close_button.setFixedSize(120, 40)
        close_button.setStyleSheet("""
            QPushButton { background-color: #084924; color: white; border-radius: 8px; font: 600 12pt 'Poppins'; }
            QPushButton:hover { background-color: #0a5a2f; }
        """)
        close_button.clicked.connect(dialog.accept)
        main_layout.addWidget(close_button, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        dialog.exec()

    def _makeActionsCell(self, status, row_index, appointment_id):
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        def make_btn(text, bg):
            btn = QtWidgets.QPushButton(text, parent=container)
            btn.setMinimumHeight(28)
            btn.setStyleSheet(f"QPushButton {{ background-color: {bg}; color: white; border-radius: 6px; padding: 4px 10px; font: 10pt 'Poppins'; }}")
            return btn

        if status == "pending":
            approve_btn = make_btn("Approve", "#27AE60")
            deny_btn = make_btn("Deny", "#EB5757")
            approve_btn.clicked.connect(lambda: self._openApproveDialog(row_index, appointment_id))
            deny_btn.clicked.connect(lambda: self._openDenyDialog(row_index, appointment_id))
            layout.addWidget(approve_btn)
            layout.addWidget(deny_btn)
        elif status == "rescheduled":
            cancel = make_btn("Cancel", "#EB5757")
            cancel.clicked.connect(lambda: self._openCancelDialog(row_index, status, appointment_id))
            layout.addWidget(cancel)
        elif status == "approved":
            reschedule_button = make_btn("Reschedule", "#2F80ED")
            reschedule_button.clicked.connect(lambda: self._emitReschedule(appointment_id))
            layout.addWidget(reschedule_button)
            cancel = make_btn("Cancel", "#EB5757")
            cancel.clicked.connect(lambda: self._openCancelDialog(row_index, status, appointment_id))
            layout.addWidget(cancel)
        elif status == "canceled" or status == "denied":
            # No actions for canceled or denied
            layout.addStretch(1)
        return container

    def _emitReschedule(self, appointment_id):
        """Emit signal to reschedule with appointment ID."""
        self.selected_appointment_id = appointment_id
        logging.debug(f"Emitting go_to_AppointmentReschedulePage with appointment_id: {appointment_id}")
        self.go_to_AppointmentReschedulePage.emit()

    def _openApproveDialog(self, row_index, appointment_id):
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Confirm Approval")
        dlg.setModal(True)
        dlg.setMinimumSize(460, 280)
        root = QtWidgets.QVBoxLayout(dlg)
        root.setContentsMargins(24, 20, 24, 20)
        root.setSpacing(12)

        title = QtWidgets.QLabel("Are you sure you want to accept\nthis appointment?")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        title.setStyleSheet("QLabel { color: #2b2b2b; font: 600 12pt 'Poppins'; }")
        root.addWidget(title)

        subtype = QtWidgets.QLabel("Meeting type:")
        subtype.setStyleSheet("QLabel { color: #2b2b2b; font: 11pt 'Poppins'; }")
        root.addWidget(subtype)

        types_row = QtWidgets.QHBoxLayout()
        chk_online = QtWidgets.QCheckBox("Online")
        chk_person = QtWidgets.QCheckBox("In person")
        for chk in (chk_online, chk_person):
            chk.setStyleSheet("QCheckBox { font: 10pt 'Poppins'; color: #2b2b2b; }")
        chk_online.setChecked(True)
        def _toggle(exclusive, other):
            if exclusive.isChecked():
                other.setChecked(False)
        chk_online.toggled.connect(lambda: _toggle(chk_online, chk_person))
        chk_person.toggled.connect(lambda: _toggle(chk_person, chk_online))
        types_row.addWidget(chk_online)
        types_row.addSpacing(24)
        types_row.addWidget(chk_person)
        types_row.addStretch(1)
        root.addLayout(types_row)

        link_edit = QtWidgets.QLineEdit()
        link_edit.setPlaceholderText("Online meeting link")
        link_edit.setStyleSheet("QLineEdit { border: 1px solid #cfd8dc; border-radius: 6px; padding: 8px 10px; font: 10pt 'Poppins'; }")
        root.addWidget(link_edit)
        chk_online.toggled.connect(lambda: link_edit.setPlaceholderText("Online meeting link"))
        chk_person.toggled.connect(lambda: link_edit.setPlaceholderText("Location details"))

        root.addStretch(1)
        btn_row = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_accept = QtWidgets.QPushButton("Accept")
        btn_cancel.setStyleSheet("QPushButton { background: #bdbdbd; border-radius: 8px; padding: 8px 20px; font: 10pt 'Poppins'; color: white; }")
        btn_accept.setStyleSheet("QPushButton { background: #084924; border-radius: 8px; padding: 8px 20px; font: 10pt 'Poppins'; color: white; }")
        btn_cancel.clicked.connect(dlg.reject)
        def _accept_clicked():
            if chk_online.isChecked() or chk_person.isChecked():
                updates = {"status": "approved", "address": link_edit.text()}
                self.crud.update_appointment(appointment_id, updates)
                self.tableWidget_8.setItem(row_index, 4, self._makeStatusItem("APPROVED", "#219653"))
                self.tableWidget_8.setCellWidget(row_index, 5, self._makeActionsCell("approved", row_index, appointment_id))
                self._refreshAppointments()
                dlg.accept()
        btn_accept.clicked.connect(_accept_clicked)
        btn_row.addWidget(btn_cancel)
        btn_row.addStretch(1)
        btn_row.addWidget(btn_accept)
        root.addLayout(btn_row)
        dlg.exec()

    def _openDenyDialog(self, row_index, appointment_id):
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Confirm Deny")
        dlg.setModal(True)
        dlg.setMinimumSize(420, 210)
        root = QtWidgets.QVBoxLayout(dlg)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(14)

        title = QtWidgets.QLabel("Are you sure you want to Deny this\nrequest?")
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
        def _deny_clicked():
            self.crud.update_appointment(appointment_id, {"status": "denied"})
            self.tableWidget_8.setItem(row_index, 4, self._makeStatusItem("DENIED", "#EB5757"))
            self.tableWidget_8.setCellWidget(row_index, 5, self._makeActionsCell("denied", row_index, appointment_id))
            self._refreshAppointments()
            dlg.accept()
        btn_deny.clicked.connect(_deny_clicked)
        btn_row.addWidget(btn_cancel)
        btn_row.addStretch(1)
        btn_row.addWidget(btn_deny)
        root.addLayout(btn_row)
        dlg.exec()

    def _openCancelDialog(self, row_index, status, appointment_id):
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Cancel")
        dlg.setModal(True)
        dlg.setMinimumSize(420, 210)
        root = QtWidgets.QVBoxLayout(dlg)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(14)

        title_text = f"Are you sure you want to Cancel this\n{status.lower()} appointment?"
        title = QtWidgets.QLabel(title_text)
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        title.setStyleSheet("QLabel { color: #2b2b2b; font: 600 12pt 'Poppins'; }")
        root.addWidget(title)
        root.addStretch(1)

        btn_row = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_confirm = QtWidgets.QPushButton("Confirm")
        btn_cancel.setStyleSheet("QPushButton { background: #e0e0e0; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: #2b2b2b; }")
        btn_confirm.setStyleSheet("QPushButton { background: #EB5757; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: white; }")
        btn_cancel.clicked.connect(dlg.reject)
        def _confirm_clicked():
            new_status = "pending" if status == "rescheduled" else "canceled"
            self.crud.update_appointment(appointment_id, {"status": new_status})
            self.tableWidget_8.setItem(row_index, 4, self._makeStatusItem(new_status.upper(), "#F2994A" if new_status == "pending" else "#EB5757"))
            self.tableWidget_8.setCellWidget(row_index, 5, self._makeActionsCell(new_status, row_index, appointment_id))
            self._refreshAppointments()
            dlg.accept()
        btn_confirm.clicked.connect(_confirm_clicked)
        btn_row.addWidget(btn_cancel)
        btn_row.addStretch(1)
        btn_row.addWidget(btn_confirm)
        root.addLayout(btn_row)
        dlg.exec()

    def _populateAppointmentsTable(self):
        """Populate the appointments table with faculty appointments."""
        all_appointments = self.crud.appointments_db.read_all()  # Read all appointments as a fallback
        appointments = self.crud.get_faculty_appointments(self.faculty_id)
        logging.debug(f"Retrieved {len(all_appointments)} total appointments, filtered to {len(appointments)} for faculty_id: {self.faculty_id}")
        logging.debug(f"All appointments: {all_appointments}")
        logging.debug(f"Filtered appointments: {appointments}")
        
        # Log additional data for debugging
        entries = self.crud.entries_db.read_all()
        blocks = self.crud.blocks_db.read_all()
        students = self.crud.list_students()
        logging.debug(f"Entries: {entries}")
        logging.debug(f"Blocks: {blocks}")
        logging.debug(f"Students: {students}")
        
        if not appointments:
            logging.info("No appointments found using get_faculty_appointments, checking all appointments")
            appointments = [a for a in all_appointments if a.get("faculty_id") == self.faculty_id]  # Fallback to direct faculty_id check
            logging.debug(f"Fallback appointments: {appointments}")

        if not appointments:
            logging.info("No appointments found, displaying placeholder message")
            self.tableWidget_8.setRowCount(1)
            placeholder_item = QtWidgets.QTableWidgetItem("No appointments available")
            placeholder_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            placeholder_item.setFont(QtGui.QFont("Poppins", 10))
            self.tableWidget_8.setItem(0, 0, placeholder_item)
            self.tableWidget_8.setSpan(0, 0, 1, 6)  # Span across all columns
            self.tableWidget_8.update()  # Force table refresh
            return

        logging.debug(f"Setting table row count to {len(appointments)}")
        self.tableWidget_8.setRowCount(len(appointments))
        status_colors = {
            "pending": "#F2994A",
            "rescheduled": "#2F80ED",
            "canceled": "#EB5757",
            "approved": "#219653",
            "denied": "#EB5757"
        }
        try:
            for r, appt in enumerate(appointments):
                logging.debug(f"Processing appointment {r + 1}: {appt}")
                student = next((s for s in students if s["id"] == appt.get("student_id", -1)), {})
                entry = next((e for e in entries if e["id"] == appt.get("appointment_schedule_entry_id", -1)), {})
                if not student:
                    logging.warning(f"No student found for student_id: {appt.get('student_id', 'unknown')}")
                if not entry:
                    logging.warning(f"No entry found for appointment_schedule_entry_id: {appt.get('appointment_schedule_entry_id', 'unknown')}")
                time_text = f"{appt.get('appointment_date', '')} {entry.get('start_time', 'N/A')}"
                slot_text = f"{entry.get('start_time', 'N/A')} - {entry.get('end_time', 'N/A')}"
                logging.debug(f"Setting row {r}: Time={time_text}, Student={student.get('name', 'Unknown')}, Slot={slot_text}")
                
                self.tableWidget_8.setItem(r, 0, QtWidgets.QTableWidgetItem(time_text))
                self.tableWidget_8.setItem(r, 1, QtWidgets.QTableWidgetItem(student.get("name", "Unknown")))
                self.tableWidget_8.setItem(r, 2, QtWidgets.QTableWidgetItem(slot_text))
                self.tableWidget_8.setCellWidget(r, 3, self._makePurposeViewCell(appt["id"]))
                self.tableWidget_8.setItem(r, 4, self._makeStatusItem(appt.get("status", "pending").upper(), status_colors.get(appt["status"], "#333333")))
                self.tableWidget_8.setCellWidget(r, 5, self._makeActionsCell(appt["status"], r, appt["id"]))
                self.tableWidget_8.setRowHeight(r, 50)
            logging.debug("Finished populating table")
        except Exception as e:
            logging.error(f"Error populating table: {str(e)}")
            self.tableWidget_8.setRowCount(1)
            placeholder_item = QtWidgets.QTableWidgetItem(f"Error loading appointments: {str(e)}")
            placeholder_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            placeholder_item.setFont(QtGui.QFont("Poppins", 10))
            self.tableWidget_8.setItem(0, 0, placeholder_item)
            self.tableWidget_8.setSpan(0, 0, 1, 6)
        finally:
            self.tableWidget_8.update()  # Force table refresh
            self.tableWidget_8.viewport().update()  # Ensure viewport is redrawn

    def retranslateUi(self):
        headers = ["Time", "Student", "Slot", "Purpose", "Status", "Actions"]
        for i, header in enumerate(headers):
            item = self.tableWidget_8.horizontalHeaderItem(i)
            if item:
                item.setText(header)
        self.label_94.setText("My Appointments")
        self.pushButton_13.setText("Appointment Scheduler")

if __name__ == "__main__":
    student = AppointmentPage_ui("Kim", ["Faculty"], "Faculty", "token123")
    print(student._get_faculty_id())