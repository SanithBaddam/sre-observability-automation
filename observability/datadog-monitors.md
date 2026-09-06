# Datadog Monitor Design

## Kubernetes restart monitor
Trigger when restart rate is sustained rather than on a single restart. Group by namespace and workload, attach team ownership, and link the pod restart runbook.

## Latency SLO monitor
Page only on fast error-budget burn. Slow-burn alerts should create a ticket or operational follow-up instead of waking an engineer.

## Node saturation monitor
Correlate CPU, memory, disk pressure, pending pods, and autoscaler events before treating node pressure as a paging event.

## Standards
Every monitor should define owner, severity, expected action, dashboard link, runbook link, and a clear recovery condition.
