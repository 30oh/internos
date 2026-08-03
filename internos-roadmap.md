# InternOS — Project Roadmap & Checklist

**Project:** Internship Tracker and Skill Gap Analyser
**Mode:** Mentor-guided, self-written code
**Last updated:** Task 1, CSS styling in progress

---

## How to use this document

- This is your single source of truth for progress. Paste it into any new chat so Claude has full context without re-explaining everything.
- When you finish a step, change `- [ ]` to `- [x]`.
- When you ask for help in a new chat, say which task/step you're on (e.g. "Task 3, step: defining the Application model") — that's enough context if this file is attached.
- Ground rules for how I'll help, carried over from your original brief:
  - I explain the *why* before the *how*.
  - I don't hand you finished files unless you explicitly ask for one.
  - I give structure, hints, and things to look up — you write the code.
  - I'll flag common beginner mistakes and ask interview-style questions after each feature.
  - I won't jump ahead to future tasks unless you ask.

---

## Tech Stack (locked in until core project is done)

Python · Flask · HTML · CSS · light JavaScript · Jinja2 · SQLite · SQLAlchemy · Flask-WTF · Pytest · Black · Ruff · Git/GitHub

No React, TypeScript, Docker, AWS, or AI agents until the core project works end-to-end.

---

## Data Model Reference

**Application**
Company · Role · Location · Job URL · Deadline · Status · Job Description · Notes

**Statuses:** Saved · Applied · Online Assessment · Interview · Offer · Rejected · Withdrawn

---

## Task 1 — Flask Starter App
**Goal:** Static multi-page Flask app with a shared layout, no database, no forms wired up yet.

