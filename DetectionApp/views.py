from django.shortcuts import render
from django.http import HttpResponse

from keras.models import load_model, Model
from keras.layers import AveragePooling2D, Dropout, Flatten, Dense, Input, Activation
from keras.layers import MaxPooling2D, Convolution2D

from lime import lime_image
from skimage.segmentation import mark_boundaries

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import cv2
import numpy as np
import io
import base64
import os


global username

explainer = lime_image.LimeImageExplainer()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def getGradCam(img, model):
    feature_model = Model(model.inputs, model.layers[-7].output)

    predict = feature_model.predict(img)
    predict = predict[0]

    pred = predict[:, :, 24]
    pred = pred * 255

    pred = cv2.resize(pred, (150, 150))

    return pred


def classifyImage(image_path, nasnet_model):
    image = cv2.imread(image_path)

    img = cv2.resize(image, (32, 32))

    im2arr = np.array(img)
    im2arr = im2arr.reshape(1, 32, 32, 3)

    img = np.asarray(im2arr)
    img = img.astype('float32')
    img = img / 255

    predict = nasnet_model.predict(img)
    predict = np.argmax(predict)

    status = 'Real'

    if predict == 0:
        status = 'Fake'

    grad_cam = getGradCam(img, nasnet_model)

    explanation = explainer.explain_instance(
        img[0],
        nasnet_model.predict
    )

    temp, mask = explanation.get_image_and_mask(
        explanation.top_labels[0],
        positive_only=True,
        num_features=5,
        hide_rest=False
    )

    lime_marking = mark_boundaries(
        temp / 2 + 0.5,
        mask
    )

    lime_marking = cv2.resize(
        lime_marking,
        (150, 150),
        interpolation=cv2.INTER_LANCZOS4
    )

    image = cv2.imread(image_path)
    image = cv2.resize(image, (150, 150))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    cv2.putText(
        image,
        status,
        (10, 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    f, axarr = plt.subplots(
        1,
        3,
        figsize=(8, 4)
    )

    axarr[0].imshow(image)
    axarr[0].title.set_text('Input Image')

    axarr[1].imshow(grad_cam)
    axarr[1].title.set_text('Grad Cam Image')

    axarr[2].imshow(lime_marking)
    axarr[2].title.set_text('Lime Explanation Image')

    plt.axis('off')

    buf = io.BytesIO()

    plt.savefig(
        buf,
        format='png',
        bbox_inches='tight'
    )

    plt.close()

    img_b64 = base64.b64encode(
        buf.getvalue()
    ).decode()

    return img_b64


def SingleImage(request):
    if request.method == 'GET':
        return render(
            request,
            'SingleImage.html',
            {}
        )


def SingleImageAction(request):
    if request.method == 'POST':

        filename = request.FILES['t1'].name

        image = request.FILES['t1'].read()

        static_dir = os.path.join(
            BASE_DIR,
            'DetectionApp',
            'static'
        )

        os.makedirs(
            static_dir,
            exist_ok=True
        )

        save_path = os.path.join(
            static_dir,
            filename
        )

        if os.path.exists(save_path):
            os.remove(save_path)

        with open(save_path, 'wb') as f:
            f.write(image)

        model_path = os.path.join(
            BASE_DIR,
            'model',
            'nasnet_weights.hdf5'
        )

        model = load_model(model_path)

        img_b64 = classifyImage(
            save_path,
            model
        )

        context = {
            'data': 'Detection Output',
            'img': img_b64
        }

        return render(
            request,
            'UserScreen.html',
            context
        )


def UserLoginAction(request):
    if request.method == 'POST':

        global username

        username = request.POST.get(
            't1',
            False
        )

        password = request.POST.get(
            't2',
            False
        )

        if username == 'admin' and password == 'admin':

            context = {
                'data': 'Welcome ' + username
            }

            return render(
                request,
                'UserScreen.html',
                context
            )

        else:

            context = {
                'data': 'Invalid username'
            }

            return render(
                request,
                'UserLogin.html',
                context
            )


def UserLogin(request):
    if request.method == 'GET':
        return render(
            request,
            'UserLogin.html',
            {}
        )


def index(request):
    if request.method == 'GET':
        return render(
            request,
            'index.html',
            {}
        )

def UserSignup(request):
    if request.method == 'GET':
        return render(
            request,
            'UserSignup.html',
            {}
        )


def UserSignupAction(request):
    if request.method == 'POST':
        from DetectionApp.models import UserSignup as UserSignupModel

        full_name = request.POST.get('t1', '').strip()
        email = request.POST.get('t2', '').strip()
        new_username = request.POST.get('t3', '').strip()
        password = request.POST.get('t4', '').strip()
        confirm_password = request.POST.get('t5', '').strip()

        # --- Validation ---
        if not all([full_name, email, new_username, password, confirm_password]):
            context = {'data': 'All fields are required.', 'error': True}
            return render(request, 'UserSignup.html', context)

        if password != confirm_password:
            context = {'data': 'Passwords do not match.', 'error': True}
            return render(request, 'UserSignup.html', context)

        if len(password) < 6:
            context = {'data': 'Password must be at least 6 characters.', 'error': True}
            return render(request, 'UserSignup.html', context)

        if UserSignupModel.objects.filter(username=new_username).exists():
            context = {'data': 'Username already taken. Please choose another.', 'error': True}
            return render(request, 'UserSignup.html', context)

        if UserSignupModel.objects.filter(email=email).exists():
            context = {'data': 'An account with this email already exists.', 'error': True}
            return render(request, 'UserSignup.html', context)

        # --- Save user ---
        import hashlib
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()

        user = UserSignupModel(
            username=new_username,
            email=email,
            password=hashed_pw,
        )
        user.save()

        context = {
            'data': 'Account created successfully! You can now log in.',
            'error': False
        }
        return render(request, 'UserLogin.html', context)
