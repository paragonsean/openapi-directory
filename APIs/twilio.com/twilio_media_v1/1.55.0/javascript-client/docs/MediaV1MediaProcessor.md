# TwilioMedia.MediaV1MediaProcessor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the MediaProcessor resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**endedReason** | **String** | The reason why a MediaProcessor ended. When a MediaProcessor is in progress, will be &#x60;null&#x60;. When a MediaProcessor is completed, can be &#x60;ended-via-api&#x60;, &#x60;max-duration-exceeded&#x60;, &#x60;error-loading-extension&#x60;, &#x60;error-streaming-media&#x60; or &#x60;internal-service-error&#x60;. See [ended reasons](/docs/live/api/mediaprocessors#mediaprocessor-ended-reason-values) for more details. | [optional] 
**extension** | **String** | The [Media Extension](/docs/live/media-extensions-overview) name or URL. Ex: &#x60;video-composer-v2&#x60; | [optional] 
**extensionContext** | **String** | The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about the context to send. | [optional] 
**maxDuration** | **Number** | The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming. | [optional] 
**sid** | **String** | The unique string generated to identify the MediaProcessor resource. | [optional] 
**status** | [**MediaProcessorEnumStatus**](MediaProcessorEnumStatus.md) |  | [optional] 
**statusCallback** | **String** | The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/api/status-callbacks) for details. | [optional] 
**statusCallbackMethod** | **String** | The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 



## Enum: StatusCallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)




