# CloudRunAdminApi.GoogleCloudRunV2Probe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failureThreshold** | **Number** | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. | [optional] 
**grpc** | [**GoogleCloudRunV2GRPCAction**](GoogleCloudRunV2GRPCAction.md) |  | [optional] 
**httpGet** | [**GoogleCloudRunV2HTTPGetAction**](GoogleCloudRunV2HTTPGetAction.md) |  | [optional] 
**initialDelaySeconds** | **Number** | Number of seconds after the container has started before the probe is initiated. Defaults to 0 seconds. Minimum value is 0. Maximum value for liveness probe is 3600. Maximum value for startup probe is 240. | [optional] 
**periodSeconds** | **Number** | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Maximum value for liveness probe is 3600. Maximum value for startup probe is 240. Must be greater or equal than timeout_seconds. | [optional] 
**tcpSocket** | [**GoogleCloudRunV2TCPSocketAction**](GoogleCloudRunV2TCPSocketAction.md) |  | [optional] 
**timeoutSeconds** | **Number** | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Maximum value is 3600. Must be smaller than period_seconds. | [optional] 


