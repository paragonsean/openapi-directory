

# PullRequestReviewComment

Pull Request Review Comments are comments on a portion of the Pull Request's diff.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**PullRequestReviewCommentLinks**](PullRequestReviewCommentLinks.md) |  |  |
|**authorAssociation** | **AuthorAssociation** |  |  |
|**body** | **String** | The text of the comment. |  |
|**bodyHtml** | **String** |  |  [optional] |
|**bodyText** | **String** |  |  [optional] |
|**commitId** | **String** | The SHA of the commit to which the comment applies. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**diffHunk** | **String** | The diff of the line that the comment refers to. |  |
|**htmlUrl** | **URI** | HTML URL for the pull request review comment. |  |
|**id** | **Integer** | The ID of the pull request review comment. |  |
|**inReplyToId** | **Integer** | The comment ID to reply to. |  [optional] |
|**nodeId** | **String** | The node ID of the pull request review comment. |  |
|**originalCommitId** | **String** | The SHA of the original commit to which the comment applies. |  |
|**originalPosition** | **Integer** | The index of the original line in the diff to which the comment applies. |  |
|**path** | **String** | The relative path of the file to which the comment applies. |  |
|**position** | **Integer** | The line index in the diff to which the comment applies. |  |
|**pullRequestReviewId** | **Integer** | The ID of the pull request review to which the comment belongs. |  |
|**pullRequestUrl** | **URI** | URL for the pull request that the review comment belongs to. |  |
|**reactions** | [**ReactionRollup**](ReactionRollup.md) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **String** | URL for the pull request review comment |  |
|**user** | [**SimpleUser**](SimpleUser.md) |  |  |



