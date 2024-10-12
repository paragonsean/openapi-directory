# AzureMachineLearningModelManagementService.ServiceResponseBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computeType** | **String** | The compute environment type for the service. | 
**createdTime** | **Date** | The time the service was created. | [optional] 
**deploymentType** | **String** | The deployment type for the service. | [optional] 
**description** | **String** | The service description. | [optional] 
**error** | [**ModelErrorResponse**](ModelErrorResponse.md) |  | [optional] 
**id** | **String** | The service Id. | [optional] 
**kvTags** | **{String: String}** | The service tag dictionary. Tags are mutable. | [optional] 
**name** | **String** | The service name. | [optional] 
**operationId** | **String** | The ID of the latest asynchronous operation for this service. | [optional] 
**properties** | **{String: String}** | The service property dictionary. Properties are immutable. | [optional] 
**state** | **String** | The current state of the service. | [optional] 
**updatedTime** | **Date** | The time the service was updated. | [optional] 



## Enum: ComputeTypeEnum


* `ACI` (value: `"ACI"`)

* `AKS` (value: `"AKS"`)

* `AMLCOMPUTE` (value: `"AMLCOMPUTE"`)

* `IOT` (value: `"IOT"`)

* `AKSENDPOINT` (value: `"AKSENDPOINT"`)

* `UNKNOWN` (value: `"UNKNOWN"`)





## Enum: DeploymentTypeEnum


* `GRPCRealtimeEndpoint` (value: `"GRPCRealtimeEndpoint"`)

* `HttpRealtimeEndpoint` (value: `"HttpRealtimeEndpoint"`)

* `Batch` (value: `"Batch"`)





## Enum: StateEnum


* `Transitioning` (value: `"Transitioning"`)

* `Healthy` (value: `"Healthy"`)

* `Unhealthy` (value: `"Unhealthy"`)

* `Failed` (value: `"Failed"`)




