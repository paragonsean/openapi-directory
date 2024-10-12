# TwilioMedia.MediaV1MediaRecording

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the MediaRecording resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**duration** | **Number** | The duration of the MediaRecording in seconds. | [optional] 
**format** | [**MediaRecordingEnumFormat**](MediaRecordingEnumFormat.md) |  | [optional] 
**links** | **Object** | The URLs of related resources. | [optional] 
**mediaSize** | **Number** | The size of the recording media in bytes. | [optional] 
**processorSid** | **String** | The SID of the MediaProcessor resource which produced the MediaRecording. | [optional] 
**resolution** | **String** | The dimensions of the video image in pixels expressed as columns (width) and rows (height). | [optional] 
**sid** | **String** | The unique string generated to identify the MediaRecording resource. | [optional] 
**sourceSid** | **String** | The SID of the resource that generated the original media track(s) of the MediaRecording. | [optional] 
**status** | [**MediaRecordingEnumStatus**](MediaRecordingEnumStatus.md) |  | [optional] 
**statusCallback** | **String** | The URL to which Twilio will send asynchronous webhook requests for every MediaRecording event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details. | [optional] 
**statusCallbackMethod** | **String** | The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 



## Enum: StatusCallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)




