# BulkSmsJsonRestApi.Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **Object** | The content of the message | 
**creditCost** | **Number** | The cost of the message (in credits).   Note that this field does not have a value in the submission response. | [optional] 
**encoding** | **String** | The type of the content.  See the &#x60;encoding&#x60; field for more information. | [optional] 
**from** | **String** | The address part of the sender id | [optional] 
**id** | **String** | A unique identifier that is assigned when the message is created. | 
**messageClass** | **Number** | See the &#x60;messageClass&#x60; field for more information. | [optional] 
**numberOfParts** | **Number** | The number of parts.  If this is a concatenated message, the number of parts will be more than 1.  Note that this field does not have a value in the submission response. | [optional] 
**protocolId** | **Number** | See the &#x60;protocolId&#x60; field for more information. | [optional] 
**relatedSentMessageId** | **String** | This field has a value only if the type is RECEIVED. With SMS messages, it is not possible to link a reply directly with a specific sent message.  However, if you specified &#x60;REPLIABLE&#x60; in the &#x60;from&#x60; property, BulkSMS will link any reply to the most recent message sent to a given phone number.  The &#x60;relatedSentMessageId&#x60; property keeps the information about this link.  You can use this property to derive an implicit conversation from a set of messages.   - If a received reply message has a &#x60;relatedSentMessageId&#x60;, you can use it to retrieve the last message that was sent before the reply was received.   - If you have the &#x60;id&#x60; of the sent message and you want all the received messages that relate to it, you can use the List Related Messages Operation.  | [optional] 
**status** | [**MessageStatus**](MessageStatus.md) |  | 
**submission** | [**MessageSubmission**](MessageSubmission.md) |  | [optional] 
**to** | **String** | The phone number of the recipient | 
**type** | **String** | The message direction | 
**userSuppliedId** | **String** | This is the value you supplied in the &#x60;userSuppliedId&#x60; field. Has a value only if the &#x60;type&#x60; is SENT.  | [optional] 



## Enum: EncodingEnum


* `TEXT` (value: `"TEXT"`)

* `UNICODE` (value: `"UNICODE"`)

* `BINARY` (value: `"BINARY"`)





## Enum: TypeEnum


* `SENT` (value: `"SENT"`)

* `RECEIVED` (value: `"RECEIVED"`)




