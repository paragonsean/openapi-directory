

# SendMessageRequest

Contains all information needed to send new message

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**forceModeration** | **Boolean** | Enable moderation on server-side requests |  [optional] |
|**isPendingMessage** | **Boolean** | Make the message a pending message. This message will not be viewable to others until it is committed. |  [optional] |
|**keepChannelHidden** | **Boolean** | Keeps the channel hidden for the sender |  [optional] |
|**message** | **MessageRequest** |  |  |
|**pendingMessageMetadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**skipEnrichUrl** | **Boolean** | Do not try to enrich the links within message |  [optional] |
|**skipPush** | **Boolean** | Disables all push notifications for this message |  [optional] |



