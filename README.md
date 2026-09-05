# 🚀 InternAI Radar

### AI-Powered Internship Intelligence, Early-Alert & Application Management Platform

> **Discover internships early. Understand them deeply. Find your fit. Apply faster. Reach out smarter. Track everything.**

---

## 📌 Overview

**InternAI Radar** is a production-oriented internship intelligence platform designed for technical students who want to:

* Discover relevant internship opportunities early
* Understand job requirements using AI
* Evaluate personal eligibility
* Receive personalized recommendations
* Identify skill gaps
* Apply through the original application source
* Track applications from one place
* Analyze application performance
* Eventually use legitimate contact intelligence for personalized outreach

Instead of being just another internship listing platform, InternAI Radar focuses on the complete internship workflow:

```text
Discover
   ↓
Analyze
   ↓
Match
   ↓
Alert
   ↓
Apply
   ↓
Track
   ↓
Cold Outreach (Later)
   ↓
Improve
```

---

# 📑 Table of Contents

* [Overview](#-overview)
* [Problem](#-problem)
* [Solution](#-solution)
* [Core Workflow](#-core-workflow)
* [Key Features](#-key-features)
* [Build Scope: MVP vs Advanced](#-build-scope-mvp-vs-advanced)
* [Priority & Early-Alert System](#-priority--early-alert-system)
* [AI Intelligence Layer](#-ai-intelligence-layer)
* [Matching Engine](#-matching-engine)
* [Match Explanation](#-match-explanation)
* [Resume Intelligence](#-resume-intelligence)
* [Skill-Gap Analysis](#-skill-gap-analysis)
* [Application Tracking](#-application-tracking)
* [Contact Intelligence](#-contact-intelligence)
* [Cold Outreach](#-cold-outreach)
* [Responsible Contact Intelligence](#-responsible-contact-intelligence)
* [Notifications](#-notifications)
* [System Architecture](#-system-architecture)
* [Project Structure](#-project-structure)
* [Technology Stack](#-technology-stack)
* [Internship Ingestion Pipeline](#-internship-ingestion-pipeline)
* [Data Source Compliance](#-data-source-compliance)
* [Deduplication](#-deduplication)
* [Database](#-database)
* [Background Processing](#-background-processing)
* [Security](#-security--responsible-automation)
* [Testing](#-testing)
* [Documentation](#-documentation)
* [Local Development](#-local-development)
* [Environment Variables](#-environment-variables)
* [Docker](#-docker)
* [Database & Migrations](#-database--migrations)
* [API](#-api)
* [Analytics](#-analytics)
* [Source Health](#-source-health)
* [Deployment](#-deployment)
* [CI/CD](#-cicd)
* [Development Roadmap](#️-development-roadmap)
* [Recommended MVP](#-recommended-mvp)
* [Engineering Principles](#-engineering-principles)
* [Why InternAI Radar?](#-why-internai-radar)
* [Project Status](#-project-status)
* [Contributing](#-contributing)
* [Security](#-security)
* [License](#-license)
* [Author](#️-author)
* [Project Vision](#-project-vision)
* [Future Roadmap](#-future-roadmap)

---

# ❗ Problem

Students searching for internships commonly face several problems.

## 1. Information Fragmentation

Internships are distributed across:

* Company career pages
* Job platforms
* University portals
* Startup websites
* Internship boards
* Other supported sources

Students have to repeatedly search multiple places to find opportunities.

---

## 2. Late Discovery

Many students discover internships only after:

* The application has already been open for days
* The position has received many applications
* The deadline is approaching
* The opportunity has already become highly competitive

InternAI Radar focuses on **early internship intelligence** rather than simply maintaining a list of existing opportunities.

---

## 3. Poor Understanding of Job Requirements

A typical job description may contain:

* Required skills
* Preferred skills
* Eligibility requirements
* Experience requirements
* Location requirements
* Education requirements
* Responsibilities
* Technology requirements

Students often struggle to determine what actually matters for the role.

---

## 4. No Personalized Matching

Most internship platforms essentially say:

> **"Here are some internships."**

InternAI Radar aims to answer:

> **"Which internships are actually relevant to YOU?"**

The platform compares internship requirements against the user's:

* Skills
* Resume
* Education
* Experience
* Location
* Preferences
* Eligibility

---

## 5. Application Management Becomes Messy

Students may apply to dozens of opportunities and lose track of:

* Application status
* Deadlines
* Interview stages
* Follow-ups
* Contacts
* Responses
* Notes

InternAI Radar provides a centralized application-tracking system.

---

## 6. Cold Outreach Is Difficult

Students often don't know:

* Who to contact
* Whether a contact is publicly available
* How to personalize an email
* When to follow up
* Which opportunities deserve outreach

Contact Intelligence and Cold Outreach are therefore planned as **Tier 2 features**, after the core platform is reliable.

---

# 💡 Solution

InternAI Radar combines:

* Internship discovery
* Opportunity normalization
* Validation
* Deduplication
* AI analysis
* Personalized matching
* Early alerts
* Application management
* Analytics
* Responsible contact intelligence

into a single platform.

The central workflow is:

```text
                     ┌─────────────────────┐
                     │    JOB SOURCES      │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │     COLLECTOR       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │    NORMALIZER       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │     VALIDATOR       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │   DEDUPLICATION     │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │  MATCHING ENGINE    │
                     │ Rule-based first    │
                     │ AI-assisted later   │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │      DATABASE       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ NOTIFICATION ENGINE │
                     │ Email first         │
                     │ Others later        │
                     └──────────┬──────────┘
                                │
                                ▼
                              👤 USER
                                │
                ┌───────────────┼────────────────┐
                ▼               ▼                ▼
            APPLY NOW      SAVE / TRACK    CONTACT INTEL *
                │                                │
                ▼                                ▼
        Original Source                   Cold Email Draft *
                │                                │
                └────────────────┬───────────────┘
                                 ▼
                         APPLICATION TRACKER

* Contact Intelligence & Cold Outreach are added after the
  core discovery → match → track loop is working end-to-end.
```

---

# 🔄 Core Workflow

## 1. Discover

Collect internship opportunities from supported and permitted sources.

---

## 2. Analyze

Understand important information from the opportunity.

The system analyzes:

* Role
* Skills
* Requirements
* Eligibility
* Experience
* Location
* Deadline
* Responsibilities

Rule-based processing comes first. AI analysis is introduced later.

---

## 3. Match

Compare the opportunity against the user's:

* Skills
* Resume
* Education
* Experience
* Preferences
* Eligibility

---

## 4. Alert

Prioritize important opportunities and notify the user.

---

## 5. Apply

Open the **original application source**.

InternAI Radar does not hide the application destination behind a fake internal workflow.

---

## 6. Track

The application lifecycle can follow:

```text
Opportunity Found
        ↓
Saved
        ↓
Applied
        ↓
Assessment
        ↓
Interview
        ↓
Offer / Rejected
```

Additional outreach stages are introduced later.

---

## 7. Cold Outreach — Later

When legitimate professional contact information is available, the system can help the user prepare personalized outreach.

---

## 8. Improve

Use:

* Application analytics
* Skill-gap insights
* Opportunity data
* Application outcomes

to improve future applications.

---

# ✨ Key Features

## 🔎 Internship Discovery

Planned Tier 1 capabilities:

* Multi-source internship ingestion
* Source adapters
* Opportunity normalization
* Opportunity validation
* Duplicate detection
* Source attribution
* Original application URLs
* Discovery timestamps
* Processing timestamps

The initial implementation targets **2–3 real sources**.

---

# 🎯 Personalized Matching

Each internship receives a personalized match score.

The first implementation uses **transparent weighted scoring** instead of a black-box ML model.

### Conceptual Weighting

| Factor      | Weight |
| ----------- | -----: |
| Skills      |    35% |
| Role        |    20% |
| Eligibility |    15% |
| Education   |    10% |
| Location    |    10% |
| Experience  |     5% |
| Preferences |     5% |

> Weights are configurable rather than permanently fixed.

The goal is not simply:

> **"Is this internship popular?"**

but:

> **"How relevant is this internship to this particular student?"**

---

# 🤖 AI Job Analysis

**Tier 2 / Advanced Feature**

Once the core system works reliably, AI can analyze internship descriptions and extract:

* Required vs preferred skills
* Responsibilities
* Education requirements
* Experience requirements
* Eligibility
* Technology stack
* Important keywords

AI is introduced only after the deterministic core workflow is established.

---

# 🧭 Build Scope: MVP vs Advanced

To keep the project honest and shippable, development is divided into two tiers.

## Tier 1 — MVP

The MVP is designed to be fully working and deployable.

### Authentication

* Register
* Login
* Logout
* Hashed passwords

### User Profile

* Education
* Skills
* Target roles
* Location

### Resume

* Resume upload
* Basic parsing
* Regex/NLP section detection
* Deterministic skill extraction
* No LLM required initially

### Internship Ingestion

* 2–3 real sources
* Public permitted ATS endpoints
* Exact-match deduplication

### Matching

* Rule-based scoring
* Explainable match results

### Dashboard

* Search
* Filtering
* Sorting
* Pagination

### Application Tracking

```text
Saved
  ↓
Applied
  ↓
Interview
  ↓
Offer / Rejected
```

### Notifications

* Email notification channel

### Background Processing

* Scheduled ingestion using cron/scheduled scripts

Redis/Celery are introduced only if actual scale requires them.

### Testing

* Unit tests
* API tests
* Core E2E coverage

### Deployment

* Frontend deployment
* Backend deployment
* Managed PostgreSQL

---

## Tier 2 — Advanced

Tier 2 starts only after Tier 1 is:

* Built
* Tested
* Deployed
* Working end-to-end

Planned additions include:

* Additional internship sources
* Fuzzy deduplication
* Semantic deduplication
* Source health monitoring
* LLM-based job analysis
* LLM-based resume analysis
* Priority engine
* Skill-gap analytics
* Market intelligence
* Telegram notifications
* Push notifications
* Watchlists
* Saved searches
* Detection-latency measurement
* Contact Intelligence
* Cold Outreach
* Security hardening
* Performance optimization
* Resume optimization suggestions

---

# ⚡ Priority & Early-Alert System

InternAI Radar is designed around **early internship intelligence**.

The system maintains timestamps such as:

```text
posted_at
discovered_at
processed_at
notified_at
```

These timestamps allow the system to reason about how quickly an opportunity moves through the pipeline.

## Important Principle

The platform should **never claim that an opportunity is "real-time" unless the underlying source actually supports real-time updates**.

Detection-latency numbers are published only after they have been measured.

Instead, the platform can communicate freshness using measurable information:

```text
Posted      → 2 hours ago
Discovered  → 8 minutes ago
Processed   → 3 minutes ago
```

---

# 🧠 AI Intelligence Layer

**Advanced / Tier 2**

The AI layer is organized into specialized modules:

```text
backend/app/ai/

├── providers/
├── resume/
├── jobs/
├── matching/
├── skill_gap/
├── cover_letter/
├── career_assistant/
├── contacts/
└── evaluation/
```

## Planned AI Capabilities

* Resume analysis
* Skill extraction
* Job analysis
* Job skill extraction
* Semantic matching
* Match explanations
* Skill-gap analysis
* Learning recommendations
* Cover-letter generation
* Career assistant
* Cold-email drafting
* AI evaluation

AI accuracy claims will only be made after evaluation against a small manual evaluation set.

---

# 🎯 Matching Engine

The matching engine begins with deterministic rule-based scoring.

Later, semantic AI matching can be added.

```text
                    User Profile
                         │
            ┌────────────┼────────────┐
            │            │            │
          Skills     Education    Experience
            │
         Location
            │
       Preferences
            │
            ▼
     ┌───────────────┐
     │    Matching   │
     │     Engine    │
     └───────┬───────┘
             │
       ┌─────┴─────┐
       ▼           ▼
 Rule Matching   AI Matching
   Tier 1          Tier 2
       │           │
       └─────┬─────┘
             ▼
        Match Score
             │
             ▼
     Match Explanation
```

Users should be able to understand **why** they received a particular score.

This explainability exists from Day 1 rather than being added only when AI arrives.

---

# 📊 Match Explanation

Instead of showing only:

```text
Match: 87%
```

InternAI Radar aims to provide meaningful reasoning:

```text
87% Match

Strong matches:
✓ Python
✓ FastAPI
✓ PostgreSQL
✓ REST APIs

Partial matches:
△ Docker
△ Redis

Missing / weak areas:
✗ Kubernetes

Eligibility:
✓ Education requirement
✓ Experience requirement
✓ Location preference
```

This makes recommendations explainable rather than black-box.

---

# 📄 Resume Intelligence

## Tier 1

The initial version supports:

* Resume upload
* Basic parsing
* Regex/NLP section detection
* Deterministic skill extraction

## Tier 2

Later versions can add:

* AI resume scoring
* AI resume analysis
* AI-generated suggestions
* Job-specific resume optimization

### Resume Flow

```text
Resume
   ↓
Skill Extraction
   ↓
User Profile
   ↓
Opportunity Matching
   ↓
Skill Gap Analysis
   ↓
Learning Recommendations
```

---

# 📈 Skill-Gap Analysis

**Tier 2**

When an internship is a strong match but the user has missing skills, InternAI Radar can identify those gaps once enough opportunity data exists.

### Example

```text
Target Role:
Backend Engineering Intern

Your skills:
✓ Python
✓ FastAPI
✓ PostgreSQL

Missing:
△ Redis
△ Docker
△ AWS

Recommended focus:
1. Docker fundamentals
2. Redis basics
3. AWS deployment fundamentals
```

The purpose is not simply to reject opportunities because of missing skills.

Instead, the system should help users understand **what they can improve**.

---

# 📌 Application Tracking

Application management is a Tier 1 feature.

## Application States

```text
Saved
Applied
Assessment
Interview
Rejected
Offer
Withdrawn
```

## Application Information

Each application can contain:

* Opportunity
* Company
* Application date
* Deadline
* Current status
* Status history
* Notes
* Interview information
* Outreach history — Tier 2

The underlying application data can later power:

* Kanban views
* Calendar views
* Application analytics

Kanban and calendar are UI layers over the same application-management system.

---

# 👤 Contact Intelligence

**Tier 2 / Phase 2 Feature**

Contact Intelligence is added only after the core discovery → matching → tracking loop is working reliably.

The purpose is **not to scrape private information**.

The system can work with:

### Manual Contact Entry

The user provides a contact they found themselves, such as from a public professional/team page.

### Legitimate Contact APIs

Supported paid contact-lookup providers may be integrated through their official APIs and terms of service.

Examples include:

* Hunter.io
* Apollo

The system should never scrape LinkedIn or private people-search sources.

---

## Contact Confidence

Contact information is represented with confidence levels:

```text
HIGH
MEDIUM
UNAVAILABLE
```

The source of the information should also be recorded.

A contact should never be presented without:

* Source
* Confidence level

---

# 📧 Cold Outreach

**Tier 2**

The planned outreach workflow is:

```text
Opportunity Found
       ↓
Saved
       ↓
Applied
       ↓
Contact Identified
       ↓
Cold Email Drafted
       ↓
User Reviews
       ↓
Email Sent Manually
       ↓
Follow-up
       ↓
Response
```

The AI email drafter can use:

* Company
* Role
* Job description
* Candidate skills
* Candidate background

The AI generates a **draft only**.

> There is no automatic email sending.

The user remains in control of the final message and sending process.

---

# 🔐 Responsible Contact Intelligence

InternAI Radar explicitly avoids:

* Guessing private email addresses at scale
* Scraping private personal information
* Scraping LinkedIn profiles
* CAPTCHA bypassing
* Authentication bypassing
* Rate-limit bypassing
* Unauthorized scraping
* Automated spam campaigns

The system is designed around **responsible automation and user control**.

---

# 🔔 Notifications

Tier 1 includes:

```text
Email
```

Telegram and push notifications are planned for Tier 2.

Additional channels will be added only after the email notification system is reliable.

---

# 🏗️ System Architecture

The target architecture is:

```text
                    ┌───────────────────┐
                    │     Next.js       │
                    │    Frontend       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │      FastAPI      │
                    │       API         │
                    └─────────┬─────────┘
                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
        PostgreSQL       Redis (T2)        AI / LLM (T2)
              │               │                │
              │               ▼                │
              │       Background Jobs          │
              │       cron → T1                │
              │       Celery → T2              │
              │               │                │
              └───────────────┼────────────────┘
                              │
                              ▼
                    Matching / Priority
                              │
                              ▼
                         Notifications
```

Redis, Celery, and AI components are introduced only when their corresponding development phases are reached.

---

# 📁 Project Structure

```text
InternAI-Radar/
│
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
│
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── database/
│   ├── ai/
│   ├── sources/
│   ├── deployment/
│   └── decisions/
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── app/
│       ├── components/
│       ├── features/
│       ├── hooks/
│       ├── lib/
│       ├── types/
│       └── tests/
│
├── backend/
│   ├── alembic/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── ingestion/
│   │   ├── ai/            # Tier 2
│   │   ├── priority/      # Tier 2
│   │   ├── notifications/
│   │   ├── workers/       # Tier 2
│   │   ├── security/
│   │   ├── utils/
│   │   └── tests/
│   │
│   └── scripts/
│
├── worker/                # Tier 2 if required
├── infrastructure/
├── tests/
├── scripts/
│
├── docker-compose.yml
├── Makefile
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

Tier 2 directories may remain empty during earlier development phases.

An empty directory is a **placeholder**, not a shipped feature.

---

# 🛠️ Technology Stack

The project separates technologies into Tier 1 and Tier 2 to maintain documentation and resume honesty.

## Frontend

| Technology   | Tier | Purpose     |
| ------------ | ---- | ----------- |
| Next.js      | T1   | App Router  |
| React        | T1   | UI          |
| TypeScript   | T1   | Type safety |
| Tailwind CSS | T1   | Styling     |

## Backend

| Technology | Tier | Purpose          |
| ---------- | ---- | ---------------- |
| Python     | T1   | Backend language |
| FastAPI    | T1   | API framework    |
| Pydantic   | T1   | Validation       |
| SQLAlchemy | T1   | ORM              |

## Database

| Technology | Tier | Purpose             |
| ---------- | ---- | ------------------- |
| PostgreSQL | T1   | Primary database    |
| Alembic    | T1   | Database migrations |

## Caching / Queues

| Technology | Tier | Purpose                              |
| ---------- | ---- | ------------------------------------ |
| Redis      | T2   | Cache / queue if justified           |
| Celery     | T2   | Background workers if scale requires |

## Background Processing

| Technology              | Tier | Purpose                     |
| ----------------------- | ---- | --------------------------- |
| Cron / Scheduled Script | T1   | Scheduled ingestion         |
| Celery + Worker         | T2   | High-concurrency processing |

## AI

| Technology  | Tier | Purpose                         |
| ----------- | ---- | ------------------------------- |
| NLP / Regex | T1   | Basic extraction                |
| LLM API     | T2   | Job/resume analysis             |
| Embeddings  | T2   | Semantic matching/deduplication |

## Contact Intelligence

| Technology           | Tier | Purpose                   |
| -------------------- | ---- | ------------------------- |
| Manual Contact Entry | T2   | User-provided contacts    |
| Paid Contact API     | T2   | Legitimate contact lookup |

## Infrastructure

| Technology     | Tier  | Purpose              |
| -------------- | ----- | -------------------- |
| Docker         | T1    | Containerization     |
| Docker Compose | T1    | Local development    |
| Nginx          | T2    | Production hardening |
| GitHub Actions | T1/T2 | CI/CD                |

> A technology is only considered **"in use"** after it has been implemented, tested, and deployed.

---

# 🔄 Internship Ingestion Pipeline

The ingestion system follows a modular pipeline:

```text
Source
  ↓
Adapter
  ↓
Client
  ↓
Parser
  ↓
Mapper
  ↓
Normalizer
  ↓
Validator
  ↓
Deduplicator
  ↓
Processor
  ↓
Database
```

Each source has its own adapter.

Example:

```text
source_001/
├── adapter.py
├── client.py
├── parser.py
└── mapper.py
```

This allows new sources to be added without rewriting the rest of the ingestion system.

---

# 📜 Data Source Compliance

Before integrating a source, the project checks:

* Access method
* Terms of service
* Rate limits
* Redistribution restrictions
* Technical limitations

Documentation for sources is maintained under:

```text
docs/sources/
```

Publicly visible data does not automatically mean unrestricted scraping or redistribution is permitted.

If a source cannot be legally or technically integrated, the limitation is documented and another permitted source is used.

The system never bypasses:

* Authentication
* CAPTCHA
* Rate limits
* Access controls

---

# 🔁 Deduplication

The goal is to avoid displaying the same opportunity multiple times.

Instead of:

```text
Google SWE Intern
Google SWE Intern
Google SWE Intern
```

the platform aims to represent:

```text
Google Software Engineering Intern

Found on 2 sources
```

## Tier 1

Exact-match deduplication based on:

* Source job ID
* Canonical URL

## Tier 2

Later additions:

* Fuzzy matching
* Semantic matching

This keeps the MVP simple and reliable.

---

# 🗄️ Database

Major database domains include:

```text
User
Profile
Education
Skill
Resume

Company
Opportunity
OpportunitySource
OpportunitySkill

Match
Application
ApplicationEvent

Notification
SavedOpportunity

Contact                  # Tier 2
Watchlist                # Tier 2
SavedSearch              # Tier 2
AuditLog                 # Tier 2
SourceHealth             # Tier 2
```

Database documentation is maintained under:

```text
docs/database/
```

including:

* Schema
* Relationships
* Indexes
* Migrations

---

# ⚙️ Background Processing

## Tier 1

A scheduled script runs the ingestion pipeline periodically.

```text
Cron
  ↓
Ingestion Pipeline
  ↓
Processing
  ↓
PostgreSQL
```

No queue infrastructure is required at MVP scale.

## Tier 2

If actual load justifies it:

```text
FastAPI
   │
   ▼
Redis Queue
   │
   ▼
Celery Worker
   │
   ├── Ingestion
   ├── Processing
   ├── AI
   ├── Matching
   ├── Contacts
   └── Notifications
```

This architecture is introduced only when needed.

---

# 🔒 Security & Responsible Automation

The system considers:

* Authentication
* Authorization
* Permissions
* Rate limiting
* File validation
* Sanitization
* Audit logging

Sensitive values must never be committed.

## Never Commit

```text
.env
API keys
Passwords
Database credentials
Private tokens
Secret keys
```

Use:

```text
.env.example
```

to document required configuration.

---

# 🧪 Testing

## Tier 1

### Unit Tests

Test important deterministic components:

* Normalizer
* Deduplicator
* Matcher
* Scoring logic
* Validators

### API Tests

Cover:

* Authentication
* CRUD operations
* Error cases
* Validation failures

### E2E

The core journey should eventually be covered:

```text
Register
   ↓
Resume
   ↓
Opportunity
   ↓
Match
   ↓
Save
   ↓
Apply
   ↓
Track
```

## Tier 2

Additional testing includes:

* Ingestion adapter integration tests
* AI evaluation tests
* Frontend unit tests
* Frontend integration tests
* Contact Intelligence E2E flow

---

# 📚 Documentation

Documentation is maintained under:

```text
docs/
```

with sections for:

```text
architecture/
api/
database/
ai/
sources/
deployment/
decisions/
```

The documentation follows the same principle as the code:

> **Document what actually exists.**

Tier 2 documentation is written as Tier 2 functionality is implemented rather than falsely presenting planned features as completed functionality.

---

# 🚀 Local Development

## 1. Clone the Repository

```bash
git clone https://github.com/sankalp-tripath12/InternAI-Radar.git
cd InternAI-Radar
```

---

## 2. Configure Environment Variables

### Frontend

```bash
cp frontend/.env.example frontend/.env.local
```

### Backend

```bash
cp backend/.env.example backend/.env
```

Never commit the generated `.env` files.

---

# 🐍 Backend Setup

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install backend dependencies:

```bash
pip install -r backend/requirements.txt
```

Run the FastAPI application according to the project's development configuration.

---

# ⚛️ Frontend Setup

Move into the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

---

# 🔐 Environment Variables

## Root

The root `.env.example` explains that each service maintains its own environment configuration.

```text
backend/.env.example
frontend/.env.example
```

Real secrets should never be stored in the root README or committed environment files.

---

## Backend Environment

Example configuration:

```env
APP_NAME=InternAI Radar
APP_ENV=development
DEBUG=true

DATABASE_URL=postgresql+asyncpg://internai:internai_dev_password@localhost:5432/internai_radar

REDIS_URL=redis://localhost:6379/0

JWT_SECRET=replace_this_with_a_real_random_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

FRONTEND_ORIGIN=http://localhost:3000

OPENAI_API_KEY=

SMTP_HOST=
SMTP_PORT=587
SMTP_USER=
SMTP_PASSWORD=
```

Redis and OpenAI are placeholders for Tier 2 until their implementation phase is reached.

---

## Frontend Environment

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1
```

---

# 🐘 Database & Migrations

Database migrations use **Alembic**.

Create a migration:

```bash
alembic revision --autogenerate -m "migration message"
```

Apply migrations:

```bash
alembic upgrade head
```

Database documentation is maintained under:

```text
docs/database/
```

---

# 🐳 Docker

Infrastructure Docker files are organized as:

```text
infrastructure/docker/

├── frontend.Dockerfile
├── backend.Dockerfile
└── worker.Dockerfile
```

The worker Dockerfile is a Tier 2 component.

The root project contains:

```text
docker-compose.yml
```

Tier 1 Docker Compose is intended to support:

* PostgreSQL
* Backend
* Frontend

Tier 2 can add:

* Redis
* Worker services

The goal is reproducible local development and deployment.

---

# 🔌 API

Backend API routes are organized under:

```text
backend/app/api/v1/
```

Tier 1 APIs include:

```text
auth
users
profiles
resumes
opportunities
matching
applications
```

Notifications begin as a Tier 1 capability.

Tier 2 can add:

```text
contacts
analytics
admin
```

API documentation is maintained under:

```text
docs/api/
```

---

# 📊 Analytics

**Tier 2**

Once sufficient real application data exists, the system can calculate metrics such as:

```text
Applications: 40
Interviews:    8
Offers:        2

Interview Rate: 20%
Offer Rate:      5%
```

Only real, measured numbers should be displayed.

> **Never invent project metrics.**

---

# 🩺 Source Health

**Tier 2**

Once multiple sources are integrated, source-health monitoring can track:

* Source availability
* Collection failures
* Processing failures
* Last successful ingestion
* Source-specific issues

This ensures that a broken source does not silently cause opportunities to disappear.

---

# 🌐 Deployment

The target deployment architecture is:

```text
Frontend
   ↓
Next.js Hosting

Backend
   ↓
FastAPI Hosting

Database
   ↓
Managed PostgreSQL

Cache
   ↓
Managed Redis
(Tier 2)

Workers
   ↓
Worker Infrastructure
(Tier 2)

Proxy
   ↓
Nginx
(Tier 2)
```

Deployment documentation is maintained under:

```text
docs/deployment/
```

---

# 🔄 CI/CD

GitHub Actions workflows are organized under:

```text
.github/workflows/

├── ci.yml
├── frontend.yml
├── backend.yml
├── worker.yml
└── security.yml
```

## Tier 1

```text
ci.yml
frontend.yml
backend.yml
```

Basic CI should run linting and tests on every push.

## Tier 2

```text
worker.yml
security.yml
```

Additional production and security automation can be introduced later.

---

# 🗺️ Development Roadmap

## Phase 1 — Foundation

**Current Status: Scaffolded**

* Repository created
* Monorepo structure scaffolded
* Git configured
* Environment configuration created
* Docker development environment

---

## Phase 2 — Backend Foundation

**Tier 1**

* FastAPI application
* PostgreSQL connection
* SQLAlchemy models
* Alembic migrations
* Authentication
* Password hashing
* User profiles

---

## Phase 3 — Internship Intelligence

**Tier 1**

* Source adapter architecture
* 2–3 real permitted sources
* Collector
* Parser
* Normalizer
* Validator
* Exact-match deduplication
* Opportunity database populated with real data

---

## Phase 4 — Matching & Dashboard

**Tier 1**

* Rule-based matching engine
* Explainable scoring
* Opportunity dashboard
* Search
* Filtering
* Sorting
* Pagination
* Resume upload
* Basic resume parsing

---

## Phase 5 — Application Tracking & Alerts

**Tier 1**

* Save opportunities
* Application tracker
* Application timeline
* Email notifications
* Cron-based scheduled ingestion

> **Tier 1 / MVP is complete when Phases 1–5 are deployed, tested, and demoable end-to-end.**

---

## Phase 6 — Multi-Source & AI Intelligence

**Tier 2**

* Additional sources
* Fuzzy deduplication
* Semantic deduplication
* Source health
* AI job analysis
* Skill extraction
* Resume analysis
* Semantic matching
* Match explanations
* Skill-gap analysis

---

## Phase 7 — Priority, Kanban & Analytics

**Tier 2**

* Priority scoring
* Freshness scoring
* Deadline scoring
* Kanban board
* Application calendar
* Application analytics
* Source analytics
* Watchlists
* Saved searches

---

## Phase 8 — Contact Intelligence & Outreach

**Tier 2**

* Manual contact entry
* Legitimate paid contact lookup APIs
* AI cold-email drafting
* Review-before-send workflow
* Outreach tracking
* Follow-up tracking

---

## Phase 9 — Production Hardening

**Tier 2**

* Telegram notifications
* Push notifications
* Security hardening
* Performance optimization
* Full CI/CD matrix
* Monitoring
* Logging
* Metrics
* Production deployment verification

---

# 🧭 Recommended MVP

The recommended Tier 1 MVP is:

```text
AUTH + PROFILE
       ↓
RESUME UPLOAD
(Basic Parsing)
       ↓
2–3 REAL SOURCES
       ↓
COLLECT
       ↓
NORMALIZE
       ↓
VALIDATE
       ↓
DEDUPLICATE
       ↓
POSTGRES
       ↓
FASTAPI
       ↓
RULE-BASED
EXPLAINABLE MATCHING
       ↓
NEXT.JS DASHBOARD
       ↓
REAL INTERNSHIPS
+ REAL MATCH SCORES
       ↓
SAVE / OPEN ORIGINAL APPLICATION
       ↓
APPLICATION TRACKER
       ↓
EMAIL ALERT ON NEW MATCH
```

The principle is:

> **Build the core loop first.**

Only after the core system works reliably end-to-end should the following be layered on:

* AI matching
* More sources
* Contact Intelligence
* Analytics
* Advanced notifications

---

# 🧠 Engineering Principles

## 1. Real Data Over Fake Demos

Use genuine internship data and real application URLs.

Test data must remain clearly separated from production data.

---

## 2. Explainable Matching

Users should always understand why they received a particular score.

This starts with the Tier 1 rule-based engine.

---

## 3. Source Transparency

Every opportunity should preserve source information wherever possible.

---

## 4. Responsible Automation

Especially for:

* Contact discovery
* Email generation
* Outreach

the user remains in control.

There is no automatic email sending.

---

## 5. Modular Architecture

The architecture should keep the following replaceable:

* Source adapters
* AI providers
* Notification providers

---

## 6. Security by Design

Security should be considered from the beginning:

* Authentication
* Authorization
* Validation
* Sanitization
* Rate limiting
* Auditing

---

## 7. Production-Minded Development

"Done" means more than writing code.

The project considers:

* Testing
* Monitoring
* Logging
* CI/CD
* Documentation
* Deployment

---

## 8. Tiered, Incremental Scope

Tier 1 must be:

```text
Built
   ↓
Tested
   ↓
Deployed
   ↓
Verified
```

before Tier 2 begins.

> **No feature is claimed as working until it demonstrably is.**

---

# 🏆 Why InternAI Radar?

Traditional internship platforms mainly answer:

> **"What internships exist?"**

InternAI Radar aims to answer a much more useful set of questions:

* What internships were discovered early?
* Which opportunities are relevant to me?
* Am I eligible?
* Why is this a good match?
* What skills am I missing?
* Should I prioritize this opportunity?
* Where do I apply?
* What have I already applied to?
* How is my internship search performing?

That is the difference between:

```text
Internship Listing Platform
```

and:

```text
Internship Intelligence System
```

---

# 👨‍💻 Project Status

```text
🚧 Active Development
```

Current status:

* Repository scaffolded
* Project structure created
* Git configured
* Tier 1 implementation in progress

The project is being developed incrementally with a focus on **real functionality rather than feature claims**.

---

# 🤝 Contributing

Contributions are welcome.

Before contributing:

1. Read `CONTRIBUTING.md`
2. Check existing issues
3. Create a focused branch
4. Make the change
5. Add or update tests where appropriate
6. Submit a pull request

Keep contributions focused, tested, and consistent with the project's architecture.

---

# 🔐 Security

Please follow the responsible disclosure process described in:

```text
SECURITY.md
```

Do not publicly expose:

* API keys
* Passwords
* Database credentials
* Private tokens
* Personal data
* Security vulnerabilities

If you discover a security issue, report it responsibly rather than publicly exposing the vulnerability.

---

# 📜 License

See:

```text
LICENSE
```

for licensing information.

---

# 👨‍💻 Author

**Sankalp Tripathi**
Computer Science & AI Student

### Focus Areas

* Full-Stack Development
* AI/ML Engineering
* Software Engineering
* Data Structures & Algorithms
* MLOps
* Open Source

---

# 🌟 Project Vision

**InternAI Radar** is being built to help technical students discover relevant internship opportunities earlier, understand their fit, and manage their application journey effectively.

### Core Vision

```text
Discover
   ↓
Analyze
   ↓
Match
   ↓
Alert
   ↓
Apply
   ↓
Track
   ↓
Improve
```

The long-term goal is to evolve InternAI Radar from an internship discovery platform into an **AI-powered career intelligence platform**.

The system should help students move from:

> **"I am searching for internships."**

to:

> **"I know which opportunities matter, why they matter, when to apply, what I should improve, and where I stand in the application process."**

---

# 🚀 Future Roadmap

Planned improvements include:

* More internship sources
* Improved opportunity deduplication
* Personalized opportunity matching
* AI-powered job analysis
* AI-powered resume analysis
* Skill-gap analysis
* Early application alerts
* Application analytics
* Watchlists
* Saved searches
* Contact Intelligence
* AI-assisted cold-email drafting
* Outreach tracking
* Follow-up tracking
* Career intelligence
* Production monitoring
* Performance optimization

Advanced capabilities will be introduced only after the core:

```text
Discovery
   ↓
Matching
   ↓
Application Tracking
```

workflow is working reliably.

---

# 🎯 Final Goal

InternAI Radar is not intended to be just another internship listing website.

The goal is to build a system that helps students:

```text
Discover earlier
      ↓
Understand better
      ↓
Match smarter
      ↓
Apply strategically
      ↓
Track progress
      ↓
Identify skill gaps
      ↓
Improve continuously
```

---

## 🚀 InternAI Radar

> **Discover earlier. Match smarter. Apply strategically.**

Built as a practical engineering project combining:

**Full-Stack Development • AI/ML • Software Engineering • System Design • DSA • MLOps • Responsible Automation**
