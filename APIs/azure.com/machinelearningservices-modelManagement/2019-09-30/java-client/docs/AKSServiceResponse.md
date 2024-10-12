

# AKSServiceResponse

The response for an AKS service.

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
|**deploymentStatus** | [**AKSReplicaStatus**](AKSReplicaStatus.md) |  |  [optional] |
|**environment** | [**ModelEnvironmentDefinition**](ModelEnvironmentDefinition.md) |  |  [optional] |
|**imageDetails** | [**ImageResponseBase**](ImageResponseBase.md) |  |  [optional] |
|**imageId** | **String** | The Id of the Image. |  [optional] |
|**livenessProbeRequirements** | [**LivenessProbeRequirements**](LivenessProbeRequirements.md) |  |  [optional] |
|**maxConcurrentRequestsPerContainer** | **Integer** | The maximum number of concurrent requests per container. |  [optional] |
|**maxQueueWaitMs** | **Integer** | Maximum time a request will wait in the queue (in milliseconds). After this time, the service will return 503 (Service Unavailable) |  [optional] |
|**modelConfigMap** | **Map&lt;String, Object&gt;** | Details on the models and configurations. |  [optional] |
|**models** | [**List&lt;Model&gt;**](Model.md) | The list of models. |  [optional] |
|**namespace** | **String** | The Kubernetes namespace of the deployment. |  [optional] |
|**numReplicas** | **Integer** | The number of replicas on the cluster. |  [optional] |
|**scoringTimeoutMs** | **Integer** | The scoring timeout in milliseconds. |  [optional] |
|**scoringUri** | **String** | The Uri for sending scoring requests. |  [optional] |
|**swaggerUri** | **String** | The Uri for sending swagger requests. |  [optional] |



