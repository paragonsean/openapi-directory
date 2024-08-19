# StorSimpleManagementClient.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The UTC time at which the job completed | [optional] 
**error** | [**JobErrorDetails**](JobErrorDetails.md) |  | [optional] 
**percentComplete** | **Number** | The percentage of the job that is already complete | 
**properties** | [**JobProperties**](JobProperties.md) |  | [optional] 
**startTime** | **Date** | The UTC time at which the job was started | [optional] 
**status** | **String** | Current status of the job | 
**id** | **String** | The identifier. | [optional] [readonly] 
**name** | **String** | The name. | [optional] [readonly] 
**type** | **String** | The type. | [optional] [readonly] 



## Enum: StatusEnum


* `Invalid` (value: `"Invalid"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `Paused` (value: `"Paused"`)

* `Scheduled` (value: `"Scheduled"`)




