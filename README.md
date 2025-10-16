[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HS6nBbT4)
# Dialogue Summarization | 일상 대화 요약
<br>

## 프로젝트 소개

### <프로젝트 소개>

- 학교 생활, 직장, 치료, 쇼핑, 여가, 여행 등 광범위한 일상 생활 중 하는 대화들에 대해 요약합니다.

## Team

| ![김수환](https://github.com/user-attachments/assets/bfe05d23-81d0-4409-aca9-b1bb1fb5107f) | ![김명철](https://github.com/user-attachments/assets/0c545d12-539f-419d-816a-a0e4263cc0b2) | ![김상윤](https://github.com/user-attachments/assets/5bd23640-3d34-4292-bc81-e202136a1b6f) | ![김광묵](https://github.com/user-attachments/assets/5aee2fa3-df3c-4183-a780-f2028ad613ca) | ![장윤정](https://github.com/user-attachments/assets/bee0c0c4-ae06-4477-8ea6-a3cdaf2b00f8) |
| :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: |
|            [김수환](https://github.com/suhwankimkim)             |            [김명철](https://github.com/qpwpep)             |            [김상윤](https://github.com/94KSY)             |            [김광묵](https://github.com/JackFink)             |            [장윤정](https://github.com/yjjang06)             |
|                            팀장, <br>실험환경 구성 및 모델 개발                             |                            모델 개발                             |                            모델 개발                             |                            모델 개발                             |                            모델 개발                             |

<br>

<br>

## 0. Overview

### Environment

- Python 3.10

### Requirements

```
pandas==2.1.4
numpy==1.23.5
wandb==0.16.1
tqdm==4.66.1
pytorch_lightning==2.1.2
transformers[torch]==4.35.2
rouge==1.0.1
jupyter==1.0.0
jupyterlab==4.0.9
```

<br>

## 3. 구현 기능

### 기능1

- _작품에 대한 주요 기능을 작성해주세요_

### 기능2

- _작품에 대한 주요 기능을 작성해주세요_

### 기능3

- _작품에 대한 주요 기능을 작성해주세요_

<br>

## 4. 작품 아키텍처(필수X)
- #### _아래 이미지는 예시입니다_
![이미지 설명](https://www.cadgraphics.co.kr/UPLOAD/editor/2024/07/04//2024726410gH04SyxMo3_editor_image.png)

<br>

## 5. Experiment

## 5. 트러블 슈팅

### 1. OOO 에러 발견

#### 설명
- _프로젝트 진행 중 발생한 트러블에 대해 작성해주세요_

#### 해결
- _프로젝트 진행 중 발생한 트러블 해결방법 대해 작성해주세요_

### Presentation

- [AI-부트캠프-14기.pptx]()

## etc

### Meeting Log
오전오후 유기적인 미팅으로 진행상황 및 이슈사항 공유

|날짜|회의 내용|
|-----|-----|
||• Team Building|
|2025-10-01|• 서버 생성 및 환경 구축, Baseline실행 및 submission 파일 제출<br>• train, test set에 대한 EDA 진행|
|2025-10-10|• EDA 진행 내용 공유<br>• Hydra, wandb 등 실험 환경 구축에 대한 내용 논의|
|2025-10-13 (2회)|• 각자 실험을 위한 코드 개발 및 실험 진행 내용 공유<br>• 데이터셋에 대한 내용 논의|
|2025-10-14 (2회)|• 각자 진행한 실험 내용 공유<br>• 실험 재현에 대한 내용 논의|
|2025-10-15 (2회)|• 각자 진행한 실험 내용 공유|

<br>


## 6. 프로젝트 회고
### 김수환
- 비밀

### 김명철
- 이여러 모델과 여러 하이퍼 파라미터 조합을 시도한 것보다 추가적인 데이터 정제를 한 것이 더 성능이  좋은 것을 보고, 다시 한 번 데이터 전처리에 대한 중요성을 느꼈다.

### 김상윤
- 지금까지 진행한 경진대회 중 제일 난이도가 높게 느껴졌고 데이터에서 topic에 시간투자를 많이 했는데 생각한 만큼의 결과를 가져오지 못해 아쉬웠고 추후에 기회가 있다면좀 더 다양한 시도를 해보고 싶다는  생각이 들었습니다

### 김광묵
-  실험에서 제외시킨 모델(api를 이용한 대규모 모델과 다국어 모델)의 점수도 궁금함,
 데이터의 정갈함이 얼마나 많은 부분을 차지하고 있는지 다시 한번 깨닳음

### 장윤정
- 데이터 정제에 시간을 많이 할애하여 증강이나 프롬프트 엔지니어링을 해보지 못해 아쉬웠습니다. 추후 기회가 된다면 공부해보려고 합니다!
<br>

## 7. 참고자료
- _참고자료를 첨부해주세요_
