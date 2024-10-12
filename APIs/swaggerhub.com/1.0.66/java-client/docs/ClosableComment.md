

# ClosableComment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Markdown contents of the comment |  |
|**created** | **OffsetDateTime** | The UTC date and time when the comment was added |  |
|**id** | **String** | The unique ID of the comment |  |
|**modified** | **OffsetDateTime** | The UTC date and time the when the comment was last edited |  [optional] |
|**user** | [**User**](User.md) |  |  |
|**position** | **Integer** | The line number (zero-based) the comment is associated with. For example, if the comment is on line 7 in the editor, &#x60;position&#x60;&#x3D;6.  |  [optional] |
|**replies** | [**List&lt;Comment&gt;**](Comment.md) | A list of replies to this comment |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Comment status |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OPEN | &quot;OPEN&quot; |
| RESOLVED | &quot;RESOLVED&quot; |



