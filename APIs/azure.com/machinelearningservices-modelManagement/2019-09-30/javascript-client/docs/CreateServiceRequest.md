# AzureMachineLearningModelManagementService.CreateServiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computeType** | **String** | The compute environment type for the service. | 
**deploymentType** | **String** | The deployment type for the service. | [optional] 
**description** | **String** | The description of the service. | [optional] 
**environmentImageRequest** | [**EnvironmentImageRequest**](EnvironmentImageRequest.md) |  | [optional] 
**imageId** | **String** | The Image Id. | [optional] 
**keys** | [**AuthKeys**](AuthKeys.md) |  | [optional] 
**kvTags** | **{String: String}** | The service tag dictionary. Tags are mutable. | [optional] 
**location** | **String** | The location of the service. | [optional] 
**name** | **String** | The service name. | 
**properties** | **{String: String}** | The service properties dictionary. Properties are immutable. | [optional] 



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




