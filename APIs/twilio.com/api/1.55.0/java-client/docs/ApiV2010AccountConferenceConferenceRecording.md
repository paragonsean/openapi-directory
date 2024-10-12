

# ApiV2010AccountConferenceConferenceRecording


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resource. |  [optional] |
|**apiVersion** | **String** | The API version used to create the recording. |  [optional] |
|**callSid** | **String** | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Conference Recording resource is associated with. |  [optional] |
|**channels** | **Integer** | The number of channels in the final recording file.  Can be: &#x60;1&#x60;, or &#x60;2&#x60;. Separating a two leg call into two separate channels of the recording file is supported in [Dial](https://www.twilio.com/docs/voice/twiml/dial#attributes-record) and [Outbound Rest API](https://www.twilio.com/docs/voice/make-calls) record options. |  [optional] |
|**conferenceSid** | **String** | The Conference SID that identifies the conference associated with the recording. |  [optional] |
|**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **String** | The date and time in GMT that the resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**duration** | **String** | The length of the recording in seconds. |  [optional] |
|**encryptionDetails** | **Object** | How to decrypt the recording if it was encrypted using [Call Recording Encryption](https://www.twilio.com/docs/voice/tutorials/voice-recording-encryption) feature. |  [optional] |
|**errorCode** | **Integer** | The error code that describes why the recording is &#x60;absent&#x60;. The error code is described in our [Error Dictionary](https://www.twilio.com/docs/api/errors). This value is null if the recording &#x60;status&#x60; is not &#x60;absent&#x60;. |  [optional] |
|**price** | **String** | The one-time cost of creating the recording in the &#x60;price_unit&#x60; currency. |  [optional] |
|**priceUnit** | **String** | The currency used in the &#x60;price&#x60; property. Example: &#x60;USD&#x60;. |  [optional] |
|**sid** | **String** | The unique string that that we created to identify the Conference Recording resource. |  [optional] |
|**source** | **ConferenceRecordingEnumSource** |  |  [optional] |
|**startTime** | **String** | The start time of the recording in GMT and in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format. |  [optional] |
|**status** | **ConferenceRecordingEnumStatus** |  |  [optional] |
|**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. |  [optional] |



