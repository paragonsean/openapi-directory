

# CommentsBatch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addComment** | [**List&lt;NewComment&gt;**](NewComment.md) |  |  [optional] |
|**addReply** | **Map&lt;String, List&lt;NewReply&gt;&gt;** |  |  [optional] |
|**deleteComment** | **List&lt;String&gt;** |  |  [optional] |
|**deleteReply** | **Map&lt;String, Set&lt;String&gt;&gt;** |  |  [optional] |
|**updateComment** | [**Map&lt;String, ClosableCommentPatch&gt;**](ClosableCommentPatch.md) |  |  [optional] |
|**updateReply** | **Map&lt;String, Map&lt;String, CommentPatch&gt;&gt;** |  |  [optional] |
|**updateStatus** | [**Map&lt;String, InnerEnum&gt;**](#Map&lt;String, InnerEnum&gt;) |  |  [optional] |



## Enum: Map&lt;String, InnerEnum&gt;

| Name | Value |
|---- | -----|
| OPEN | &quot;OPEN&quot; |
| RESOLVED | &quot;RESOLVED&quot; |



