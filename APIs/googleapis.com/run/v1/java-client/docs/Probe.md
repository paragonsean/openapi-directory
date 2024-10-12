

# Probe

Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exec** | [**ExecAction**](ExecAction.md) |  |  [optional] |
|**failureThreshold** | **Integer** | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |  [optional] |
|**grpc** | [**GRPCAction**](GRPCAction.md) |  |  [optional] |
|**httpGet** | [**HTTPGetAction**](HTTPGetAction.md) |  |  [optional] |
|**initialDelaySeconds** | **Integer** | Number of seconds after the container has started before the probe is initiated. Defaults to 0 seconds. Minimum value is 0. Maximum value for liveness probe is 3600. Maximum value for startup probe is 240. |  [optional] |
|**periodSeconds** | **Integer** | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Maximum value for liveness probe is 3600. Maximum value for startup probe is 240. Must be greater or equal than timeout_seconds. |  [optional] |
|**successThreshold** | **Integer** | Minimum consecutive successes for the probe to be considered successful after having failed. Must be 1 if set. |  [optional] |
|**tcpSocket** | [**TCPSocketAction**](TCPSocketAction.md) |  |  [optional] |
|**timeoutSeconds** | **Integer** | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Maximum value is 3600. Must be smaller than period_seconds; if period_seconds is not set, must be less or equal than 10. |  [optional] |



