#!/bin/bash
set -e

echo "🚀 Creating InternAI-Radar project structure..."

mkdir -p \
docs/{architecture/diagrams,api,database,ai/prompts,sources,deployment,decisions} \
frontend/public/{images,icons} \
"frontend/src/app/(auth)"/{login,register,forgot-password,reset-password} \
frontend/src/app/{dashboard,notifications,analytics,opportunities/'[id]',opportunities/saved,opportunities/recommended,profile/skills,profile/preferences,profile/education,resume/upload,resume/analysis,resume/optimization,applications/'[id]',applications/kanban,applications/calendar,contacts/'[id]',settings/account,settings/notifications,settings/security,admin/sources,admin/source-health,admin/users,admin/system} \
frontend/src/components/{ui,layout,opportunities,profile,resume,applications,contacts,notifications,analytics,admin} \
frontend/src/features/{auth,profile,resume,opportunities,matching,applications,contacts,notifications,analytics} \
frontend/src/{lib,hooks,types,tests/{unit,integration,e2e}} \
backend/alembic/versions \
backend/app/{config,api/v1,models,schemas} \
backend/app/services/{auth,users,profiles,resumes,companies,opportunities,matching,applications,contacts/providers,notifications/templates,analytics} \
backend/app/ingestion/{base,sources/source_001/tests,sources/source_002,sources/source_003,sources/source_004,sources/source_005,pipeline} \
backend/app/ai/{providers,resume,jobs,matching,skill_gap,cover_letter,career_assistant,contacts,evaluation/{datasets,benchmarks}} \
backend/app/{priority,notifications/templates,workers/tasks,security,utils,tests/{unit,integration,api,ingestion,ai,e2e}} \
backend/scripts \
worker \
infrastructure/{docker,nginx,monitoring/{logging,metrics,alerts},deployment} \
tests/{e2e,fixtures/{resumes,opportunities,users,contacts},test-data} \
scripts \
.github/{workflows,ISSUE_TEMPLATE}

