

# ActivityObject

The object of this activity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actor** | [**ActivityObjectActor**](ActivityObjectActor.md) |  |  [optional] |
|**attachments** | [**List&lt;ActivityObjectAttachmentsInner&gt;**](ActivityObjectAttachmentsInner.md) | The media objects attached to this activity. |  [optional] |
|**content** | **String** | The HTML-formatted content, which is suitable for display. |  [optional] |
|**id** | **String** | The ID of the object. When resharing an activity, this is the ID of the activity that is being reshared. |  [optional] |
|**objectType** | **String** | The type of the object. Possible values include, but are not limited to, the following values:   - \&quot;note\&quot; - Textual content.  - \&quot;activity\&quot; - A Google+ activity. |  [optional] |
|**originalContent** | **String** | The content (text) as provided by the author, which is stored without any HTML formatting. When creating or updating an activity, this value must be supplied as plain text in the request. |  [optional] |
|**plusoners** | [**ActivityObjectPlusoners**](ActivityObjectPlusoners.md) |  |  [optional] |
|**replies** | [**ActivityObjectReplies**](ActivityObjectReplies.md) |  |  [optional] |
|**resharers** | [**ActivityObjectResharers**](ActivityObjectResharers.md) |  |  [optional] |
|**url** | **String** | The URL that points to the linked resource. |  [optional] |



