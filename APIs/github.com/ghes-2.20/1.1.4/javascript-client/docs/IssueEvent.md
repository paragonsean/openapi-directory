# GitHubV3RestApi.IssueEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**assigner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**authorAssociation** | [**AuthorAssociation**](AuthorAssociation.md) |  | [optional] 
**commitId** | **String** |  | 
**commitUrl** | **String** |  | 
**createdAt** | **Date** |  | 
**dismissedReview** | [**IssueEventDismissedReview**](IssueEventDismissedReview.md) |  | [optional] 
**event** | **String** |  | 
**id** | **Number** |  | 
**issue** | [**IssueSimple**](IssueSimple.md) |  | [optional] 
**label** | [**IssueEventLabel**](IssueEventLabel.md) |  | [optional] 
**lockReason** | **String** |  | [optional] 
**milestone** | [**IssueEventMilestone**](IssueEventMilestone.md) |  | [optional] 
**nodeId** | **String** |  | 
**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  | [optional] 
**projectCard** | [**IssueEventProjectCard**](IssueEventProjectCard.md) |  | [optional] 
**rename** | [**IssueEventRename**](IssueEventRename.md) |  | [optional] 
**requestedReviewer** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**requestedTeam** | [**Team**](Team.md) |  | [optional] 
**reviewRequester** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**url** | **String** |  | 


