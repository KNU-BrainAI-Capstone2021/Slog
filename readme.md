# SLOG 팀 
![슬로그](https://user-images.githubusercontent.com/80320168/119520172-05dc8380-bdb5-11eb-90c0-670155246297.jpg)

SLOG의 뜻 : (시간이 오래 걸리는 힘든지루한 일을) 열심히[묵묵히] 하다 또는 힘겹게[묵묵히] 걷다[다니다]

# 1학기 프로젝트
SNS사용자의 데이터를 분석하여 autotag 프로그램 개발

[1학기 졸업프로젝트](https://github.com/KNU-BrainAI-Capstone2021/Slog/blob/main/1%ED%95%99%EA%B8%B0readme.md)

# 2학기 프로젝트 내용
1학기 프로젝트때 구현한 크롤러를 바탕으로 SNS에서 사진을 받아와서 학습시키고, YOLOv5를 이용해 object detection 기술을 활용하여 autotagging 을 고안한다.


#구성인원: 총 5명

역할|이름|Github ID|
---|---|---|
조장|이승훈|16SeungHun|
조원|정재호|jaeho98|
조원|윤성민|newskyy135|
조원|이지현|ww42777|
조원|김영호|yeongho24|

# 개념


# 진행과정

#인스타그램 게시물을 크롤링하기

![ezgif com-gif-maker](https://user-images.githubusercontent.com/80320168/119503688-34069700-bda6-11eb-9eaa-943547a03576.gif)

![ezgif com-gif-maker](https://user-images.githubusercontent.com/80320168/122638602-035d1780-d130-11eb-9d32-b3a73187138c.gif)

#매일 해결중인 과제 주제

날짜| 요약|
---|---|
9/1|2학기 첫 팀미팅|
9/13|주차별 계획 확립|
9/27|YOLO V5모델 |

# 사용한 기술들
### Computer Vision For Image Hashtag
![image](https://user-images.githubusercontent.com/79971467/143189410-7ece86b7-4a08-4910-8f23-8126ff9f9785.png)

위의 그림은 이미지 해시태그를 추출하는 과정의 구조도입니다. 
유저가 사진을 input으로 넣으면, yolov4가 object detection을 실시하게 됩니다.


![image](https://user-images.githubusercontent.com/79971467/143190361-1fbb7e3f-773c-407f-ae07-2688a3388659.png)

이후 나온 labels들을 한국어로 바꿔주기 위하여 파파고 api를 추가하였습니다.
(label 프로그램은 영어로만 class 이름들을 저장 할 수 있기 때문입니다.)

### Natural Language Processing For Text Hashtag
![image](https://user-images.githubusercontent.com/79971467/143189971-d2fbda83-79d2-429d-a45f-d7b59cbd59f9.png)

위의 그림은 텍스트 해시태그를 추출하는 과정의 구조도입니다.
유저가 텍스트를 input으로 넣으면, kobart가 summarization을 실시하게 되고, 이후 나온 요약문장에서 KKMA Tokenizer를 이용하여 Nouns만 추출하여 output으로 제시합니다. 추가로 한 글자는 제거하는 기능을 추가했습니다.

![image](https://user-images.githubusercontent.com/79971467/143190613-0bd8ffe9-c0a2-4cb4-a2b9-9cc9b98dd98d.png)

kobart는 기존의 BERT와 GPT의 단점들을 보완한 모델로써, 주어진 텍스트를 요약하기 위해 사용했습니다.

![image](https://user-images.githubusercontent.com/79971467/143190732-e19842f1-a5fb-44d8-90a9-7cfa85e92167.png)

요약된 문장에서 명사만 추출하기 위하여 저희는 KKMA tokenizer를 이용했습니다.

### Sum Image + Text hashtag
![image](https://user-images.githubusercontent.com/79971467/143190163-4134f3f3-28e4-46b4-add7-fc374719ac94.png)

위의 그림은 두가지 해시태그를 더해서 중복을 제거하고 최종 해시태그를 제시하는 구조도입니다.
이 과정의 결과값이 사용자에게 보여집니다.

### Full Structure
![해시태그 구조 최종](https://user-images.githubusercontent.com/79971467/143190839-83c96b04-3b7c-4c8e-91c1-afef1b041d0e.png)

전체 구조도입니다.

# To Make Application - 윤성민

