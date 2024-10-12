# TwilioConversations.ConversationsV1Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this configuration. | [optional] 
**defaultChatServiceSid** | **String** | The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) used when creating a conversation. | [optional] 
**defaultClosedTimer** | **String** | Default ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] 
**defaultInactiveTimer** | **String** | Default ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] 
**defaultMessagingServiceSid** | **String** | The SID of the default [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) used when creating a conversation. | [optional] 
**links** | **Object** | Contains absolute API resource URLs to access the webhook and default service configurations. | [optional] 
**url** | **String** | An absolute API resource URL for this global configuration. | [optional] 


