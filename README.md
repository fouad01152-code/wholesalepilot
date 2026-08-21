# WholesalePilot 🚀

WholesalePilot is a B2B wholesale sales workspace for buyer discovery, outreach, quotes, orders, payments, fulfillment, and sales intelligence.

## Production architecture

- 🐍 Python web application (`server.py`)
- 🗄️ PostgreSQL in production through `DATABASE_URL`
- 💾 SQLite fallback for local development and tests
- ⚙️ Background outreach worker (embedded for the free beta deployment; `worker.py` can run separately later)
- 📧 Gmail / Outlook OAuth or SMTP + IMAP
- 💳 Stripe Checkout + manual bank-transfer confirmation
- 🔐 Workspace-based authentication and role permissions

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python server.py
```

Open `http://127.0.0.1:8765`.

Demo login:

- Email: `demo@wholesalepilot.local`
- Password: `Demo123!`

## Database

Production uses PostgreSQL when `DATABASE_URL` is present. The application automatically applies the current schema from `postgres_schema.sql` on startup.

Without `DATABASE_URL`, WholesalePilot uses local SQLite for development/testing.

## Render

`render.yaml` defines the intended production topology and links `wholesalepilot-live` to `wholesalepilot-db` using Render's private PostgreSQL connection string.

For beta, the web service runs the outreach worker in-process (`RUN_EMBEDDED_WORKER=true`) so scheduled jobs continue without the browser being open. Move it to a dedicated Render background worker before larger-volume sending.

## Tests

```bash
python ui_wiring_audit.py
python smoke_test.py
python smoke_test_v10.py
```

The regression suite covers authentication, buyer discovery, buyer portal, cart/quote/order, payment gating, fulfillment, campaign launch checks, background processing, SMTP delivery, and persistence.
