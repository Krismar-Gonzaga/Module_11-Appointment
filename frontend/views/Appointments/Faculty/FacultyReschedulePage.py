
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class FacultyReschedulePage_ui(QWidget):
    back = QtCore.pyqtSignal()
    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self._setupFacultyReschedulePage()
        self.retranslateUi()

    def _setupFacultyReschedulePage(self):

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

        # Reschedule button
        self.button_4 = QtWidgets.QPushButton("Reschedule")
        self.button_4.setFixedHeight(50)
        self.button_4.setContentsMargins(0, 20, 0, 0)
        self.button_4.clicked.connect(lambda: self._openDenyDialog())
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

    def retranslateUi(self):
        self.label_29.setText("Shapi Dot Com")
        self.label_30.setText("Select Date & Time")
        self.label_31.setText("Available Slots")
        self.button_4.setText("Reschedule")
        self.FacultyListPage.setText("Reschedule")
        
    def _openDenyDialog(self):
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Reschedule Appointment")
        dlg.setModal(True)
        dlg.setFixedSize(420, 210)

        root = QtWidgets.QVBoxLayout(dlg)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(14)

        title = QtWidgets.QLabel("Are you sure you want to Reschedule this\nAppointment?")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        title.setStyleSheet("QLabel { color: #2b2b2b; font: 600 12pt 'Poppins'; }")
        root.addWidget(title)

        root.addStretch(1)

        btn_row = QtWidgets.QHBoxLayout()
        btn_cancel = QtWidgets.QPushButton("Cancel")
        confirm = QtWidgets.QPushButton("Confirm")
        confirm.setFixedSize(100, 32)
        btn_cancel.setStyleSheet("QPushButton { background: #e0e0e0; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: #2b2b2b; }")
        confirm.setStyleSheet("QPushButton { background: #EB5757; border-radius: 6px; padding: 6px 16px; font: 10pt 'Poppins'; color: white; }")
        btn_cancel.clicked.connect(dlg.reject)
        confirm.clicked.connect(_confirm_clicked())
        btn_row.addWidget(btn_cancel)
        def _confirm_clicked():
            self.back.emit()
            dlg.accept()
        btn_row.addStretch(1)
        btn_row.addWidget(confirm)
        root.addLayout(btn_row)

        result = dlg.exec()