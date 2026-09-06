from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Incident:
    alert: str
    severity: str
    namespace: str | None
    resource: str | None


def normalize_alert(payload: dict[str, Any]) -> Incident:
    labels = payload.get("labels", {})
    return Incident(
        alert=labels.get("alertname", "unknown"),
        severity=labels.get("severity", "unknown"),
        namespace=labels.get("namespace"),
        resource=labels.get("pod") or labels.get("node"),
    )


def diagnostic_plan(incident: Incident) -> list[str]:
    common = ["check recent deployments", "inspect related events", "review saturation signals"]
    if "Node" in incident.alert:
        return ["inspect node conditions", "review node pool capacity", *common]
    if "Restart" in incident.alert:
        return ["inspect previous container logs", "check probes and resource limits", *common]
    return common
