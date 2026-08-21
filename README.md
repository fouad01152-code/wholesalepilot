# WholesalePilot

WholesalePilot is the B2B wholesale sales workspace currently deployed on Render.

## Current signup flow

- Create a real workspace/company
- Enter owner name, email, and password
- Owner account is created automatically
- New account is logged in immediately after signup
- Existing demo login remains available

Demo login:

- Email: `demo@wholesalepilot.local`
- Password: `Demo123!`

## Exact tested source snapshot

The exact tested source used for this deployment is stored in `source_bundle/part-*`.

To reconstruct the source tree locally:

```bash
python reconstruct_source.py
```

This extracts `wholesale-autopilot-v101/` with the complete application source, tests, deployment files, and documentation.

Archive SHA-256: `9367c7034b7a37a5e80dc70da39e3fb97090949cbf6d5ac3edd272c4b995160b`

Live service: https://wholesalepilot-live.onrender.com
