

# Job

Information of a job execution in a workflow run

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkRunUrl** | **String** |  |  |
|**completedAt** | **OffsetDateTime** | The time that the job finished, in ISO 8601 format. |  |
|**conclusion** | [**ConclusionEnum**](#ConclusionEnum) | The outcome of the job. |  |
|**headSha** | **String** | The SHA of the commit that is being run. |  |
|**htmlUrl** | **String** |  |  |
|**id** | **Integer** | The id of the job. |  |
|**labels** | **List&lt;String&gt;** | Labels for the workflow job. Specified by the \&quot;runs_on\&quot; attribute in the action&#39;s workflow file. |  |
|**name** | **String** | The name of the job. |  |
|**nodeId** | **String** |  |  |
|**runAttempt** | **Integer** | Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run. |  [optional] |
|**runId** | **Integer** | The id of the associated workflow run. |  |
|**runUrl** | **String** |  |  |
|**runnerGroupId** | **Integer** | The ID of the runner group to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) |  |
|**runnerGroupName** | **String** | The name of the runner group to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) |  |
|**runnerId** | **Integer** | The ID of the runner to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) |  |
|**runnerName** | **String** | The name of the runner to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) |  |
|**startedAt** | **OffsetDateTime** | The time that the job started, in ISO 8601 format. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The phase of the lifecycle that the job is currently in. |  |
|**steps** | [**List&lt;JobStepsInner&gt;**](JobStepsInner.md) | Steps in this job. |  [optional] |
|**url** | **String** |  |  |



## Enum: ConclusionEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILURE | &quot;failure&quot; |
| NEUTRAL | &quot;neutral&quot; |
| CANCELLED | &quot;cancelled&quot; |
| SKIPPED | &quot;skipped&quot; |
| TIMED_OUT | &quot;timed_out&quot; |
| ACTION_REQUIRED | &quot;action_required&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| COMPLETED | &quot;completed&quot; |



