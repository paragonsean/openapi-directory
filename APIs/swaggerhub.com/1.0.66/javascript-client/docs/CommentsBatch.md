# SwaggerHubRegistryApi.CommentsBatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addComment** | [**[NewComment]**](NewComment.md) |  | [optional] 
**addReply** | **{String: [NewReply]}** |  | [optional] 
**deleteComment** | **[String]** |  | [optional] 
**deleteReply** | **{String: [String]}** |  | [optional] 
**updateComment** | [**{String: ClosableCommentPatch}**](ClosableCommentPatch.md) |  | [optional] 
**updateReply** | **{String: {String: CommentPatch}}** |  | [optional] 
**updateStatus** | **{String: String}** |  | [optional] 



## Enum: {String: String}


* `OPEN` (value: `"OPEN"`)

* `RESOLVED` (value: `"RESOLVED"`)