touch \
README.md LICENSE .gitignore .env.example .dockerignore docker-compose.yml Makefile CONTRIBUTING.md SECURITY.md CHANGELOG.md \
docs/README.md \
docs/architecture/{system-architecture.md,data-flow.md,request-flow.md,background-job-flow.md,ai-pipeline.md,opportunity-ingestion-flow.md} \
docs/api/{authentication.md,users.md,profiles.md,resumes.md,opportunities.md,matching.md,applications.md,contacts.md,notifications.md,analytics.md,admin.md} \
docs/database/{schema.md,relationships.md,indexes.md,migrations.md} \
docs/ai/{ai-architecture.md,resume-analysis.md,job-analysis.md,matching.md,skill-gap-analysis.md,evaluation.md} \
docs/ai/prompts/{resume-analysis.md,job-analysis.md,matching.md,career-assistant.md} \
docs/sources/{source-policy.md,source-permissions.md,source-adapter-guide.md,supported-sources.md} \
docs/deployment/{deployment-guide.md,environment-variables.md,docker.md,production-checklist.md} \
docs/decisions/{ADR-001-monorepo.md,ADR-002-postgresql.md,ADR-003-background-workers.md,ADR-004-ai-provider.md,ADR-005-source-adapter-architecture.md} \
frontend/{package.json,next.config.ts,tsconfig.json,postcss.config.mjs,eslint.config.mjs,tailwind.config.ts,.env.example} \
frontend/public/logo.svg \
frontend/src/app/{layout.tsx,page.tsx,globals.css} \
frontend/src/app/dashboard/{page.tsx,loading.tsx,error.tsx} \
frontend/src/app/opportunities/{page.tsx,'[id]'/page.tsx,saved/page.tsx,recommended/page.tsx} \
frontend/src/app/profile/{page.tsx,skills/page.tsx,preferences/page.tsx,education/page.tsx} \
frontend/src/app/resume/{page.tsx,upload/page.tsx,analysis/page.tsx,optimization/page.tsx} \
frontend/src/app/applications/{page.tsx,'[id]'/page.tsx,kanban/page.tsx,calendar/page.tsx} \
frontend/src/app/contacts/{page.tsx,'[id]'/page.tsx} \
frontend/src/app/notifications/page.tsx \
frontend/src/app/analytics/page.tsx \
frontend/src/app/settings/{page.tsx,account/page.tsx,notifications/page.tsx,security/page.tsx} \
frontend/src/app/admin/{page.tsx,sources/page.tsx,source-health/page.tsx,users/page.tsx,system/page.tsx} \
"frontend/src/app/(auth)"/{login/page.tsx,register/page.tsx,forgot-password/page.tsx,reset-password/page.tsx} \
frontend/src/components/ui/{Button,Input,Select,Modal,Badge,Card,Tabs,Dropdown,Skeleton,Spinner,Toast}.tsx \
frontend/src/components/layout/{Navbar,Sidebar,Footer,DashboardLayout}.tsx \
frontend/src/components/opportunities/{OpportunityCard,OpportunityList,OpportunityFilters,OpportunitySearch,OpportunityDetails,MatchScore,SkillMatch,EligibilityBadge,FreshnessBadge,PriorityScore,SourceBadge}.tsx \
frontend/src/components/profile/{ProfileForm,SkillsEditor,EducationForm,PreferencesForm}.tsx \
frontend/src/components/resume/{ResumeUploader,ResumePreview,ResumeScore,SkillExtraction,ResumeAnalysis,ResumeSuggestions}.tsx \
frontend/src/components/applications/{ApplicationCard,ApplicationTable,ApplicationKanban,ApplicationStatus,ApplicationTimeline,ApplicationForm}.tsx \
frontend/src/components/contacts/{ContactCard,ContactList,ManualContactForm,ColdEmailDraft}.tsx \
frontend/src/components/notifications/{NotificationBell,NotificationList,NotificationPreferences}.tsx \
frontend/src/components/analytics/{ApplicationStats,InterviewStats,ResponseRate,SourcePerformance}.tsx \
frontend/src/components/admin/{SourceHealth,SystemMetrics,UserManagement}.tsx \
frontend/src/features/auth/{api,hooks,types,validation}.ts \
frontend/src/features/profile/{api,hooks,types,validation}.ts \
frontend/src/features/resume/{api,hooks,types,validation}.ts \
frontend/src/features/opportunities/{api,hooks,types,filters}.ts \
frontend/src/features/matching/{api,hooks,types}.ts \
frontend/src/features/applications/{api,hooks,types}.ts \
frontend/src/features/contacts/{api,hooks,types}.ts \
frontend/src/features/notifications/{api,hooks,types}.ts \
frontend/src/features/analytics/{api,hooks,types}.ts \
frontend/src/lib/{api-client,auth,constants,utils,formatters,validators}.ts \
frontend/src/hooks/{useAuth,useDebounce,usePagination,useNotifications}.ts \
frontend/src/types/{auth,user,opportunity,resume,application,contact,notification}.ts \
backend/requirements.txt backend/pyproject.toml backend/Dockerfile backend/.env.example backend/alembic.ini \
backend/alembic/{env.py,script.py.mako} \
backend/app/main.py \
backend/app/config/{settings,database,redis,logging,security}.py \
backend/app/api/{router,deps}.py \
backend/app/api/v1/{auth,users,profiles,resumes,opportunities,matching,applications,contacts,notifications,analytics,admin}.py \
backend/app/models/{user,profile,education,skill,resume,company,opportunity,opportunity_source,opportunity_skill,match,application,application_event,contact,watchlist,saved_search,notification,saved_opportunity,audit_log,source_health}.py \
backend/app/schemas/{auth,user,profile,resume,company,opportunity,matching,application,contact,notification,analytics,common}.py \
backend/app/services/auth/{service,password,token}.py \
backend/app/services/users/service.py \
backend/app/services/profiles/service.py \
backend/app/services/resumes/{service,parser,storage}.py \
backend/app/services/companies/service.py \
backend/app/services/opportunities/{service,normalizer,validator,deduplicator}.py \
backend/app/services/matching/{service,skill_matcher,eligibility,scoring}.py \
backend/app/services/applications/service.py \
backend/app/services/contacts/{service,manual}.py \
backend/app/services/contacts/providers/hunter_provider.py \
backend/app/services/notifications/{service,email,telegram,push}.py \
backend/app/services/analytics/service.py \
backend/app/ingestion/base/{adapter,client,parser,exceptions}.py \
backend/app/ingestion/sources/source_001/{adapter,client,parser,mapper}.py \
backend/app/ingestion/sources/source_002/{adapter,client,parser,mapper}.py \
backend/app/ingestion/sources/source_003/{adapter,client,parser,mapper}.py \
backend/app/ingestion/sources/source_004/{adapter,client,parser,mapper}.py \
backend/app/ingestion/sources/source_005/{adapter,client,parser,mapper}.py \
backend/app/ingestion/pipeline/{collector,normalizer,validator,deduplicator,processor}.py \
backend/app/ingestion/registry.py \
backend/app/ai/providers/{base,llm_provider}.py \
backend/app/ai/resume/{analyzer,skill_extractor,scorer}.py \
backend/app/ai/jobs/{analyzer,skill_extractor,classifier}.py \
backend/app/ai/matching/{embeddings,semantic_matcher,explanation}.py \
backend/app/ai/skill_gap/{analyzer,recommendations}.py \
backend/app/ai/cover_letter/generator.py \
backend/app/ai/career_assistant/{assistant,tools}.py \
backend/app/ai/contacts/email_drafter.py \
backend/app/ai/evaluation/{metrics,evaluator}.py \
backend/app/priority/{scorer,freshness,deadline,rules}.py \
backend/app/notifications/{dispatcher,preferences}.py \
backend/app/workers/celery_app.py \
backend/app/workers/tasks/{ingestion_tasks,processing_tasks,ai_tasks,matching_tasks,contact_tasks,notification_tasks,cleanup_tasks}.py \
backend/app/security/{permissions,rate_limit,file_validation,sanitization,audit}.py \
backend/app/utils/{datetime,text,urls,hashing}.py \
backend/scripts/{seed_dev_data,create_admin,run_ingestion,health_check}.py \
worker/{Dockerfile,requirements.txt,worker.py,README.md} \
infrastructure/docker/{frontend.Dockerfile,backend.Dockerfile,worker.Dockerfile} \
infrastructure/nginx/nginx.conf \
infrastructure/deployment/{production.env.example,staging.env.example,deployment.md} \
tests/e2e/{auth.spec.ts,opportunity-discovery.spec.ts,matching.spec.ts,application-tracker.spec.ts,contacts.spec.ts,notifications.spec.ts} \
tests/test-data/README.md \
scripts/{setup.sh,dev.sh,test.sh,lint.sh,build.sh,deploy.sh} \
.github/workflows/{ci.yml,frontend.yml,backend.yml,worker.yml,security.yml} \
.github/ISSUE_TEMPLATE/{bug_report.md,feature_request.md} \
.github/pull_request_template.md

touch frontend/src/tests/{unit,integration,e2e}/.gitkeep
touch backend/app/tests/{unit,integration,api,ingestion,ai,e2e}/.gitkeep
touch backend/alembic/versions/.gitkeep
touch tests/fixtures/{resumes,opportunities,users,contacts}/.gitkeep
touch docs/architecture/diagrams/.gitkeep
touch backend/app/ai/evaluation/{datasets,benchmarks}/.gitkeep
touch infrastructure/monitoring/{logging,metrics,alerts}/.gitkeep

echo ""
echo "=========================================="
echo "✅ InternAI-Radar structure created!"
echo "=========================================="
echo ""
echo "Files: $(find . -type f | wc -l | tr -d ' ')"
echo "Folders: $(find . -type d | wc -l | tr -d ' ')"
