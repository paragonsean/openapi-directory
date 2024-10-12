# InfluxOssApiService.Run

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finishedAt** | **Date** | Time run finished executing, RFC3339Nano. | [optional] [readonly] 
**id** | **String** |  | [optional] [readonly] 
**links** | [**RunLinks**](RunLinks.md) |  | [optional] 
**log** | [**[LogEvent]**](LogEvent.md) | An array of logs associated with the run. | [optional] [readonly] 
**requestedAt** | **Date** | Time run was manually requested, RFC3339Nano. | [optional] [readonly] 
**scheduledFor** | **Date** | Time used for run&#39;s \&quot;now\&quot; option, RFC3339. | [optional] 
**startedAt** | **Date** | Time run started executing, RFC3339Nano. | [optional] [readonly] 
**status** | **String** |  | [optional] [readonly] 
**taskID** | **String** |  | [optional] [readonly] 



## Enum: StatusEnum


* `scheduled` (value: `"scheduled"`)

* `started` (value: `"started"`)

* `failed` (value: `"failed"`)

* `success` (value: `"success"`)

* `canceled` (value: `"canceled"`)




