# AI-Generated Image Detection + XAI Visibility

> A web-based application for detecting whether an image is **real or AI-generated**, with **Explainable AI (XAI)** visualizations to help users understand the model's prediction.

---
 **LIVE DEMO** :https://ai-generated-image-detection-rxkk.onrender.com
## 📌 Overview

**AI-Generated Image Detection + XAI Visibility** is a Django-based machine learning application designed to identify AI-generated images.

The application accepts an uploaded image, processes it using trained deep learning models, and provides a prediction indicating whether the image is **Real** or **AI-Generated**.

To improve transparency, the application also provides **Explainable AI visualizations** using techniques such as **Grad-CAM** and **LIME**, highlighting image regions that contribute to the model's decision.

---

## ✨ Key Features

* 🔐 User Login
* 📝 User Registration / Signup
* 🖼️ Image Upload
* 🤖 AI-Generated Image Detection
* 🧠 CNN-based Image Classification
* 📊 Prediction Confidence
* 🔍 Grad-CAM Visualization
* 🔍 LIME Explanation
* 📈 Model evaluation support
* 🗃️ SQLite database
* 🌐 Django web interface
* ☁️ Deployment-ready configuration for Render
* 📦 Static-file handling with WhiteNoise

---

## 🏗️ Application Workflow

```text
                ┌─────────────────────┐
                │      User Login     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Upload an Image   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Image Preprocessing │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │  CNN Model / Model  │
                │      Prediction     │
                └──────────┬──────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
        ┌─────────────────┐  ┌─────────────────┐
        │ Real / AI-Gen   │  │  XAI Analysis   │
        │   Prediction    │  │ Grad-CAM / LIME │
        └────────┬────────┘  └────────┬────────┘
                 │                    │
                 └──────────┬─────────┘
                            ▼
                  ┌──────────────────┐
                  │  Result Display  │
                  └──────────────────┘
```

---

## 🧩 Main Modules

### 1. User Authentication

Provides:

* User Login
* User Registration
* Username validation
* Email validation
* Password validation
* Duplicate username/email checking

### 2. Image Upload

Users can upload an image through the web interface for analysis.

### 3. Image Classification

The uploaded image is preprocessed and passed to the trained deep learning model.

The system predicts whether the image is:

```text
Real Image
     OR
AI-Generated Image
```

### 4. Explainable AI

The application provides visual explanations for model predictions using:

#### Grad-CAM

Grad-CAM highlights important regions of the image that influenced the CNN prediction.

#### LIME

LIME provides a local explanation by identifying image regions that contribute to the prediction.

---

## 🧠 Machine Learning

The project uses deep learning-based image classification.

### Models / Model Files

The repository contains trained model files including:

```text
model/
├── nasnet_weights.hdf5
├── densenet_weights.hdf5
├── X.npy
└── Y.npy
```

The application uses the trained weights for image classification and prediction.

---

## 🛠️ Technologies Used

### Backend

* Python
* Django
* SQLite
* Gunicorn

### Machine Learning

* TensorFlow
* Keras
* NumPy
* Pandas
* Scikit-learn
* OpenCV
* Scikit-image

### Explainable AI

* Grad-CAM
* LIME

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap / custom styling

### Deployment

* Git
* GitHub
* Render
* Netlify
* WhiteNoise

---

## 📂 Project Structure

```text
Ai-generated-image-detection/
│
├── Detection/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── DetectionApp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── UserLogin.html
│   │   ├── UserSignup.html
│   │   └── ...
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── model/
│   ├── nasnet_weights.hdf5
│   ├── densenet_weights.hdf5
│   ├── X.npy
│   └── Y.npy
│
├── Dataset/
│   └── ...
│
├── testImages/
│   └── ...
│
├── manage.py
├── requirements.txt
├── Procfile
├── render.yaml
├── runtime.txt
├── netlify.toml
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Prerequisites

Make sure the following are installed:

* Python 3.7.x
* Git
* pip

> This project uses an older TensorFlow/Keras environment. Using the specified Python and package versions is recommended for compatibility.

---

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/NityasriNandyala/Ai-generated-image-detection.git
```

Navigate into the project:

```bash
cd Ai-generated-image-detection
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```cmd
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Apply database migrations

```bash
python manage.py migrate
```

---

### 5. Collect static files

```bash
python manage.py collectstatic --noinput
```

---

### 6. Start the Django server

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

If port 8000 is unavailable:

```bash
python manage.py runserver 127.0.0.1:8001
```

---

## 🔐 Login

For the current demonstration setup, the application supports:

```text
Username: admin
Password: admin
```

