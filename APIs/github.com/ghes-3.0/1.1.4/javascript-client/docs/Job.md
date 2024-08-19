# GitHubV3RestApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkRunUrl** | **String** |  | 
**completedAt** | **Date** | The time that the job finished, in ISO 8601 format. | 
**conclusion** | **String** | The outcome of the job. | 
**headSha** | **String** | The SHA of the commit that is being run. | 
**htmlUrl** | **String** |  | 
**id** | **Number** | The id of the job. | 
**name** | **String** | The name of the job. | 
**nodeId** | **String** |  | 
**runAttempt** | **Number** | Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run. | [optional] 
**runId** | **Number** | The id of the associated workflow run. | 
**runUrl** | **String** |  | 
**startedAt** | **Date** | The time that the job started, in ISO 8601 format. | 
**status** | **String** | The phase of the lifecycle that the job is currently in. | 
**steps** | [**[JobStepsInner]**](JobStepsInner.md) | Steps in this job. | [optional] 
**url** | **String** |  | 



## Enum: StatusEnum


* `queued` (value: `"queued"`)

* `in_progress` (value: `"in_progress"`)

* `completed` (value: `"completed"`)




