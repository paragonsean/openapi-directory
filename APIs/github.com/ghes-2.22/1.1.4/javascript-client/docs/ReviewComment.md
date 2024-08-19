# GitHubV3RestApi.ReviewComment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ReviewCommentLinks**](ReviewCommentLinks.md) |  | 
**authorAssociation** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**body** | **String** |  | 
**bodyHtml** | **String** |  | [optional] 
**bodyText** | **String** |  | [optional] 
**commitId** | **String** |  | 
**createdAt** | **Date** |  | 
**diffHunk** | **String** |  | 
**htmlUrl** | **String** |  | 
**id** | **Number** |  | 
**inReplyToId** | **Number** |  | [optional] 
**line** | **Number** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment | [optional] 
**nodeId** | **String** |  | 
**originalCommitId** | **String** |  | 
**originalLine** | **Number** | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment | [optional] 
**originalPosition** | **Number** |  | 
**originalStartLine** | **Number** | The original first line of the range for a multi-line comment. | [optional] 
**path** | **String** |  | 
**position** | **Number** |  | 
**pullRequestReviewId** | **Number** |  | 
**pullRequestUrl** | **String** |  | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 
**side** | **String** | The side of the first line of the range for a multi-line comment. | [optional] [default to &#39;RIGHT&#39;]
**startLine** | **Number** | The first line of the range for a multi-line comment. | [optional] 
**startSide** | **String** | The side of the first line of the range for a multi-line comment. | [optional] [default to &#39;RIGHT&#39;]
**updatedAt** | **Date** |  | 
**url** | **String** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 



## Enum: SideEnum


* `LEFT` (value: `"LEFT"`)

* `RIGHT` (value: `"RIGHT"`)





## Enum: StartSideEnum


* `LEFT` (value: `"LEFT"`)

* `RIGHT` (value: `"RIGHT"`)




