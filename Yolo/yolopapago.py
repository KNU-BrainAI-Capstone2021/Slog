import cv2
import numpy as np
 
# Yolo 로드

modelConfiguration= r"C:\Users\PC00\Desktop\SLOG\yolo\yolov4.cfg" 
modelWeights= r"C:\Users\PC00\Desktop\SLOG\yolo\yolov4.weights"
net = cv2.dnn.readNet(modelConfiguration, modelWeights)
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# 이미지 가져오기
img = cv2.imread("baseball.PNG")

img = cv2.resize(img, None, fx=1.0, fy=1.0)
height, width, channels = img.shape
 
# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# 정보를 화면에 표시
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            # 좌표
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
            
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)


output_box=[]
font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        output_box.append(label)
        color = colors[i]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y + 30), font, 2, color, 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

tag = output_box


import requests

def get_translate(tag):
    client_id = "lBCugyrl82R5FinNW3xw" # <-- client_id 기입
    client_secret = "676ai6oqPe" # <-- client_secret 기입

    data = {'text' : tag,
            'source' : 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)


trans = [] 

for i in range(len(tag)):
        
    trans.append(get_translate(tag[i]))


print("이미지해시태그는 다음과 같습니다:", set(trans))

imagehashtag = set(trans)

    
import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration

tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')


text = input('내용을 입력해주세요 : ')

raw_input_ids = tokenizer.encode(text)
input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

summary_ids = model.generate(torch.tensor([input_ids]))
tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)

textresult = tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
print(textresult)

from konlpy.tag import Kkma

kkma = Kkma()

kkma_nouns = kkma.nouns(textresult)

def biggerthanlen2(x):
    return len(x)>1

texthashtag = list(filter(biggerthanlen2,kkma_nouns))

outputlist = set(trans + texthashtag)

print("텍스트해시태그는 다음과 같습니다:", set(texthashtag))

print("최종 추천태그는 다음과 같습니다 :" , outputlist)