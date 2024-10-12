# AzureMachineLearningModelManagementService.AsyncOperationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTime** | **Date** | The async operation creation time (UTC). | [optional] 
**endTime** | **Date** | The async operation end time (UTC)l | [optional] 
**error** | [**ModelErrorResponse**](ModelErrorResponse.md) |  | [optional] 
**id** | **String** | The async operation id. | [optional] 
**operationDetails** | [**AsyncOperationDetails**](AsyncOperationDetails.md) |  | [optional] 
**operationLog** | **String** | The async operation log. | [optional] 
**operationType** | **String** | The async operation type. | [optional] 
**parentRequestId** | **String** | The request id that created this operation | [optional] 
**resourceLocation** | **String** | The resource created/updated by the async operation. | [optional] 
**state** | **String** | The async operation state. | [optional] 



## Enum: StateEnum


* `NotStarted` (value: `"NotStarted"`)

* `Running` (value: `"Running"`)

* `Cancelled` (value: `"Cancelled"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `TimedOut` (value: `"TimedOut"`)




