# SIGNATURE REALTY CRM

A comprehensive, enterprise-grade Real Estate CRM and Brokerage Management Platform.

## 🏗️ Project Structure

```
signature-realty-crm/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI app entry point
│   │   ├── config.py          # Configuration & settings
│   │   ├── database.py        # Database connection
│   │   ├── models/            # SQLAlchemy models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── routes/            # API endpoints
│   │   ├── services/          # Business logic
│   │   ├── utils/             # Utility functions
│   │   ├── middleware/        # Authentication, RBAC
│   │   ├── tasks/             # Async tasks (Celery)
│   │   └── tests/
│   ├── migrations/            # Alembic migrations
│   ├── seeds/                 # Seed data
│   ├── requirements.txt
│   ├── .env.example
│   ├── Dockerfile
│   └── README.md
│
├── frontend/                   # React + TypeScript
│   ├── public/
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   ├── pages/             # Page components
│   │   ├── services/          # API calls
│   │   ├── hooks/             # Custom hooks
│   │   ├── context/           # Context API
│   │   ├── types/             # TypeScript interfaces
│   │   ├── styles/            # Tailwind CSS
│   │   ├── utils/             # Utility functions
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── Dockerfile
│   └── README.md
│
├── mobile/                     # React Native
│   ├── src/
│   │   ├── screens/
│   │   ├── components/
│   │   ├── navigation/
│   │   ├── services/
│   │   ├── types/
│   │   └── App.tsx
│   ├── package.json
│   ├── app.json
│   └── README.md
│
├── docs/                       # Documentation
│   ├── API.md                 # API Documentation
│   ├── DATABASE.md            # Database schema
│   ├── ARCHITECTURE.md        # System architecture
│   ├── DEPLOYMENT.md          # Deployment guide
│   └── RBAC.md               # Role-based access control
│
├── docker-compose.yml          # Docker orchestration
├── .gitignore
├── .env.example
└── package.json                # Root package.json
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL 15+
- Docker & Docker Compose

### Installation

```bash
# Clone repository
git clone https://github.com/VIKASHBHATTER/real-estate-crm.git
cd real-estate-crm

# Copy environment files
cp .env.example .env

# With Docker
docker-compose up -d

# Without Docker - Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
python -m uvicorn app.main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm start
```

## 📊 Modules

1. **Lead Management** - Capture, score, and track leads
2. **Client Requirements** - Requirement discovery and tracking
3. **Lead Scoring Engine** - Automatic lead qualification
4. **Follow-up Management** - Intelligent follow-up scheduling
5. **Inventory Management** - Property listing and management
6. **Owner Management** - Property owner details
7. **Project Management** - Builder project tracking
8. **Property Matching** - AI-powered property recommendations
9. **Site Visit Management** - Visit scheduling and tracking
10. **Deal Tracking** - Deal pipeline management
11. **Brokerage Management** - Commission tracking
12. **Agent Management** - Agent performance tracking
13. **Reports & Analytics** - Comprehensive reporting
14. **Dashboard** - Real-time metrics and KPIs
15. **Kanban Board** - Visual deal pipeline
16. **Automation** - Workflow automation
17. **Mobile App** - React Native app

## 🔐 Security Features

- JWT Authentication
- Role-Based Access Control (RBAC)
- Data Encryption
- Audit Logs
- Rate Limiting
- CORS Protection

## 💻 Tech Stack

- **Frontend**: React 18, TypeScript, Tailwind CSS, Zustand
- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Database**: PostgreSQL
- **Cache**: Redis
- **Message Queue**: Celery
- **File Storage**: Google Drive API
- **Notifications**: WhatsApp API
- **Deployment**: Docker, Render

## 📚 Documentation

Detailed documentation available in `/docs` folder

## 📝 License

Private - All rights reserved
