from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QMessageBox
from datetime import datetime


class AdminAppointmentPage_ui(QWidget):
    go_to_AppointmentSchedulerPage = QtCore.pyqtSignal()
    go_to_AppointmentReschedulePage = QtCore.pyqtSignal()
    

    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)

        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self._setupAppointmentsPage()
        self.retranslateUi()
        
        # Set expanding size policy for the entire page
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )

    def _setupAppointmentsPage(self):
        self.setObjectName("Appointments_2")
        # Main layout for appointments page
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
        self.Academics_6.setText("Appointments")
        
        # Spacer
        header_layout.addWidget(self.Academics_6)
        header_layout.addStretch(1)

        # Back button
        self.backButton_8 = QtWidgets.QLabel()
        self.backButton_8.setFixedSize(40, 40)
        self.backButton_8.setText("Back")
        self.backButton_8.setPixmap(QtGui.QPixmap(":/assets/back_button.png"))
        self.backButton_8.setScaledContents(True)
        self.backButton_8.setObjectName("backButton_8")
        
        header_layout.addWidget(self.backButton_8)
        
        appointments_layout.addWidget(header_widget)
        
        # Content widget - IMPROVED RESPONSIVENESS
        self.widget_27 = QtWidgets.QWidget()
        # Remove fixed height and maximum width constraints
        self.widget_27.setMinimumHeight(100)  # Reasonable minimum height
        self.widget_27.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Expanding  # Changed from Fixed to Expanding
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
        
        # REMOVED: Section header with "My Appointments" title and Appointment Scheduler button
        
        # ADDED: Combined Filter and Search Section
        filter_search_widget = QtWidgets.QWidget()
        filter_search_widget.setFixedHeight(80)
        filter_search_widget.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Fixed
        )
        
        filter_search_layout = QtWidgets.QHBoxLayout(filter_search_widget)
        filter_search_layout.setContentsMargins(0, 10, 0, 10)
        filter_search_layout.setSpacing(20)
        
        # Date Filter Section - LEFT SIDE
        filter_widget = QtWidgets.QWidget()
        filter_layout = QtWidgets.QHBoxLayout(filter_widget)
        filter_layout.setContentsMargins(0, 0, 0, 0)
        filter_layout.setSpacing(20)
        
        # From Date section
        from_widget = QtWidgets.QWidget()
        from_layout = QtWidgets.QVBoxLayout(from_widget)
        from_layout.setContentsMargins(0, 0, 0, 0)
        from_layout.setSpacing(5)
        
        from_label = QtWidgets.QLabel("From")
        from_label.setStyleSheet("""
            QLabel {
                color: #333333;
                font: 600 12pt 'Poppins';
            }
        """)
        from_layout.addWidget(from_label)
        
        self.from_date_edit = QtWidgets.QDateEdit()
        self.from_date_edit.setCalendarPopup(True)
        self.from_date_edit.setDate(QtCore.QDate.currentDate().addDays(-30))  # Default to 30 days ago
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
        
        # To Date section
        to_widget = QtWidgets.QWidget()
        to_layout = QtWidgets.QVBoxLayout(to_widget)
        to_layout.setContentsMargins(0, 0, 0, 0)
        to_layout.setSpacing(5)
        
        to_label = QtWidgets.QLabel("To")
        to_label.setStyleSheet("""
            QLabel {
                color: #333333;
                font: 600 12pt 'Poppins';
            }
        """)
        to_layout.addWidget(to_label)
        
        self.to_date_edit = QtWidgets.QDateEdit()
        self.to_date_edit.setCalendarPopup(True)
        self.to_date_edit.setDate(QtCore.QDate.currentDate())  # Default to today
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
        
        # Filter button
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
            QPushButton:pressed {
                background-color: #06381c;
            }
        """)
        self.filter_button.clicked.connect(self.apply_date_filter)
        
        # Clear filter button
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
            QPushButton:pressed {
                background-color: #545b62;
            }
        """)
        self.clear_filter_button.clicked.connect(self.clear_filters)
        
        filter_layout.addWidget(from_widget)
        filter_layout.addWidget(to_widget)
        filter_layout.addWidget(self.filter_button)
        filter_layout.addWidget(self.clear_filter_button)
        
        # Search Bar Section - RIGHT SIDE
        search_widget = QtWidgets.QWidget()
        search_layout = QtWidgets.QHBoxLayout(search_widget)
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(15)
        
        # Search label
        search_label = QtWidgets.QLabel("Search:")
        search_label.setStyleSheet("""
            QLabel {
                color: #333333;
                font: 600 12pt 'Poppins';
                margin-left: 5px;
            }
        """)
        search_layout.addWidget(search_label)
        
        # Search input field
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
            QLineEdit::placeholder {
                color: #6c757d;
                font-style: italic;
            }
        """)
        self.search_input.textChanged.connect(self.apply_search_filter)
        search_layout.addWidget(self.search_input)
        
        # Add both filter and search to the main filter_search_layout
        filter_search_layout.addWidget(filter_widget)
        filter_search_layout.addStretch(1)  # Push search to the right
        filter_search_layout.addWidget(search_widget)
        
        widget_layout.addWidget(filter_search_widget)
        
        # ADDED: Separator line
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
        self.tableWidget_8.setRowCount(6)
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(6)
        
        # Set expanding size policy for table
        self.tableWidget_8.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        
        # Set minimum height for table
        self.tableWidget_8.setMinimumHeight(200)
        
        # IMPROVED RESPONSIVE COLUMN RESIZING
        header = self.tableWidget_8.horizontalHeader()
        try:
            # More flexible column resizing strategy
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Interactive)  # Time - adjustable
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Interactive)  # Faculty - adjustable
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Interactive)  # Student - adjustable
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)      # Purpose - takes remaining space
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Interactive)  # Slot - adjustable
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)  # Status - fit content
            
            # Set stretch last section to false for better control
            header.setStretchLastSection(False)
        except:
            # Fallback for older PyQt versions
            header.setResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)
            header.setResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Interactive)
            header.setResizeMode(5, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        
        # Set initial column widths with better proportions
        self.tableWidget_8.setColumnWidth(0, 200)  # Time
        self.tableWidget_8.setColumnWidth(1, 180)  # Faculty
        self.tableWidget_8.setColumnWidth(2, 180)  # Student
        self.tableWidget_8.setColumnWidth(4, 150)  # Slot
        self.tableWidget_8.setColumnWidth(5, 120)  # Status
        # Column 3 (Purpose) will stretch automatically
                
        # Header styling
        self.tableWidget_8.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget_8.horizontalHeader().setStyleSheet(
            """
            QHeaderView::section {
                background-color: #0a5a2f;
                color: white;
                padding: 12px 8px;
                border: 0px;
                font: 600 11pt "Poppins";
                text-align: left;
            }
            QTableCornerButton::section { background-color: #0a5a2f; border: 0px; }
            """
        )
        self.tableWidget_8.setStyleSheet(
            """
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
            QTableWidget::item:selected {
                background-color: #e8f5e8;
            }
            """
        )
        
        # Enable word wrap for better text display
        self.tableWidget_8.setWordWrap(True)
        
        # Set reasonable row height
        self.tableWidget_8.verticalHeader().setDefaultSectionSize(60)
        
        # Table header - UPDATED COLUMN ORDER
        headers = ["Time", "Faculty", "Student", "Purpose", "Slot", "Status"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setFamily("Poppins")
            font.setPointSize(11)
            item.setFont(font)
            self.tableWidget_8.setHorizontalHeaderItem(i, item)
        
        widget_layout.addWidget(self.tableWidget_8, 1)
        
        appointments_layout.addWidget(self.widget_27, 1)
        
        # Store all appointments data for filtering
        self.all_appointments = []
        
        # Populate initial rows
        self._populateAppointmentsTable()

    def apply_search_filter(self, search_text):
        """Apply search filter to the appointments table"""
        if not search_text.strip():
            # If search is empty, show all appointments
            self._updateTableWithData(self.all_appointments)
            return
        
        search_text_lower = search_text.lower().strip()
        filtered_appointments = []
        
        for appointment in self.all_appointments:
            # Search in faculty, student, purpose, slot, and status
            time_text, faculty, student, _purpose, slot, status = appointment
            
            # Check if search text exists in any of the fields
            if (search_text_lower in faculty.lower() or 
                search_text_lower in student.lower() or 
                search_text_lower in slot.lower() or 
                search_text_lower in status.lower() or
                search_text_lower in time_text.lower()):
                filtered_appointments.append(appointment)
        
        # Update table with filtered data
        self._updateTableWithData(filtered_appointments)
        
        # Show search status
        if search_text.strip():
            self._showFilterStatus(len(filtered_appointments), len(self.all_appointments), f"Search: '{search_text}'")

    def apply_date_filter(self):
        """Apply date filter to the appointments table"""
        from_date = self.from_date_edit.date()
        to_date = self.to_date_edit.date()
        
        # Validate date range
        if from_date > to_date:
            QtWidgets.QMessageBox.warning(self, "Invalid Date Range", 
                                        "From date cannot be after To date.")
            return
        
        # Get current search text
        search_text = self.search_input.text().strip()
        
        # First filter by date
        date_filtered_appointments = []
        for appointment in self.all_appointments:
            appointment_date_str = appointment[0].split()[0]  # Get date part from timestamp
            appointment_date = QtCore.QDate.fromString(appointment_date_str, "yyyy-MM-dd")
            if from_date <= appointment_date <= to_date:
                date_filtered_appointments.append(appointment)
        
        # Then apply search filter if there's search text
        if search_text:
            search_text_lower = search_text.lower()
            final_filtered_appointments = []
            for appointment in date_filtered_appointments:
                time_text, faculty, student, _purpose, slot, status = appointment
                if (search_text_lower in faculty.lower() or 
                    search_text_lower in student.lower() or 
                    search_text_lower in slot.lower() or 
                    search_text_lower in status.lower() or
                    search_text_lower in time_text.lower()):
                    final_filtered_appointments.append(appointment)
        else:
            final_filtered_appointments = date_filtered_appointments
        
        # Update table with filtered data
        self._updateTableWithData(final_filtered_appointments)
        
        # Show filter status
        filter_info = f"Date: {from_date.toString('MM/dd/yyyy')} - {to_date.toString('MM/dd/yyyy')}"
        if search_text:
            filter_info += f" | Search: '{search_text}'"
        self._showFilterStatus(len(final_filtered_appointments), len(self.all_appointments), filter_info)

    def clear_filters(self):
        """Clear all filters (search and date) and show all appointments"""
        self.search_input.clear()
        self.from_date_edit.setDate(QtCore.QDate.currentDate().addDays(-30))
        self.to_date_edit.setDate(QtCore.QDate.currentDate())
        self._updateTableWithData(self.all_appointments)
        self._showFilterStatus(len(self.all_appointments), len(self.all_appointments), "All filters cleared")

    def _showFilterStatus(self, showing_count, total_count, filter_info=""):
        """Show filter status message"""
        if showing_count == total_count:
            status_message = f"Showing all {total_count} appointments"
        else:
            status_message = f"Showing {showing_count} of {total_count} appointments"
        
        if filter_info:
            status_message += f" | {filter_info}"
        
        # You can show this in a status bar or as a temporary message
        print(status_message)  # For now, just print to console
        # Alternatively, you can show a QMessageBox or update a status label

    def _updateTableWithData(self, appointments_data):
        """Update table with provided appointments data"""
        status_colors = {
            "PENDING": "#F2994A",
            "RESCHEDULED": "#2F80ED",
            "CANCELED": "#EB5757",
            "APPROVED": "#219653",
        }
        
        self.tableWidget_8.setRowCount(len(appointments_data))
        for r, (time_text, faculty, student, _purpose, slot, status) in enumerate(appointments_data):
            # Time
            self.tableWidget_8.setItem(r, 0, QtWidgets.QTableWidgetItem(time_text))
            # Faculty
            self.tableWidget_8.setItem(r, 1, QtWidgets.QTableWidgetItem(faculty))
            # Student
            self.tableWidget_8.setItem(r, 2, QtWidgets.QTableWidgetItem(student))
            # Purpose (View link)
            self.tableWidget_8.setCellWidget(r, 3, self._makePurposeViewCell())
            # Slot
            self.tableWidget_8.setItem(r, 4, QtWidgets.QTableWidgetItem(slot))
            # Status colored
            self.tableWidget_8.setItem(r, 5, self._makeStatusItem(status, status_colors.get(status, "#333333")))
            self.tableWidget_8.setRowHeight(r, 60)

    def _populateAppointmentsTable(self):
        """Populate the table with sample appointment data"""
        rows = [
            ("2025-08-21 09:00:00", "Sir. John Doe", "Shapi Dot Com", "View", "2025-08-21 09:00 - 9:30", "PENDING"),
            ("2025-08-21 09:30:00", "Sir. John Doe", "Shapi Dot Com", "View", "2025-08-21 09:30 - 10:00", "RESCHEDULED"),
            ("2025-08-21 10:00:00", "Sir. John Doe", "Shapi Dot Com", "View", "2025-08-21 10:00 - 10:30", "CANCELED"),
            ("2025-08-21 10:30:00", "Sir. John Doe", "Shapi Dot Com", "View", "2025-08-21 10:30 - 11:00", "APPROVED"),
            ("2025-08-21 11:00:00", "Sir. John Doe", "Shapi Dot Com", "View", "2025-08-21 11:00 - 11:30", "PENDING"),
            ("2025-08-21 11:30:00", "Sir. John Doe", "Jane Smith", "View", "2025-08-21 11:30 - 12:00", "PENDING"),
            ("2025-09-01 14:00:00", "Dr. Alice Brown", "Mike Johnson", "View", "2025-09-01 14:00 - 14:30", "APPROVED"),
            ("2025-09-15 10:00:00", "Prof. Carol White", "Sarah Davis", "View", "2025-09-15 10:00 - 10:30", "PENDING"),
            ("2025-09-20 13:00:00", "Sir. John Doe", "Robert Wilson", "View", "2025-09-20 13:00 - 13:30", "RESCHEDULED"),
            ("2025-09-25 15:00:00", "Dr. Alice Brown", "Emily Chen", "View", "2025-09-25 15:00 - 15:30", "APPROVED"),
        ]
        
        # Store all appointments for filtering
        self.all_appointments = rows.copy()
        
        # Display all appointments initially
        self._updateTableWithData(rows)

    def resizeEvent(self, event):
        """Handle window resize to adjust layout and table appropriately"""
        super().resizeEvent(event)
        
        # Get current window size
        window_width = self.width()
        window_height = self.height()
        
        # Adjust table and layout based on window size
        if hasattr(self, 'tableWidget_8') and hasattr(self, 'widget_27'):
            
            # Calculate available width for table (accounting for margins)
            available_width = window_width - 80  # Account for main layout margins
            
            # Dynamic column adjustment based on available width
            if available_width > 1200:  # Large window
                self.tableWidget_8.setColumnWidth(0, 220)  # Time
                self.tableWidget_8.setColumnWidth(1, 200)  # Faculty
                self.tableWidget_8.setColumnWidth(2, 200)  # Student
                self.tableWidget_8.setColumnWidth(4, 150)  # Slot
                self.tableWidget_8.setColumnWidth(5, 140)  # Status
                
            elif available_width > 900:  # Medium window
                self.tableWidget_8.setColumnWidth(0, 180)  # Time
                self.tableWidget_8.setColumnWidth(1, 160)  # Faculty
                self.tableWidget_8.setColumnWidth(2, 160)  # Student
                self.tableWidget_8.setColumnWidth(3, 100)  # Purpose
                self.tableWidget_8.setColumnWidth(4, 130)  # Slot
                self.tableWidget_8.setColumnWidth(5, 120)  # Status
                
            elif available_width > 600:  # Small window
                self.tableWidget_8.setColumnWidth(0, 150)  # Time
                self.tableWidget_8.setColumnWidth(1, 130)  # Faculty
                self.tableWidget_8.setColumnWidth(2, 130)  # Student
                self.tableWidget_8.setColumnWidth(3, 100)  # Purpose
                self.tableWidget_8.setColumnWidth(4, 110)  # Slot
                self.tableWidget_8.setColumnWidth(5, 100)  # Status
                
            else:  # Very small window
                self.tableWidget_8.setColumnWidth(0, 120)  # Time
                self.tableWidget_8.setColumnWidth(1, 100)  # Faculty
                self.tableWidget_8.setColumnWidth(2, 100)  # Student
                self.tableWidget_8.setColumnWidth(3, 100)  # Purpose
                self.tableWidget_8.setColumnWidth(4, 90)   # Slot
                self.tableWidget_8.setColumnWidth(5, 80)   # Status
            
            # Adjust table height based on available height
            available_height = window_height - 200  # Account for headers and margins
            if available_height > 400:
                self.tableWidget_8.setMinimumHeight(400)
            else:
                self.tableWidget_8.setMinimumHeight(max(300, available_height))
            
            # Force update of the table view
            self.tableWidget_8.resizeColumnsToContents()
            self.tableWidget_8.updateGeometry()

    def _setupBackButton(self):
        # Back button (using QPushButton for click support)
        self.backButton_9 = QtWidgets.QPushButton(self)
        self.backButton_9.setFixedSize(40, 40)
        self.backButton_9.setStyleSheet("border: none; background: transparent;")
        self.backButton_9.setIcon(QtGui.QIcon(":/assets/back_button.png"))
        self.backButton_9.setIconSize(QtCore.QSize(40, 40))
        self.backButton_9.setObjectName("backButton_9")
        
        # Connect back button to navigation
        self.backButton_9.clicked.connect(self.goBackPage)
   
    def goBackPage(self):
        if self.currentPage > 0:
            self.currentPage -= 1
            self.stackedWidget.setCurrentIndex(self.currentPage)

    def _makeStatusItem(self, text, color_hex):
        item = QtWidgets.QTableWidgetItem(text)
        brush = QtGui.QBrush(QtGui.QColor(color_hex))
        item.setForeground(brush)
        item.setFont(QtGui.QFont("Poppins", 10, QtGui.QFont.Weight.DemiBold))
        return item

    def _makePurposeViewCell(self):
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        link = QtWidgets.QLabel("View", parent=container)
        
        # Connect the click event to show purpose details dialog
        def showPurposeDetails(event):
            self._showPurposeDetailsDialog()
        
        link.mousePressEvent = showPurposeDetails
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        link.setFont(font)
        link.setStyleSheet("QLabel { color: #2F80ED; text-decoration: underline; }")
        link.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        layout.addWidget(link, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        return container

    def _showPurposeDetailsDialog(self):
        """Show an enhanced dialog with purpose details and appointment info"""
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Appointment Details")
        dialog.setModal(True)
        dialog.setFixedSize(550, 600)
        dialog.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 12px;
            }
        """)
        
        # Main layout for the dialog
        main_layout = QtWidgets.QVBoxLayout(dialog)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create scroll area
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background: white;
            }
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
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)
        
        # Create scroll content widget
        scroll_content = QtWidgets.QWidget()
        scroll_content.setStyleSheet("QWidget { background: white; }")
        
        # Main content layout for scroll area
        content_layout = QtWidgets.QVBoxLayout(scroll_content)
        content_layout.setContentsMargins(10, 10, 10, 10)
        content_layout.setSpacing(20)
        
        # Header with icon and title
        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        # Icon
        icon_label = QtWidgets.QLabel()
        icon_label.setFixedSize(32, 32)
        icon_label.setStyleSheet("QLabel { background-color: #084924; border-radius: 8px; }")
        icon_label.setScaledContents(True)
        
        # Title
        title_label = QtWidgets.QLabel("Appointment Purpose")
        title_label.setStyleSheet("""
            QLabel {
                color: #084924;
                font: 600 20pt 'Poppins';
                background: transparent;
            }
        """)
        
        header_layout.addWidget(icon_label)
        header_layout.addSpacing(12)
        header_layout.addWidget(title_label)
        header_layout.addStretch(1)
        
        content_layout.addWidget(header_widget)
        
        # Separator
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        separator.setStyleSheet("QFrame { background-color: #e0e0e0; }")
        separator.setFixedHeight(1)
        content_layout.addWidget(separator)
        
        # Appointment info section
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
        
        # Sample appointment data
        appointment_data = [
            ("Student:", "Shapi Dot Com"),
            ("Faculty:", "Sir. John Doe"),
            ("Date & Time:", "2025-08-21 09:00 AM"),
            ("Duration:", "30 minutes"),
            ("Status:", "Pending"),
            ("Mode:", "Online"),
            ("Meeting Link:", "https://meet.google.com/xyz-abc-def"),
            ("Contact Email:", "shapi@example.com")
        ]
        
        for label, value in appointment_data:
            label_widget = QtWidgets.QLabel(label)
            label_widget.setStyleSheet("QLabel { font: 600 11pt 'Poppins'; color: #333; }")
            
            value_widget = QtWidgets.QLabel(value)
            value_widget.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #666; }")
            
            info_layout.addRow(label_widget, value_widget)
        
        content_layout.addWidget(info_group)
        
        # Purpose section
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
        
        # Extended purpose text
        purpose_text = """
    
    1. Discussion of project requirements and timeline
    2. Review of previous assignment feedback
    3. Planning for upcoming examinations
    4. Career guidance and academic advising
    5. Research collaboration opportunities
    6. Technical issues and troubleshooting
    7. Course registration assistance
    8. Internship and placement discussions

    This meeting is crucial for aligning on the next steps and ensuring academic success. Please come prepared with any questions or concerns you may have regarding the course material or your academic progress.
        """.strip()
        
        purpose_label = QtWidgets.QLabel(purpose_text)
        purpose_label.setWordWrap(True)
        purpose_label.setStyleSheet("""
            QLabel {
                color: #2b2b2b;
                font: 11pt 'Poppins';
                background: transparent;
                line-height: 1.5;
            }
        """)
        purpose_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        
        # Scroll area for purpose text
        purpose_scroll_area = QtWidgets.QScrollArea()
        purpose_scroll_area.setWidgetResizable(True)
        purpose_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        purpose_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        purpose_scroll_area.setStyleSheet("""
            QScrollArea {
                border: 1px solid #f0f0f0;
                border-radius: 6px;
                background: #fafafa;
            }
        """)
        purpose_scroll_area.setFixedHeight(200)
        
        purpose_scroll_content = QtWidgets.QWidget()
        purpose_scroll_layout = QtWidgets.QVBoxLayout(purpose_scroll_content)
        purpose_scroll_layout.setContentsMargins(10, 10, 10, 10)
        purpose_scroll_layout.addWidget(purpose_label)
        
        purpose_scroll_area.setWidget(purpose_scroll_content)
        purpose_layout.addWidget(purpose_scroll_area)
        
        content_layout.addWidget(purpose_group)
        
        # Add some spacing before the button
        content_layout.addStretch(1)
        
        # Button row
        button_widget = QtWidgets.QWidget()
        button_widget.setStyleSheet("QWidget { background: white; }")
        button_layout = QtWidgets.QHBoxLayout(button_widget)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        # Image View Section
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
        
        # Image display area
        image_display = QtWidgets.QLabel()
        image_display.setFixedSize(400, 200)
        image_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        image_display.setText("No image selected")
        image_display.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 2px dashed #dee2e6;
                border-radius: 8px;
                color: #6c757d;
                font: 10pt 'Poppins';
            }
        """)
        
        # Image controls
        image_controls_layout = QtWidgets.QHBoxLayout()
        
        view_btn = QtWidgets.QPushButton("View Full Size")
        view_btn.setFixedSize(120, 35)
        view_btn.setStyleSheet("""
            QPushButton {
                background-color: #2F80ED;
                color: white;
                border-radius: 6px;
                font: 600 10pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #2a75e0;
            }
        """)
        
        image_controls_layout.addWidget(view_btn)
        image_controls_layout.addStretch(1)
        
        image_layout.addWidget(image_display)
        image_layout.addLayout(image_controls_layout)
        
        content_layout.addWidget(image_group)

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
        
        button_layout.addStretch(1)
        button_layout.addWidget(close_button)
        
        content_layout.addWidget(button_widget)
        
        # Set the scroll content
        scroll_area.setWidget(scroll_content)
        
        # Add scroll area to main layout
        main_layout.addWidget(scroll_area)
        
        # Show the dialog
        dialog.exec()

    def retranslateUi(self):
        # UPDATED: Corrected header order to match new column arrangement
        headers_8 = ["Time", "Faculty", "Student", "Purpose", "Slot", "Status"]
        for i, header in enumerate(headers_8):
            item = self.tableWidget_8.horizontalHeaderItem(i)
            if item is not None:
                item.setText(header)
        
        # REMOVED: Setting text for label_94 and pushButton_13 since they are removed