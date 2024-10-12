

# CreateServiceRequest

The base class for creating a service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeType** | [**ComputeTypeEnum**](#ComputeTypeEnum) | The compute environment type for the service. |  |
|**deploymentType** | [**DeploymentTypeEnum**](#DeploymentTypeEnum) | The deployment type for the service. |  [optional] |
|**description** | **String** | The description of the service. |  [optional] |
|**environmentImageRequest** | [**EnvironmentImageRequest**](EnvironmentImageRequest.md) |  |  [optional] |
|**imageId** | **String** | The Image Id. |  [optional] |
|**keys** | [**AuthKeys**](AuthKeys.md) |  |  [optional] |
|**kvTags** | **Map&lt;String, String&gt;** | The service tag dictionary. Tags are mutable. |  [optional] |
|**location** | **String** | The location of the service. |  [optional] |
|**name** | **String** | The service name. |  |
|**properties** | **Map&lt;String, String&gt;** | The service properties dictionary. Properties are immutable. |  [optional] |



## Enum: ComputeTypeEnum

| Name | Value |
|---- | -----|
| ACI | &quot;ACI&quot; |
| AKS | &quot;AKS&quot; |
| AMLCOMPUTE | &quot;AMLCOMPUTE&quot; |
| IOT | &quot;IOT&quot; |
| AKSENDPOINT | &quot;AKSENDPOINT&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



## Enum: DeploymentTypeEnum

| Name | Value |
|---- | -----|
| GRPC_REALTIME_ENDPOINT | &quot;GRPCRealtimeEndpoint&quot; |
| HTTP_REALTIME_ENDPOINT | &quot;HttpRealtimeEndpoint&quot; |
| BATCH | &quot;Batch&quot; |



