# TwilioVerify.VerifyV2ServiceWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**eventTypes** | **[String]** | The array of events that this Webhook is subscribed to. Possible event types: &#x60;*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied&#x60; | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the webhook. **This value should not contain PII.** | [optional] 
**serviceSid** | **String** | The unique SID identifier of the Service. | [optional] 
**sid** | **String** | The unique string that we created to identify the Webhook resource. | [optional] 
**status** | [**WebhookEnumStatus**](WebhookEnumStatus.md) |  | [optional] 
**url** | **String** | The absolute URL of the Webhook resource. | [optional] 
**version** | [**WebhookEnumVersion**](WebhookEnumVersion.md) |  | [optional] 
**webhookMethod** | [**WebhookEnumMethods**](WebhookEnumMethods.md) |  | [optional] 
**webhookUrl** | **String** | The URL associated with this Webhook. | [optional] 


