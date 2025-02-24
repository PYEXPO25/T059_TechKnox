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

## LOGIN PAGE

![Image](https://github.com/user-attachments/assets/2bfda925-ed04-4357-afaf-da1c5a4df62b)

## DASHBOARD

![Image](https://github.com/user-attachments/assets/42d4a805-4faf-4d23-868c-f8a89d5e4290)

## BUTTON SLIDER

![Image](https://github.com/user-attachments/assets/d59eb8df-061b-43cc-a161-39700fd92ca7)

## PROFILE

![Image](https://github.com/user-attachments/assets/fe77fef0-51f2-491d-baf9-38550837ea09)

## LIVE MAP

![Image](https://github.com/user-attachments/assets/08528b69-b9c6-4549-bb8f-e3d3a6dc7b88)

## BUS ROUTES

![Image](https://github.com/user-attachments/assets/3ac1c6c4-471f-4b58-8a38-eae3cda2118f)

## MESSAGE PAGE

![Image](https://github.com/user-attachments/assets/51ea2188-3841-47a4-bab9-df3e32a89624)

## NOTIFICATION PAGE

![Image](https://github.com/user-attachments/assets/ea63b4a4-0f79-4c78-ba6e-d1e8ccd7fe22)

## ABOUT US PAGE

![Image](https://github.com/user-attachments/assets/92fb7cf1-6a85-4edf-bf30-8583724e877d)





---

**👨‍💼 Developed By [Team Tech_Knox]🚀**

