

# Comment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdOn** | **String** | The time in ISO 8601 format when the comment was posted. |  |
|**metadata** | [**CommentMetadata**](CommentMetadata.md) |  |  |
|**resourceKey** | **String** | The resource key string for the comment. |  |
|**text** | **String** | The content of the comment. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The Vimeo content to which the comment relates:  Option descriptions:  * &#x60;video&#x60; - The comment is about a video.  |  |
|**uri** | **String** | The unique identifier to access the comment resource. |  |
|**user** | [**User**](User.md) | The user who posted the comment. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VIDEO | &quot;video&quot; |



