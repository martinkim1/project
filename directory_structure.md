# 📂 프로젝트 디렉토리 구조 설명

이 문서는 **AI Native English Tutor** 프로젝트의 폴더 및 파일 구조를 설명합니다.

```
project/
├── 📂 frontend/                # [클라이언트] React 웹 애플리케이션
│   ├── public/                 # 정적 리소스 (이미지, 파비콘 등)
│   ├── src/                    # 소스 코드
│   │   ├── components/         # 재사용 가능한 UI 컴포넌트 (버튼, 채팅창 등)
│   │   ├── hooks/              # 커스텀 React Hooks (LiveKit 연결 등)
│   │   ├── pages/              # 페이지 단위 컴포넌트 (메인, 채팅방)
│   │   ├── App.tsx             # 앱 진입점
│   │   └── main.tsx            # DOM 렌더링 진입점
│   ├── package.json            # 프론트엔드 의존성 및 스크립트 관리
│   ├── tsconfig.json           # TypeScript 설정 파일
│   └── vite.config.ts          # Vite 빌드 도구 설정
│
├── 📂 backend/                 # [서버] FastAPI 및 AI 에이전트
│   ├── venv/                   # Python 가상환경 (라이브러리 격리)
│   ├── agent.py                # LiveKit Worker (AI 에이전트 로직)
│   ├── main.py                 # FastAPI 서버 진입점 (HTTP API)
│   ├── llm.py                  # LangChain & Ollama 연동 로직
│   ├── stt_tts.py              # 음성 인식(Whisper) 및 합성(Edge-TTS) 모듈
│   └── requirements.txt        # 백엔드 의존성 목록
│
├── readme.md                   # 프로젝트 개요 및 설명
└── directory_structure.md      # (본 파일) 디렉토리 구조 설명
```

## 🏗️ 상세 설명

### 1. Frontend (`/frontend`)
사용자가 접속하는 웹 페이지입니다.
*   **Vite + React + TypeScript**: 빠르고 안정적인 개발 환경을 위해 선택했습니다.
*   **LiveKit Client SDK**: 브라우저에서 마이크/스피커를 제어하고 서버와 통신합니다.

### 2. Backend (`/backend`)
AI 두뇌와 연결되고 실시간 통신을 중개하는 서버입니다.
*   **FastAPI**: 가볍고 빠른 Python 웹 프레임워크입니다.
*   **LiveKit Server SDK**: LiveKit 클라우드와 통신하여 방(Room)을 관리합니다.
*   **Ollama/LangChain**: 로컬 LLM을 제어하여 지능적인 답변을 생성합니다.
