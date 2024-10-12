

# PullRequestSimple

Pull Request Simple

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**PullRequestLinks**](PullRequestLinks.md) |  |  |
|**activeLockReason** | **String** |  |  [optional] |
|**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**assignees** | [**List&lt;SimpleUser&gt;**](SimpleUser.md) |  |  [optional] |
|**authorAssociation** | **AuthorAssociation** |  |  |
|**autoMerge** | [**AutoMerge**](AutoMerge.md) |  |  |
|**base** | [**PullRequestSimpleBase**](PullRequestSimpleBase.md) |  |  |
|**body** | **String** |  |  |
|**closedAt** | **OffsetDateTime** |  |  |
|**commentsUrl** | **URI** |  |  |
|**commitsUrl** | **URI** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**diffUrl** | **URI** |  |  |
|**draft** | **Boolean** | Indicates whether or not the pull request is a draft. |  [optional] |
|**head** | [**PullRequestSimpleBase**](PullRequestSimpleBase.md) |  |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** |  |  |
|**issueUrl** | **URI** |  |  |
|**labels** | [**List&lt;PullRequestSimpleLabelsInner&gt;**](PullRequestSimpleLabelsInner.md) |  |  |
|**locked** | **Boolean** |  |  |
|**mergeCommitSha** | **String** |  |  |
|**mergedAt** | **OffsetDateTime** |  |  |
|**milestone** | [**NullableMilestone**](NullableMilestone.md) |  |  |
|**nodeId** | **String** |  |  |
|**number** | **Integer** |  |  |
|**patchUrl** | **URI** |  |  |
|**requestedReviewers** | [**List&lt;SimpleUser&gt;**](SimpleUser.md) |  |  [optional] |
|**requestedTeams** | [**List&lt;Team&gt;**](Team.md) |  |  [optional] |
|**reviewCommentUrl** | **String** |  |  |
|**reviewCommentsUrl** | **URI** |  |  |
|**state** | **String** |  |  |
|**statusesUrl** | **URI** |  |  |
|**title** | **String** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |
|**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |



