

# AutopilotV1AssistantWebhook


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Webhook resource. |  [optional] |
|**assistantSid** | **String** | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**events** | **String** | The list of space-separated events that this Webhook is subscribed to. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Webhook resource. |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. |  [optional] |
|**url** | **URI** | The absolute URL of the Webhook resource. |  [optional] |
|**webhookMethod** | **String** | The method used when calling the webhook&#39;s URL. |  [optional] |
|**webhookUrl** | **URI** | The URL associated with this Webhook. |  [optional] |



