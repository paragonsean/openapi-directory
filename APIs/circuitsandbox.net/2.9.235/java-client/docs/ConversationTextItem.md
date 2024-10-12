

# ConversationTextItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | The content of the text item |  [optional] |
|**contentType** | **String** | The type of the text item. It can be one of the following: RICH (with HTML content) or PLAIN (only text) |  [optional] |
|**formMetaData** | **String** | The meta data form |  [optional] |
|**isWebhookMessage** | **Boolean** | Is this a webhook message? |  [optional] |
|**likedUserIds** | **List&lt;String&gt;** | Array of IDs of the users who liked the item |  [optional] |
|**parentId** | **String** | The ID of the parent item of the text item. This field is optional and can be used for thread views |  [optional] |
|**preview** | [**Preview**](Preview.md) |  |  [optional] |
|**state** | **String** | The state of the text item. It can be one of the following: CREATED (which denotes that it was not modified since its creation), EDITED (which denotes that the creator of this item modified the item) or DELETED (which denotes that the item itself exists but its content was removed) |  [optional] |
|**subject** | **String** | TThe subject of the text item. This field is optional and maybe filled when creating the text item |  [optional] |



