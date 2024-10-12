# TwilioConversations.ConversationsV1ServiceServiceBinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this binding. | [optional] 
**bindingType** | [**ServiceBindingEnumBindingType**](ServiceBindingEnumBindingType.md) |  | [optional] 
**chatServiceSid** | **String** | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Binding resource is associated with. | [optional] 
**credentialSid** | **String** | The SID of the [Credential](https://www.twilio.com/docs/conversations/api/credential-resource) for the binding. See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info. | [optional] 
**dateCreated** | **Date** | The date that this resource was created. | [optional] 
**dateUpdated** | **Date** | The date that this resource was last updated. | [optional] 
**endpoint** | **String** | The unique endpoint identifier for the Binding. The format of this value depends on the &#x60;binding_type&#x60;. | [optional] 
**identity** | **String** | The application-defined string that uniquely identifies the [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more info. | [optional] 
**messageTypes** | **[String]** | The [Conversation message types](https://www.twilio.com/docs/chat/push-notification-configuration#push-types) the binding is subscribed to. | [optional] 
**sid** | **String** | A 34 character string that uniquely identifies this resource. | [optional] 
**url** | **String** | An absolute API resource URL for this binding. | [optional] 


