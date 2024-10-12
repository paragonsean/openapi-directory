

# ConversationItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Array of files attached to the item |  [optional] |
|**convId** | **String** | The ID of the conversation the item belongs to |  [optional] |
|**creationTime** | **BigDecimal** | UTC timestamp when the item was created |  [optional] |
|**creatorId** | **String** | The ID of the user who created the conversation item |  [optional] |
|**includeInUnreadCount** | **Boolean** | Indicates whether the item is included in the unread message count |  [optional] |
|**itemId** | **String** | The ID of the item |  [optional] |
|**modificationTime** | **BigDecimal** | UTC timestamp when the conversation was modified |  [optional] |
|**rtc** | [**RtcItem**](RtcItem.md) |  |  [optional] |
|**system** | [**SystemItem**](SystemItem.md) |  |  [optional] |
|**text** | [**ConversationTextItem**](ConversationTextItem.md) |  |  [optional] |
|**type** | **String** | The type of the conversation item. It can be one of the following TEXT, SYSTEM or RTC |  [optional] |



