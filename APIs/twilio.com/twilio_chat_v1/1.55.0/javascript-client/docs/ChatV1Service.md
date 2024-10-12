# TwilioChat.ChatV1Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the Service resource. | [optional] 
**consumptionReportInterval** | **Number** | DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**defaultChannelCreatorRoleSid** | **String** | The channel role assigned to a channel creator when they join a new channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details. | [optional] 
**defaultChannelRoleSid** | **String** | The channel role assigned to users when they are added to a channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details. | [optional] 
**defaultServiceRoleSid** | **String** | The service role assigned to users when they are added to the service. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**limits** | **Object** | An object that describes the limits of the service instance. The &#x60;limits&#x60; object contains  &#x60;channel_members&#x60; to describe the members/channel limit and &#x60;user_channels&#x60; to describe the channels/user limit. &#x60;channel_members&#x60; can be 1,000 or less, with a default of 250. &#x60;user_channels&#x60; can be 1,000 or less, with a default value of 100. | [optional] 
**links** | **Object** | The absolute URLs of the Service&#39;s [Channels](https://www.twilio.com/docs/chat/api/channels), [Roles](https://www.twilio.com/docs/chat/api/roles), and [Users](https://www.twilio.com/docs/chat/api/users). | [optional] 
**notifications** | **Object** | The notification configuration for the Service instance. See [Push Notification Configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more information. | [optional] 
**postWebhookUrl** | **String** | The URL for post-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details. | [optional] 
**preWebhookUrl** | **String** | The URL for pre-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details. | [optional] 
**reachabilityEnabled** | **Boolean** | Whether the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) is enabled for this Service instance. The default is &#x60;false&#x60;. | [optional] 
**readStatusEnabled** | **Boolean** | Whether the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature is enabled. The default is &#x60;true&#x60;. | [optional] 
**sid** | **String** | The unique string that we created to identify the Service resource. | [optional] 
**typingIndicatorTimeout** | **Number** | How long in seconds after a &#x60;started typing&#x60; event until clients should assume that user is no longer typing, even if no &#x60;ended typing&#x60; message was received.  The default is 5 seconds. | [optional] 
**url** | **String** | The absolute URL of the Service resource. | [optional] 
**webhookFilters** | **[String]** | The list of WebHook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] 
**webhookMethod** | **String** | The HTTP method to use for calls to the &#x60;pre_webhook_url&#x60; and &#x60;post_webhook_url&#x60; webhooks.  Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] 
**webhooks** | **Object** | An object that contains information about the webhooks configured for this service. | [optional] 


