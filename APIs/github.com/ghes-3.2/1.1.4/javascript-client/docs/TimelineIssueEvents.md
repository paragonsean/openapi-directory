# GitHubV3RestApi.TimelineIssueEvents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**SimpleUser**](SimpleUser.md) |  | 
**commitId** | **String** |  | 
**commitUrl** | **String** |  | 
**createdAt** | **String** |  | 
**event** | **String** |  | 
**id** | **Number** |  | 
**label** | [**LabeledIssueEventLabel**](LabeledIssueEventLabel.md) |  | 
**nodeId** | **String** |  | 
**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  | 
**url** | **String** |  | 
**milestone** | [**DemilestonedIssueEventMilestone**](DemilestonedIssueEventMilestone.md) |  | 
**rename** | [**RenamedIssueEventRename**](RenamedIssueEventRename.md) |  | 
**requestedReviewer** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**requestedTeam** | [**Team**](Team.md) |  | [optional] 
**reviewRequester** | [**SimpleUser**](SimpleUser.md) |  | 
**dismissedReview** | [**ReviewDismissedIssueEventDismissedReview**](ReviewDismissedIssueEventDismissedReview.md) |  | 
**lockReason** | **String** |  | 
**projectCard** | [**AddedToProjectIssueEventProjectCard**](AddedToProjectIssueEventProjectCard.md) |  | [optional] 
**authorAssociation** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**body** | **String** | The text of the review. | 
**bodyHtml** | **String** |  | [optional] 
**bodyText** | **String** |  | [optional] 
**htmlUrl** | **String** |  | 
**issueUrl** | **String** |  | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 
**updatedAt** | **Date** |  | 
**user** | [**SimpleUser**](SimpleUser.md) |  | 
**source** | [**TimelineCrossReferencedEventSource**](TimelineCrossReferencedEventSource.md) |  | 
**author** | [**GitCommitAuthor**](GitCommitAuthor.md) |  | 
**committer** | [**GitCommitAuthor**](GitCommitAuthor.md) |  | 
**message** | **String** | Message describing the purpose of the commit | 
**parents** | [**[GitCommitParentsInner]**](GitCommitParentsInner.md) |  | 
**sha** | **String** | SHA for the commit | 
**tree** | [**GitCommitTree**](GitCommitTree.md) |  | 
**verification** | [**GitCommitVerification**](GitCommitVerification.md) |  | 
**links** | [**PullRequestReviewLinks**](PullRequestReviewLinks.md) |  | 
**pullRequestUrl** | **String** |  | 
**state** | **String** |  | 
**submittedAt** | **Date** |  | [optional] 
**comments** | [**[CommitComment]**](CommitComment.md) |  | [optional] 
**assignee** | [**SimpleUser**](SimpleUser.md) |  | 
**stateReason** | **String** |  | [optional] 


