from PIL import Image
import os, glob, numpy as np
import os 
from sklearn.model_selection import train_test_split


caltech_dir = "C:/Users/sam56/Desktop/CNN/img"
categories = ["개","고양이","달력","대학교","음식","모자","비행기","새","십자가","아이유","아파트","오토바이","자동차","책","컴퓨터"]
nb_classes = len(categories)

image_w = 64
image_h = 64

pixels = image_h * image_w * 3

X = []
y = []

for idx, cat in enumerate(categories):
    
    #one-hot 돌리기.
    label = [0 for i in range(nb_classes)]
    label[idx] = 1

    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir+"/*.jpg")
    print(cat, " 파일 길이 : ", len(files))
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)

        X.append(data)
        y.append(label)

        if i % 700 == 0:
            print(cat, " : ", f)

X = np.array(X)
y = np.array(y)
#1 0 0 0 이면 airplanes
#0 1 0 0 이면 buddha 이런식


X_train, X_test, y_train, y_test = train_test_split(X, y)
xy = (X_train, X_test, y_train, y_test)
np.save("C:/Users/sam56/Desktop/CNN/multi_image_data.npy", xy)

print("ok", len(y))

import os, glob, numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt
import keras.backend.tensorflow_backend as K

import tensorflow as tf
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True

import numpy as np
# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

X_train, X_test, y_train, y_test = np.load('C:/Users/sam56/Desktop/CNN/multi_image_data.npy')

# restore np.load for future normal usage
np.load = np_load_old

print(X_train.shape)
print(X_train.shape[0])

categories = ["개","고양이","달력","대학교","음식","모자","비행기","새","십자가","아이유","아파트","오토바이","자동차","책","컴퓨터"]
nb_classes = len(categories)

#일반화
X_train = X_train.astype(float) / 255
X_test = X_test.astype(float) / 255


with K.tf_ops.device('/device:CPU:0'):
    model = Sequential()
    model.add(Conv2D(32, (3,3), padding="same", input_shape=X_train.shape[1:], activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Conv2D(64, (3,3), padding="same", activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes, activation='softmax'))
    #model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
    model_dir = './model'
    
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)
    
    model_path = model_dir + '/multi_img_classification.model'
    #model_path = model_dir + 'img_classify_categorical.model'
    checkpoint = ModelCheckpoint(filepath=model_path , monitor='val_loss', verbose=1, save_best_only=True)
    early_stopping = EarlyStopping(monitor='val_loss', patience=6)

history = model.fit(X_train, y_train, batch_size=50, epochs=50, validation_data=(X_test, y_test), callbacks=[checkpoint, early_stopping])

model.summary()

print("정확도 : %.4f" % (model.evaluate(X_test, y_test)[1]))

y_vloss = history.history['val_loss']
y_loss = history.history['loss']

x_len = np.arange(len(y_loss))

plt.plot(x_len, y_vloss, marker='.', c='red', label='val_set_loss')
plt.plot(x_len, y_loss, marker='.', c='blue', label='train_set_oss')
plt.legend()
plt.xlabel('epochs')
plt.ylabel('loss')
plt.grid()
plt.show()


from PIL import Image
import os, glob, numpy as np
from keras.models import load_model

caltech_dir = r"C:\Users\sam56\Desktop\CNN\test"
image_w = 64
image_h = 64

pixels = image_h * image_w * 3

X = []
filenames = []
files = glob.glob(caltech_dir+"/*.*")
for i, f in enumerate(files):
    img = Image.open(f)
    img = img.convert("RGB")
    img = img.resize((image_w, image_h))
    data = np.asarray(img)
    filenames.append(f)
    X.append(data)

X = np.array(X)
model = load_model('./model/multi_img_classification.model')

prediction = model.predict(X)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
cnt = 0

#이 비교는 그냥 파일들이 있으면 해당 파일과 비교. 카테고리와 함께 비교해서 진행하는 것은 _4 파일.
for i in prediction:
    pre_ans = i.argmax()  # 예측 레이블
    print(i) 
    print(pre_ans)
    pre_ans_str = '' #"개","고양이","달력","대학교","맛집","모자","비행기","새","십자가","아이유","아파트","오토바이","자동차","책","컴퓨터"
    if pre_ans == 0: pre_ans_str = "개"
    elif pre_ans == 1: pre_ans_str = "고양이"
    elif pre_ans == 2: pre_ans_str = "달력"
    elif pre_ans == 3: pre_ans_str = "대학교"
    elif pre_ans == 4: pre_ans_str = "음식"
    elif pre_ans == 5: pre_ans_str = "모자"
    elif pre_ans == 6: pre_ans_str = "비행기"
    elif pre_ans == 7: pre_ans_str = "새"
    elif pre_ans == 8: pre_ans_str = "십자가"
    elif pre_ans == 9: pre_ans_str = "아이유"
    elif pre_ans == 10: pre_ans_str = "아파트"
    elif pre_ans == 11: pre_ans_str = "오토바이"
    elif pre_ans == 12: pre_ans_str = "자동차"
    elif pre_ans == 13: pre_ans_str = "책"
    else: pre_ans_str = "컴퓨터"
    if i[0] >= 0.8 : print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[1] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"으로 추정됩니다.")
    if i[2] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[3] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[4] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[5] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[6] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[7] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[8] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[9] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[10] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[11] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[12] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    if i[13] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
    cnt += 1
    # print(i.argmax()) #얘가 레이블 [1. 0. 0.] 이런식으로 되어 있는 것을 숫자로 바꿔주는 것.
    # 즉 얘랑, 나중에 카테고리 데이터 불러와서 카테고리랑 비교를 해서 같으면 맞는거고, 아니면 틀린거로 취급하면 된다.
    # 이걸 한 것은 _4.py에.