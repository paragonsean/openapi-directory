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
**labels** | **[String]** | Labels for the workflow job. Specified by the \&quot;runs_on\&quot; attribute in the action&#39;s workflow file. | 
**name** | **String** | The name of the job. | 
**nodeId** | **String** |  | 
**runAttempt** | **Number** | Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run. | [optional] 
**runId** | **Number** | The id of the associated workflow run. | 
**runUrl** | **String** |  | 
**runnerGroupId** | **Number** | The ID of the runner group to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) | 
**runnerGroupName** | **String** | The name of the runner group to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) | 
**runnerId** | **Number** | The ID of the runner to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) | 
**runnerName** | **String** | The name of the runner to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) | 
**startedAt** | **Date** | The time that the job started, in ISO 8601 format. | 
**status** | **String** | The phase of the lifecycle that the job is currently in. | 
**steps** | [**[JobStepsInner]**](JobStepsInner.md) | Steps in this job. | [optional] 
**url** | **String** |  | 



## Enum: ConclusionEnum


* `success` (value: `"success"`)

* `failure` (value: `"failure"`)

* `neutral` (value: `"neutral"`)

* `cancelled` (value: `"cancelled"`)

* `skipped` (value: `"skipped"`)

* `timed_out` (value: `"timed_out"`)

* `action_required` (value: `"action_required"`)





## Enum: StatusEnum


* `queued` (value: `"queued"`)

* `in_progress` (value: `"in_progress"`)

* `completed` (value: `"completed"`)




