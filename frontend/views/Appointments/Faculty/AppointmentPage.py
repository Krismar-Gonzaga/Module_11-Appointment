from datetime import datetime
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox
from .appointment_crud import appointment_crud
from datetime import datetime
import logging

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
        
        # Create sample data if no appointments exist
        self._ensure_sample_data()
        logging.debug(f"Sample data ensured for faculty_id: {self.faculty_id}")
        self.setFixedSize(1000, 550)
        self._setupAppointmentsPage()
        self.retranslateUi()

    def _get_faculty_id(self):
        """Get faculty ID based on username."""
        faculty = self.crud.get_faculty_by_username(self.username)
        if faculty:
            logging.debug(f"Found faculty: {faculty['name']} with ID: {faculty['id']}")
            return faculty["id"]
        else:
            # If no faculty found, create one for testing
            logging.warning(f"No faculty found for username: {self.username}, creating sample faculty")
            new_faculty = self.crud.create_faculty(self.username, f"{self.username}@school.edu", "Sample Department")
            if new_faculty:
                return new_faculty["id"]
            else:
                logging.error("Failed to create sample faculty")
                return 1  # Fallback ID

    def _ensure_sample_data(self):
        """Ensure there is sample data for testing."""
        appointments = self.crud.get_faculty_appointments(self.faculty_id)
        if not appointments:
            logging.info("No appointments found, creating sample data")
            self.crud.create_sample_data()

    def _setupAppointmentsPage(self):
        self.setObjectName("Appointments_2")
        appointments_layout = QtWidgets.QVBoxLayout(self)
        appointments_layout.setContentsMargins(10, 10, 10, 10)
        appointments_layout.setSpacing(10)
        appointments_layout.setObjectName("appointments_layout")

        # Header with title and buttons
        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(10)

        self.Academics_6 = QtWidgets.QLabel()
        font = QtGui.QFont("Poppins", 24)
        self.Academics_6.setFont(font)
        self.Academics_6.setStyleSheet("QLabel { color: #084924; }")
        self.Academics_6.setObjectName("Academics_6")
        header_layout.addWidget(self.Academics_6)
        header_layout.addStretch(1)

        # Refresh button
        self.refreshButton = QtWidgets.QPushButton()
        self.refreshButton.setFixedSize(40, 40)
        self.refreshButton.setStyleSheet("""
            QPushButton {
                border: none; 
                background: transparent;
            }
            QPushButton:hover {
                background: #f0f0f0;
                border-radius: 20px;
            }
        """)
        self.refreshButton.setIcon(QtGui.QIcon(":/assets/refresh_icon.png"))
        self.refreshButton.setIconSize(QtCore.QSize(30, 30))
        self.refreshButton.clicked.connect(self._refreshAppointments)
        header_layout.addWidget(self.refreshButton)

        # Back button
        self.backButton_9 = QtWidgets.QPushButton()
        self.backButton_9.setFixedSize(40, 40)
        self.backButton_9.setStyleSheet("""
            QPushButton {
                border: none; 
                background: transparent;
            }
            QPushButton:hover {
                background: #f0f0f0;
                border-radius: 20px;
            }
        """)
        self.backButton_9.setIcon(QtGui.QIcon(":/assets/back_button.png"))
        self.backButton_9.setIconSize(QtCore.QSize(30, 30))
        self.backButton_9.clicked.connect(self.goBackPage)
        header_layout.addWidget(self.backButton_9)

        appointments_layout.addWidget(header_widget)

        # Main content widget
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

        # Section header
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

        # Table widget
        self.tableWidget_8 = QtWidgets.QTableWidget()
        self.tableWidget_8.setAlternatingRowColors(True)
        self.tableWidget_8.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_8.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_8.setShowGrid(False)
        self.tableWidget_8.verticalHeader().setVisible(True)
        self.tableWidget_8.horizontalHeader().setVisible(True)
        self.tableWidget_8.setColumnCount(6)
        
        # Set column widths
        self.tableWidget_8.setColumnWidth(0, 200)  # Time
        self.tableWidget_8.setColumnWidth(1, 180)  # Student
        self.tableWidget_8.setColumnWidth(2, 220)  # Slot
        self.tableWidget_8.setColumnWidth(3, 250)  # Purpose
        self.tableWidget_8.setColumnWidth(4, 120)  # Status
        self.tableWidget_8.setColumnWidth(5, 150)  # Actions
        
        # Header styling
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
        
        # Table styling
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
            QTableWidget::item:selected {
                background-color: #e8f5e8;
            }
        """)
        
        # Set headers
        headers = ["Time", "Student", "Slot", "Purpose", "Status", "Actions"]
        for i, header_text in enumerate(headers):
            item = QtWidgets.QTableWidgetItem(header_text)
            item.setFont(QtGui.QFont("Poppins", 11))
            self.tableWidget_8.setHorizontalHeaderItem(i, item)
            
        widget_layout.addWidget(self.tableWidget_8, 1)
        appointments_layout.addWidget(self.widget_27, 1)
        
        # Populate table
        self._populateAppointmentsTable()

    def resizeEvent(self, event):
        """Adjust table column widths on resize."""
        width = self.tableWidget_8.width()
        self.tableWidget_8.setColumnWidth(0, int(width * 0.30))  # Time
        self.tableWidget_8.setColumnWidth(1, int(width * 0.30))  # Student
        self.tableWidget_8.setColumnWidth(2, int(width * 0.30))  # Slot
        self.tableWidget_8.setColumnWidth(3, int(width * 0.30))  # Purpose
        self.tableWidget_8.setColumnWidth(4, int(width * 0.25))  # Status
        self.tableWidget_8.setColumnWidth(5, int(width * 0.25))  # Actions
        super().resizeEvent(event)

    def goBackPage(self):
        self.back.emit()

    def _refreshAppointments(self):
        """Refresh the appointments table."""
        logging.debug("Refreshing appointments table")
        self._populateAppointmentsTable()
        QMessageBox.information(self, "Refreshed", "Appointments data has been refreshed!")

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
        """Show dialog with appointment details."""
        try:
            dialog = QtWidgets.QDialog(self)
            dialog.setWindowTitle("Appointment Details")
            dialog.setModal(True)
            dialog.setFixedSize(550, 600)
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

            # Header
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

            # Separator
            separator = QtWidgets.QFrame()
            separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
            separator.setStyleSheet("QFrame { background-color: #e0e0e0; }")
            content_layout.addWidget(separator)

            # Get appointment data
            appointment = None
            appointments = self.crud.get_faculty_appointments(self.faculty_id)
            for appt in appointments:
                if appt.get("id") == appointment_id:
                    appointment = appt
                    break

            if appointment:
                # Get student info
                student = self.crud.get_student_by_id(appointment.get("student_id"))
                student_name = student.get("name", "Unknown") if student else "Unknown"
                student_email = student.get("email", "") if student else ""
                
                # Get schedule entry info
                entry = None
                entries = self.crud.entries_db.read_all()
                for e in entries:
                    if e.get("id") == appointment.get("appointment_schedule_entry_id"):
                        entry = e
                        break
                
                # Appointment information
                info_group = QtWidgets.QGroupBox("Appointment Information")
                info_group.setStyleSheet("""
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
                        padding: 0 8px; 
                    }
                """)
                
                info_layout = QtWidgets.QFormLayout(info_group)
                info_data = [
                    ("Student:", student_name),
                    ("Date & Time:", f"{appointment.get('appointment_date', 'Unknown')} {entry.get('start_time', '') if entry else ''}"),
                    ("Duration:", "30 minutes"),
                    ("Status:", appointment.get("status", "").capitalize()),
                    ("Mode:", "Online" if appointment.get("address", "").startswith("http") else "In person"),
                    ("Meeting Link:", appointment.get("address", "N/A")),
                    ("Contact Email:", student_email)
                ]
                
                for label, value in info_data:
                    label_widget = QtWidgets.QLabel(label)
                    label_widget.setStyleSheet("QLabel { font: 600 11pt 'Poppins'; color: #333; }")
                    value_widget = QtWidgets.QLabel(value)
                    value_widget.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #666; }")
                    info_layout.addRow(label_widget, value_widget)
                
                content_layout.addWidget(info_group)

                # Purpose details
                purpose_group = QtWidgets.QGroupBox("Purpose Details")
                purpose_group.setStyleSheet("""
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
                        padding: 0 8px; 
                    }
                """)
                
                purpose_layout = QtWidgets.QVBoxLayout(purpose_group)
                purpose_text = appointment.get("additional_details", "No details provided")
                purpose_label = QtWidgets.QLabel(purpose_text)
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
                content_layout.addWidget(QtWidgets.QLabel("No appointment details available"))

            scroll_area.setWidget(scroll_content)
            main_layout.addWidget(scroll_area)
            
            # Close button
            button_widget = QtWidgets.QWidget()
            button_layout = QtWidgets.QHBoxLayout(button_widget)
            button_layout.addStretch(1)
            
            close_button = QtWidgets.QPushButton("Close")
            close_button.setFixedSize(120, 40)
            close_button.setStyleSheet("""
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
            close_button.clicked.connect(dialog.accept)
            button_layout.addWidget(close_button)
            
            main_layout.addWidget(button_widget)
            dialog.exec()
            
        except Exception as e:
            logging.error(f"Error showing purpose details: {str(e)}")
            QMessageBox.warning(self, "Error", f"Could not load appointment details: {str(e)}")

    def _makeActionsCell(self, status, row_index, appointment_id):
        """Create action buttons based on appointment status."""
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        def make_btn(text, bg_color):
            btn = QtWidgets.QPushButton(text, parent=container)
            btn.setMinimumHeight(28)
            btn.setStyleSheet(f"""
                QPushButton {{ 
                    background-color: {bg_color}; 
                    color: white; 
                    border-radius: 6px; 
                    padding: 4px 10px; 
                    font: 10pt 'Poppins'; 
                }}
                QPushButton:hover {{
                    background-color: {self._darken_color(bg_color)};
                }}
            """)
            return btn

        if status == "pending":
            approve_btn = make_btn("Approve", "#27AE60")
            deny_btn = make_btn("Deny", "#EB5757")
            approve_btn.clicked.connect(lambda: self._openApproveDialog(row_index, appointment_id))
            deny_btn.clicked.connect(lambda: self._openDenyDialog(row_index, appointment_id))
            layout.addWidget(approve_btn)
            layout.addWidget(deny_btn)
        elif status == "approved":
            reschedule_btn = make_btn("Reschedule", "#2F80ED")
            cancel_btn = make_btn("Cancel", "#EB5757")
            reschedule_btn.clicked.connect(lambda: self._emitReschedule(appointment_id))
            cancel_btn.clicked.connect(lambda: self._openCancelDialog(row_index, status, appointment_id))
            layout.addWidget(reschedule_btn)
            layout.addWidget(cancel_btn)
        elif status in ["canceled", "denied"]:
            # No actions for canceled or denied appointments
            layout.addStretch(1)
        else:
            layout.addStretch(1)

        return container

    def _darken_color(self, hex_color):
        """Darken a hex color for hover effect."""
        try:
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            darkened = tuple(max(0, c - 30) for c in rgb)
            return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"
        except:
            return hex_color

    def _emitReschedule(self, appointment_id):
        """Emit signal to reschedule with appointment ID."""
        self.selected_appointment_id = appointment_id
        logging.debug(f"Emitting go_to_AppointmentReschedulePage with appointment_id: {appointment_id}")
        self.go_to_AppointmentReschedulePage.emit()

    def _openApproveDialog(self, row_index, appointment_id):
        """Open dialog to approve appointment."""
        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle("Confirm Approval")
        dlg.setModal(True)
        dlg.setFixedSize(400, 200)
        
        layout = QtWidgets.QVBoxLayout(dlg)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)

        title = QtWidgets.QLabel("Are you sure you want to approve this appointment?")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("QLabel { color: #2b2b2b; font: 600 12pt 'Poppins'; }")
        layout.addWidget(title)

        layout.addStretch(1)

        btn_layout = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_approve = QtWidgets.QPushButton("Approve")
        
        btn_cancel.setStyleSheet("""
            QPushButton {
                background: #e0e0e0;
                border-radius: 6px;
                padding: 8px 20px;
                font: 10pt 'Poppins';
                color: #2b2b2b;
            }
            QPushButton:hover {
                background: #d0d0d0;
            }
        """)
        
        btn_approve.setStyleSheet("""
            QPushButton {
                background: #27AE60;
                border-radius: 6px;
                padding: 8px 20px;
                font: 10pt 'Poppins';
                color: white;
            }
            QPushButton:hover {
                background: #219653;
            }
        """)
        
        btn_cancel.clicked.connect(dlg.reject)
        
        def _approve_clicked():
            try:
                result = self.crud.update_appointment(appointment_id, {"status": "approved"})
                if result:
                    self._refreshAppointments()
                    QMessageBox.information(self, "Success", "Appointment approved successfully!")
                    dlg.accept()
                else:
                    QMessageBox.warning(self, "Error", "Failed to approve appointment.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to approve appointment: {str(e)}")
        
        btn_approve.clicked.connect(_approve_clicked)
        
        btn_layout.addWidget(btn_cancel)
        btn_layout.addStretch(1)
        btn_layout.addWidget(btn_approve)
        layout.addLayout(btn_layout)

        dlg.exec()

    def _openDenyDialog(self, row_index, appointment_id):
        """Open dialog to deny appointment."""
        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle("Confirm Denial")
        dlg.setModal(True)
        dlg.setFixedSize(400, 200)
        
        layout = QtWidgets.QVBoxLayout(dlg)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)

        title = QtWidgets.QLabel("Are you sure you want to deny this appointment?")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("QLabel { color: #2b2b2b; font: 600 12pt 'Poppins'; }")
        layout.addWidget(title)

        layout.addStretch(1)

        btn_layout = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_deny = QtWidgets.QPushButton("Deny")
        
        btn_cancel.setStyleSheet("""
            QPushButton {
                background: #e0e0e0;
                border-radius: 6px;
                padding: 8px 20px;
                font: 10pt 'Poppins';
                color: #2b2b2b;
            }
            QPushButton:hover {
                background: #d0d0d0;
            }
        """)
        
        btn_deny.setStyleSheet("""
            QPushButton {
                background: #EB5757;
                border-radius: 6px;
                padding: 8px 20px;
                font: 10pt 'Poppins';
                color: white;
            }
            QPushButton:hover {
                background: #d04545;
            }
        """)
        
        btn_cancel.clicked.connect(dlg.reject)
        
        def _deny_clicked():
            try:
                result = self.crud.update_appointment(appointment_id, {"status": "denied"})
                if result:
                    self._refreshAppointments()
                    QMessageBox.information(self, "Success", "Appointment denied successfully!")
                    dlg.accept()
                else:
                    QMessageBox.warning(self, "Error", "Failed to deny appointment.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to deny appointment: {str(e)}")
        
        btn_deny.clicked.connect(_deny_clicked)
        
        btn_layout.addWidget(btn_cancel)
        btn_layout.addStretch(1)
        btn_layout.addWidget(btn_deny)
        layout.addLayout(btn_layout)

        dlg.exec()

    def _openCancelDialog(self, row_index, status, appointment_id):
        """Open dialog to cancel appointment."""
        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle("Confirm Cancellation")
        dlg.setModal(True)
        dlg.setFixedSize(400, 200)
        
        layout = QtWidgets.QVBoxLayout(dlg)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)

        title = QtWidgets.QLabel("Are you sure you want to cancel this appointment?")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("QLabel { color: #2b2b2b; font: 600 12pt 'Poppins'; }")
        layout.addWidget(title)

        layout.addStretch(1)

        btn_layout = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("No")
        btn_confirm = QtWidgets.QPushButton("Yes, Cancel")
        
        btn_cancel.setStyleSheet("""
            QPushButton {
                background: #e0e0e0;
                border-radius: 6px;
                padding: 8px 20px;
                font: 10pt 'Poppins';
                color: #2b2b2b;
            }
            QPushButton:hover {
                background: #d0d0d0;
            }
        """)
        
        btn_confirm.setStyleSheet("""
            QPushButton {
                background: #EB5757;
                border-radius: 6px;
                padding: 8px 20px;
                font: 10pt 'Poppins';
                color: white;
            }
            QPushButton:hover {
                background: #d04545;
            }
        """)
        
        btn_cancel.clicked.connect(dlg.reject)
        
        def _confirm_clicked():
            try:
                result = self.crud.update_appointment(appointment_id, {"status": "canceled"})
                if result:
                    self._refreshAppointments()
                    QMessageBox.information(self, "Success", "Appointment canceled successfully!")
                    dlg.accept()
                else:
                    QMessageBox.warning(self, "Error", "Failed to cancel appointment.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to cancel appointment: {str(e)}")
        
        btn_confirm.clicked.connect(_confirm_clicked)
        
        btn_layout.addWidget(btn_cancel)
        btn_layout.addStretch(1)
        btn_layout.addWidget(btn_confirm)
        layout.addLayout(btn_layout)

        dlg.exec()

    def _populateAppointmentsTable(self):
        """Populate the appointments table with faculty appointments."""
        try:
            logging.debug(f"Populating appointments table for faculty_id: {self.faculty_id}")
            
            # Get appointments
            appointments = self.crud.get_faculty_appointments(self.faculty_id)
            logging.debug(f"Found {len(appointments)} appointments: {appointments}")
            
            if not appointments:
                logging.info("No appointments found")
                self.tableWidget_8.setRowCount(1)
                placeholder_item = QtWidgets.QTableWidgetItem("No appointments available")
                placeholder_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                placeholder_item.setFont(QtGui.QFont("Poppins", 12))
                self.tableWidget_8.setItem(0, 0, placeholder_item)
                self.tableWidget_8.setSpan(0, 0, 1, 6)
                return

            # Set up table - CLEAR ANY EXISTING DATA FIRST
            self.tableWidget_8.clearContents()
            self.tableWidget_8.setRowCount(len(appointments))
            
            status_colors = {
                "pending": "#F2994A",
                "rescheduled": "#2F80ED",
                "canceled": "#EB5757",
                "approved": "#219653",
                "denied": "#EB5757"
            }

            # Get additional data
            students = self.crud.list_students()
            entries = self.crud.entries_db.read_all()

            for row, appointment in enumerate(appointments):
                try:
                    logging.debug(f"Processing appointment {row}: {appointment}")

                    # Get student info
                    student = None
                    for s in students:
                        if s.get("id") == appointment.get("student_id"):
                            student = s
                            break

                    # Get schedule entry info
                    entry = None
                    for e in entries:
                        if e.get("id") == appointment.get("appointment_schedule_entry_id"):
                            entry = e
                            break

                    # Handle missing student or entry data
                    if student is None:
                        logging.warning(f"Student with ID {appointment.get('student_id')} not found.")
                        student_name = "Unknown Student"
                    else:
                        student_name = student.get("name", "Unknown")

                    if entry is None:
                        logging.warning(f"Entry with ID {appointment.get('appointment_schedule_entry_id')} not found.")
                        time_text = "Unknown Time"
                        slot_text = "Unknown Slot"
                    else:
                        time_text = f"{appointment.get('appointment_date', 'Unknown')} {entry.get('start_time', '')}"
                        slot_text = f"{entry.get('start_time', '')} - {entry.get('end_time', '')}"

                    status = appointment.get("status", "pending")

                    # Debug each column
                    logging.debug(f"Row {row}: Time={time_text}, Student={student_name}, Slot={slot_text}, Status={status}")

                    # Set items in table
                    time_item = QtWidgets.QTableWidgetItem(time_text)
                    student_item = QtWidgets.QTableWidgetItem(student_name)
                    slot_item = QtWidgets.QTableWidgetItem(slot_text)

                    self.tableWidget_8.setItem(row, 0, time_item)
                    self.tableWidget_8.setItem(row, 1, student_item)
                    self.tableWidget_8.setItem(row, 2, slot_item)
                    self.tableWidget_8.setCellWidget(row, 3, self._makePurposeViewCell(appointment["id"]))
                    self.tableWidget_8.setItem(row, 4, self._makeStatusItem(status.upper(), status_colors.get(status, "#333333")))
                    self.tableWidget_8.setCellWidget(row, 5, self._makeActionsCell(status, row, appointment["id"]))
                    self.tableWidget_8.setRowHeight(row, 60)

                    # Force update the table
                    self.tableWidget_8.viewport().update()

                except Exception as e:
                    logging.error(f"Error processing appointment row {row}: {str(e)}")
                    # Add error indicator to the table
                    error_item = QtWidgets.QTableWidgetItem(f"Error: {str(e)}")
                    self.tableWidget_8.setItem(row, 0, error_item)
                    continue
                    
            logging.debug("Successfully populated appointments table")
            self.tableWidget_8.setVisible(True)
            self.tableWidget_8.show()
            
            
        except Exception as e:
            logging.error(f"Error populating appointments table: {str(e)}")
            self.tableWidget_8.setRowCount(1)
            error_item = QtWidgets.QTableWidgetItem(f"Error loading appointments: {str(e)}")
            error_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            error_item.setFont(QtGui.QFont("Poppins", 10))
            self.tableWidget_8.setItem(0, 0, error_item)
            self.tableWidget_8.setSpan(0, 0, 1, 6)

    def retranslateUi(self):
        """Set UI text."""
        self.Academics_6.setText("Appointments")
        self.label_94.setText("My Appointments")
        self.pushButton_13.setText("Appointment Scheduler")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = AppointmentPage_ui("Kim", ["Faculty"], "Faculty", "token123")
    window.show()
    sys.exit(app.exec())