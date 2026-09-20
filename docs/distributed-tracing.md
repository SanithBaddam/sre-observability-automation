# Distributed Tracing

Metrics answer whether a service is unhealthy; traces help explain where request time is being spent across service boundaries.

The reference OpenTelemetry Collector accepts OTLP over gRPC/HTTP and keeps collection separate from vendor-specific backends.

Useful production attributes include service name, environment, deployment version, trace/span IDs, dependency name, and error status. Avoid attaching secrets or high-cardinality user data to telemetry.
