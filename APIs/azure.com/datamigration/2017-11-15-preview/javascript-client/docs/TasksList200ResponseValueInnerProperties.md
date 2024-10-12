# AzureDataMigrationServiceResourceProvider.TasksList200ResponseValueInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[OperationsListDefaultResponseError]**](OperationsListDefaultResponseError.md) | Array of errors. This is ignored if submitted. | [optional] [readonly] 
**state** | **String** | The state of the task. This is ignored if submitted. | [optional] [readonly] 
**taskType** | **String** | Task type. | 



## Enum: StateEnum


* `Unknown` (value: `"Unknown"`)

* `Queued` (value: `"Queued"`)

* `Running` (value: `"Running"`)

* `Canceled` (value: `"Canceled"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `FailedInputValidation` (value: `"FailedInputValidation"`)

* `Faulted` (value: `"Faulted"`)




