

# Event


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**advisorId** | **String** |  |  [optional] |
|**createdAt** | **String** |  |  [optional] |
|**eventContent** | [**EventContent**](EventContent.md) |  |  [optional] |
|**originalUrl** | **String** |  |  |
|**originatorEmail** | **String** |  |  [optional] |
|**originatorId** | **String** |  |  [optional] |
|**parentEventId** | **String** |  |  [optional] |
|**referer** | **String** |  |  [optional] |
|**subjectEmail** | **String** |  |  |
|**subjectId** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PAGE_VIEW | &quot;page_view&quot; |
| SIGN_UP | &quot;sign_up&quot; |
| SIGN_IN | &quot;sign_in&quot; |
| CONTENT_POSTED | &quot;content_posted&quot; |
| CREATE_POST | &quot;create_post&quot; |
| PUBLISH_POST | &quot;publish_post&quot; |
| UPDATE_POST | &quot;update_post&quot; |
| DELETE_POST | &quot;delete_post&quot; |
| UNPUBLISH_POST | &quot;unpublish_post&quot; |
| INVITE | &quot;invite&quot; |
| PUBLISH_NEWSLETTER | &quot;publish_newsletter&quot; |
| PUBLISH_SOCIAL | &quot;publish_social&quot; |
| CLICK | &quot;click&quot; |
| DELIVERED | &quot;delivered&quot; |
| OPEN | &quot;open&quot; |
| DROPPED | &quot;dropped&quot; |
| BOUNCE | &quot;bounce&quot; |



