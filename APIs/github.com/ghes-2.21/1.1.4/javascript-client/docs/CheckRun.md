# GitHubV3RestApi.CheckRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**NullableIntegration**](NullableIntegration.md) |  | 
**checkSuite** | [**CheckRunCheckSuite**](CheckRunCheckSuite.md) |  | 
**completedAt** | **Date** |  | 
**conclusion** | **String** |  | 
**deployment** | [**DeploymentSimple**](DeploymentSimple.md) |  | [optional] 
**detailsUrl** | **String** |  | 
**externalId** | **String** |  | 
**headSha** | **String** | The SHA of the commit that is being checked. | 
**htmlUrl** | **String** |  | 
**id** | **Number** | The id of the check. | 
**name** | **String** | The name of the check. | 
**nodeId** | **String** |  | 
**output** | [**CheckRunOutput**](CheckRunOutput.md) |  | 
**pullRequests** | [**[PullRequestMinimal]**](PullRequestMinimal.md) |  | 
**startedAt** | **Date** |  | 
**status** | **String** | The phase of the lifecycle that the check is currently in. | 
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




