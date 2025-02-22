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
📁 Project Root
│── 📁 static                  # Stores static assets (images, CSS, JS, etc.)
│   │── bus.jpg
│   │── kg.png
│   │── kgbus.png
│   │── profile.jpg
│   │── rot1.png
│   │── rot2.png
│   │── rot3.png
│   │── Transport.jpg
│   │── work.png
│
│── 📁 templates copy          # Contains HTML templates for Flask rendering
│   │── about.html
│   │── dashboard.html
│   │── login.html
│   │── map.html
│   │── message.html
│   │── noti.html
│   │── profile.html
│   │── rot.html
│   │── settings.html
│
│── app.py                     # Main Flask application
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

## 📽️DEMO VIDEO LINK
https://drive.google.com/file/d/1KphNVTlRHtROGWSbx2_u5CbFWyl_84Qy/view?usp=drive_link

## PPT of our project
https://drive.google.com/file/d/18w-PtlVfkhcwFeQie8jy_lfzKUvpPby8/view?usp=drive_link

## over all folder of demo video and PPT
https://drive.google.com/drive/folders/1bdBAGTNtmyMk-1ENNH-kQNvQrncUdogG?usp=drive_link

---

🚀 **Developed with ❤️ by [Team Tech_Knox]**

