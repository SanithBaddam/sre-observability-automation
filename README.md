# SRE Observability & Automated Incident Response

An operations-focused reliability platform that combines Prometheus alerting, Python-based incident enrichment, Kubernetes health signals, and repeatable runbooks.

## Goals

- Detect actionable reliability symptoms rather than noisy infrastructure events
- Standardize alert metadata, ownership, severity, and runbook links
- Automate first-response diagnostics without automating unsafe remediation
- Demonstrate SRE practices: SLOs, error budgets, incident response, and postmortems

## Flow

```text
Application / Kubernetes
        |
        v
Prometheus ---> Alertmanager ---> Incident webhook
                                    |
                                    v
                              Python enricher
                                    |
                         diagnostics + runbook
```

## Repository layout

- `prometheus/` alerting rules
- `automation/` incident enrichment service
- `runbooks/` operational procedures
- `slo/` service-level objectives
- `.github/workflows/` validation pipeline

The automation intentionally gathers evidence before remediation. Production incident automation should have bounded permissions, auditable actions, and explicit rollback behavior.
