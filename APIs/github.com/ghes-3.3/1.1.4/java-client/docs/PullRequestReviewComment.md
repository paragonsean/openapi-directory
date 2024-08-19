

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
|**line** | **Integer** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |  [optional] |
|**nodeId** | **String** | The node ID of the pull request review comment. |  |
|**originalCommitId** | **String** | The SHA of the original commit to which the comment applies. |  |
|**originalLine** | **Integer** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |  [optional] |
|**originalPosition** | **Integer** | The index of the original line in the diff to which the comment applies. This field is deprecated; use &#x60;original_line&#x60; instead. |  |
|**originalStartLine** | **Integer** | The first line of the range for a multi-line comment. |  [optional] |
|**path** | **String** | The relative path of the file to which the comment applies. |  |
|**position** | **Integer** | The line index in the diff to which the comment applies. This field is deprecated; use &#x60;line&#x60; instead. |  |
|**pullRequestReviewId** | **Integer** | The ID of the pull request review to which the comment belongs. |  |
|**pullRequestUrl** | **URI** | URL for the pull request that the review comment belongs to. |  |
|**reactions** | [**ReactionRollup**](ReactionRollup.md) |  |  [optional] |
|**side** | [**SideEnum**](#SideEnum) | The side of the diff to which the comment applies. The side of the last line of the range for a multi-line comment |  [optional] |
|**startLine** | **Integer** | The first line of the range for a multi-line comment. |  [optional] |
|**startSide** | [**StartSideEnum**](#StartSideEnum) | The side of the first line of the range for a multi-line comment. |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **String** | URL for the pull request review comment |  |
|**user** | [**SimpleUser**](SimpleUser.md) |  |  |



## Enum: SideEnum

| Name | Value |
|---- | -----|
| LEFT | &quot;LEFT&quot; |
| RIGHT | &quot;RIGHT&quot; |



## Enum: StartSideEnum

| Name | Value |
|---- | -----|
| LEFT | &quot;LEFT&quot; |
| RIGHT | &quot;RIGHT&quot; |



