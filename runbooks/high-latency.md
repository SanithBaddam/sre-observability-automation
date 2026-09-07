# Runbook: High Service Latency

## Detection

Trigger on sustained p95/p99 latency degradation correlated with customer-impacting request paths.

## Triage

1. Confirm whether traffic volume changed.
2. Compare latency across service instances and zones.
3. Review CPU, memory, thread pools, connection pools, and queue depth.
4. Check downstream dependency latency.
5. Compare against recent deployments and configuration changes.
6. Inspect saturation and retry amplification.

## Mitigation

Prefer reversible actions such as rollback, scaling, traffic shifting, or disabling an expensive feature path.

## Follow-up

Record the latency source, missed signals, and whether SLO alert thresholds need adjustment.
