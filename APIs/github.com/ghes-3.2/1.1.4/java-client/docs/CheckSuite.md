

# CheckSuite

A suite of checks performed on the code of a given code change

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**after** | **String** |  |  |
|**app** | [**NullableIntegration**](NullableIntegration.md) |  |  |
|**before** | **String** |  |  |
|**checkRunsUrl** | **String** |  |  |
|**conclusion** | [**ConclusionEnum**](#ConclusionEnum) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**headBranch** | **String** |  |  |
|**headCommit** | [**SimpleCommit**](SimpleCommit.md) |  |  |
|**headSha** | **String** | The SHA of the head commit that is being checked. |  |
|**id** | **Integer** |  |  |
|**latestCheckRunsCount** | **Integer** |  |  |
|**nodeId** | **String** |  |  |
|**pullRequests** | [**List&lt;PullRequestMinimal&gt;**](PullRequestMinimal.md) |  |  |
|**repository** | [**MinimalRepository**](MinimalRepository.md) |  |  |
|**rerequestable** | **Boolean** |  |  [optional] |
|**runsRerequestable** | **Boolean** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
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