> For production deployment, replace demonstration credentials with a secure authentication implementation and environment-based configuration.

---

## 🖼️ Image Detection

### Steps

1. Open the application.
2. Log in.
3. Navigate to the image detection page.
4. Upload an image.
5. Submit the image for analysis.
6. The model processes the image.
7. View the prediction.
8. View the Grad-CAM and LIME explanations.

---

## 📊 Prediction Output

The application provides information such as:

```text
Prediction:
AI-Generated Image

Confidence:
XX.XX%
```

The exact output depends on the trained model and input image.

---

## 🔍 Explainable AI Output

### Grad-CAM

Grad-CAM generates a heatmap showing areas that contributed strongly to the CNN's prediction.

```text
Original Image
      ↓
CNN Prediction
      ↓
Grad-CAM
      ↓
Important Image Regions
```

### LIME

LIME provides a local explanation of the model's prediction by identifying influential image regions.

---

## 🗄️ Database

The project uses **SQLite** during local development.

Database configuration is handled through Django's settings.

The local database file:

```text
db.sqlite3
```

is excluded from Git using `.gitignore`.

---

## 🔒 Environment Variables

Production configuration should use environment variables instead of storing secrets directly in source code.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=.onrender.com,.netlify.app
```

Do not commit `.env` files or production secrets to GitHub.

---

## ☁️ Deployment

The project includes deployment configuration for cloud hosting.

### Backend

The Django backend can be deployed using:

**Render**

The repository contains:

```text
Procfile
render.yaml
runtime.txt
```

Example start command:

```bash
gunicorn Detection.wsgi:application
```

### Frontend / Static Hosting

The project also contains:

```text
netlify.toml
```

for Netlify configuration.

The Django backend should remain responsible for:

* Image processing
* Machine learning inference
* XAI processing
* Database operations
* API/backend functionality

---

## 📦 Important Model Files

The following model/data files are included in the repository:

```text
model/nasnet_weights.hdf5
model/densenet_weights.hdf5
model/X.npy
model/Y.npy
```

`model/X.npy` is larger than GitHub's recommended 50 MB file size, although it is below GitHub's hard 100 MB individual-file limit.

For larger future model files, consider using **Git LFS** or external model storage.

---

## 🧪 Testing

Test images can be found in:

```text
testImages/
```

The project also contains supporting testing files and datasets.

For Django configuration checks:

```bash
python manage.py check
```

Expected result:

```text
System check identified no issues.
```

---

## 🛡️ Security Notes

Before production deployment:

* Change demonstration login credentials.
* Set `DEBUG=False`.
* Use a strong production `SECRET_KEY`.
* Store secrets in environment variables.
* Configure production database storage.
* Configure secure file-upload validation.
* Restrict allowed hosts.
* Configure HTTPS.
* Review authentication and authorization.
* Avoid storing sensitive user data unnecessarily.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Detect AI-generated images.
2. Provide an easy-to-use image analysis interface.
3. Use deep learning for image classification.
4. Improve model transparency using XAI.
5. Visualize important regions using Grad-CAM.
6. Provide local explanations using LIME.
7. Demonstrate an end-to-end machine learning web application.

---

## 🔮 Future Enhancements

Potential future improvements include:

* REST API for image detection
* Improved model architectures
* Support for additional AI-generated image types
* Model confidence calibration
* User detection history
* Downloadable analysis reports
* Improved authentication and authorization
* Cloud database integration
* Object storage for uploaded images
* Docker deployment
* Automated CI/CD
* Model version management
* Advanced XAI visualizations

---

## 👩‍💻 Project Information

**Project:** AI-Generated Image Detection + XAI Visibility

**Technology:** Python | Django | TensorFlow | Keras | CNN | Grad-CAM | LIME

**Project Type:** Machine Learning / Web Application

**Developer:** Nitya Sri Nandyala

---

## 📄 License

This project is intended for educational and demonstration purposes.

If you plan to use, modify, or redistribute the project, add an appropriate license and verify the licensing requirements of the datasets, pretrained models, and third-party libraries used.

---

## ⭐ Acknowledgements

This project uses open-source technologies and libraries including:

* Django
* TensorFlow
* Keras
* NumPy
* Pandas
* Scikit-learn
* OpenCV
* LIME
* WhiteNoise
* Gunicorn

---

## 📬 Contact

**Nitya Sri Nandyala**

* GitHub: `NityaSri165`
* LinkedIn: `NITYA SRI NANDYALA`
* Email: `nandyalanityasri99@gmail.com`

---

**If you find this project useful, consider giving the repository a ⭐ on GitHub.**
