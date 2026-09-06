# Observability Dashboards

This folder contains portfolio-ready dashboard definitions for three common enterprise observability stacks.

## Grafana

- `kubernetes-cluster-overview.json` — node readiness, pod state, CPU, memory, restart trends, pending pods
- `service-slo-overview.json` — availability, error budget, request rate, 5xx rate, p95 latency, burn rate

Import these JSON files into Grafana and bind the `prometheus` datasource UID to your Prometheus instance.

## Datadog

- `kubernetes-platform-dashboard.json` — cluster/workload health dashboard-as-code example

Metric names can vary depending on Datadog Agent/OpenMetrics configuration, so adjust queries to match the deployed integration.

## Azure Monitor

- `aks-workbook.json` — AKS node, pod, and restart workbook using Log Analytics KQL

The queries assume Container Insights tables such as `KubeNodeInventory` and `KubePodInventory`.

## Dashboard design principles

A useful SRE dashboard should answer four questions quickly:

1. Is the service healthy?
2. Is customer impact occurring?
3. Is the platform saturated or failing?
4. What changed recently?

These dashboards intentionally emphasize health, saturation, errors, latency, restarts, and SLO/error-budget signals instead of decorative infrastructure counts.
