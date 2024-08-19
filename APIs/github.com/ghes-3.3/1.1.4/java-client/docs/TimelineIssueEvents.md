

# TimelineIssueEvents

Timeline Event

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actor** | [**SimpleUser**](SimpleUser.md) |  |  |
|**commitId** | **String** |  |  |
|**commitUrl** | **String** |  |  |
|**createdAt** | **String** |  |  |
|**event** | **String** |  |  |
|**id** | **Integer** |  |  |
|**label** | [**LabeledIssueEventLabel**](LabeledIssueEventLabel.md) |  |  |
|**nodeId** | **String** |  |  |
|**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  |  |
|**url** | **String** |  |  |
|**milestone** | [**DemilestonedIssueEventMilestone**](DemilestonedIssueEventMilestone.md) |  |  |
|**rename** | [**RenamedIssueEventRename**](RenamedIssueEventRename.md) |  |  |
|**requestedReviewer** | [**SimpleUser**](SimpleUser.md) |  |  [optional] |
|**requestedTeam** | [**Team**](Team.md) |  |  [optional] |
|**reviewRequester** | [**SimpleUser**](SimpleUser.md) |  |  |
|**dismissedReview** | [**ReviewDismissedIssueEventDismissedReview**](ReviewDismissedIssueEventDismissedReview.md) |  |  |
|**lockReason** | **String** |  |  |
|**projectCard** | [**AddedToProjectIssueEventProjectCard**](AddedToProjectIssueEventProjectCard.md) |  |  [optional] |
|**authorAssociation** | **AuthorAssociation** |  |  |
|**body** | **String** | The text of the review. |  |
|**bodyHtml** | **String** |  |  [optional] |
|**bodyText** | **String** |  |  [optional] |
|**htmlUrl** | **URI** |  |  |
|**issueUrl** | **URI** |  |  |
|**reactions** | [**ReactionRollup**](ReactionRollup.md) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  |
|**user** | [**SimpleUser**](SimpleUser.md) |  |  |
|**source** | [**TimelineCrossReferencedEventSource**](TimelineCrossReferencedEventSource.md) |  |  |
|**author** | [**GitCommitAuthor**](GitCommitAuthor.md) |  |  |
|**committer** | [**GitCommitAuthor**](GitCommitAuthor.md) |  |  |
|**message** | **String** | Message describing the purpose of the commit |  |
|**parents** | [**List&lt;GitCommitParentsInner&gt;**](GitCommitParentsInner.md) |  |  |
|**sha** | **String** | SHA for the commit |  |
|**tree** | [**GitCommitTree**](GitCommitTree.md) |  |  |
|**verification** | [**GitCommitVerification**](GitCommitVerification.md) |  |  |
|**links** | [**PullRequestReviewLinks**](PullRequestReviewLinks.md) |  |  |
|**pullRequestUrl** | **URI** |  |  |
|**state** | **String** |  |  |
|**submittedAt** | **OffsetDateTime** |  |  [optional] |
|**comments** | [**List&lt;CommitComment&gt;**](CommitComment.md) |  |  [optional] |
|**assignee** | [**SimpleUser**](SimpleUser.md) |  |  |
|**stateReason** | **String** |  |  [optional] |



