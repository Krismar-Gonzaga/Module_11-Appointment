from datetime import datetime
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QMessageBox
from .appointment_crud import appointment_crud

class AdminAppointmentPage_ui(QWidget):
    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self.appointment_crud = appointment_crud()
        self.rows = []  # Store appointment data
        self._setupAppointmentsPage()
        self._populateAppointmentsTable()  # Load initial data
        self.setFixedSize(1000, 550)
        # Set expanding size policy for the entire page
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )

    def _setupAppointmentsPage(self):
        self.setObjectName("Appointments_2")
        appointments_layout = QtWidgets.QVBoxLayout(self)
        appointments_layout.setContentsMargins(10, 10, 10, 10)
        appointments_layout.setSpacing(15)
        appointments_layout.setObjectName("appointments_layout")
        
        # Header section
        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(0)
        
        # Page title
        self.Academics_6 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        self.Academics_6.setFont(font)
        self.Academics_6.setStyleSheet("QLabel { color: #084924; }")
        self.Academics_6.setObjectName("Academics_6")
        
        header_layout.addWidget(self.Academics_6)
        header_layout.addStretch(1)
        
        appointments_layout.addWidget(header_widget)
        
        # Content widget
        self.widget_27 = QtWidgets.QWidget()
        self.widget_27.setMinimumHeight(100)
        self.widget_27.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.widget_27.setStyleSheet("""
            QWidget#widget_27 { 
                background-color: #FFFFFF; 
                border-radius: 20px;
                padding: 20px;
            }
        """)
        self.widget_27.setObjectName("widget_27")
        
        widget_layout = QtWidgets.QVBoxLayout(self.widget_27)
        widget_layout.setContentsMargins(10, 10, 10, 10)
        widget_layout.setSpacing(15)
        widget_layout.setObjectName("widget_layout")
        
        # Combined Filter and Search Section
        filter_search_widget = QtWidgets.QWidget()
        filter_search_widget.setFixedHeight(80)
        filter_search_widget.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        
        filter_search_layout = QtWidgets.QHBoxLayout(filter_search_widget)
        filter_search_layout.setContentsMargins(0, 10, 0, 10)
        filter_search_layout.setSpacing(20)
        
        # Date Filter Section
        filter_widget = QtWidgets.QWidget()
        filter_layout = QtWidgets.QHBoxLayout(filter_widget)
        filter_layout.setContentsMargins(0, 0, 0, 0)
        filter_layout.setSpacing(20)
        
        from_widget = QtWidgets.QWidget()
        from_layout = QtWidgets.QVBoxLayout(from_widget)
        from_layout.setContentsMargins(0, 0, 0, 0)
        from_layout.setSpacing(5)
        
        from_label = QtWidgets.QLabel("From")
        from_label.setStyleSheet("QLabel { color: #333333; font: 600 12pt 'Poppins'; }")
        from_layout.addWidget(from_label)
        
        self.from_date_edit = QtWidgets.QDateEdit()
        self.from_date_edit.setCalendarPopup(True)
        self.from_date_edit.setDate(QtCore.QDate.currentDate().addDays(-30))
        self.from_date_edit.setStyleSheet("""
            QDateEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 6px;
                padding: 8px 12px;
                font: 11pt 'Poppins';
                min-width: 120px;
            }
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: center right;
                width: 20px;
                border-left: 1px solid #dee2e6;
            }
        """)
        from_layout.addWidget(self.from_date_edit)
        
        to_widget = QtWidgets.QWidget()
        to_layout = QtWidgets.QVBoxLayout(to_widget)
        to_layout.setContentsMargins(0, 0, 0, 0)
        to_layout.setSpacing(5)
        
        to_label = QtWidgets.QLabel("To")
        to_label.setStyleSheet("QLabel { color: #333333; font: 600 12pt 'Poppins'; }")
        to_layout.addWidget(to_label)
        
        self.to_date_edit = QtWidgets.QDateEdit()
        self.to_date_edit.setCalendarPopup(True)
        self.to_date_edit.setDate(QtCore.QDate.currentDate())
        self.to_date_edit.setStyleSheet("""
            QDateEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 6px;
                padding: 8px 12px;
                font: 11pt 'Poppins';
                min-width: 120px;
            }
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: center right;
                width: 20px;
                border-left: 1px solid #dee2e6;
            }
        """)
        to_layout.addWidget(self.to_date_edit)
        
        self.filter_button = QtWidgets.QPushButton("Apply Filter")
        self.filter_button.setFixedSize(120, 40)
        self.filter_button.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 8px;
                font: 600 11pt 'Poppins';
                margin-top: 18px;
            }
            QPushButton:hover {
                background-color: #0a5a2f;
            }
        """)
        self.filter_button.clicked.connect(self.apply_date_filter)
        
        self.clear_filter_button = QtWidgets.QPushButton("Clear")
        self.clear_filter_button.setFixedSize(80, 40)
        self.clear_filter_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 8px;
                font: 600 11pt 'Poppins';
                margin-top: 18px;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        self.clear_filter_button.clicked.connect(self.clear_filters)
        
        filter_layout.addWidget(from_widget)
        filter_layout.addWidget(to_widget)
        filter_layout.addWidget(self.filter_button)
        filter_layout.addWidget(self.clear_filter_button)
        
        search_widget = QtWidgets.QWidget()
        search_layout = QtWidgets.QHBoxLayout(search_widget)
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(15)
        
        search_label = QtWidgets.QLabel("Search:")
        search_label.setStyleSheet("QLabel { color: #333333; font: 600 12pt 'Poppins'; margin-left: 5px; }")
        search_layout.addWidget(search_label)
        
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setPlaceholderText("Search appointments...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 10px 15px;
                font: 11pt 'Poppins';
                min-width: 300px;
            }
            QLineEdit:focus {
                border-color: #084924;
                background-color: #ffffff;
            }
        """)
        self.search_input.textChanged.connect(self.apply_search_filter)
        search_layout.addWidget(self.search_input)
        
        filter_search_layout.addWidget(filter_widget)
        filter_search_layout.addStretch(1)
        filter_search_layout.addWidget(search_widget)
        
        widget_layout.addWidget(filter_search_widget)
        
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        separator.setStyleSheet("QFrame { background-color: #e0e0e0; margin: 5px 0; }")
        separator.setFixedHeight(1)
        widget_layout.addWidget(separator)
        
        # Appointments table
        self.tableWidget_8 = QtWidgets.QTableWidget()
        self.tableWidget_8.setAlternatingRowColors(True)
        self.tableWidget_8.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_8.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_8.setShowGrid(False)
        self.tableWidget_8.verticalHeader().setVisible(False)
        self.tableWidget_8.horizontalHeader().setVisible(True)
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.setColumnCount(6)  # Removed Actions column
        
        self.tableWidget_8.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.tableWidget_8.setMinimumHeight(100)
        
        header = self.tableWidget_8.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.Stretch)
       
        self.tableWidget_8.setColumnWidth(0, 220)
        self.tableWidget_8.setColumnWidth(1, 200)
        self.tableWidget_8.setColumnWidth(2, 200)
        self.tableWidget_8.setColumnWidth(4, 170)
        self.tableWidget_8.setColumnWidth(5, 170)
        self.tableWidget_8.setFixedWidth(950)
        self.tableWidget_8.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget_8.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #0a5a2f;
                color: white;
                padding: 12px 8px;
                border: 0px;
                font: 600 11pt "Poppins";
                text-align: left;
            }
        """)
        self.tableWidget_8.setStyleSheet("""
            QTableWidget {
                background: white;
                gridline-color: transparent;
                border: none;
                font: 10pt "Poppins";
                selection-background-color: #e8f5e8;
            }
            QTableWidget::item { 
                padding: 10px 8px;
                border-bottom: 1px solid #f0f0f0;
            }
        """)
        
        self.tableWidget_8.setWordWrap(True)
        self.tableWidget_8.verticalHeader().setDefaultSectionSize(60)
        
        headers = ["Time", "Faculty", "Student", "Purpose", "Slot", "Status"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setFamily("Poppins")
            font.setPointSize(11)
            item.setFont(font)
            item.setText(header)
            self.tableWidget_8.setHorizontalHeaderItem(i, item)
        
        widget_layout.addWidget(self.tableWidget_8, 1)
        appointments_layout.addWidget(self.widget_27, 1)

    def apply_search_filter(self, search_text):
        """Apply search filter to the appointments table"""
        if not search_text.strip():
            self._updateTableWithData(self.rows)
            return
        
        search_text_lower = search_text.lower().strip()
        filtered_appointments = []
        
        for appointment in self.rows:
            time_text, faculty, student, purpose, slot, status = appointment
            if (search_text_lower in faculty.lower() or 
                search_text_lower in student.lower() or 
                search_text_lower in slot.lower() or 
                search_text_lower in status.lower() or
                search_text_lower in time_text.lower() or
                search_text_lower in purpose.lower()):
                filtered_appointments.append(appointment)
        
        self._updateTableWithData(filtered_appointments)
        if search_text.strip():
            self._showFilterStatus(len(filtered_appointments), len(self.rows), f"Search: '{search_text}'")

    def apply_date_filter(self):
        """Apply date filter to the appointments table"""
        from_date = self.from_date_edit.date()
        to_date = self.to_date_edit.date()
        
        if from_date > to_date:
            QtWidgets.QMessageBox.warning(self, "Invalid Date Range", 
                                        "From date cannot be after To date.")
            return
        
        search_text = self.search_input.text().strip()
        date_filtered_appointments = []
        for appointment in self.rows:
            appointment_date_str = appointment[0].split()[0]
            appointment_date = QtCore.QDate.fromString(appointment_date_str, "yyyy-MM-dd")
            if from_date <= appointment_date <= to_date:
                date_filtered_appointments.append(appointment)
        
        if search_text:
            search_text_lower = search_text.lower()
            final_filtered_appointments = []
            for appointment in date_filtered_appointments:
                time_text, faculty, student, purpose, slot, status = appointment
                if (search_text_lower in faculty.lower() or 
                    search_text_lower in student.lower() or 
                    search_text_lower in slot.lower() or 
                    search_text_lower in status.lower() or
                    scroll_text_lower in time_text.lower() or
                    search_text_lower in purpose.lower()):
                    final_filtered_appointments.append(appointment)
        else:
            final_filtered_appointments = date_filtered_appointments
        
        self._updateTableWithData(final_filtered_appointments)
        
        filter_info = f"Date: {from_date.toString('MM/dd/yyyy')} - {to_date.toString('MM/dd/yyyy')}"
        if search_text:
            filter_info += f" | Search: '{search_text}'"
        self._showFilterStatus(len(final_filtered_appointments), len(self.rows), filter_info)

    def clear_filters(self):
        """Clear all filters and show all appointments"""
        self.search_input.clear()
        self.from_date_edit.setDate(QtCore.QDate.currentDate().addDays(-30))
        self.to_date_edit.setDate(QtCore.QDate.currentDate())
        self._updateTableWithData(self.rows)
        self._showFilterStatus(len(self.rows), len(self.rows), "All filters cleared")

    def _showFilterStatus(self, showing_count, total_count, filter_info=""):
        """Show filter status message"""
        if showing_count == total_count:
            status_message = f"Showing all {total_count} appointments"
        else:
            status_message = f"Showing {showing_count} of {total_count} appointments"
        
        if filter_info:
            status_message += f" | {filter_info}"
        print(status_message)

    def _updateTableWithData(self, appointments_data):
        """Update table with provided appointments data"""
        status_colors = {
            "PENDING": "#F2994A",
            "CANCELED": "#EB5757",
            "APPROVED": "#219653",
            "DENIED": "#EB5757",
        }
        
        self.tableWidget_8.setRowCount(len(appointments_data))
        for r, (time_text, faculty, student, purpose, slot, status) in enumerate(appointments_data):
            self.tableWidget_8.setItem(r, 0, QtWidgets.QTableWidgetItem(time_text))
            self.tableWidget_8.setItem(r, 1, QtWidgets.QTableWidgetItem(faculty))
            self.tableWidget_8.setItem(r, 2, QtWidgets.QTableWidgetItem(student))
            self.tableWidget_8.setCellWidget(r, 3, self._makePurposeViewCell(purpose))
            self.tableWidget_8.setItem(r, 4, QtWidgets.QTableWidgetItem(slot))
            self.tableWidget_8.setItem(r, 5, self._makeStatusItem(status, status_colors.get(status, "#333333")))
            self.tableWidget_8.setRowHeight(r, 60)

    def _populateAppointmentsTable(self):
        """Populate the table with appointment data from database"""
        try:
            appointments = self.appointment_crud.appointments_db.read_all()
            faculties = {f['id']: f['name'] for f in self.appointment_crud.list_faculty()}
            students = {s['id']: s['name'] for s in self.appointment_crud.list_students()}
            entries = self.appointment_crud.entries_db.read_all()
            blocks = self.appointment_crud.blocks_db.read_all()
            
            self.rows = []
            for appt in appointments:
                if 'appointment_schedule_entry_id' not in appt:
                    continue
                
                entry = next((e for e in entries if e['id'] == appt['appointment_schedule_entry_id']), None)
                if not entry:
                    continue
                
                block = next((b for b in blocks if b['id'] == entry['schedule_block_entry_id']), None)
                if not block:
                    continue
                
                faculty_id = block.get('faculty_id', 0)
                faculty_name = faculties.get(faculty_id, 'Unknown')
                student_name = students.get(appt.get('student_id', 0), 'Unknown')
                slot = f"{entry['day_of_week']} {entry['start_time']} - {entry['end_time']}"
                time_text = f"{appt['appointment_date']} {entry['start_time']}"
                
                self.rows.append((
                    time_text,
                    faculty_name,
                    student_name,
                    appt.get('additional_details', 'N/A'),
                    slot,
                    appt.get('status', 'Unknown').upper()
                ))
            
            self.all_appointments = self.rows.copy()
            self._updateTableWithData(self.rows)
        
        except Exception as e:
            print(f"Error loading appointments data: {e}")
            QMessageBox.warning(self, "Error", f"Failed to load appointments: {str(e)}")
            

    def resizeEvent(self, event):
        """Handle window resize to adjust layout and table"""
        super().resizeEvent(event)
        window_width = self.width()
        available_width = window_width - 80
        
        if available_width > 1200:
            self.tableWidget_8.setColumnWidth(0, 220)
            self.tableWidget_8.setColumnWidth(1, 200)
            self.tableWidget_8.setColumnWidth(2, 200)
            self.tableWidget_8.setColumnWidth(4, 150)
            self.tableWidget_8.setColumnWidth(5, 140)
        elif available_width > 900:
            self.tableWidget_8.setColumnWidth(0, 180)
            self.tableWidget_8.setColumnWidth(1, 160)
            self.tableWidget_8.setColumnWidth(2, 160)
            self.tableWidget_8.setColumnWidth(4, 130)
            self.tableWidget_8.setColumnWidth(5, 120)
        elif available_width > 600:
            self.tableWidget_8.setColumnWidth(0, 150)
            self.tableWidget_8.setColumnWidth(1, 130)
            self.tableWidget_8.setColumnWidth(2, 130)
            self.tableWidget_8.setColumnWidth(4, 110)
            self.tableWidget_8.setColumnWidth(5, 100)
        else:
            self.tableWidget_8.setColumnWidth(0, 120)
            self.tableWidget_8.setColumnWidth(1, 100)
            self.tableWidget_8.setColumnWidth(2, 100)
            self.tableWidget_8.setColumnWidth(4, 90)
            self.tableWidget_8.setColumnWidth(5, 80)
        
        available_height = self.height() - 200
        self.tableWidget_8.setMinimumHeight(max(300, available_height))
        self.tableWidget_8.resizeColumnsToContents()

    def _makeStatusItem(self, text, color_hex):
        """Create a styled status table item"""
        item = QtWidgets.QTableWidgetItem(text)
        brush = QtGui.QBrush(QtGui.QColor(color_hex))
        item.setForeground(brush)
        item.setFont(QtGui.QFont("Poppins", 10, QtGui.QFont.Weight.DemiBold))
        return item

    def _makePurposeViewCell(self, purpose_text):
        """Create a clickable 'View' link for the purpose column"""
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        link = QtWidgets.QLabel("View", parent=container)
        
        def showPurposeDetails(event):
            self._showPurposeDetailsDialog(purpose_text)
        
        link.mousePressEvent = showPurposeDetails
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        link.setFont(font)
        link.setStyleSheet("QLabel { color: #2F80ED; text-decoration: underline; }")
        link.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        layout.addWidget(link, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        return container

    def _showPurposeDetailsDialog(self, purpose_text):
        """Show dialog with purpose details and appointment info"""
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Appointment Details")
        dialog.setModal(True)
        dialog.setFixedSize(550, 600)
        dialog.setStyleSheet("QDialog { background-color: white; border-radius: 12px; }")
        
        main_layout = QtWidgets.QVBoxLayout(dialog)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Create scroll area for all content except OK button
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea { border: none; background: transparent; }
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
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }
        """)
        
        # Container widget for scrollable content
        content_widget = QtWidgets.QWidget()
        content_layout = QtWidgets.QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(20)
        
        # Header section
        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        icon_label = QtWidgets.QLabel()
        icon_label.setFixedSize(32, 32)
        icon_label.setStyleSheet("QLabel { background-color: #084924; border-radius: 8px; }")
        
        title_label = QtWidgets.QLabel("Appointment Purpose")
        title_label.setStyleSheet("QLabel { color: #084924; font: 600 20pt 'Poppins'; background: transparent; }")
        header_layout.addWidget(icon_label)
        header_layout.addSpacing(12)
        header_layout.addWidget(title_label)
        header_layout.addStretch(1)
        content_layout.addWidget(header_widget)
        
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        separator.setStyleSheet("QFrame { background-color: #e0e0e0; }")
        separator.setFixedHeight(1)
        content_layout.addWidget(separator)
        
        # Appointment Information section
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
                padding: 0 8px 0 8px;
            }
        """)
        
        info_layout = QtWidgets.QFormLayout(info_group)
        info_layout.setVerticalSpacing(8)
        info_layout.setHorizontalSpacing(20)
        
        selected_row = self.tableWidget_8.currentRow()
        if selected_row >= 0 and selected_row < len(self.rows):
            time_text, faculty, student, purpose, slot, status = self.rows[selected_row]
            appointment_data = [
                ("Student:", student),
                ("Faculty:", faculty),
                ("Date & Time:", time_text),
                ("Duration:", "30 minutes"),
                ("Status:", status),
                ("Mode:", "Online"),
                ("Meeting Link:", "https://meet.google.com/xyz-abc-def"),
                ("Contact Email:", "contact@university.edu")
            ]
        else:
            appointment_data = [
                ("Student:", "Unknown"),
                ("Faculty:", "Unknown"),
                ("Date & Time:", "Unknown"),
                ("Duration:", "Unknown"),
                ("Status:", "Unknown"),
                ("Mode:", "Unknown"),
                ("Meeting Link:", "Unknown"),
                ("Contact Email:", "Unknown")
            ]
        
        for label, value in appointment_data:
            label_widget = QtWidgets.QLabel(label)
            label_widget.setStyleSheet("QLabel { font: 600 11pt 'Poppins'; color: #333; }")
            value_widget = QtWidgets.QLabel(value)
            value_widget.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #666; }")
            info_layout.addRow(label_widget, value_widget)
        
        content_layout.addWidget(info_group)
        
        # Purpose Details section
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
                padding: 0 8px 0 8px;
            }
        """)
        
        purpose_layout = QtWidgets.QVBoxLayout(purpose_group)
        purpose_label = QtWidgets.QLabel(purpose_text or "No purpose provided")
        purpose_label.setWordWrap(True)
        purpose_label.setStyleSheet("QLabel { color: #2b2b2b; font: 11pt 'Poppins'; background: transparent; line-height: 1.5; }")
        purpose_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        
        purpose_scroll_area = QtWidgets.QScrollArea()
        purpose_scroll_area.setWidgetResizable(True)
        purpose_scroll_area.setStyleSheet("""
            QScrollArea { border: none; background: transparent; }
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
        purpose_scroll_area.setWidget(purpose_label)
        purpose_layout.addWidget(purpose_scroll_area, 1)
        content_layout.addWidget(purpose_group, 1)
        
        # Supporting Documents section
        image_group = QtWidgets.QGroupBox("Supporting Documents")
        image_group.setStyleSheet("""
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
        
        image_layout = QtWidgets.QVBoxLayout(image_group)
        image_display = QtWidgets.QLabel()
        image_display.setFixedSize(400, 200)
        image_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        image_display.setText("No image available")
        image_display.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 2px dashed #dee2e6;
                border-radius: 8px;
                color: #6c757d;
                font: 10pt 'Poppins';
            }
        """)
        image_layout.addWidget(image_display)
        content_layout.addWidget(image_group)
        
        # Set the content widget as the scroll area's widget
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area, 1)
        
        # OK button (outside scroll area)
        ok_button = QtWidgets.QPushButton("OK")
        ok_button.setFixedSize(120, 40)
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
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(ok_button)
        main_layout.addLayout(button_layout)
        
        dialog.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_appointment = AdminAppointmentPage_ui(
        "admin@university.edu",
        ["admin"],
        "admin",
        "sample_token"
    )
    admin_appointment.show()
    sys.exit(app.exec())