

# ChatV1ServiceUserUserChannel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the User Channel resource. |  [optional] |
|**channelSid** | **String** | The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource belongs to. |  [optional] |
|**lastConsumedMessageIndex** | **Integer** | The index of the last [Message](https://www.twilio.com/docs/api/chat/rest/messages) in the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) that the Member has read. |  [optional] |
|**links** | **Object** | The absolute URLs of the [Members](https://www.twilio.com/docs/chat/api/members), [Messages](https://www.twilio.com/docs/chat/api/messages) , [Invites](https://www.twilio.com/docs/chat/api/invites) and, if it exists, the last [Message](https://www.twilio.com/docs/chat/api/messages) for the Channel. |  [optional] |
|**memberSid** | **String** | The SID of a [Member](https://www.twilio.com/docs/api/chat/rest/members) that represents the User on the Channel. |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) the resource is associated with. |  [optional] |
|**status** | **UserChannelEnumChannelStatus** |  |  [optional] |
|**unreadMessagesCount** | **Integer** | The number of unread Messages in the Channel for the User. Note that retrieving messages on a client endpoint does not mean that messages are consumed or read. See [Consumption Horizon feature](/docs/api/chat/guides/consumption-horizon) to learn how to mark messages as consumed. |  [optional] |



