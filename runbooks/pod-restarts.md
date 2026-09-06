# Runbook: Repeated Pod Restarts

1. Confirm impact and affected namespaces.
2. Review `kubectl describe pod` events.
3. Inspect current and previous container logs.
4. Compare restart timing with deployments/config changes.
5. Check OOMKilled, probe failures, dependency errors, and throttling.
6. Roll back only when a recent change is strongly correlated and rollback is safe.

Record the root cause and add a prevention action after recovery.
