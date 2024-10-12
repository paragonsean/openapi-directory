# TwilioApi.ApiV2010AccountRecording

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource. | [optional] 
**apiVersion** | **String** | The API version used during the recording. | [optional] 
**callSid** | **String** | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Recording resource is associated with. This will always refer to the parent leg of a two-leg call. | [optional] 
**channels** | **Number** | The number of channels in the final recording file. Can be: &#x60;1&#x60; or &#x60;2&#x60;. You can split a call with two legs into two separate recording channels if you record using [TwiML Dial](https://www.twilio.com/docs/voice/twiml/dial#record) or the [Outbound Rest API](https://www.twilio.com/docs/voice/make-calls#manage-your-outbound-call). | [optional] 
**conferenceSid** | **String** | The Conference SID that identifies the conference associated with the recording, if a conference recording. | [optional] 
**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**duration** | **String** | The length of the recording in seconds. | [optional] 
**encryptionDetails** | **Object** | How to decrypt the recording if it was encrypted using [Call Recording Encryption](https://www.twilio.com/docs/voice/tutorials/voice-recording-encryption) feature. | [optional] 
**errorCode** | **Number** | The error code that describes why the recording is &#x60;absent&#x60;. The error code is described in our [Error Dictionary](https://www.twilio.com/docs/api/errors). This value is null if the recording &#x60;status&#x60; is not &#x60;absent&#x60;. | [optional] 
**mediaUrl** | **String** | The URL of the media file associated with this recording resource. When stored externally, this is the full URL location of the media file. | [optional] 
**price** | **String** | The one-time cost of creating the recording in the &#x60;price_unit&#x60; currency. | [optional] 
**priceUnit** | **String** | The currency used in the &#x60;price&#x60; property. Example: &#x60;USD&#x60;. | [optional] 
**sid** | **String** | The unique string that that we created to identify the Recording resource. | [optional] 
**source** | [**RecordingEnumSource**](RecordingEnumSource.md) |  | [optional] 
**startTime** | **String** | The start time of the recording in GMT and in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format. | [optional] 
**status** | [**RecordingEnumStatus**](RecordingEnumStatus.md) |  | [optional] 
**subresourceUris** | **Object** | A list of related resources identified by their relative URIs. | [optional] 
**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 


