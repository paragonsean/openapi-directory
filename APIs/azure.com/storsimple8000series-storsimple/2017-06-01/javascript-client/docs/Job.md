# StorSimple8000SeriesManagementClient.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The UTC time at which the job completed. | [optional] 
**error** | [**JobErrorDetails**](JobErrorDetails.md) |  | [optional] 
**percentComplete** | **Number** | The percentage of the job that is already complete. | 
**properties** | [**JobProperties**](JobProperties.md) |  | [optional] 
**startTime** | **Date** | The UTC time at which the job was started. | [optional] 
**status** | **String** | The current status of the job. | 
**id** | **String** | The path ID that uniquely identifies the object. | [optional] [readonly] 
**kind** | **String** | The Kind of the object. Currently only Series8000 is supported | [optional] 
**name** | **String** | The name of the object. | [optional] [readonly] 
**type** | **String** | The hierarchical type of the object. | [optional] [readonly] 



## Enum: StatusEnum


* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)





## Enum: KindEnum


* `Series8000` (value: `"Series8000"`)




