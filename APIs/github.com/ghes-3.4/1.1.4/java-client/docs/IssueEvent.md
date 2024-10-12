

# IssueEvent

Issue Event

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actor** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  [optional] |
|**assigner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  [optional] |
|**authorAssociation** | **AuthorAssociation** |  |  [optional] |
|**commitId** | **String** |  |  |
|**commitUrl** | **String** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**dismissedReview** | [**IssueEventDismissedReview**](IssueEventDismissedReview.md) |  |  [optional] |
|**event** | **String** |  |  |
|**id** | **Integer** |  |  |
|**issue** | [**NullableIssue**](NullableIssue.md) |  |  [optional] |
|**label** | [**IssueEventLabel**](IssueEventLabel.md) |  |  [optional] |
|**lockReason** | **String** |  |  [optional] |
|**milestone** | [**IssueEventMilestone**](IssueEventMilestone.md) |  |  [optional] |
|**nodeId** | **String** |  |  |
|**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  |  [optional] |
|**projectCard** | [**IssueEventProjectCard**](IssueEventProjectCard.md) |  |  [optional] |
|**rename** | [**IssueEventRename**](IssueEventRename.md) |  |  [optional] |
|**requestedReviewer** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  [optional] |
|**requestedTeam** | [**Team**](Team.md) |  |  [optional] |
|**reviewRequester** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  [optional] |
|**url** | **URI** |  |  |



