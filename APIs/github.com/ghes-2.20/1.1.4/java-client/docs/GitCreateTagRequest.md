

# GitCreateTagRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The tag message. |  |
|**_object** | **String** | The SHA of the git object this is tagging. |  |
|**tag** | **String** | The tag&#39;s name. This is typically a version (e.g., \&quot;v0.0.1\&quot;). |  |
|**tagger** | [**GitCreateTagRequestTagger**](GitCreateTagRequestTagger.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the object we&#39;re tagging. Normally this is a &#x60;commit&#x60; but it can also be a &#x60;tree&#x60; or a &#x60;blob&#x60;. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMMIT | &quot;commit&quot; |
| TREE | &quot;tree&quot; |
| BLOB | &quot;blob&quot; |



