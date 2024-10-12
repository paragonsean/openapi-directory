# GitHubV3RestApi.CheckSuite

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **String** |  | 
**app** | [**NullableIntegration**](NullableIntegration.md) |  | 
**before** | **String** |  | 
**checkRunsUrl** | **String** |  | 
**conclusion** | **String** |  | 
**createdAt** | **Date** |  | 
**headBranch** | **String** |  | 
**headCommit** | [**SimpleCommit**](SimpleCommit.md) |  | 
**headSha** | **String** | The SHA of the head commit that is being checked. | 
**id** | **Number** |  | 
**latestCheckRunsCount** | **Number** |  | 
**nodeId** | **String** |  | 
**pullRequests** | [**[PullRequestMinimal]**](PullRequestMinimal.md) |  | 
**repository** | [**MinimalRepository**](MinimalRepository.md) |  | 
**status** | **String** |  | 
**updatedAt** | **Date** |  | 
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




