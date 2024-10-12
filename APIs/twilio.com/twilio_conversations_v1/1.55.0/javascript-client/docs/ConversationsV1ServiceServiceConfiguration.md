# TwilioConversations.ConversationsV1ServiceServiceConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chatServiceSid** | **String** | The unique string that we created to identify the Service configuration resource. | [optional] 
**defaultChatServiceRoleSid** | **String** | The service-level role assigned to users when they are added to the service. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles. | [optional] 
**defaultConversationCreatorRoleSid** | **String** | The conversation-level role assigned to a conversation creator when they join a new conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles. | [optional] 
**defaultConversationRoleSid** | **String** | The conversation-level role assigned to users when they are added to a conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles. | [optional] 
**links** | **Object** | Contains an absolute API resource URL to access the push notifications configuration of this service. | [optional] 
**reachabilityEnabled** | **Boolean** | Whether the [Reachability Indicator](https://www.twilio.com/docs/conversations/reachability) is enabled for this Conversations Service. The default is &#x60;false&#x60;. | [optional] 
**url** | **String** | An absolute API resource URL for this service configuration. | [optional] 


