
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class StudentRequestPage_ui(QWidget):
    back = QtCore.pyqtSignal()
    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self._setupStudentRequestPage()
        self.retranslateUi()

    def _setupStudentRequestPage(self):

        self.setObjectName("facultyreschedule")
        
        # Main layout
        reschedule_layout = QtWidgets.QVBoxLayout(self)
        reschedule_layout.setContentsMargins(0, 0, 0, 0)
        reschedule_layout.setSpacing(10)
        
        # Header
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
        self.backbutton.clicked.connect(self.back)
        header_layout.addWidget(self.backbutton)
        
        self.backButton = QtWidgets.QLabel()
        self.backButton.setFixedSize(40, 40)
        self.backButton.setText("")
        self.backButton.setPixmap(QtGui.QPixmap(":/assets/back_button.png"))
        self.backButton.setScaledContents(True)
        self.backButton.setObjectName("backButton")
        
        header_layout.addWidget(self.backButton)
        
        reschedule_layout.addWidget(header_widget)
        
        # Content widget
        self.widget_3 = QtWidgets.QWidget()
        self.widget_3.setStyleSheet("QWidget#widget_3 { background-color: #FFFFFF; border-radius: 20px; }")
        self.widget_3.setObjectName("widget_3")
        
        widget_layout = QtWidgets.QVBoxLayout(self.widget_3)
        widget_layout.setContentsMargins(10, 0, 10, 0)
        widget_layout.setSpacing(5)
        
        # Faculty header - Updated to match screenshot design
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
        
        #Effects

        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 3)
        shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.nameheader.setGraphicsEffect(shadow)

        nameheader_layout = QtWidgets.QHBoxLayout(self.nameheader)
        nameheader_layout.setContentsMargins(20, 0, 20, 0)
        nameheader_layout.setSpacing(12)
        nameheader_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Profile icon inside a blue circle
        self.label_32 = QtWidgets.QLabel()
        self.label_32.setFixedSize(50, 50)
        self.label_32.setPixmap(QtGui.QPixmap(":/assets/profile_icon.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setStyleSheet("""
            QLabel {
                background: #4285F4;      /* Blue circle */
                border-radius: 25px;      /* Half of width/height */
                border: 2px solid white;
            }
        """)
        
        # Name text
        self.label_29 = QtWidgets.QLabel("Shapi Dot Com")
        font = QtGui.QFont("Poppins", 18, QtGui.QFont.Weight.Bold)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: #084924;")  # Dark green
        self.label_29.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)

        nameheader_layout.addWidget(self.label_32)
        nameheader_layout.addWidget(self.label_29, 1)
        # Center the floating header in the main layout
        center_layout = QtWidgets.QHBoxLayout()
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.addStretch()
        center_layout.addWidget(self.nameheader)
        center_layout.addStretch()

        widget_layout.addLayout(center_layout)

        # Subtitle: "Select Date & Time"
        self.subtitle = QtWidgets.QLabel("Select Date & Time")
        subtitle_font = QtGui.QFont("Poppins", 14, QtGui.QFont.Weight.Medium)
        self.subtitle.setFont(subtitle_font)
        self.subtitle.setStyleSheet("color: #084924;")  # Dark green
        self.subtitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Add under header
        widget_layout.addWidget(self.subtitle)

        # Main content area - Updated layout to match screenshot
        content_widget = QtWidgets.QWidget()
        content_layout = QtWidgets.QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(20)
        
        # Left side - Calendar section
        left_widget = QtWidgets.QWidget()
        left_layout = QtWidgets.QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)
        
        # Section header - Updated to match screenshot
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
        
        # Month/year header - Added to match screenshot
        month_header = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        month_header.setFont(font)
        month_header.setStyleSheet("QLabel { color: #084924; background: transparent; }")
        month_header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        month_header.setText("August 2025")
        left_layout.addWidget(month_header)
        
        # Days of week header - Added to match screenshot
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


        # Parent container (QWidget) for calendar
        self.calendarCard = QtWidgets.QWidget()
        self.calendarCard.setStyleSheet("""
            QWidget#calendarCard {
                background: #ffffff;
                border-radius: 12px;
                border: 1px solid #e0e0e0;
            }
        """)
        self.calendarCard.setObjectName("calendarCard")


        # Layout for the card
        calendar_layout = QtWidgets.QVBoxLayout(self.calendarCard)
        calendar_layout.setContentsMargins(10, 10, 10, 10)
        
        
        # Calendar widget - Updated styling
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

            /* Navigation bar (month/year and arrows) */
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

            /* Left/right month arrows */
            QCalendarWidget QToolButton#qt_calendar_prevmonth {
                qproperty-icon: url(:/assets/arrow_left.png);
                icon-size: 16px;
            }
            QCalendarWidget QToolButton#qt_calendar_nextmonth {
                qproperty-icon: url(:/assets/arrow_right.png);
                icon-size: 16px;
            }

            /* Month/Year label */
            QCalendarWidget QToolButton#qt_calendar_monthbutton,
            QCalendarWidget QToolButton#qt_calendar_yearbutton {
                font: bold 12pt 'Poppins';
                color: #084924;
            }

            /* Days of week header */
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

            /* Days grid */
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

        self.calendarWidget.setObjectName("calendarWidget")
        # Add calendar to the card layout
        calendar_layout.addWidget(self.calendarWidget)
       
       
        # Set to August 2025 as shown in screenshot
        target_date = QtCore.QDate(2025, 8, 1)
        self.calendarWidget.setSelectedDate(target_date)
        
        # Now add the calendarCard into your main page layout
        left_layout.addWidget(self.calendarCard, 1)

        
        # Right (time slots)
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
        available_layout.setContentsMargins(0, 0, 0, 0)  # removes top/bottom/left/right margins
        available_layout.setSpacing(10)


        # Slot buttons (radio style)
        self.slot_buttons = []
        slot_times = ["7:00am - 7:30am", "8:00am - 8:30am", "9:00am - 9:30am"]

        slots_layout = QtWidgets.QHBoxLayout()
        slots_layout.setSpacing(12)

        for i, time in enumerate(slot_times):
            btn = QtWidgets.QPushButton(time)
            btn.setFixedHeight(45)
            btn.setCheckable(True)
            btn.setStyleSheet(self.slot_style(default=True))
            btn.clicked.connect(lambda checked, b=btn: self.select_slot(b))
            slots_layout.addWidget(btn)
            self.slot_buttons.append(btn)

        # Default select first button
        self.slot_buttons[0].setChecked(True)
        self.slot_buttons[0].setStyleSheet(self.slot_style(selected=True))

        available_layout.addLayout(slots_layout)

        # Request button
        self.button_4 = QtWidgets.QPushButton("Request")
        self.button_4.setFixedHeight(50)
        self.button_4.setContentsMargins(0, 20, 0, 0)
        self.button_4.clicked.connect(lambda: self._showRequestDialog())
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
        """)
        available_layout.addWidget(self.button_4)

        right_layout.addWidget(self.availableSlot, 1)

        content_layout.addWidget(left_widget, 1)
        content_layout.addWidget(right_widget, 1)

        widget_layout.addWidget(content_widget, 1)
        reschedule_layout.addWidget(self.widget_3, 1)
        
       
    def timebutton_clicked(self, button):
        self.button_1.setStyleSheet("""
            QPushButton#button_1 {
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #084924;
                border-radius: 8px;
                padding: 10px 20px;
                font: 600 11pt 'Poppins';
            }
            QPushButton#button_1:hover {
                background-color: #f0f7f3;
            }
            QPushButton#button_1:pressed {
                background-color: #e0f0e8;
            }
        """)
        self.button_2.setStyleSheet("""
            QPushButton#button_2 {
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #084924;
                border-radius: 8px;
                padding: 10px 20px;
                font: 600 11pt 'Poppins';
            }
            QPushButton#button_2:hover {
                background-color: #f0f7f3;
            }
            QPushButton#button_2:pressed {
                background-color: #e0f0e8;
            }
        """)
        self.button_3.setStyleSheet("""
            QPushButton#button_3 {
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #084924;
                border-radius: 8px;
                padding: 10px 20px;
                font: 600 11pt 'Poppins';
            }
            QPushButton#button_3:hover {
                background-color: #f0f7f3;
            }
            QPushButton#button_3:pressed {
                background-color: #e0f0e8;
            }
        """)
        if button == self.button_1:
            self.button_1.setStyleSheet("""
                QPushButton#button_1 {
                    background-color: #084924;
                    color: white;
                    border: 2px solid #084924;
                    border-radius: 8px;
                    padding: 10px 20px;
                    font: 600 11pt 'Poppins';
                }
            """)
        elif button == self.button_2:
            self.button_2.setStyleSheet("""
                QPushButton#button_2 {
                    background-color: #084924;
                    color: white;
                    border: 2px solid #084924;
                    border-radius: 8px;
                    padding: 10px 20px;
                    font: 600 11pt 'Poppins';
                }
            """)
        elif button == self.button_3:
            self.button_3.setStyleSheet("""
                QPushButton#button_3 {
                    background-color: #084924;
                    color: white;
                    border: 2px solid #084924;
                    border-radius: 8px;
                    padding: 10px 20px;
                    font: 600 11pt 'Poppins';
                }
            """)

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
            }"""
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
            QPushButton:hover { background-color: #f0f7f3; }
            QPushButton:pressed { background-color: #e0f0e8; }
            """

    def select_slot(self, button):
        for btn in self.slot_buttons:
            btn.setChecked(False)
            btn.setStyleSheet(self.slot_style(default=True))
        button.setChecked(True)
        button.setStyleSheet(self.slot_style(selected=True))



    def _showRequestDialog(self):
        """Show an enhanced dialog with purpose details and appointment info"""
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Appointment Details")
        dialog.setModal(True)
        dialog.setFixedSize(550, 700)  # Increased height to accommodate new elements
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
        
        
        
        # REASON SECTION - NEW
        reason_group = QtWidgets.QGroupBox("Reason")
        reason_group.setStyleSheet("""
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
        
        reason_layout = QtWidgets.QVBoxLayout(reason_group)
        
        # Text edit for reason input
        self.reason_text_edit = QtWidgets.QTextEdit()
        self.reason_text_edit.setPlaceholderText("Enter your reason here...")
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
        content_layout.addWidget(reason_group)
        
        # UPLOAD FILE SECTION - NEW
        upload_group = QtWidgets.QGroupBox("Upload File")
        upload_group.setStyleSheet("""
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
        
        upload_layout = QtWidgets.QVBoxLayout(upload_group)
        
        # File info display
        self.file_info_widget = QtWidgets.QWidget()
        file_info_layout = QtWidgets.QHBoxLayout(self.file_info_widget)
        file_info_layout.setContentsMargins(0, 0, 0, 0)
        
        self.file_name_label = QtWidgets.QLabel("Sample.png")
        self.file_name_label.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #333; }")
        
        self.file_progress_label = QtWidgets.QLabel("50%")
        self.file_progress_label.setStyleSheet("QLabel { font: 11pt 'Poppins'; color: #666; }")
        
        file_info_layout.addWidget(self.file_name_label)
        file_info_layout.addStretch(1)
        file_info_layout.addWidget(self.file_progress_label)
        
        upload_layout.addWidget(self.file_info_widget)
        
        # Upload button
        self.upload_button = QtWidgets.QPushButton("Upload Now")
        self.upload_button.setFixedHeight(40)
        self.upload_button.setStyleSheet("""
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
        self.upload_button.clicked.connect(self._handleFileUpload)
        
        upload_layout.addWidget(self.upload_button)
        content_layout.addWidget(upload_group)
        
        # Image preview section (initially hidden)
        self.image_preview_group = QtWidgets.QGroupBox("Image Preview")
        self.image_preview_group.setStyleSheet("""
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
        
        image_preview_layout = QtWidgets.QVBoxLayout(self.image_preview_group)
        
        # Image display
        self.image_display = QtWidgets.QLabel()
        self.image_display.setFixedSize(400, 200)
        self.image_display.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 2px dashed #dee2e6;
                border-radius: 8px;
            }
        """)
        self.image_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image_display.setText("No image selected")
        self.image_display.setStyleSheet("""
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
        
        self.view_btn = QtWidgets.QPushButton("View Full Size")
        self.view_btn.setFixedSize(120, 35)
        self.view_btn.clicked.connect(self._viewImageFullSize)
        self.view_btn.setStyleSheet("""
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
        self.view_btn.setEnabled(False)  # Disabled until image is loaded
        
        image_controls_layout.addWidget(self.view_btn)
        image_controls_layout.addStretch(1)
        
        image_preview_layout.addWidget(self.image_display)
        image_preview_layout.addLayout(image_controls_layout)
        
        content_layout.addWidget(self.image_preview_group)
        self.image_preview_group.hide()  # Hide initially
        
        # Add some spacing before the buttons
        content_layout.addStretch(1)
        
        # Button row (this stays fixed at the bottom)
        button_widget = QtWidgets.QWidget()
        button_widget.setStyleSheet("QWidget { background: white; }")
        button_layout = QtWidgets.QHBoxLayout(button_widget)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        # Cancel and Submit buttons
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
        
        submit_button = QtWidgets.QPushButton("Submit")
        submit_button.setFixedSize(120, 40)
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
        submit_button.clicked.connect(self._handleSubmit)
        
        button_layout.addStretch(1)
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(submit_button)
        
        content_layout.addWidget(button_widget)
        
        # Set the scroll content
        scroll_area.setWidget(scroll_content)
        
        # Add scroll area to main layout
        main_layout.addWidget(scroll_area)
        
        # Store dialog reference for use in methods
        self.purpose_dialog = dialog
        
        # Show the dialog
        dialog.exec()

    def _handleFileUpload(self):
        """Handle file upload button click"""
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self.purpose_dialog,
            "Select Image File",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        
        if file_path:
            # Update file info
            file_name = file_path.split('/')[-1]
            self.file_name_label.setText(file_name)
            self.file_progress_label.setText("100%")
            
            # Load and display image
            pixmap = QtGui.QPixmap(file_path)
            if not pixmap.isNull():
                # Scale pixmap to fit display area while maintaining aspect ratio
                scaled_pixmap = pixmap.scaled(
                    self.image_display.width(), 
                    self.image_display.height(),
                    QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                    QtCore.Qt.TransformationMode.SmoothTransformation
                )
                self.image_display.setPixmap(scaled_pixmap)
                self.image_display.setText("")
                self.view_btn.setEnabled(True)
                
                # Store full size pixmap for full-size viewing
                self.full_size_pixmap = pixmap
                
                # Show preview section
                self.image_preview_group.show()
            else:
                QtWidgets.QMessageBox.warning(
                    self.purpose_dialog,
                    "Invalid Image",
                    "The selected file is not a valid image file."
                )

    def _viewImageFullSize(self):
        """Show image in full size dialog"""
        if hasattr(self, 'full_size_pixmap') and not self.full_size_pixmap.isNull():
            image_dialog = QtWidgets.QDialog()
            image_dialog.setWindowTitle("Image Preview")
            image_dialog.setModal(True)
            image_dialog.resize(800, 600)
            
            layout = QtWidgets.QVBoxLayout(image_dialog)
            
            image_label = QtWidgets.QLabel()
            image_label.setPixmap(self.full_size_pixmap)
            image_label.setScaledContents(True)
            
            scroll_area = QtWidgets.QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(image_label)
            
            close_button = QtWidgets.QPushButton("Close")
            close_button.clicked.connect(image_dialog.accept)
            
            layout.addWidget(scroll_area)
            layout.addWidget(close_button)
            
            image_dialog.exec()

    def _handleSubmit(self):
        """Handle submit button click"""
        reason_text = self.reason_text_edit.toPlainText().strip()
        
        if not reason_text:
            QtWidgets.QMessageBox.warning(
                self.purpose_dialog,
                "Missing Information",
                "Please enter a reason before submitting."
            )
            return
        
        # Here you would typically process the form data
        # For example: save reason text and handle the uploaded file
        
        print(f"Reason: {reason_text}")
        if hasattr(self, 'full_size_pixmap'):
            print("Image uploaded successfully")
        
        
        self.purpose_dialog.accept()
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
        message_label = QtWidgets.QLabel("Faculty has been requested!")
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
        ok_button.clicked.connect(self.back)
        
        layout.addWidget(ok_button)
        
        # Show the dialog
        dialog.exec()
    def retranslateUi(self):
        self.label_29.setText("Shapi Dot Com")
        self.label_30.setText("Select Date & Time")
        self.label_31.setText("Available Slots")
        self.button_4.setText("Request")
        self.FacultyListPage.setText("Request")
        
    