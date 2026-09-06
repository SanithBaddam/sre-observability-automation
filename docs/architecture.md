# Reliability Architecture

```mermaid
flowchart LR
    App[Services] --> Metrics[Prometheus Metrics]
    K8s[Kubernetes Events] --> Metrics
    Metrics --> Rules[Recording & Alert Rules]
    Rules --> AM[Alertmanager]
    AM --> Enricher[Incident Enricher]
    Enricher --> Pager[Pager / ChatOps]
    Enricher --> Runbook[Runbook]
    Metrics --> Grafana[Grafana]
    Metrics --> SLO[SLO / Error Budget]
```

The design separates signal collection, alert evaluation, enrichment, and human response. Automated remediation is intentionally bounded so incidents remain auditable and reversible.
