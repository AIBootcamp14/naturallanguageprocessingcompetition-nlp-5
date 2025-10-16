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

## Overview

### Environment

- Python 3.12.11
- UV==0.9.3

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

## EDA

### 대화문(dialogue) 발화자 수 확인

- Train 데이터의 경우 Person1-7, 최대 7명의 대화문
- Valid, Test 데이터의 경우 대부분 2명의 대화문으로 구성

### 마스킹 처리된 데이터 확인

- Train 데이터의 경우 17개의 마스킹 처리
- Valid, Test 데이터의 경우 각 3개의 마스킹

### dialogue 내 불필요한 문자 제거

- ‘??’, ‘!!’, ‘...’ 등 중복 문자를 하나의 문자로 변경
- ‘www.yahoo.com’ 등 웹 주소 형태의 텍스트를 #WebAddress#로 마스킹

### Kiwipiepy 모듈 사용

- Kiwi 형태소 분석기를 통해 불필요한 태그 제거
- SO(붙임표, - ~), IC(감탄사), SP(구분 부호, / ;) SSO, SSC(인용 부호 및 괄호) 등을 제거

<br>

## 실험 추적 및 평가
Wandb를 이용해서 모델 추적 및 평가 진행

<br>

## Experiment

[실험 기록](https://docs.google.com/spreadsheets/d/14OCF-IG1Ow3Q75yJ32m3QmpuRJgbQS-B4O3NNMDZAYU/edit?gid=0#gid=0)

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


## 참고자료

#### Reference
- [Text Summarization Repo](https://github.com/uoneway/Text-Summarization-Repo)
- [QLoRA + 4bit quantization + LDCC-SOLAR-10.7B](https://dacon.io/en/competitions/official/236216/codeshare/9692)
- [Prompt engineering guide](https://www.promptingguide.ai/kr)

#### Libraries/Tool
- [uv-docs](https://docs.astral.sh/uv/)
- [uv-gitgub](https://github.com/astral-sh/uv)
