import cv2
from cropface import crop_face, crop_face2
from keras.models import load_model
import tensorflow as tf
import face_recognition

tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=1)

model_age1 = load_model('1.hdf5',compile=False)
model_age2 = load_model('2.hdf5',compile=False)
model_age3 = load_model('3.hdf5',compile=False)
model_age4 = load_model('4.hdf5',compile=False)
model_age5 = load_model('5.hdf5',compile=False)
model_age6 = load_model('6.hdf5',compile=False)
model_age7 = load_model('7.hdf5',compile=False)
model_gender = load_model('model_48_gender.hdf5',compile=False)


# Defining a function to create the predicted age overlay on the image by centering the text.

def create_age_text(img, text, gender_str, gender, x, y, w, h):
    # Defining font, scales and thickness.
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    text_scale = 1.1
    yrsold_scale = 0.7
    gender_scale = 0.7

    # Getting width, height and baseline of age text and "years old".
    (text_width, text_height), text_bsln = cv2.getTextSize(text, fontFace=fontFace, fontScale=text_scale, thickness=2)
    (yrsold_width, yrsold_height), yrsold_bsln = cv2.getTextSize("tahun", fontFace=fontFace, fontScale=yrsold_scale,
                                                                 thickness=1)
    (pct_text_width, pct_text_height), pct_text_bsln = cv2.getTextSize(gender_str, fontFace=fontFace,
                                                                       fontScale=gender_scale, thickness=1)

    # Calculating center point coordinates of text background rectangle.
    x_center = x + (w / 2)
    y_text_center = y + h + 38
    y_yrsold_center = y + h + 65
    y_pct_text_center = y + h + 10

    # Calculating bottom left corner coordinates of text based on text size and center point of background rectangle calculated above.
    x_text_org = int(round(x_center - (text_width / 2)))
    y_text_org = int(round(y_text_center + (text_height / 2)))
    x_yrsold_org = int(round(x_center - (yrsold_width / 2)))
    y_yrsold_org = int(round(y_yrsold_center + (yrsold_height / 2)))
    x_pct_text_org = int(round(x_center - (pct_text_width / 2)))
    y_pct_text_org = int(round(y_pct_text_center + (pct_text_height / 2)))

    if gender == 1:
        face_age_background = cv2.rectangle(img, (x - 1, y + h), (x + w + 1, y + h + 90), (150, 0, 0), cv2.FILLED)
    else:
        face_age_background = cv2.rectangle(img, (x - 1, y + h), (x + w + 1, y + h + 90), (0, 150, 0), cv2.FILLED)
    face_age_text = cv2.putText(img, text, org=(x_text_org, y_text_org), fontFace=fontFace, fontScale=text_scale,
                                thickness=2, color=(255, 255, 255), lineType=cv2.LINE_AA)
    yrsold_text = cv2.putText(img, "tahun", org=(x_yrsold_org, y_yrsold_org), fontFace=fontFace, fontScale=yrsold_scale,
                              thickness=1, color=(255, 255, 255), lineType=cv2.LINE_AA)
    pct_age_text = cv2.putText(img, gender_str, org=(x_pct_text_org, y_pct_text_org), fontFace=fontFace,
                               fontScale=gender_scale, thickness=1, color=(255, 255, 255), lineType=cv2.LINE_AA)

    return (face_age_background, pct_age_text, face_age_text, yrsold_text)


# Defining a function to find faces in an image and then classify each found face into age-ranges defined above.

def classify_age(im):
    img = im.copy()

    face_locations = face_recognition.face_locations(img)
    for face_location in face_locations:
        top, right, bottom, left = face_location

        ##gender
        plus = int(0 * abs(top - bottom))
        try:
            face_roi = img[top - plus:bottom + plus, left - plus:right + plus]
        except:
            try:
                face_roi = img[top:bottom, left:right]
            except:
                face_roi = img

        face_roi = cv2.resize(face_roi, (224, 224))
        face_roi = face_roi.reshape(-1, 224, 224, 3)
        gender = model_gender.predict(face_roi) >= 0.5
        gender = gender.astype(int)
        print(gender)

        ##age
        #age1 = model_age1.predict(face_roi)[0][0]
        #age2 = model_age2.predict(face_roi)[0][0]
        #age3 = model_age3.predict(face_roi)[0][0]
        #age4 = model_age4.predict(face_roi)[0][0]
        #age5 = model_age5.predict(face_roi)[0][0]
        age6 = model_age6.predict(face_roi)[0][0]
        #age7 = model_age7.predict(face_roi)[0][0]
        #face_age = str(round((age1+age2+age3+age4+age5+age6+age7)/7))
        face_age = str(round(age6))

        if gender[0][1] == 1:
            face_rect = cv2.rectangle(img, (left, top), (right, bottom), (150, 0, 0), 3)
            gender_str = "laki-laki"
        else:
            face_rect = cv2.rectangle(img, (left, top), (right, bottom), (0, 150, 0), 3)
            gender_str = "perempuan"

        face_age_background, pct_age_text, face_age_text, yrsold_text = create_age_text(img, face_age, gender_str,
                                                                                        gender[0][1], left, top,
                                                                                        abs(left - right),
                                                                                        abs(top - bottom))

    return img

video = cv2.VideoCapture(0)
out = cv2.VideoWriter('output.mp4', -1, 8, (640,480))

while True:
    ret, frame = video.read()

    frame = classify_age(frame[:, :, ::-1])
    out.write(frame[:, :, ::-1])

    cv2.imshow('Gender & Age Detection',frame[:, :, ::-1])
    k = cv2.waitKey(1)
    if k == ord('q'):
       break
video.release()
cv2.destroyAllWindows()
