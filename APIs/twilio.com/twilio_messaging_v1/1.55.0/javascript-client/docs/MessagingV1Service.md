# TwilioMessaging.MessagingV1Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource. | [optional] 
**areaCodeGeomatch** | **Boolean** | Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/messaging/services#area-code-geomatch) on the Service Instance. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**fallbackMethod** | **String** | The HTTP method we use to call &#x60;fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**fallbackToLongCode** | **Boolean** | [OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures. | [optional] 
**fallbackUrl** | **String** | The URL that we call using &#x60;fallback_method&#x60; if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;fallback_url&#x60; defined for the Messaging Service. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**inboundMethod** | **String** | The HTTP method we use to call &#x60;inbound_request_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**inboundRequestUrl** | **String** | The URL we call using &#x60;inbound_method&#x60; when a message is received by any phone number or short code in the Service. When this property is &#x60;null&#x60;, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60; defined for the Messaging Service. | [optional] 
**links** | **Object** | The absolute URLs of related resources. | [optional] 
**mmsConverter** | **Boolean** | Whether to enable the [MMS Converter](https://www.twilio.com/docs/messaging/services#mms-converter) for messages sent through the Service instance. | [optional] 
**scanMessageContent** | [**ServiceEnumScanMessageContent**](ServiceEnumScanMessageContent.md) |  | [optional] 
**sid** | **String** | The unique string that we created to identify the Service resource. | [optional] 
**smartEncoding** | **Boolean** | Whether to enable [Smart Encoding](https://www.twilio.com/docs/messaging/services#smart-encoding) for messages sent through the Service instance. | [optional] 
**statusCallback** | **String** | The URL we call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery. | [optional] 
**stickySender** | **Boolean** | Whether to enable [Sticky Sender](https://www.twilio.com/docs/messaging/services#sticky-sender) on the Service instance. | [optional] 
**synchronousValidation** | **Boolean** | Reserved. | [optional] 
**url** | **String** | The absolute URL of the Service resource. | [optional] 
**usAppToPersonRegistered** | **Boolean** | Whether US A2P campaign is registered for this Service. | [optional] 
**useInboundWebhookOnNumber** | **Boolean** | A boolean value that indicates either the webhook url configured on the phone number will be used or &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; defined for the Messaging Service. | [optional] 
**usecase** | **String** | A string that describes the scenario in which the Messaging Service will be used. Possible values are &#x60;notifications&#x60;, &#x60;marketing&#x60;, &#x60;verification&#x60;, &#x60;discussion&#x60;, &#x60;poll&#x60;, &#x60;undeclared&#x60;. | [optional] 
**validityPeriod** | **Number** | How long, in seconds, messages sent from the Service are valid. Can be an integer from &#x60;1&#x60; to &#x60;14,400&#x60;. | [optional] 



## Enum: FallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)





## Enum: InboundMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)




