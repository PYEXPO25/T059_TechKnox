# College Bus Live Location Tracking

## 📌 Project Overview
This project is a **live location tracking system for college buses**, utilizing an **ESP-32 microcontroller**, **NEO-6M GPS module**, and **Flask** backend. The system fetches real-time GPS coordinates and transmits them to a web-based interface for tracking.

## 🛠️ Tech Stack
### **Hardware**
- **ESP-32** – Microcontroller to process GPS data
- **NEO-6M GPS Module** – For fetching location coordinates

### **Software**
- **Flask (Python)** – Backend to handle GPS data
- **Frontend (TBD)** – Web interface for live tracking
- **MQTT/HTTP** – Communication between ESP-32 and Flask
- **Google Maps API / Leaflet.js** – Map visualization

## 📂 Project Structure
```
📁 college-bus-tracker
│── 📂 backend            # Flask backend
│   │── app.py           # Main Flask application
│   │── requirements.txt # Dependencies
│   │── config.py        # Configuration settings
│   └── ...
│
│── 📂 esp32_firmware     # ESP-32 firmware
│   │── main.py          # Code to read GPS and send data
│   └── ...
│
│── 📂 frontend           # Web application
│   │── index.html       # Main UI
│   │── app.js          # Handles frontend logic
│   │── styles.css      # Styling
│   └── ...
│
│── README.md             # Project documentation
└── LICENSE               # License file
```

## 🚀 Features
- **Live GPS Tracking** – Updates in real-time
- **ESP-32 Integration** – Fetches and transmits GPS data
- **Flask API** – Backend processes and serves GPS data
- **Interactive Map** – Displays bus location
- **Responsive UI** – Works on mobile and desktop

## 🔧 Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/college-bus-tracker.git
cd college-bus-tracker
```

### **2️⃣ Setup the Backend**
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### **3️⃣ Flash ESP-32 with Firmware**
1. Connect ESP-32 to your computer.
2. Upload `main.py` from the `esp32_firmware` folder.
3. Ensure WiFi credentials and server URL are correctly set.

### **4️⃣ Run the Frontend**
Simply open `index.html` in a browser or set up a local web server.

## 📡 Data Flow
1. **ESP-32** reads GPS data.
2. Data is sent to the **Flask server** via HTTP/MQTT.
3. **Flask processes** the data and updates the database (if needed).
4. The **frontend fetches** the data and updates the map in real-time.

## 🎯 Future Enhancements
- User authentication for access control
- Multiple bus tracking
- Database integration for route history
- Mobile app version

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🚀 **Developed with ❤️ by [Your Name]**

