from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from .appointment_crud import appointment_crud

class StudentBrowseFaculty_ui(QWidget):
    go_to_RequestPage = QtCore.pyqtSignal(dict)  # Emit faculty data
    back = QtCore.pyqtSignal()

    def __init__(self, username, roles, primary_role, token, parent=None):
        super().__init__(parent)
        self.username = username
        self.roles = roles
        self.primary_role = primary_role
        self.token = token
        self.Appointment_crud = appointment_crud()
        
        self.setWindowTitle("Appointment Scheduler")
        self.current_page = 0
        self.items_per_page = 6
        self.faculties = []
        self.setFixedSize(1000, 550)
        self._setupBrowseFacultyPage()
        self.load_faculties_data()
       
    def load_faculties_data(self):
        """Load faculty data from JSON database"""
        try:
            faculties_data = self.Appointment_crud.list_faculty()
            self.faculties = []
            
            for faculty in faculties_data:
                self.faculties.append({
                    "id": faculty.get('id'),
                    "name": faculty.get('name', 'Unknown'),
                    "email": faculty.get('email', 'No email'),
                    "department": faculty.get('department', 'Unknown Department'),
                    "role": "Request"
                })
            
            if not self.faculties:
                self._create_sample_faculties()
                faculties_data = self.Appointment_crud.list_faculty()
                for faculty in faculties_data:
                    self.faculties.append({
                        "id": faculty.get('id'),
                        "name": faculty.get('name', 'Unknown'),
                        "email": faculty.get('email', 'No email'),
                        "department": faculty.get('department', 'Unknown Department'),
                        "role": "Request"
                    })
            
            self._populateFacultiesGrid()
            
        except Exception as e:
            print(f"Error loading faculties data: {e}")
            QMessageBox.warning(self, "Error", f"Failed to load faculty data: {str(e)}")
            self.faculties = [
                {"id": 1, "name": "Dr. Smith", "email": "smith@university.edu", "department": "Computer Science", "role": "Request"},
                {"id": 2, "name": "Prof. Johnson", "email": "johnson@university.edu", "department": "Mathematics", "role": "Request"},
                {"id": 3, "name": "Dr. Brown", "email": "brown@university.edu", "department": "Physics", "role": "Request"},
                {"id": 4, "name": "Prof. Davis", "email": "davis@university.edu", "department": "Chemistry", "role": "Request"},
                {"id": 5, "name": "Dr. Wilson", "email": "wilson@university.edu", "department": "Biology", "role": "Request"},
                {"id": 6, "name": "Prof. Taylor", "email": "taylor@university.edu", "department": "Engineering", "role": "Request"},
            ]
            self._populateFacultiesGrid()

    def _create_sample_faculties(self):
        """Create sample faculty data if none exists"""
        try:
            sample_faculties = [
                {"name": "Dr. Smith", "email": "smith@university.edu", "department": "Computer Science"},
                {"name": "Prof. Johnson", "email": "johnson@university.edu", "department": "Mathematics"},
                {"name": "Dr. Brown", "email": "brown@university.edu", "department": "Physics"},
                {"name": "Prof. Davis", "email": "davis@university.edu", "department": "Chemistry"},
                {"name": "Dr. Wilson", "email": "wilson@university.edu", "department": "Biology"},
                {"name": "Prof. Taylor", "email": "taylor@university.edu", "department": "Engineering"},
                {"name": "Dr. Anderson", "email": "anderson@university.edu", "department": "Psychology"},
                {"name": "Prof. Martinez", "email": "martinez@university.edu", "department": "Sociology"},
                {"name": "Dr. Clark", "email": "clark@university.edu", "department": "Economics"},
                {"name": "Prof. Rodriguez", "email": "rodriguez@university.edu", "department": "Business"},
            ]
            
            for faculty in sample_faculties:
                self.Appointment_crud.create_faculty(
                    faculty["name"],
                    faculty["email"],
                    faculty["department"]
                )
                
        except Exception as e:
            print(f"Error creating sample faculties: {e}")

    def _setupBrowseFacultyPage(self):
        self.setObjectName("AppointmentScheduler")
        
        scheduler_layout = QtWidgets.QVBoxLayout(self)
        scheduler_layout.setContentsMargins(0, 0, 0, 0)
        scheduler_layout.setSpacing(10)
        
        header_widget = QtWidgets.QWidget()
        header_layout = QtWidgets.QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        self.Academics_5 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        self.Academics_5.setFont(font)
        self.Academics_5.setStyleSheet("QLabel { color: #084924; }")
        self.Academics_5.setObjectName("Academics_5")
        
        header_layout.addWidget(self.Academics_5)
        header_layout.addStretch(1)

        self.refreshButton = QtWidgets.QPushButton("Refresh")
        self.refreshButton.setFixedSize(100, 35)
        self.refreshButton.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 8px;
                margin-right: 10px;
                font: 10pt 'Poppins';
            }
            QPushButton:hover {
                background-color: #2a75e0;
            }
        """)
        self.refreshButton.clicked.connect(self.load_faculties_data)
        header_layout.addWidget(self.refreshButton)

        self.backbutton = QtWidgets.QPushButton("<- Back")
        self.backbutton.setIcon(QtGui.QIcon(":/assets/images/back_button.png"))
        self.backbutton.clicked.connect(self.back)
        header_layout.addWidget(self.backbutton)
        
        scheduler_layout.addWidget(header_widget)
        
        self.widget_25 = QtWidgets.QWidget()
        self.widget_25.setStyleSheet("QWidget#widget_25 { background-color: #FFFFFF; border-radius: 20px; }")
        self.widget_25.setObjectName("widget_25")
        
        widget_layout = QtWidgets.QVBoxLayout(self.widget_25)
        widget_layout.setContentsMargins(20, 20, 20, 20)
        widget_layout.setSpacing(15)
        
        self._setupFacultiesSection(widget_layout)
        
        scheduler_layout.addWidget(self.widget_25, 1)
        
        self.retranslateUi()

    def _setupFacultiesSection(self, parent_layout):
        faculties_container = QtWidgets.QWidget()
        faculties_container.setObjectName("faculties_container")
        
        faculties_layout = QtWidgets.QVBoxLayout(faculties_container)
        faculties_layout.setContentsMargins(0, 0, 0, 0)
        faculties_layout.setSpacing(15)
        
        faculties_header = QtWidgets.QLabel()
        faculties_header.setObjectName("faculties_header")
        faculties_header.setStyleSheet("""
            QLabel {
                font: 14pt 'Poppins';
                color: #000000;
                padding: 8px 0;
            }
        """)
        faculties_layout.addWidget(faculties_header)
        
        self.faculties_scroll_area = QtWidgets.QScrollArea()
        self.faculties_scroll_area.setWidgetResizable(True)
        self.faculties_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.faculties_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.faculties_scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background: transparent;
            }
            QScrollBar:vertical {
                background: #f0f0f0;
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                border-radius: 5px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
        """)
        
        self.faculties_grid_widget = QtWidgets.QWidget()
        self.faculties_grid_layout = QtWidgets.QGridLayout(self.faculties_grid_widget)
        self.faculties_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.faculties_grid_layout.setHorizontalSpacing(20)
        self.faculties_grid_layout.setVerticalSpacing(15)
        
        self.faculties_scroll_area.setWidget(self.faculties_grid_widget)
        faculties_layout.addWidget(self.faculties_scroll_area, 1)
        
        self._setupPaginationControls(faculties_layout)
        
        parent_layout.addWidget(faculties_container, 1)

    def _setupPaginationControls(self, parent_layout):
        pagination_widget = QtWidgets.QWidget()
        pagination_layout = QtWidgets.QHBoxLayout(pagination_widget)
        pagination_layout.setContentsMargins(0, 10, 0, 0)
        
        self.prev_button = QtWidgets.QPushButton("Previous")
        self.prev_button.setFixedSize(100, 35)
        self.prev_button.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 8px;
                font: 10pt 'Poppins';
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        self.prev_button.clicked.connect(self._previousPage)
        
        self.page_info = QtWidgets.QLabel()
        self.page_info.setStyleSheet("""
            QLabel {
                font: 10pt 'Poppins';
                color: #000000;
            }
        """)
        self.page_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.next_button = QtWidgets.QPushButton("Next")
        self.next_button.setFixedSize(100, 35)
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                border-radius: 8px;
                font: 10pt 'Poppins';
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        self.next_button.clicked.connect(self._nextPage)
        
        pagination_layout.addStretch(1)
        pagination_layout.addWidget(self.prev_button)
        pagination_layout.addSpacing(10)
        pagination_layout.addWidget(self.page_info)
        pagination_layout.addSpacing(10)
        pagination_layout.addWidget(self.next_button)
        pagination_layout.addStretch(1)
        
        parent_layout.addWidget(pagination_widget)

    def _populateFacultiesGrid(self):
        for i in reversed(range(self.faculties_grid_layout.count())):
            widget = self.faculties_grid_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        
        start_index = self.current_page * self.items_per_page
        end_index = min(start_index + self.items_per_page, len(self.faculties))
        
        for i in range(start_index, end_index):
            faculty = self.faculties[i]
            print(faculty)
            position = i - start_index
            row = position // 3
            col = position % 3
            faculty_card = self._createFacultyCard(faculty)
            self.faculties_grid_layout.addWidget(faculty_card, row, col)
        
        total_pages = (len(self.faculties) + self.items_per_page - 1) // self.items_per_page
        self.page_info.setText(f"Page {self.current_page + 1} of {total_pages}")
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < total_pages - 1)

    def _createFacultyCard(self, faculty):
        card = QtWidgets.QWidget()
        card.setFixedSize(250, 300)
        card.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
                border: 2px solid #E0E0E0;
                border-radius: 15px;
            }
            QWidget:hover {
                border: 2px solid #084924;
                background-color: #F8FFF8;
            }
        """)
        
        card_layout = QtWidgets.QVBoxLayout(card)
        card_layout.setContentsMargins(15, 15, 15, 15)
        card_layout.setSpacing(10)
        
        profile_image = QLabel()
        profile_image.setFixedSize(80, 80)
        profile_image.setStyleSheet("""
            QLabel {
                background-color: #0078D4;
                border-radius: 40px;
            }
        """)
        card_layout.addWidget(profile_image, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        
        email_label = QLabel(faculty["email"])
        email_label.setStyleSheet("""
            QLabel {
                font: 12pt 'Poppins';
                color: #064420;
                text-align: center;
            }
        """)
        email_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        email_label.setWordWrap(True)
        card_layout.addWidget(email_label)
        
        name_label = QLabel(faculty["name"])
        name_label.setStyleSheet("""
            QLabel {
                font: 14pt 'Poppins';
                color: #000000;
                text-align: center;
            }
        """)
        name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(name_label)
        
        dept_label = QLabel(faculty["department"])
        dept_label.setStyleSheet("""
            QLabel {
                font: 11pt 'Poppins';
                color: #666666;
                text-align: center;
            }
        """)
        dept_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(dept_label)
        

        request_button = QPushButton(faculty["role"])
        request_button.setFixedSize(230, 40)
        active_block = self.Appointment_crud.get_active_block(faculty["id"])
        if active_block and "error" not in active_block:
            request_button.setEnabled(True)
            request_button.setStyleSheet("""
                QPushButton {
                    background-color: #084924;
                    color: white;
                    border-radius: 8px;
                    font: bold 12pt 'Poppins';
                    border: none;
                }
                QPushButton:hover {
                    background-color: #0a5a2f;
                }
                QPushButton:pressed {
                    background-color: #063818;
                }
            """)
        else:
            request_button.setEnabled(False)
            request_button.setToolTip("No available schedule")
            request_button.setText("No available schedule")
            request_button.setStyleSheet("""
                QPushButton {
                    background-color: #E0E0E0;
                    color: black;
                    border-radius: 8px;
                }
            """)
        
        request_button.clicked.connect(lambda checked, f=faculty: self._onRequestClicked(f))
        
        button_container = QtWidgets.QWidget()
        button_layout = QtWidgets.QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.addStretch(1)
        button_layout.addWidget(request_button)
        button_layout.addStretch(1)
        
        card_layout.addWidget(button_container)
        
        return card

    def _onRequestClicked(self, faculty):
        """Handle request button click"""
        print(f"Request appointment with {faculty['name']}")
        try:
            active_block = self.Appointment_crud.get_active_block(faculty["id"])
            if active_block and "error" not in active_block:
                self.go_to_RequestPage.emit(faculty)
            else:
                QMessageBox.information(
                    self,
                    "No Available Schedule",
                    f"{faculty['name']} doesn't have any available schedule at the moment.\n\nPlease check back later or contact the faculty directly."
                )
        except Exception as e:
            print(f"Error checking faculty availability: {e}")
            QMessageBox.warning(
                self,
                "Error",
                f"Failed to check faculty availability: {str(e)}"
            )

    def _previousPage(self):
        if self.current_page > 0:
            self.current_page -= 1
            self._populateFacultiesGrid()

    def _nextPage(self):
        total_pages = (len(self.faculties) + self.items_per_page - 1) // self.items_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self._populateFacultiesGrid()

    def retranslateUi(self):
        self.Academics_5.setText("Faculties")
        faculties_header = self.findChild(QtWidgets.QLabel, "faculties_header")
        if faculties_header:
            faculties_header.setText("See Available Faculties")