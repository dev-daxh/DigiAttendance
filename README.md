# DigiAttendance

DigiAttendance is an innovative attendance management system designed for educational institutions. It leverages QR codes, location verification, and secure authentication to streamline the attendance process, prevent proxy attendance, and provide real-time updates and insights.

## Features

1. **🔄 Dynamic QR Codes**: Faculty generates time-limited QR codes for students to scan.
2. **🔐 Two-Step Authentication**: Secure access using registered mobile numbers and PIN/password.
3. **📍 Location and Bluetooth Verification**: Ensures physical presence during attendance marking.
4. **📊 Real-Time Data Updates**: Attendance data is instantly updated in a centralized database.
5. **🗓️ Monthly Reporting**: Generate comprehensive attendance reports based on selected date ranges.
6. **📧 Automated Alerts**: System sends personalized email alerts for attendance shortages.
7. **📈 Scalability**: Suitable for institutions of all sizes, from small colleges to large universities.
8. **🔒 Enhanced Security**: Tamper-proof records using secure data storage methods.
9. **🔑 Forgot Password**: Users can recover their password if forgotten.
10. **🕒 Time Limit for Scanning QR Code**: QR codes are valid for a specified duration.
    - ⏳ **Time-Limited QR Codes**: Faculty can generate QR codes that are valid for a specified duration (e.g., 25 seconds).
11. **📊 Attendance Viewing for Faculty**: Faculty can view attendance records conveniently.
    - 📈 **Attendance Monitoring**: Faculty can easily monitor attendance updates in an Excel sheet format with timestamps.

## Technology Stack

- **🐍 Python**: Core programming language for developing the application.
- **🖼️ Tkinter**: GUI library for creating the application interface.
- **🐬 MySQL**: Database for storing attendance records.
- **📊 Excel**: For generating and exporting attendance reports.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/itz-daxh94/DigiAttendance

2. **Install the required Python libraries:**
   ```sh
   pip install -r requirements.txt

3. **Set up MySQL:**
   - Install MySQL and create a database.
   - Import the provided SQL file to set up the necessary tables as mentioned in database_schema.txt.
   - Update the database connection settings in the application.
4. **Run the application:**
```sh
   python welcome.py
```
## Usage

1. **👩‍🏫 Faculty**:
   - 🔑 Log in with your credentials.
   - 📷 Generate a QR code for attendance.
   - ⏲️ Set a time limit for the QR code.
   - 🖥️ Display the QR code on a digital board via Projector with new Technology.
   - 📈 Monitor real-time attendance updates in the Excel Sheet with timestamps.

2. **🎓 Students**:
   - 🔑 Log in with your credentials.
   - 📲 Scan the QR code displayed by the faculty within the time limit.
   - 📍 Ensure your location and Bluetooth are enabled for verification.

## Contribution

🎉 Contributions are welcome! Please fork the repository and submit a pull request for review.

## Contact

📬 For more information or queries, please contact us at [support@devdakshtit@gmail.com](mailto:devdakshtit@gmail.com)
