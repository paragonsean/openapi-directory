

# RetrieveConversation200Response

Conversation Object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**LinksConversation**](LinksConversation.md) |  |  [optional] |
|**apiKey** | **String** | The API key for your account |  [optional] |
|**displayName** | **String** | The display name for the conversation. It does not have to be unique |  [optional] |
|**members** | [**List&lt;RetrieveConversation200ResponseMembersInner&gt;**](RetrieveConversation200ResponseMembersInner.md) | Users associated to this conversation as members |  [optional] |
|**name** | **String** | Unique name for a conversation |  [optional] |
|**numbers** | **Object** |  |  [optional] |
|**properties** | [**RetrieveConversation200ResponseProperties**](RetrieveConversation200ResponseProperties.md) |  |  [optional] |
|**sequenceNumber** | **String** | The last Event ID in this conversation. This ID can be used to [retrieve a specific event](#getEvent) |  [optional] |
|**timestamp** | [**TimestampResConversation**](TimestampResConversation.md) |  |  [optional] |
|**uuid** | **String** | The unique identifier for this conversation |  |



