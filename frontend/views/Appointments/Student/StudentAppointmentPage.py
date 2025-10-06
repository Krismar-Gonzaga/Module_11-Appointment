from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class StudentAppointmentPage_ui(QWidget):
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
        

    def _setupAppointmentsPage(self):
        self.setObjectName("Appointments_2")
        # Main layout for appointments page
        appointments_layout = QtWidgets.QVBoxLayout(self)
        appointments_layout.setContentsMargins(0, 0, 0, 0)
        appointments_layout.setSpacing(10)
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
        
        # Content widget
        self.widget_27 = QtWidgets.QWidget()
        self.widget_27.setStyleSheet("""
            QWidget#widget_27 { 
                background-color: #FFFFFF; 
                border-radius: 20px;
                padding: 20px;
            }
        """)
        self.widget_27.setObjectName("widget_27")
        
        widget_layout = QtWidgets.QVBoxLayout(self.widget_27)
        widget_layout.setContentsMargins(20, 20, 20, 20)
        widget_layout.setSpacing(15)
        widget_layout.setObjectName("widget_layout")
        
        # Section header
        section_header = QtWidgets.QWidget()
        section_layout = QtWidgets.QHBoxLayout(section_header)
        section_layout.setContentsMargins(0, 0, 0, 0)
        section_layout.setSpacing(0)
        
        self.label_94 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_94.setFont(font)
        self.label_94.setObjectName("label_94")
        
        section_layout.addWidget(self.label_94)
        section_layout.addStretch(1)
        
        self.pushButton_13 = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setText("Browse Faculty")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.go_to_AppointmentSchedulerPage.emit)
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
        section_layout.addWidget(self.pushButton_13)
        
        widget_layout.addWidget(section_header)
        
        # Appointments table
        self.tableWidget_8 = QtWidgets.QTableWidget()
        self.tableWidget_8.setAlternatingRowColors(True)
        self.tableWidget_8.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_8.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_8.setShowGrid(False)
        self.tableWidget_8.verticalHeader().setVisible(False)
        self.tableWidget_8.horizontalHeader().setVisible(True)
        self.tableWidget_8.setRowCount(5)
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(6)
        self.tableWidget_8.setMaximumWidth(2000)
        self.tableWidget_8.setColumnWidth(0, 150)  # Time
        self.tableWidget_8.setColumnWidth(1, 200)  # Student
        self.tableWidget_8.setColumnWidth(2, 200)  # Slot   
        self.tableWidget_8.setColumnWidth(3, 250)  # Purpose
        self.tableWidget_8.setColumnWidth(4, 150)  # Status
        self.tableWidget_8.setColumnWidth(5, 150)  # Actions
        header = self.tableWidget_8.horizontalHeader()
        try:
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)  # Slot column
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)  # Propose column  
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)  # Status column
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)  # Actions column
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.Stretch)  # Purpose column
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.Stretch)
            
        except:
            # Fallback for older PyQt versions
            header.setResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
            header.setResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
            header.setResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
                
        # Header styling
        self.tableWidget_8.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignJustify | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget_8.horizontalHeader().setStyleSheet(
            """
            QHeaderView::section {
                background-color: #0a5a2f;
                color: white;
                padding: 12px 8px;
                border: 0px;
                font: 600 11pt "Poppins";
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
            }
            QTableWidget::item { 
                padding: 10px 8px;
                border-bottom: 1px solid #f0f0f0;
            }
            """
        )
        
        # Table header
        headers = ["Time", "Student", "Slot", "Purpose", "Status", "Actions"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setFamily("Poppins")
            font.setPointSize(11)
            item.setFont(font)
            self.tableWidget_8.setHorizontalHeaderItem(i, item)
        
        widget_layout.addWidget(self.tableWidget_8, 1)
        
        appointments_layout.addWidget(self.widget_27, 1)
        appointments_layout.addWidget(self.backButton_8)
        # self.stackedWidget.addWidget(self.Appointments_2)
        
        # Populate initial rows to match mockup
        self._populateAppointmentsTable()
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
        dialog.setFixedSize(550, 600)  # Fixed dialog size
        dialog.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 12px;
            }
        """)
        
        # Main layout for the dialog
        main_layout = QtWidgets.QVBoxLayout(dialog)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for scroll area
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
        content_layout.setContentsMargins(24, 20, 24, 20)
        content_layout.setSpacing(20)
        
        # Header with icon and title
        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        # Icon
        icon_label = QtWidgets.QLabel()
        icon_label.setFixedSize(32, 32)
        # Note: Make sure you have this icon in your resources
        # icon_label.setPixmap(QtGui.QPixmap(":/assets/appointments_icon.png"))
        icon_label.setStyleSheet("QLabel { background-color: #084924; border-radius: 8px; }")  # Placeholder
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
        
        # Sample appointment data - you can replace this with actual data
        appointment_data = [
            ("Student:", "Shapi Dot Com"),
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
        
        # Extended purpose text to demonstrate scrolling
        purpose_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

    Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet.

    Additional details about the appointment purpose:

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
        
        # Scroll area for purpose text (nested scroll area within the main scroll area)
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
        purpose_scroll_area.setFixedHeight(200)  # Fixed height for purpose text area
        
        purpose_scroll_content = QtWidgets.QWidget()
        purpose_scroll_layout = QtWidgets.QVBoxLayout(purpose_scroll_content)
        purpose_scroll_layout.setContentsMargins(12, 12, 12, 12)
        purpose_scroll_layout.addWidget(purpose_label)
        
        purpose_scroll_area.setWidget(purpose_scroll_content)
        purpose_layout.addWidget(purpose_scroll_area)
        
        content_layout.addWidget(purpose_group)
        
        # Add some spacing before the button
        content_layout.addStretch(1)
        
        # Button row (this stays fixed at the bottom)
        button_widget = QtWidgets.QWidget()
        button_widget.setStyleSheet("QWidget { background: white; }")
        button_layout = QtWidgets.QHBoxLayout(button_widget)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        # Image View Section - ADDED THIS SECTION
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
        image_display.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 2px dashed #dee2e6;
                border-radius: 8px;
            }
        """)
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
        # view_btn.clicked.connect(lambda: self._viewImageFullSize(image_display)
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
        # END OF ADDED IMAGE VIEW SECTION

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

    def _makeActionsCell(self, status, row_index=None):
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        def make_btn(text, bg):
            btn = QtWidgets.QPushButton(text, parent=container)
            btn.setMinimumHeight(28)
            btn.setStyleSheet(f"QPushButton {{ background-color: {bg}; color: white; border-radius: 6px; padding: 4px 10px; font: 10pt 'Poppins'; }}")
            return btn

        cancel = make_btn("Cancel", "#EB5757")
        cancel.clicked.connect(lambda: self._openCancelDialog(row_index, status))
        layout.addWidget(cancel)

        layout.addStretch(1)
        return container

    def _openApproveDialog(self, row_index):
        # Build a modal dialog matching the updated mock (with online link field)
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Confirm Approval")
        dlg.setModal(True)
        dlg.setFixedSize(460, 280)

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

        # Meeting type selection
        types_row = QtWidgets.QHBoxLayout()
        chk_online = QtWidgets.QCheckBox("Online")
        chk_person = QtWidgets.QCheckBox("In person")
        for chk in (chk_online, chk_person):
            chk.setStyleSheet("QCheckBox { font: 10pt 'Poppins'; color: #2b2b2b; }")
        chk_online.setChecked(True)
        def _toggle(exclusive, other):
            if exclusive.isChecked():
                other.setChecked(False)
            
        chk_online.toggled.connect(lambda _: _toggle(chk_online, chk_person))
        chk_person.toggled.connect(lambda _: _toggle(chk_person, chk_online))
        types_row.addWidget(chk_online)
        types_row.addSpacing(24)
        types_row.addWidget(chk_person)
        types_row.addStretch(1)
        root.addLayout(types_row)

        # Online link field (only visible when Online is selected)
        link_edit = QtWidgets.QLineEdit()
        link_edit.setPlaceholderText("Online meeting link")
        link_edit.setStyleSheet(
            "QLineEdit { border: 1px solid #cfd8dc; border-radius: 6px; padding: 8px 10px; font: 10pt 'Poppins'; }"
        )
        root.addWidget(link_edit)

        
        chk_online.toggled.connect(lambda _: link_edit.setPlaceholderText("Online meeting link"))
        chk_person.toggled.connect(lambda _: link_edit.setPlaceholderText("Location details"))

        root.addStretch(1)

        # Buttons row
        btn_row = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_accept = QtWidgets.QPushButton("Accept")
        btn_cancel.setStyleSheet("QPushButton { background: #bdbdbd; border-radius: 8px; padding: 8px 20px; font: 10pt 'Poppins'; color: white; }")
        btn_accept.setStyleSheet("QPushButton { background: #084924; border-radius: 8px; padding: 8px 20px; font: 10pt 'Poppins'; color: white; }")
        btn_accept.setEnabled(True)

        # Enable accept when at least one type is chosen and if Online then require link text
        
            
        

        btn_cancel.clicked.connect(dlg.reject)
        btn_accept.clicked.connect(lambda:_accept_clicked())
        def _accept_clicked():
            if chk_online.isChecked() or chk_person.isChecked():
                print("Approved with link:", link_edit.text())
                self.tableWidget_8.setItem(row_index, 4, self._makeStatusItem("APPROVED", "#219653"))
                self.tableWidget_8.setCellWidget(row_index, 5, self._makeActionsCell("APPROVED", row_index))
                dlg.accept()
        btn_row.addWidget(btn_cancel)
        btn_row.addStretch(1)
        btn_row.addWidget(btn_accept)
        root.addLayout(btn_row)
        dlg.exec()

        # if result == QtWidgets.QDialog.DialogCode.Accepted and row_index is not None:
        #     # Update the row to APPROVED and refresh actions
        #     print("Approved with link:", link_edit.text() if chk_online.isChecked() else "In person")
        #     try:
        #         status_item = self._makeStatusItem("APPROVED", "#219653")
        #         self.tableWidget_8.setItem(row_index, 4, status_item)
        #         self.tableWidget_8.setCellWidget(row_index, 5, self._makeActionsCell("APPROVED", row_index))
        #     except Exception:
        #         pass

    def _openDenyDialog(self, row_index):
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Confirm Deny")
        dlg.setModal(True)
        dlg.setFixedSize(420, 210)

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
        btn_deny.clicked.connect(dlg.accept)
        btn_row.addWidget(btn_cancel)
        btn_row.addStretch(1)
        btn_row.addWidget(btn_deny)
        root.addLayout(btn_row)

        result = dlg.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted and row_index is not None:
            try:
                status_item = self._makeStatusItem("CANCELED", "#EB5757")
                self.tableWidget_8.setItem(row_index, 4, status_item)
                self.tableWidget_8.setCellWidget(row_index, 5, self._makeActionsCell("CANCELED", row_index))
            except Exception:
                pass
    def _openCancelDialog(self, row_index, status):
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Cancel")
        dlg.setModal(True)
        dlg.setFixedSize(420, 210)

        root = QtWidgets.QVBoxLayout(dlg)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(14)
        
        
        title = QtWidgets.QLabel("Are you sure you want to Cancel this" + "\nrequest?")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        title.setStyleSheet("QLabel { color: #2b2b2b; font: 600 12pt 'Poppins'; }")
        root.addWidget(title)

        root.addStretch(1)

        btn_row = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_deny = QtWidgets.QPushButton("Confirm")
        btn_cancel.setStyleSheet("QPushButton { background: #e0e0e0; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: #2b2b2b; }")
        btn_deny.setStyleSheet("QPushButton { background: #EB5757; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: white; }")
        btn_cancel.clicked.connect(dlg.reject)
        btn_deny.clicked.connect(dlg.accept)
        btn_row.addWidget(btn_cancel)
        btn_row.addStretch(1)
        btn_row.addWidget(btn_deny)
        root.addLayout(btn_row)

        result = dlg.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted and row_index is not None:
            try:
                
                status_item = self._makeStatusItem("CANCELED", "#EB5757")
                self.tableWidget_8.setCellWidget(row_index, 5, self._makeActionsCell("DENIED", row_index))
                self.tableWidget_8.setItem(row_index, 4, status_item)
                
            except Exception:
                pass

    def _populateAppointmentsTable(self):
        rows = [
            ("2025-08-21 09:00:00", "Shapi Dot Com", "2025-08-21 09:00 - 9:30", "View", "PENDING"),
            ("2025-08-21 09:30:00", "Shapi Dot Com", "2025-08-21 09:00 - 9:30", "View", "RESCHEDULED"),
            ("2025-08-21 09:00:00", "Shapi Dot Com", "2025-08-21 09:00 - 9:30", "View", "CANCELED"),
            ("2025-08-21 09:00:00", "Shapi Dot Com", "2025-08-21 09:00 - 9:30", "View", "APPROVED"),
            ("2025-08-21 09:00:00", "Shapi Dot Com", "2025-08-21 09:00 - 9:30", "View", "PENDING"),
        ]
        status_colors = {
            "PENDING": "#F2994A",
            "RESCHEDULED": "#2F80ED",
            "CANCELED": "#EB5757",
            "APPROVED": "#219653",
        }
        self.tableWidget_8.setRowCount(len(rows))
        for r, (time_text, student, slot, _purpose, status) in enumerate(rows):
            # Time
            self.tableWidget_8.setItem(r, 0, QtWidgets.QTableWidgetItem(time_text))
            # Student
            self.tableWidget_8.setItem(r, 1, QtWidgets.QTableWidgetItem(student))
            # Slot
            self.tableWidget_8.setItem(r, 2, QtWidgets.QTableWidgetItem(slot))
            # Purpose (View link)
            self.tableWidget_8.setCellWidget(r, 3, self._makePurposeViewCell())
            # Status colored
            self.tableWidget_8.setItem(r, 4, self._makeStatusItem(status, status_colors.get(status, "#333333")))
            # Actions
            self.tableWidget_8.setCellWidget(r, 5, self._makeActionsCell(status, r))
            self.tableWidget_8.setRowHeight(r, 50)
    def retranslateUi(self):

        headers_8 = ["Time", "Student", "Slot", "Purpose", "Status", "Actions"]
        for i, header in enumerate(headers_8):
            item = self.tableWidget_8.horizontalHeaderItem(i)
            if item is not None:
                item.setText(header)
        
        self.label_94.setText("My Appointments")
        self.pushButton_13.setText("Browse Faculty")
        
        