# AzureMachineLearningComputeManagementClient.AsyncOperationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The date time that the async operation finished. | [optional] [readonly] 
**errorInfo** | [**AsyncOperationErrorInfo**](AsyncOperationErrorInfo.md) |  | [optional] 
**id** | **String** | Async operation id. | [optional] 
**name** | **String** | Async operation name. | [optional] 
**percentComplete** | **Number** | Async operation progress. | [optional] 
**provisioningState** | **String** | Read Only: The provisioning state of the cluster. Valid values are Unknown, Provisioning, Succeeded, and Failed. | [optional] [readonly] 
**startTime** | **Date** | The date time that the async operation started. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Unknown` (value: `"Unknown"`)

* `Updating` (value: `"Updating"`)

* `Creating` (value: `"Creating"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)




