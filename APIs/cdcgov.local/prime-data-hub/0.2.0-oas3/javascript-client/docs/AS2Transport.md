# PrimeReportStream.AS2Transport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentDescription** | **String** | A description of the content of the message. Usually, the same for all messages. | [optional] [default to &#39;SARS-CoV-2 Electronic Lab Results&#39;]
**mimeType** | **String** | The MIME type of the message | [optional] [default to &#39;application/hl7-v2&#39;]
**receiverId** | **String** | The AS2 id of the receiver. Usually, the same for all senders. | 
**receiverUrl** | **String** | The URL to the AS2 end-point | 
**senderEmail** | **String** | The email address to contact someone about the message | [optional] [default to &#39;reportstream@cdc.gov&#39;]
**senderId** | **String** | The AS2 id of the sender. Usually, assigned by receiver to PRIME. | 
**type** | **String** | The discriminator | 


