from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

data = {
    "project_name": "AMK Digital Platform Kickoff",
    "scope": {
        "In Scope": [
            "Set up Spring Cloud Configuration",
            "Set up Spring Cloud Gateway",
            "Setup Kubernetes",
            "Set up Spring Cloud Circuit Breaker",
            "Monitoring: Grafana, Prometheus, Loki, OpenTelemetry, Tempo",
            "Set up Spring Cloud Stream with Kafka",
            "Microservice-based architecture",
            "Promote Biz Solution as services"
        ],
        "Out of Scope": ["Details for each functionality are not within the scope."]
    },
    "milestones": [
        "Architecture: Piseth",
        "Project Oversight: Piseth & AMK",
        "Testing: QA/UAT Team",
        "Final UAT Sign-off: Piseth & AMK"
    ],
    "deliverables": [
        "User Management (LDAP, Auth Module)",
        "Independent Auth Microservice",
        "Microservices Foundation Architecture",
        "Security & Cryptography Library",
        "Performance: 100 TPS Guaranteed",
        "Source Code Handover & Training"
    ],
    "org_structure": {
        "Project Sponsor": "Mr. Sok Kosal",
        "Project Manager": "Mr. Horn Daneth",
        "Software Architect": "Mr. Lorn Sothy",
        "Developers": ["Mr. Ing Piseth", "Leap Panha", "Mr. Sub Tam"],
        "QA/UAT": ["Mrs. Buth Marina", "Mr. Heng Ratha"],
        "Infrastructure": ["Phai Sophanith", "Mr. Sror Sreu"]
    },
    "risks": {
        "Risks": [
            "Infrastructure setup delay",
            "Legacy system integration issues",
            "Performance bottlenecks",
            "Unavailability of key resources"
        ],
        "Mitigation": [
            "Weekly tracking and checkpoints",
            "Stakeholder alignment sessions",
            "Dedicated infrastructure support"
        ]
    }
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": data, "title": "Home"})

@app.get("/scope", response_class=HTMLResponse)
async def scope(request: Request):
    return templates.TemplateResponse("scope.html", {"request": request, "data": data, "title": "Scope"})

@app.get("/milestones", response_class=HTMLResponse)
async def milestones(request: Request):
    return templates.TemplateResponse("milestones.html", {"request": request, "data": data, "title": "Milestones"})

@app.get("/risks", response_class=HTMLResponse)
async def risks(request: Request):
    return templates.TemplateResponse("risks.html", {"request": request, "data": data, "title": "Risks"})

@app.get("/team", response_class=HTMLResponse)
async def team(request: Request):
    return templates.TemplateResponse("team.html", {"request": request, "data": data, "title": "Team"})
