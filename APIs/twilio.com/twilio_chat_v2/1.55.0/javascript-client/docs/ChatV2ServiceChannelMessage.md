# TwilioChat.ChatV2ServiceChannelMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resource. | [optional] 
**attributes** | **String** | The JSON string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] 
**body** | **String** | The content of the message. | [optional] 
**channelSid** | **String** | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource belongs to. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**from** | **String** | The [Identity](https://www.twilio.com/docs/chat/identity) of the message&#39;s author. The default value is &#x60;system&#x60;. | [optional] 
**index** | **Number** | The index of the message within the [Channel](https://www.twilio.com/docs/chat/channels). Indices may skip numbers, but will always be in order of when the message was received. | [optional] 
**lastUpdatedBy** | **String** | The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable. | [optional] 
**media** | **Object** | An object that describes the Message&#39;s media, if the message contains media. The object contains these fields: &#x60;content_type&#x60; with the MIME type of the media, &#x60;filename&#x60; with the name of the media, &#x60;sid&#x60; with the SID of the Media resource, and &#x60;size&#x60; with the media object&#39;s file size in bytes. If the Message has no media, this value is &#x60;null&#x60;. | [optional] 
**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Message resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Message resource. | [optional] 
**to** | **String** | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) that the message was sent to. | [optional] 
**type** | **String** | The Message type. Can be: &#x60;text&#x60; or &#x60;media&#x60;. | [optional] 
**url** | **String** | The absolute URL of the Message resource. | [optional] 
**wasEdited** | **Boolean** | Whether the message has been edited since it was created. | [optional] 


