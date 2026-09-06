# Sample Data Strategy

The dashboards are built against real Prometheus/Kubernetes metric conventions rather than fake chart values.

For a local portfolio demonstration, point Prometheus at a Kubernetes cluster with kube-state-metrics and node-exporter enabled. The dashboards will then populate automatically from live metrics.

For screenshots or interviews, useful scenarios to demonstrate include:

- a namespace with elevated pod restarts
- a Pending pod caused by insufficient CPU
- a node moving out of Ready state
- a service generating controlled 5xx responses
- a latency increase that consumes SLO error budget

Avoid hard-coding fabricated production numbers into the dashboards. The dashboard definitions should stay reusable while the underlying metrics tell the story.