- [x] Flask project setup
- [x] Folder structure (`app.py`, `templates/`, `static/css/`)
- [x] Base template (`base.html`) — shared shell only, no page-specific content
- [x] Navbar using `url_for()`
- [x] Home page
- [x] Applications page (static example cards)
- [x] Add Application page (visual-only form, doesn't submit)
- [x] Dashboard page (placeholder stats)
- [ ] CSS styling — in progress, working through in this order:
  - [ ] Reset
  - [ ] Body
  - [ ] Container/layout
  - [ ] Navbar
  - [ ] Buttons
  - [ ] Cards
  - [ ] Forms
  - [ ] Dashboard grid
  - [ ] Responsive design (media queries)
- [ ] Manual test pass: click through every page, check every nav link resolves, no broken links/images
- [ ] Final Task 1 commit + push

**Interview angle to be ready for:** "Why separate `base.html` from page templates? What does `{% block %}` actually do at render time?"

---

## Task 2 — Add Application Form (in-memory)
**Goal:** Learn GET vs POST, form handling, redirects — before touching a database.

- [ ] Create an in-memory Python list of dicts to hold applications
- [ ] Wire the Add Application form to a POST route
- [ ] Read submitted data via `request.form`
- [ ] Redirect after successful POST (Post/Redirect/Get pattern — look up *why* this pattern exists)
- [ ] Loop over the list with Jinja to render real cards on the Applications page
- [ ] Add a flash message on successful submission
- [ ] Commit: something like `feature/add-application-form: wire up form to in-memory list`

**Interview angle:** "Why redirect after a POST instead of just rendering the result directly?"

---

## Task 3 — Replace List with SQLite (SQLAlchemy)
**Goal:** Learn CRUD with a real database.

- [ ] Install Flask-SQLAlchemy
- [ ] `config.py` — database URI, config class(es)
- [ ] Define `Application` model in `models.py`
- [ ] Initialize `db` and create tables
- [ ] Add Application → insert into DB instead of the list
- [ ] Applications page → query all rows from DB
- [ ] Commit: `feature/database: migrate to SQLite with SQLAlchemy`

**Interview angle:** "What does an ORM give you over writing raw SQL? What's a trade-off?"

---

## Task 4 — Edit, Delete, Status Update, Filter, Sort
- [ ] Edit application (route + pre-filled form)
- [ ] Delete application (with a confirmation step)
- [ ] Update status (inline dropdown or dedicated route)
- [ ] Filter by status (via query parameters)
- [ ] Sort by deadline (via query parameters)
- [ ] Commit per sub-feature, not all at once

**Interview angle:** "How do you prevent someone from editing an application that isn't theirs, once auth exists?" (Note this now, solve it in Task 7.)

---

## Task 5 — Skill Gap Analyser (keyword matching, no AI)
- [ ] Define a keyword list of trackable skills
- [ ] Textarea input for pasting a job description
- [ ] `skill_analyser.py`: extract skills via simple string/keyword matching
- [ ] Compare extracted skills against the user's own skills (hardcoded list for now)
- [ ] Render Required / Your / Missing skills
- [ ] Commit: `feature/skill-analyser: keyword-based extraction`

**Interview angle:** "What are the limitations of keyword matching vs. NLP? Why might that trade-off be fine for v1?"

---

## Task 6 — Recommendations
- [ ] `recommendations.py`: lookup/dict mapping missing skill → suggested project(s)
- [ ] Render recommended projects based on missing skills
- [ ] Commit

---

## Task 7 — Authentication
- [ ] `User` model with hashed passwords (`werkzeug.security`)
- [ ] Register route + Flask-WTF form + validation
- [ ] Login route + session handling (Flask-Login is the standard choice)
- [ ] Logout route
- [ ] `@login_required` on protected routes
- [ ] Foreign key: `Application.user_id` → `User.id`
- [ ] Every query filtered by `current_user.id` — this is what actually enforces "users only see their own data"
- [ ] CSRF protection (Flask-WTF gives this by default — understand *why* it's needed)
- [ ] Secret key and DB path from environment variables (`.env`, `python-dotenv`, `.gitignore`'d)
- [ ] Secure session cookie settings
- [ ] Commit: `feature/authentication: ...`

**Interview angle:** "Walk me through what happens, step by step, when a logged-in user tries to edit someone else's application."

---

## Task 8 — Testing & Code Quality
- [ ] Pytest setup: `conftest.py`, test client fixture, test DB (separate from dev DB)
- [ ] Test CRUD operations
- [ ] Test skill extraction logic
- [ ] Test recommendation logic
- [ ] Test register/login/logout
- [ ] Test access control (user A cannot read/edit user B's applications)
- [ ] Run Black, fix formatting
- [ ] Run Ruff, fix lint warnings
- [ ] Commit

---

## Task 9 — UI Polish, README, Screenshots
- [ ] Consistent styling pass across all pages
- [ ] Mobile responsiveness check
- [ ] README: project description, features, tech stack, setup instructions, screenshots
- [ ] Screenshots saved and linked in README
- [ ] Commit

---

## Task 10 — Deploy & CV
- [ ] Pick a host (e.g. Render, PythonAnywhere, Railway — worth comparing free tiers when you get here)
- [ ] Production config: `DEBUG=False`, env vars set on host
- [ ] Deploy, smoke-test the live site
- [ ] Update CV with project + live link
- [ ] Prepare 3–5 interview talking points (architecture decisions, security choices, one bug you had to debug)

---

## Security Checklist (cross-cutting — tick off as each lands, mostly Task 7–8)

- [ ] Password hashing
- [ ] CSRF protection
- [ ] Input validation (WTForms validators)
- [ ] Environment variables for secrets
- [ ] SQL injection prevention (ORM usage, no raw string-built queries)
- [ ] Access control (`login_required` + ownership filtering on every query)
- [ ] Secure session cookies
- [ ] Debug mode off in production

---

## Git Workflow Reminder

```
main
feature/add-application-form
feature/database
feature/skill-analyser
feature/authentication
```

Small, focused commits. One logical change per commit.

---

## Current Status Snapshot

**On:** Task 1 — CSS styling (reset done, body/container/navbar/etc. next)
**Not started:** Tasks 2–10
