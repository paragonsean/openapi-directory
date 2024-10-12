

# Phase

Phase represents a collection of jobs that are logically grouped together for a `Rollout`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childRolloutJobs** | [**ChildRolloutJobs**](ChildRolloutJobs.md) |  |  [optional] |
|**deploymentJobs** | [**DeploymentJobs**](DeploymentJobs.md) |  |  [optional] |
|**id** | **String** | Output only. The ID of the Phase. |  [optional] [readonly] |
|**skipMessage** | **String** | Output only. Additional information on why the Phase was skipped, if available. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the Phase. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| ABORTED | &quot;ABORTED&quot; |
| SKIPPED | &quot;SKIPPED&quot; |



