# AzureMlWebServicesManagementClient.AsyncOperationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The date time that the async operation finished. | [optional] [readonly] 
**errorInfo** | [**AsyncOperationErrorInfo**](AsyncOperationErrorInfo.md) |  | [optional] 
**id** | **String** | Async operation id. | [optional] [readonly] 
**name** | **String** | Async operation name. | [optional] [readonly] 
**percentComplete** | **Number** | Async operation progress. | [optional] [readonly] 
**provisioningState** | **String** | Read Only: The provisioning state of the web service. Valid values are Unknown, Provisioning, Succeeded, and Failed. | [optional] [readonly] 
**startTime** | **Date** | The date time that the async operation started. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Unknown` (value: `"Unknown"`)

* `Provisioning` (value: `"Provisioning"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)




