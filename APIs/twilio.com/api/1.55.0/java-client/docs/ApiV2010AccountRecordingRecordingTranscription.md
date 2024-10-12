

# ApiV2010AccountRecordingRecordingTranscription


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource. |  [optional] |
|**apiVersion** | **String** | The API version used to create the transcription. |  [optional] |
|**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **String** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**duration** | **String** | The duration of the transcribed audio in seconds. |  [optional] |
|**price** | **BigDecimal** | The charge for the transcript in the currency associated with the account. This value is populated after the transcript is complete so it may not be available immediately. |  [optional] |
|**priceUnit** | **String** | The currency in which &#x60;price&#x60; is measured, in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. &#x60;usd&#x60;, &#x60;eur&#x60;, &#x60;jpy&#x60;). |  [optional] |
|**recordingSid** | **String** | The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) from which the transcription was created. |  [optional] |
|**sid** | **String** | The unique string that that we created to identify the Transcription resource. |  [optional] |
|**status** | **RecordingTranscriptionEnumStatus** |  |  [optional] |
|**transcriptionText** | **String** | The text content of the transcription. |  [optional] |
|**type** | **String** | The transcription type. |  [optional] |
|**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. |  [optional] |



