# Master Skills Library - Robert Bailey

**Comprehensive AI Agent Skills & Knowledge Base**  
Version: 1.0.0 | Last Updated: March 17, 2026  
For: Robert A Bailey Jr - CEO/CFO/COO/CTO Operations

---

## 📚 Table of Contents

1. [Executive Multi-Role Skills](#1-executive-multi-role-skills)
2. [Anthropic Claude Cookbooks](#2-anthropic-claude-cookbooks)
3. [QuickBooks Desktop Integration](#3-quickbooks-desktop-integration)
4. [Airtable Integrations](#4-airtable-integrations)
5. [Knowledge Base](#5-knowledge-base)
6. [Scripts & Automation](#6-scripts--automation)

---

## 1. Executive Multi-Role Skills

### 1.1 Financial Cleanup and Recovery

| Skill | Purpose | Trigger |
|-------|---------|---------|
| `account-inventorying` | Build complete inventory of bank, credit, loan, SaaS, utility accounts | "I need to declutter my tech" |
| `account-merging-planning` | Decide what to close, keep, merge, or migrate | "I need to migrate and merge accounts" |
| `billing-reconciliation` | Match statements, invoices, ledger entries to find duplicates | "Find billing errors" |
| `charge-disputing` | Prepare dispute packets for recent and legacy charges | "I need to dispute charges" |
| `collections-follow-up` | Track customer balances, aging, next actions | "Follow up with customers" |
| `accounts-payable-triage` | Prioritize vendors, due dates, payment terms | "Pay vendors" |
| `cash-flow-forecasting` | Build 13-week cash flow and runway views | "Cash flow projection" |
| `financial-modeling` | Produce scenario models for debt payoff, consolidation, growth | "Financial scenario" |

### 1.2 Legal and Dispute Support

| Skill | Purpose | Trigger |
|-------|---------|---------|
| `case-intake-structuring` | Convert emails, notes, files into case timeline | "Organize case documents" |
| `evidence-packaging` | Organize screenshots, statements, contracts, correspondence | "Prepare evidence" |
| `demand-letter-drafting` | Generate structured demand and follow-up drafts | "Send demand letter" |
| `compliance-checklisting` | Build action checklists by jurisdiction and deadline | "Compliance check" |
| `document-redlining-support` | Compare contract versions and flag risky changes | "Review contract" |
| `litigation-prep-tracking` | Maintain hearing dates, filing requirements, status logs | "Court prep" |

### 1.3 Revenue and Customer Operations

| Skill | Purpose | Trigger |
|-------|---------|---------|
| `crm-pipeline-hygiene` | Clean stale records, stage deals, assign owners | "Clean up CRM" |
| `inside-sales-sequencing` | Draft outbound call/text/email sequences | "Sales outreach" |
| `customer-followup-automation` | Queue reminders for open quotes and unpaid invoices | "Customer follow-up" |
| `meeting-and-lunch-scheduling` | Prioritize and schedule relationship-building meetings | "Set lunches" |
| `response-drafting` | Draft concise customer replies for email and SMS | "Respond to customers" |
| `business-development-research` | Surface warm introductions and strategic targets | "Find leads" |

### 1.4 Technology and Migration

| Skill | Purpose | Trigger |
|-------|---------|---------|
| `identity-and-access-audit` | Map all logins, MFA methods, recovery channels | "Security audit" |
| `account-migration-orchestration` | Move services to new email domains and admin identities | "Migrate accounts" |
| `tool-rationalization` | Remove duplicate software and standardize core stack | "Declutter tech" |
| `data-backup-and-export` | Export records before shutdowns or merges | "Backup data" |
| `security-hardening-baseline` | Enforce password manager, MFA, device controls | "Secure accounts" |
| `openclaw-bootstrap` | Create startup checklist for spinning up OpenClaw safely | "Spin up OpenClaw" |

### 1.5 Executive Operating System

| Skill | Purpose | Trigger |
|-------|---------|---------|
| `weekly-priority-planning` | Convert goals into daily execution blocks | "Plan my week" |
| `project-portfolio-triage` | Rank projects by ROI, urgency, strategic fit | "Prioritize projects" |
| `delegation-and-handoff-writing` | Create clear SOPs for assistants or teams | "Write SOP" |
| `decision-log-maintenance` | Track major decisions, rationale, expected outcomes | "Log decision" |
| `kpi-dashboarding` | Report top metrics for CEO/CFO/COO views | "KPI dashboard" |

### 1.6 Personal and Relationship Management

| Skill | Purpose | Trigger |
|-------|---------|---------|
| `family-calendar-coordination` | Keep personal and business schedules aligned | "Schedule conflict" |
| `communication-queue-management` | Process unread messages by urgency and category | "Clear inbox" |
| `stress-reduction-through-systems` | Build routines that reduce cognitive overload | "Reduce stress" |
| `life-admin-batching` | Batch recurring personal admin tasks into fixed windows | "Batch tasks" |

---

## 2. Anthropic Claude Cookbooks

### 2.1 Capabilities

| Cookbook | Description | Use Case |
|----------|-------------|----------|
| **Classification** | Text and data classification techniques | Categorize documents, emails, tickets |
| **Retrieval Augmented Generation** | Enhance responses with external knowledge | RAG pipelines, knowledge bases |
| **Summarization** | Effective text summarization techniques | Meeting notes, document summaries |

### 2.2 Tool Use and Integration

| Cookbook | Description | Use Case |
|----------|-------------|----------|
| **Tool Use** | Integrate Claude with external tools/functions | Custom tool integration |
| **Customer Service Agent** | Tool use for customer service applications | Support automation |
| **Calculator Integration** | Mathematical computation integration | Financial calculations |
| **SQL Queries** | Database query generation and execution | Data analysis |

### 2.3 Third-Party Integrations

| Cookbook | Description | Use Case |
|----------|-------------|----------|
| **Vector Databases (Pinecone)** | Supplement knowledge with vector search | Semantic search, RAG |
| **Wikipedia** | Search and integrate Wikipedia content | Research, fact-checking |
| **Web Pages** | Read and process web page content | Web scraping, monitoring |
| **Embeddings (Voyage AI)** | Create embeddings for semantic search | Document similarity |

### 2.4 Multimodal Capabilities

| Cookbook | Description | Use Case |
|----------|-------------|----------|
| **Getting Started with Images** | Introduction to vision capabilities | Image analysis |
| **Best Practices for Vision** | Best practices for image processing | Optimal image use |
| **Interpreting Charts and Graphs** | Read charts, graphs, PowerPoints | Data visualization analysis |
| **Extracting Content from Forms** | Transcribe text from forms | Form processing |
| **Generate Images** | Use Claude with Stable Diffusion | Image generation |

### 2.5 Advanced Techniques

| Cookbook | Description | Use Case |
|----------|-------------|----------|
| **Sub-Agents** | Use Haiku as sub-agent with Opus | Multi-agent systems |
| **Upload PDFs** | Parse and pass PDFs as text | Document processing |
| **Automated Evaluations** | Automate prompt evaluation | Quality assurance |
| **Enable JSON Mode** | Ensure consistent JSON output | Structured data |
| **Moderation Filter** | Content moderation filter | Safety, compliance |
| **Prompt Caching** | Efficient prompt caching techniques | Cost optimization |

---

## 3. QuickBooks Desktop Integration

### 3.1 QBWC Connector

**Location:** `qb-desktop-connector/`

| Component | Purpose | Status |
|-----------|---------|--------|
| `node-connector/server.js` | Node.js SOAP server (8 QBWC methods) | ✅ Built |
| `python-connector/server.py` | Python SOAP server (8 QBWC methods) | ✅ Built |
| `wsdl/qbwebconnectorsvc.wsdl` | WSDL reference | ✅ Created |
| `sample.qwc` | QBWC registration file | ✅ Created |
| `scripts/01-setup-node.sh` | Node.js setup script | ✅ Created |
| `scripts/02-setup-python.sh` | Python setup script | ✅ Created |
| `scripts/03-deploy-aws.sh` | AWS deployment script | ✅ Created |
| `aws/task-definition.json` | ECS task definition | ✅ Created |

### 3.2 qbXML Queries

| Query | Purpose | Use Case |
|-------|---------|----------|
| `CustomerQuery` | Get all customers with balances | Customer management |
| `InvoiceQuery` | Get all invoices with due dates | Accounts receivable |
| `VendorQuery` | Get all vendors with balances | Accounts payable |
| `ItemQuery` | Get all items with quantities | Inventory tracking |

### 3.3 Integration Workflows

**For Talian Technologies Oil & Gas:**
- Customer tracking (E&P operators, service companies)
- Invoice management (service invoices, materials)
- Vendor management (suppliers, contractors)
- Inventory tracking (equipment, parts)

---

## 4. Airtable Integrations

### 4.1 API Configuration

**Account:** rbailey@connectedenergyservices.com  
**Token Name:** airtablecesapimaster  
**API Key:** `patwdhF1zazB2cdz9`  
**Scopes:** data.records:read + 8 more  
**Expires:** Mar 4, 2026

### 4.2 Suggested Bases for Talian Technologies

| Base | Purpose | Tables |
|------|---------|--------|
| **Project Tracker** | CEO dashboard for oil & gas projects | Projects, Milestones, Teams, Status |
| **Asset Management** | Equipment tracking across sites | Assets, Locations, Maintenance, Status |
| **Vendor Tracker** | Contract and compliance management | Vendors, Contracts, Performance, Compliance |
| **Field Operations Log** | Daily activity reports | Logs, Sites, Teams, Incidents |
| **Maintenance Scheduler** | Automated service reminders | Schedule, Assets, Technicians, History |
| **Regulatory Compliance** | Permit and inspection tracking | Permits, Inspections, Deadlines, Status |
| **Production Dashboard** | Output visualization | Production, Sites, Metrics, Trends |
| **Incident Tracker** | Safety/operational incident logging | Incidents, Projects, Personnel, Resolution |

---

## 5. Knowledge Base

### 5.1 Connected Energy Services

| Entity | Type | Status |
|--------|------|--------|
| Connected Energy Services, LLC | Primary operating company | Active |
| Breakwater Energy | Subsidiary/Partner | Active |
| R-9 Recycling | Project/Initiative | In Development |
| SWD (Saltwater Disposal) | Service Line | Active |

### 5.2 Talian Technologies

| Entity | Type | Status |
|--------|------|--------|
| Talian Technologies | Primary entity | Active |
| Onshore Oil & Gas | Focus Area | Active |
| Eagle Ford Shale | Operating Region | Active |

### 5.3 Litigation Force

| Entity | Type | Status |
|--------|------|--------|
| Litigation Force | Legal tech platform | In Development |
| Multi-Agent Legal Tech | Agent system | Deployed |

### 5.4 Key Relationships

| Contact | Company | Relationship |
|---------|---------|--------------|
| Brandon Davis | Tejas Environmental / Trisun Energy | Business Partner |
| (Various) | E&P Operators | Customers/Partners |
| (Various) | Oilfield Services | Vendors/Partners |
| (Various) | Trucking/Water Haulers | Vendors/Partners |

---

## 6. Scripts & Automation

### 6.1 Financial Scripts

```bash
# Account inventory
python scripts/financial-cleanup.py --inventory

# Merge/close planning
python scripts/account-merging.py --plan

# Dispute packet generation
python scripts/dispute-generator.py --all

# Cash flow forecast
python scripts/cash-flow.py --weeks 13
```

### 6.2 Migration Scripts

```bash
# Identity and access audit
python scripts/identity-audit.py --all-accounts

# Account migration orchestration
python scripts/migrate-accounts.py --target new-email@domain.com

# Tool rationalization
python scripts/tool-rationalization.py --scan
```

### 6.3 Customer Operations

```bash
# CRM pipeline hygiene
python scripts/crm-cleanup.py --stale-days 30

# Customer follow-up automation
python scripts/customer-followup.py --overdue

# Response drafting
python scripts/response-drafter.py --queue
```

### 6.4 Executive Operations

```bash
# Weekly priority planning
python scripts/weekly-planning.py --date 2026-03-17

# Project portfolio triage
python scripts/project-triage.py --score

# KPI dashboard generation
python scripts/kpi-dashboard.py --role ceo
```

---

## 7. 90-Minute Rapid Start Workflow

### Phase 1: Inventory (20 min)
```bash
# Gather all accounts, tools, debts, open disputes
python scripts/rapid-start.py --phase inventory
```

### Phase 2: Stabilize (20 min)
```bash
# Freeze non-essential spend, enable MFA, set follow-ups
python scripts/rapid-start.py --phase stabilize
```

### Phase 3: Recover (20 min)
```bash
# Open dispute files, reconcile top 10 transactions, send customer updates
python scripts/rapid-start.py --phase recover
```

### Phase 4: Consolidate (20 min)
```bash
# Pick target tools/accounts, schedule migration windows
python scripts/rapid-start.py --phase consolidate
```

### Phase 5: Operate (10 min)
```bash
# Build tomorrow's top-3 priorities and message queue
python scripts/rapid-start.py --phase operate
```

---

## 8. File Structure

```
master-skills/
├── README.md (this file)
├── anthropic-cookbooks/
│   ├── classification/
│   ├── rag/
│   ├── summarization/
│   ├── tool-use/
│   ├── multimodal/
│   └── advanced/
├── executive-skills/
│   ├── financial/
│   ├── legal/
│   ├── revenue/
│   ├── technology/
│   ├── executive/
│   └── personal/
├── quickbooks-connector/
│   ├── node-connector/
│   ├── python-connector/
│   ├── scripts/
│   └── aws/
├── airtable-integrations/
│   ├── bases/
│   └── scripts/
├── knowledge-base/
│   ├── entities.md
│   ├── relationships.md
│   └── history.md
└── scripts/
    ├── financial-cleanup.py
    ├── account-merging.py
    ├── dispute-generator.py
    ├── customer-followup.py
    ├── weekly-planning.py
    └── rapid-start.py
```

---

## 9. Quick Reference

### API Keys & Credentials (Store in 1Password)

| Service | Account | Key/Token | Notes |
|---------|---------|-----------|-------|
| Airtable | rbailey@connectedenergyservices.com | patwdhF1zazB2cdz9 | Expires Mar 4, 2026 |
| QuickBooks | (TBD) | (TBD) | SDK 17.0 |
| AWS | (TBD) | (TBD) | us-east-1 |

### 1Password Items to Create

1. **airtablecesapimaster** - Airtable API key
2. **quickbooks-enterprise** - QuickBooks Desktop SDK credentials
3. **aws-root** - AWS root account credentials
4. **connected-energy-banking** - Business banking credentials
5. **talian-operations** - Talian Technologies credentials

---

## 10. Next Steps

### Immediate (Today)
- [ ] Add Airtable credential to 1Password
- [ ] Test QuickBooks connector locally
- [ ] Run financial cleanup inventory script

### This Week
- [ ] Complete account inventory across all entities
- [ ] Set up Airtable bases for project tracking
- [ ] Deploy QuickBooks connector to AWS

### This Month
- [ ] Migrate/consolidate duplicate accounts
- [ ] Dispute all erroneous charges
- [ ] Implement weekly priority planning system

---

**Generated:** March 17, 2026  
**For:** Robert A Bailey Jr  
**Contact:** rbailey@connectedenergyservices.com
