# TwilioApi.ApiV2010AccountMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource | [optional] 
**apiVersion** | **String** | The API version used to process the Message | [optional] 
**body** | **String** | The text content of the message | [optional] 
**dateCreated** | **String** | The [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) timestamp (in GMT) of when the Message resource was created | [optional] 
**dateSent** | **String** | The [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) timestamp (in GMT) of when the Message was sent. For an outgoing message, this is when Twilio sent the message. For an incoming message, this is when Twilio sent the HTTP request to your incoming message webhook URL. | [optional] 
**dateUpdated** | **String** | The [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) timestamp (in GMT) of when the Message resource was last updated | [optional] 
**direction** | [**MessageEnumDirection**](MessageEnumDirection.md) |  | [optional] 
**errorCode** | **Number** | The [error code](https://www.twilio.com/docs/api/errors) returned if the Message &#x60;status&#x60; is &#x60;failed&#x60; or &#x60;undelivered&#x60;. If no error was encountered, the value is &#x60;null&#x60;. | [optional] 
**errorMessage** | **String** | The description of the &#x60;error_code&#x60; if the Message &#x60;status&#x60; is &#x60;failed&#x60; or &#x60;undelivered&#x60;. If no error was encountered, the value is &#x60;null&#x60;. | [optional] 
**from** | **String** | The sender&#39;s phone number (in [E.164](https://en.wikipedia.org/wiki/E.164) format), [alphanumeric sender ID](https://www.twilio.com/docs/sms/quickstart), [Wireless SIM](https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands), [short code](https://www.twilio.com/en-us/messaging/channels/sms/short-codes), or  [channel address](https://www.twilio.com/docs/messaging/channels) (e.g., &#x60;whatsapp:+15554449999&#x60;). For incoming messages, this is the number or channel address of the sender. For outgoing messages, this value is a Twilio phone number, alphanumeric sender ID, short code, or channel address from which the message is sent. | [optional] 
**messagingServiceSid** | **String** | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) associated with the Message resource. The value is &#x60;null&#x60; if a Messaging Service was not used. | [optional] 
**numMedia** | **String** | The number of media files associated with the Message resource. | [optional] 
**numSegments** | **String** | The number of segments that make up the complete message. SMS message bodies that exceed the [character limit](https://www.twilio.com/docs/glossary/what-sms-character-limit) are segmented and charged as multiple messages. Note: For messages sent via a Messaging Service, &#x60;num_segments&#x60; is initially &#x60;0&#x60;, since a sender hasn&#39;t yet been assigned. | [optional] 
**price** | **String** | The amount billed for the message in the currency specified by &#x60;price_unit&#x60;. The &#x60;price&#x60; is populated after the message has been sent/received, and may not be immediately availalble. View the [Pricing page](https://www.twilio.com/en-us/pricing) for more details. | [optional] 
**priceUnit** | **String** | The currency in which &#x60;price&#x60; is measured, in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. &#x60;usd&#x60;, &#x60;eur&#x60;, &#x60;jpy&#x60;). | [optional] 
**sid** | **String** | The unique, Twilio-provided string that identifies the Message resource. | [optional] 
**status** | [**MessageEnumStatus**](MessageEnumStatus.md) |  | [optional] 
**subresourceUris** | **Object** | A list of related resources identified by their URIs relative to &#x60;https://api.twilio.com&#x60; | [optional] 
**to** | **String** | The recipient&#39;s phone number (in [E.164](https://en.wikipedia.org/wiki/E.164) format) or [channel address](https://www.twilio.com/docs/messaging/channels) (e.g. &#x60;whatsapp:+15552229999&#x60;) | [optional] 
**uri** | **String** | The URI of the Message resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 


