# HybridDataManagementClient.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | Time at which the job ended in UTC ISO 8601 format. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**properties** | [**JobProperties**](JobProperties.md) |  | 
**startTime** | **Date** | Time at which the job was started in UTC ISO 8601 format. | 
**status** | **String** | Status of the job. | 
**id** | **String** | Id of the object. | [optional] [readonly] 
**name** | **String** | Name of the object. | [optional] [readonly] 
**type** | **String** | Type of the object. | [optional] [readonly] 



## Enum: StatusEnum


* `None` (value: `"None"`)

* `InProgress` (value: `"InProgress"`)

* `Succeeded` (value: `"Succeeded"`)

* `WaitingForAction` (value: `"WaitingForAction"`)

* `Failed` (value: `"Failed"`)

* `Cancelled` (value: `"Cancelled"`)

* `Cancelling` (value: `"Cancelling"`)




