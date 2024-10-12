

# InboundMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiKey** | **String** | The Vonage API Key of the receiving account. |  |
|**concat** | **String** | True - if this is a concatenated message. This field does not exist if it is a single message |  [optional] |
|**concatPart** | **String** | The number of this part in the message. Counting starts at 1. |  [optional] |
|**concatRef** | **String** | The transaction reference. All parts of this message share this value. |  [optional] |
|**concatTotal** | **String** | The number of parts in this concatenated message. |  [optional] |
|**data** | **File** | The content of this message, if type is binary. |  [optional] |
|**keyword** | **String** | The first word in the message body. Converted to upper case. |  |
|**messageTimestamp** | **String** | The time when Vonage started to push this Delivery Receipt to your webhook endpoint. |  |
|**messageId** | **String** | The ID of the message |  |
|**msisdn** | **String** | The phone number that this inbound message was sent from. Numbers are specified in E.164 format. |  |
|**nonce** | **String** | A random string that forms part of the signed set of parameters, it adds an extra element of unpredictability into the signature for the request. You use the nonce and timestamp parameters with your shared secret to calculate and validate the signature for inbound messages. |  [optional] |
|**text** | **String** | The message body for this inbound message. |  |
|**timestamp** | **String** | A unix timestamp representation of message-timestamp. |  [optional] |
|**to** | **String** | The phone number the message was sent to. **This is your virtual number**. Numbers are specified in E.164 format. |  |
|**type** | **String** | Possible values are:    - &#x60;text&#x60; - standard text.   - &#x60;unicode&#x60; - URLencoded   unicode  . This is valid for standard GSM, Arabic, Chinese, double-encoded characters and so on.   - &#x60;binary&#x60; - a binary message.  |  |
|**udh** | **String** | The hex encoded User Data Header, if type is binary |  [optional] |



