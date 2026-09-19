# AI-Generated Image Detection App
## CNN + Grad-CAM + LIME Explainability

---

## PART 1 — Run Locally on Windows

### Step 1: Install Python 3.7.9
1. Go to: https://www.python.org/downloads/release/python-379/
2. Download **Windows installer (64-bit)**
3. Run installer — CHECK the box **Add Python 3.7 to PATH**
4. Click Install Now

### Step 2: Run the App
1. Navigate to: C:\AIDetect
2. Double-click **un_local.bat**
3. First run will auto-install all dependencies (~10-15 min)
4. When you see Starting development server, open your browser:

`
http://127.0.0.1:8000/DetectionApp/index.html
`

### Step 3: Use the App
- Login: **admin** / **admin**
- Click **Single Image Detection**
- Upload any image from 	estImages/ folder
- See the Grad-CAM and LIME explanations

---

## PART 2 — Deploy to Render.com (Backend) + Netlify (Public URL)

### Prerequisites
- GitHub account (free): https://github.com
- Render.com account (free): https://render.com
- Netlify account (free): https://netlify.com

---

### Step A: Push Code to GitHub

1. Install Git: https://git-scm.com/download/win
2. Open Command Prompt in C:\AIDetect and run:

`ash
git init
git add .
git commit -m Initial commit - AI Detection App
`

3. Create a new repository on GitHub.com (name it i-detection-app)
4. Copy the remote URL and run:

`ash
git remote add origin https://github.com/YOUR-USERNAME/ai-detection-app.git
git push -u origin main
`

> NOTE: The model .hdf5 files are ~640MB total.
> For GitHub (100MB limit per file), use Git LFS:
> Run: git lfs install && git lfs track *.hdf5 *.npy
> Then: git add .gitattributes && git add . && git commit -m Add LFS files && git push

---

### Step B: Deploy Backend to Render.com

1. Go to https://render.com and sign in
2. Click **New** → **Web Service**
3. Connect your GitHub repo i-detection-app
4. Fill in settings:
   - **Name**: i-detection-app
   - **Runtime**: Python 3
   - **Build Command**: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   - **Start Command**: gunicorn Detection.wsgi --log-file -
5. Under **Environment Variables**, add:
   - SECRET_KEY = (any random long string)
   - DEBUG = False
   - ALLOWED_HOSTS = *.onrender.com
6. Click **Create Web Service**
7. Wait ~5-10 minutes for first deploy
8. Your app URL will be: https://ai-detection-app.onrender.com

---

### Step C: Update netlify.toml

Edit C:\AIDetect\netlify.toml:
- Replace YOUR-APP.onrender.com with your actual Render URL
- Commit and push to GitHub

---

### Step D: Deploy Frontend to Netlify

1. Go to https://netlify.com and sign in
2. Click **Add new site** → **Import an existing project**
3. Connect GitHub → select your i-detection-app repo
4. Build settings:
   - **Publish directory**: . (root — leave blank or use .)
   - Build command: leave empty
5. Click **Deploy site**
6. Your public Netlify URL will be: https://your-site.netlify.app

---

## App Credentials
| Field    | Value  |
|----------|--------|
| Username | admin  |
| Password | admin  |

## Project Structure
`
C:\AIDetect\
├── manage.py              # Django entry point
├── requirements.txt       # Python dependencies
├── Procfile               # Render.com start command
├── runtime.txt            # Python version for Render
├── render.yaml            # Render auto-deploy config
├── netlify.toml           # Netlify proxy config
├── run_local.bat          # Double-click to run locally
├── Detection/             # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── DetectionApp/          # Main app
│   ├── views.py           # ML logic (CNN + LIME + Grad-CAM)
│   ├── urls.py
│   ├── models.py
│   └── templates/         # HTML pages
├── model/
│   ├── nasnet_weights.hdf5  # Trained CNN model
│   └── densenet_weights.hdf5
└── testImages/            # Sample images to test
`
