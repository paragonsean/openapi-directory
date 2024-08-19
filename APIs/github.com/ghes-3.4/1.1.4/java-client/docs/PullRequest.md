

# PullRequest

Pull requests let you tell others about changes you've pushed to a repository on GitHub. Once a pull request is sent, interested parties can review the set of changes, discuss potential modifications, and even push follow-up commits if necessary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**PullRequestLinks**](PullRequestLinks.md) |  |  |
|**activeLockReason** | **String** |  |  [optional] |
|**additions** | **Integer** |  |  |
|**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**assignees** | [**List&lt;SimpleUser&gt;**](SimpleUser.md) |  |  [optional] |
|**authorAssociation** | **AuthorAssociation** |  |  |
|**autoMerge** | [**AutoMerge**](AutoMerge.md) |  |  |
|**base** | [**PullRequestBase**](PullRequestBase.md) |  |  |
|**body** | **String** |  |  |
|**changedFiles** | **Integer** |  |  |
|**closedAt** | **OffsetDateTime** |  |  |
|**comments** | **Integer** |  |  |
|**commentsUrl** | **URI** |  |  |
|**commits** | **Integer** |  |  |
|**commitsUrl** | **URI** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**deletions** | **Integer** |  |  |
|**diffUrl** | **URI** |  |  |
|**draft** | **Boolean** | Indicates whether or not the pull request is a draft. |  [optional] |
|**head** | [**PullRequestHead**](PullRequestHead.md) |  |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** |  |  |
|**issueUrl** | **URI** |  |  |
|**labels** | [**List&lt;PullRequestLabelsInner&gt;**](PullRequestLabelsInner.md) |  |  |
|**locked** | **Boolean** |  |  |
|**maintainerCanModify** | **Boolean** | Indicates whether maintainers can modify the pull request. |  |
|**mergeCommitSha** | **String** |  |  |
|**mergeable** | **Boolean** |  |  |
|**mergeableState** | **String** |  |  |
|**merged** | **Boolean** |  |  |
|**mergedAt** | **OffsetDateTime** |  |  |
|**mergedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**milestone** | [**NullableMilestone**](NullableMilestone.md) |  |  |
|**nodeId** | **String** |  |  |
|**number** | **Integer** | Number uniquely identifying the pull request within its repository. |  |
|**patchUrl** | **URI** |  |  |
|**rebaseable** | **Boolean** |  |  [optional] |
|**requestedReviewers** | [**List&lt;SimpleUser&gt;**](SimpleUser.md) |  |  [optional] |
|**requestedTeams** | [**List&lt;TeamSimple&gt;**](TeamSimple.md) |  |  [optional] |
|**reviewCommentUrl** | **String** |  |  |
|**reviewComments** | **Integer** |  |  |
|**reviewCommentsUrl** | **URI** |  |  |
|**state** | [**StateEnum**](#StateEnum) | State of this Pull Request. Either &#x60;open&#x60; or &#x60;closed&#x60;. |  |
|**statusesUrl** | **URI** |  |  |
|**title** | **String** | The title of the pull request. |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |
|**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;open&quot; |
| CLOSED | &quot;closed&quot; |



