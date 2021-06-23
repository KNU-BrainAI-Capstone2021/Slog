# SLOG 팀 
![슬로그](https://user-images.githubusercontent.com/80320168/119520172-05dc8380-bdb5-11eb-90c0-670155246297.jpg)

SLOG의 뜻 : (시간이 오래 걸리는 힘든지루한 일을) 열심히[묵묵히] 하다 또는 힘겹게[묵묵히] 걷다[다니다]

# 1학기 프로젝트 내용
SNS사용자의 데이터를 분석하여 autotag 프로그램 개발

#인스타그램

<img src="https://user-images.githubusercontent.com/80320168/119504353-d7f04280-bda6-11eb-855c-d841a7730b8d.jpg"  width="400" height="300">

#해쉬태그

<img src="https://user-images.githubusercontent.com/80320168/122916162-8fbd4380-d397-11eb-8fd1-009f7451ed7a.png"  width="400" height="280">

#구성인원: 총 4명

역할|이름|Github ID|
---|---|---|
조장|이승훈|16SeungHun|
조원|정재호|jaeho98|
조원|윤성민|newskyy135|
조원|이지현|ww42777|

# 개념

#WORD2VEC

-CBOW model

<img src="https://user-images.githubusercontent.com/80320168/122943382-efc0e380-d3b1-11eb-87ec-ab9ed4c95a83.png"  width="400" height="280"><img src="https://user-images.githubusercontent.com/80320168/122943596-1e3ebe80-d3b2-11eb-9072-9a58bba17d69.png" width="400" height="250">

-Skip gram model

<img src="https://user-images.githubusercontent.com/80320168/122943826-4fb78a00-d3b2-11eb-8ab9-e5ff0cae559e.png" width="400" height="280"><img src="https://user-images.githubusercontent.com/80320168/122945821-cef98d80-d3b3-11eb-8cbd-e67cf0afec42.png" width="400" height="250">

# 준비과정

#웹드라이버인 chromedriver.exe 설치

<img src="https://user-images.githubusercontent.com/80320168/122917316-de1f1200-d398-11eb-8b75-ad014d8ed9c4.png"  width="500" height="250">

#import할 라이브러리 사전 준비

-Beautiful Soup와 Selenium을 설치하고, 진행하면서 필요한 라이브러리 추가로 설치한다.

![준비과정최종](https://user-images.githubusercontent.com/80320168/122919704-803ff980-d39b-11eb-9a95-de0d4a1faa8c.jpg)

# 진행과정

#자동로그인과 자동으로 태그를 검색하기

![자동로그인](https://user-images.githubusercontent.com/80320168/119519066-13453e00-bdb4-11eb-8243-11c7bc1e3ed1.gif)

#인스타그램 게시물을 크롤링하기

![ezgif com-gif-maker](https://user-images.githubusercontent.com/80320168/119503688-34069700-bda6-11eb-9eaa-943547a03576.gif)

#태그분석을 위한 워드클라우드 출력하기

<img src="https://user-images.githubusercontent.com/80320168/119524340-8355c300-bdb8-11eb-9393-1c24ad3fcce4.png"  width="550" height="450">

#자동로그인과 다운받고 싶은 이미지의 태그를 입력하여 첫페이지의 사진을 자동으로 다운받아 지정된 폴더에 태그이름+숫자 형태로 자동 저장하기

![ezgif com-gif-maker](https://user-images.githubusercontent.com/80320168/122638602-035d1780-d130-11eb-9d32-b3a73187138c.gif)

#csv파일을 열었을 때 한글 안 나오는 문제 해결하기

![한글나옴](https://user-images.githubusercontent.com/80320168/122915759-11f93800-d397-11eb-85d4-2c8d5c996f1b.gif)



날짜| 요약|
---|---|
1/16|팀 이름 및 조장 정하기|
3/7|1차 회의 및 아이디어 찾기|
3/8|교수님과 1차 상담|
3/22|스터디|
3/30|팀 회식 및 친목 도모|
4/13|스터디|
4/28|2차 회의 및 아이디어 구상, 선행조사|
5/1|ppt만들기|
5/7|교수님 팀미팅(발표자 이승훈)|
5/12|온라인 미팅(발표자 윤성민)|
5/20|팀미팅 예행연습|
5/25|조교님과 논의|

#매일 해결중인 과제 주제

날짜| 내용|
---|---|
~5.9|MNIST 손글씨 인식하기(CNN사용)|
5.10|주어진 데이터로 폐암환자 생존률 예측하기|
~5.18|직접 인스타그램 크롤러 만들기(자동로그인,자동댓글,태그입력시 자동으로 이미지
5.20|회의를 통해 서로 공부한 부분 공유|
5.25|발표전 코드 수정&연습|
6.18|웹크롤러 코드 다시짜기|
6.19|텍스트크롤러 코드 완성|
6.20|데이터를 바탕으로 cnn완성|
6.22|word2vec 코드 완성|

# 깃허브 소스코드 파일

자료| 내용|
---|---|
[new 이미지 크롤러.py](https://github.com/KNU-BrainAI-Capstone2021/Slog/blob/main/%EC%9D%B8%EC%8A%A4%ED%83%80%EA%B7%B8%EB%9E%A8%20%ED%81%AC%EB%A1%A4%EB%9F%AC/new%20%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%81%AC%EB%A1%A4%EB%9F%AC.py)|인스타그램 이미지 다운(image download)|
[텍스트크롤링 최종본(업로드용).py](https://github.com/KNU-BrainAI-Capstone2021/Slog/blob/main/%EC%9D%B8%EC%8A%A4%ED%83%80%EA%B7%B8%EB%9E%A8%20%ED%81%AC%EB%A1%A4%EB%9F%AC/%ED%85%8D%EC%8A%A4%ED%8A%B8%ED%81%AC%EB%A1%A4%EB%A7%81%20%EC%B5%9C%EC%A2%85%EB%B3%B8(%EC%97%85%EB%A1%9C%EB%93%9C%EC%9A%A9).py)|텍스트 크롤링(text crawler)|
[cnn학습.py](https://github.com/KNU-BrainAI-Capstone2021/Slog/blob/main/cnn%ED%95%99%EC%8A%B5.py)|이미지의 CNN 학습|
