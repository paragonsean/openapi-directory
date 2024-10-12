# AzureMediaServices.JobProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlationData** | **{String: String}** | Customer provided correlation data that will be returned in Job completed events. | [optional] 
**created** | **Date** | The UTC date and time when the Job was created, in &#39;YYYY-MM-DDThh:mm:ssZ&#39; format. | [optional] [readonly] 
**description** | **String** | Optional customer supplied description of the Job. | [optional] 
**input** | [**JobInput**](JobInput.md) |  | 
**lastModified** | **Date** | The UTC date and time when the Job was last updated, in &#39;YYYY-MM-DDThh:mm:ssZ&#39; format. | [optional] [readonly] 
**outputs** | [**[JobOutput]**](JobOutput.md) | The outputs for the Job. | 
**priority** | **String** | Priority with which the job should be processed. Higher priority jobs are processed before lower priority jobs. If not set, the default is normal. | [optional] 
**state** | **String** | The current state of the job. | [optional] [readonly] 



## Enum: PriorityEnum


* `Low` (value: `"Low"`)

* `Normal` (value: `"Normal"`)

* `High` (value: `"High"`)





## Enum: StateEnum


* `Canceled` (value: `"Canceled"`)

* `Canceling` (value: `"Canceling"`)

* `Error` (value: `"Error"`)

* `Finished` (value: `"Finished"`)

* `Processing` (value: `"Processing"`)

* `Queued` (value: `"Queued"`)

* `Scheduled` (value: `"Scheduled"`)




