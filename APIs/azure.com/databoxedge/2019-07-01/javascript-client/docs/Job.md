# DataBoxEdgeManagementClient.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The UTC date and time at which the job completed. | [optional] [readonly] 
**error** | [**JobErrorDetails**](JobErrorDetails.md) |  | [optional] 
**id** | **String** | The path ID that uniquely identifies the object. | [optional] [readonly] 
**name** | **String** | The name of the object. | [optional] [readonly] 
**percentComplete** | **Number** | The percentage of the job that is complete. | [optional] [readonly] 
**properties** | [**JobProperties**](JobProperties.md) |  | [optional] 
**startTime** | **Date** | The UTC date and time at which the job started. | [optional] [readonly] 
**status** | **String** | The current status of the job. | [optional] [readonly] 
**type** | **String** | The hierarchical type of the object. | [optional] [readonly] 



## Enum: StatusEnum


* `Invalid` (value: `"Invalid"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `Paused` (value: `"Paused"`)

* `Scheduled` (value: `"Scheduled"`)




