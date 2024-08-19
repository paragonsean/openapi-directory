# GitHubV3RestApi.JobStepsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completedAt** | **Date** | The time that the job finished, in ISO 8601 format. | [optional] 
**conclusion** | **String** | The outcome of the job. | 
**name** | **String** | The name of the job. | 
**number** | **Number** |  | 
**startedAt** | **Date** | The time that the step started, in ISO 8601 format. | [optional] 
**status** | **String** | The phase of the lifecycle that the job is currently in. | 



## Enum: StatusEnum


* `queued` (value: `"queued"`)

* `in_progress` (value: `"in_progress"`)

* `completed` (value: `"completed"`)




