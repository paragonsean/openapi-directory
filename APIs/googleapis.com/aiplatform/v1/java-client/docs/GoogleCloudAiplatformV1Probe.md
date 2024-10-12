

# GoogleCloudAiplatformV1Probe

Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exec** | [**GoogleCloudAiplatformV1ProbeExecAction**](GoogleCloudAiplatformV1ProbeExecAction.md) |  |  [optional] |
|**periodSeconds** | **Integer** | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. Must be less than timeout_seconds. Maps to Kubernetes probe argument &#39;periodSeconds&#39;. |  [optional] |
|**timeoutSeconds** | **Integer** | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. Must be greater or equal to period_seconds. Maps to Kubernetes probe argument &#39;timeoutSeconds&#39;. |  [optional] |



