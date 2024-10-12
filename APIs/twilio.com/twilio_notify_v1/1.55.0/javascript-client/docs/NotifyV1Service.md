# TwilioNotify.NotifyV1Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource. | [optional] 
**alexaSkillId** | **String** | Deprecated. | [optional] 
**apnCredentialSid** | **String** | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**defaultAlexaNotificationProtocolVersion** | **String** | Deprecated. | [optional] 
**defaultApnNotificationProtocolVersion** | **String** | The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] 
**defaultFcmNotificationProtocolVersion** | **String** | The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] 
**defaultGcmNotificationProtocolVersion** | **String** | The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] 
**deliveryCallbackEnabled** | **Boolean** | Callback configuration that enables delivery callbacks, default false | [optional] 
**deliveryCallbackUrl** | **String** | URL to send delivery status callback. | [optional] 
**facebookMessengerPageId** | **String** | Deprecated. | [optional] 
**fcmCredentialSid** | **String** | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**gcmCredentialSid** | **String** | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings. | [optional] 
**links** | **Object** | The URLs of the Binding, Notification, Segment, and User resources related to the service. | [optional] 
**logEnabled** | **Boolean** | Whether to log notifications. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] 
**messagingServiceSid** | **String** | The SID of the [Messaging Service](https://www.twilio.com/docs/sms/quickstart#messaging-services) to use for SMS Bindings. In order to send SMS notifications this parameter has to be set. | [optional] 
**sid** | **String** | The unique string that we created to identify the Service resource. | [optional] 
**url** | **String** | The absolute URL of the Service resource. | [optional] 


