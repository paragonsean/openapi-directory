

# ServiceResponseBase

The base service response. The correct inherited response based on computeType will be returned (ex. ACIServiceResponse)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeType** | [**ComputeTypeEnum**](#ComputeTypeEnum) | The compute environment type for the service. |  |
|**createdTime** | **OffsetDateTime** | The time the service was created. |  [optional] |
|**deploymentType** | [**DeploymentTypeEnum**](#DeploymentTypeEnum) | The deployment type for the service. |  [optional] |
|**description** | **String** | The service description. |  [optional] |
|**error** | [**ModelErrorResponse**](ModelErrorResponse.md) |  |  [optional] |
|**id** | **String** | The service Id. |  [optional] |
|**kvTags** | **Map&lt;String, String&gt;** | The service tag dictionary. Tags are mutable. |  [optional] |
|**name** | **String** | The service name. |  [optional] |
|**operationId** | **String** | The ID of the latest asynchronous operation for this service. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | The service property dictionary. Properties are immutable. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the service. |  [optional] |
|**updatedTime** | **OffsetDateTime** | The time the service was updated. |  [optional] |



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



## Enum: StateEnum

| Name | Value |
|---- | -----|
| TRANSITIONING | &quot;Transitioning&quot; |
| HEALTHY | &quot;Healthy&quot; |
| UNHEALTHY | &quot;Unhealthy&quot; |
| FAILED | &quot;Failed&quot; |



