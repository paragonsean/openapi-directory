

# Issue

Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeLockReason** | **String** |  |  [optional] |
|**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**assignees** | [**List&lt;SimpleUser&gt;**](SimpleUser.md) |  |  [optional] |
|**authorAssociation** | **AuthorAssociation** |  |  |
|**body** | **String** | Contents of the issue |  [optional] |
|**bodyHtml** | **String** |  |  [optional] |
|**bodyText** | **String** |  |  [optional] |
|**closedAt** | **OffsetDateTime** |  |  |
|**closedBy** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  [optional] |
|**comments** | **Integer** |  |  |
|**commentsUrl** | **URI** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**draft** | **Boolean** |  |  [optional] |
|**eventsUrl** | **URI** |  |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** |  |  |
|**labels** | [**List&lt;IssueLabelsInner&gt;**](IssueLabelsInner.md) | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository |  |
|**labelsUrl** | **String** |  |  |
|**locked** | **Boolean** |  |  |
|**milestone** | [**NullableMilestone**](NullableMilestone.md) |  |  |
|**nodeId** | **String** |  |  |
|**number** | **Integer** | Number uniquely identifying the issue within its repository |  |
|**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  |  [optional] |
|**pullRequest** | [**IssuePullRequest**](IssuePullRequest.md) |  |  [optional] |
|**reactions** | [**ReactionRollup**](ReactionRollup.md) |  |  [optional] |
|**repository** | [**Repository**](Repository.md) |  |  [optional] |
|**repositoryUrl** | **URI** |  |  |
|**state** | **String** | State of the issue; either &#39;open&#39; or &#39;closed&#39; |  |
|**stateReason** | [**StateReasonEnum**](#StateReasonEnum) | The reason for the current state |  [optional] |
|**timelineUrl** | **URI** |  |  [optional] |
|**title** | **String** | Title of the issue |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** | URL for the issue |  |
|**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |



## Enum: StateReasonEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;completed&quot; |
| REOPENED | &quot;reopened&quot; |
| NOT_PLANNED | &quot;not_planned&quot; |



