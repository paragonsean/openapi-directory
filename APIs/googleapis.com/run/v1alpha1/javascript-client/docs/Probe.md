# CloudRunAdminApi.Probe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exec** | [**ExecAction**](ExecAction.md) |  | [optional] 
**failureThreshold** | **Number** | (Optional) Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. | [optional] 
**grpc** | [**GRPCAction**](GRPCAction.md) |  | [optional] 
**httpGet** | [**HTTPGetAction**](HTTPGetAction.md) |  | [optional] 
**initialDelaySeconds** | **Number** | (Optional) Number of seconds after the container has started before the probe is initiated. Defaults to 0 seconds. Minimum value is 0. Maximum value for liveness probe is 3600. Maximum value for startup probe is 240. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 
**periodSeconds** | **Number** | (Optional) How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Maximum value for liveness probe is 3600. Maximum value for startup probe is 240. Must be greater or equal than timeout_seconds. | [optional] 
**successThreshold** | **Number** | (Optional) Minimum consecutive successes for the probe to be considered successful after having failed. Must be 1 if set. | [optional] 
**tcpSocket** | [**TCPSocketAction**](TCPSocketAction.md) |  | [optional] 
**timeoutSeconds** | **Number** | (Optional) Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Maximum value is 3600. Must be smaller than period_seconds. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 


