# TwilioChat.ChatV2ServiceChannelChannelWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Channel Webhook resource. | [optional] 
**channelSid** | **String** | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource belongs to. | [optional] 
**configuration** | **Object** | The JSON string that describes how the channel webhook is configured. The configuration object contains the &#x60;url&#x60;, &#x60;method&#x60;, &#x60;filters&#x60;, and &#x60;retry_count&#x60; values that are configured by the create and update actions. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Channel Webhook resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Channel Webhook resource. | [optional] 
**type** | **String** | The type of webhook. Can be: &#x60;webhook&#x60;, &#x60;studio&#x60;, or &#x60;trigger&#x60;. | [optional] 
**url** | **String** | The absolute URL of the Channel Webhook resource. | [optional] 


