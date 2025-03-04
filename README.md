### **README.md**

# Music Recommendation System Based on Facial Emotions 🎵😊

## Overview
This project is a **Music Recommendation System** that uses **Facial Emotion Recognition** to recommend songs based on the user's mood.

## Project Structure

📁 Project  
│── 📁 Angry         # Songs for the 'Angry' emotion  
│── 📁 Fear          # Songs for the 'Fear' emotion  
│── 📁 Happy         # Songs for the 'Happy' emotion  
│── 📁 Neutral       # Songs for the 'Neutral' emotion  
│── 📁 Sad           # Songs for the 'Sad' emotion  
│── 📁 images        # UI images (icons for play, pause, next, etc.)  
│── 📄 Music.py      # Main Python script for the music player and emotion detection  
│── 📄 README.md     # Project documentation  
│── 📄 requirements.txt  # Python dependencies  

## Features
✔ **Detects facial emotions** using a **Convolutional Neural Network (CNN)**  
✔ **Categorizes emotions** into **Happy, Sad, Angry, Neutral, and Fear**  
✔ **Recommends songs** based on the detected mood  
✔ Uses **OpenCV** for face detection and **Tkinter** for GUI-based music player  
✔ Supports **Telugu songs** for different moods  
✔ Implements **DeepFace and Keras** for emotion recognition  

## Technologies Used
- **Python** (Primary programming language)
- **OpenCV** (Face detection)
- **Keras & TensorFlow** (CNN model for emotion recognition)
- **DeepFace** (Pre-trained facial emotion recognition model)
- **Pygame** (For audio playback)
- **Tkinter** (For GUI-based music player)
- **NumPy & Matplotlib** (For data handling and visualization)


## Installation & Setup
### 1. Clone the Repository
``` sh
git clone https://github.com/yourusername/music-recommendation-system.git
cd music-recommendation-system
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required libraries:
``` sh
pip install -r requirements.txt
```

### 3. Run the Application
Run the Python script to start the music recommendation system:
```sh
python Music.py
```

## Usage
1. The system captures your **facial expression** using a webcam.
2. It classifies your **emotion** (Happy, Sad, Angry, Neutral, or Fear).
3. A **playlist** corresponding to your mood is generated.
4. The built-in **music player** plays songs automatically.
5. You can manually **pause, skip, or adjust volume**.

## Dataset
- The emotion detection model was trained using the **FER2013 dataset**.
- Pre-trained **DeepFace** model helps improve accuracy.

## Possible Enhancements
🔹 Improve accuracy by training on a **larger dataset**  
🔹 Support **more emotions** like *Disgust* and *Surprise*  
🔹 Expand music recommendations to **multiple languages**  
🔹 Develop a **mobile version** (Android/iOS app)  

## Contributors
👤 **Akash Babu Pedapaga**  
  

## License
This project is licensed under the **MIT License**.

