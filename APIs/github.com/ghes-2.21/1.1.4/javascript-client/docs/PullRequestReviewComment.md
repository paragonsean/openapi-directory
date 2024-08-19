# GitHubV3RestApi.PullRequestReviewComment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PullRequestReviewCommentLinks**](PullRequestReviewCommentLinks.md) |  | 
**authorAssociation** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**body** | **String** | The text of the comment. | 
**bodyHtml** | **String** |  | [optional] 
**bodyText** | **String** |  | [optional] 
**commitId** | **String** | The SHA of the commit to which the comment applies. | 
**createdAt** | **Date** |  | 
**diffHunk** | **String** | The diff of the line that the comment refers to. | 
**htmlUrl** | **String** | HTML URL for the pull request review comment. | 
**id** | **Number** | The ID of the pull request review comment. | 
**inReplyToId** | **Number** | The comment ID to reply to. | [optional] 
**line** | **Number** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment | [optional] 
**nodeId** | **String** | The node ID of the pull request review comment. | 
**originalCommitId** | **String** | The SHA of the original commit to which the comment applies. | 
**originalLine** | **Number** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment | [optional] 
**originalPosition** | **Number** | The index of the original line in the diff to which the comment applies. | 
**originalStartLine** | **Number** | The first line of the range for a multi-line comment. | [optional] 
**path** | **String** | The relative path of the file to which the comment applies. | 
**position** | **Number** | The line index in the diff to which the comment applies. | 
**pullRequestReviewId** | **Number** | The ID of the pull request review to which the comment belongs. | 
**pullRequestUrl** | **String** | URL for the pull request that the review comment belongs to. | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 
**side** | **String** | The side of the diff to which the comment applies. The side of the last line of the range for a multi-line comment | [optional] [default to &#39;RIGHT&#39;]
**startLine** | **Number** | The first line of the range for a multi-line comment. | [optional] 
**startSide** | **String** | The side of the first line of the range for a multi-line comment. | [optional] [default to &#39;RIGHT&#39;]
**updatedAt** | **Date** |  | 
**url** | **String** | URL for the pull request review comment | 
**user** | [**SimpleUser**](SimpleUser.md) |  | 



## Enum: SideEnum


* `LEFT` (value: `"LEFT"`)

* `RIGHT` (value: `"RIGHT"`)





## Enum: StartSideEnum


* `LEFT` (value: `"LEFT"`)

* `RIGHT` (value: `"RIGHT"`)




