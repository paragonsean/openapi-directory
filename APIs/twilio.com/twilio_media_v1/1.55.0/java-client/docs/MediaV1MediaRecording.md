

# MediaV1MediaRecording


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the MediaRecording resource. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**duration** | **Integer** | The duration of the MediaRecording in seconds. |  [optional] |
|**format** | **MediaRecordingEnumFormat** |  |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**mediaSize** | **Long** | The size of the recording media in bytes. |  [optional] |
|**processorSid** | **String** | The SID of the MediaProcessor resource which produced the MediaRecording. |  [optional] |
|**resolution** | **String** | The dimensions of the video image in pixels expressed as columns (width) and rows (height). |  [optional] |
|**sid** | **String** | The unique string generated to identify the MediaRecording resource. |  [optional] |
|**sourceSid** | **String** | The SID of the resource that generated the original media track(s) of the MediaRecording. |  [optional] |
|**status** | **MediaRecordingEnumStatus** |  |  [optional] |
|**statusCallback** | **URI** | The URL to which Twilio will send asynchronous webhook requests for every MediaRecording event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details. |  [optional] |
|**statusCallbackMethod** | [**StatusCallbackMethodEnum**](#StatusCallbackMethodEnum) | The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |



## Enum: StatusCallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



