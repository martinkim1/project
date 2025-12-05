# 📘 AI Native English Tutor Group Chat Service
> **University Project Edition** > 실시간 그룹 음성 채팅 기반, AI 원어민 강사와의 영어 회화 서비스

## 1. Project Overview (프로젝트 개요)
* **목표:** 최대 3인의 사용자와 1명의 AI 원어민 강사가 함께하는 실시간 영어 회화 그룹 채팅 구현.
* **특징:** 상업용 고비용 인프라 대신, **오픈소스(Ollama, LangChain, HF)**와 **무료 티어(LiveKit Cloud)**를 활용하여 비용 0원으로 구축.
* **핵심 가치:** Low Latency(저지연) 대화 경험, AI의 사회자(Moderator) 역할 수행.

---

## 2. Tech Stack (기술 스택)

### A. Frontend (Client)
* **Framework:** React (Vite)
* **Language:** TypeScript (or JavaScript)
* **Styling:** Tailwind CSS (빠른 UI 개발)
* **Role:** 사용자 인터페이스, 마이크/스피커 제어, 방(Room) 접속 관리.

### B. Backend & Server (Local Host)
* **Framework:** FastAPI (Python)
* **Server Exposure:** Ngrok (로컬 서버를 외부 URL로 터널링하여 데모 시연)
* **Role:** 클라이언트 요청 처리, AI Agent 구동, 비동기 작업 처리.

### C. Real-time Communication (RTC)
* **Infrastructure:** LiveKit Cloud (Free Tier)
* **Role:** WebRTC 서버 구축 없이 고품질 음성 스트리밍 및 그룹 통화(SFU) 관리.

### D. AI & Intelligence (The Core)
* **LLM (Brain):** **Ollama** (Model: `Llama 3` or `Gemma 2`)
    * *사용 이유:* 로컬 구동으로 API 비용 무료, 오프라인 작동 가능.
* **Orchestration:** **LangChain**
    * *사용 이유:* 대화 맥락(Context) 유지, 프롬프트 템플릿 관리 (AI 페르소나 부여).
* **STT/TTS (Ear & Mouth):** **Hugging Face** Transformers & **Edge-TTS**
    * *STT:* Whisper (Tiny/Base model for speed)
    * *TTS:* Edge-TTS (무료, 준수한 품질) 또는 Suno/Bark.

---

## 3. System Architecture (아키텍처)

### Data Flow
1.  **User Speech:** 사용자가 웹(React)에서 말함 -> **LiveKit Cloud**로 오디오 전송.
2.  **Reception:** LiveKit이 오디오 스트림을 백엔드(**FastAPI/Agent**)로 전달.
3.  **Processing (AI Pipeline):**
    * `STT`: 오디오 -> 텍스트 변환 (Whisper).
    * `LLM`: 텍스트 + 대화 맥락 -> **LangChain(Ollama)** -> 답변 생성.
    * `TTS`: 답변 텍스트 -> 오디오 변환.
4.  **Response:** 생성된 오디오를 LiveKit을 통해 방 전체에 송출.

### Infrastructure Diagram
```mermaid
graph LR
    User[Web Client] -- WebRTC Audio --> LiveKit[LiveKit Cloud (SFU)]
    LiveKit -- Audio Stream --> Laptop[Local Server (FastAPI + AI)]
    
    subgraph "Local Laptop Server"
        Agent[LiveKit Agent]
        STT[Whisper (HF)]
        LLM[Ollama (Llama3)]
        TTS[Edge-TTS]
        
        Agent --> STT
        STT --> LLM
        LLM --> TTS
        TTS --> Agent
    end
```
