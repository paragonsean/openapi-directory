

# ReviewComment

Legacy Review Comment

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**ReviewCommentLinks**](ReviewCommentLinks.md) |  |  |
|**authorAssociation** | **AuthorAssociation** |  |  |
|**body** | **String** |  |  |
|**bodyHtml** | **String** |  |  [optional] |
|**bodyText** | **String** |  |  [optional] |
|**commitId** | **String** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**diffHunk** | **String** |  |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** |  |  |
|**inReplyToId** | **Integer** |  |  [optional] |
|**line** | **Integer** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |  [optional] |
|**nodeId** | **String** |  |  |
|**originalCommitId** | **String** |  |  |
|**originalLine** | **Integer** | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |  [optional] |
|**originalPosition** | **Integer** |  |  |
|**originalStartLine** | **Integer** | The original first line of the range for a multi-line comment. |  [optional] |
|**path** | **String** |  |  |
|**position** | **Integer** |  |  |
|**pullRequestReviewId** | **Integer** |  |  |
|**pullRequestUrl** | **URI** |  |  |
|**reactions** | [**ReactionRollup**](ReactionRollup.md) |  |  [optional] |
|**side** | [**SideEnum**](#SideEnum) | The side of the first line of the range for a multi-line comment. |  [optional] |
|**startLine** | **Integer** | The first line of the range for a multi-line comment. |  [optional] |
|**startSide** | [**StartSideEnum**](#StartSideEnum) | The side of the first line of the range for a multi-line comment. |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |
|**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |



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



