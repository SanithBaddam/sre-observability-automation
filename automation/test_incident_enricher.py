from incident_enricher import diagnostic_plan, normalize_alert


def test_restart_alert_plan():
    incident = normalize_alert({"labels": {
        "alertname": "KubernetesHighPodRestartRate",
        "severity": "warning",
        "namespace": "payments",
        "pod": "api-123",
    }})
    assert incident.resource == "api-123"
    assert "inspect previous container logs" in diagnostic_plan(incident)
