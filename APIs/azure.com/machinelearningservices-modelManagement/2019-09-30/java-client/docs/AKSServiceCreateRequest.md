

# AKSServiceCreateRequest

The request to create an AKS service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aadAuthEnabled** | **Boolean** | Whether or not AAD authentication is enabled. |  [optional] |
|**appInsightsEnabled** | **Boolean** | Whether or not Application Insights is enabled. |  [optional] |
|**authEnabled** | **Boolean** | Whether or not authentication is enabled. |  [optional] |
|**autoScaler** | [**AutoScaler**](AutoScaler.md) |  |  [optional] |
|**computeName** | **String** | The name of the compute resource. |  [optional] |
|**containerResourceRequirements** | [**ContainerResourceRequirements**](ContainerResourceRequirements.md) |  |  [optional] |
|**dataCollection** | [**ModelDataCollection**](ModelDataCollection.md) |  |  [optional] |
|**livenessProbeRequirements** | [**LivenessProbeRequirements**](LivenessProbeRequirements.md) |  |  [optional] |
|**maxConcurrentRequestsPerContainer** | **Integer** | The maximum number of concurrent requests per container. |  [optional] |
|**maxQueueWaitMs** | **Integer** | Maximum time a request will wait in the queue (in milliseconds). After this time, the service will return 503 (Service Unavailable) |  [optional] |
|**namespace** | **String** | Kubernetes namespace for the service. |  [optional] |
|**numReplicas** | **Integer** | The number of replicas on the cluster. |  [optional] |
|**scoringTimeoutMs** | **Integer** | The scoring timeout in milliseconds. |  [optional] |



