

# VideoV1Recording


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource. |  [optional] |
|**codec** | **RecordingEnumCodec** |  |  [optional] |
|**containerFormat** | **RecordingEnumFormat** |  |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**duration** | **Integer** | The duration of the recording in seconds rounded to the nearest second. Sub-second tracks have a &#x60;Duration&#x60; property of 1 second |  [optional] |
|**groupingSids** | **Object** | A list of SIDs related to the recording. Includes the &#x60;room_sid&#x60; and &#x60;participant_sid&#x60;. |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**mediaExternalLocation** | **URI** | The URL of the media file associated with the recording when stored externally. See [External S3 Recordings](/docs/video/api/external-s3-recordings) for more details. |  [optional] |
|**offset** | **Long** | The time in milliseconds elapsed between an arbitrary point in time, common to all group rooms, and the moment when the source room of this track started. This information provides a synchronization mechanism for recordings belonging to the same room. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Recording resource. |  [optional] |
|**size** | **Long** | The size of the recorded track, in bytes. |  [optional] |
|**sourceSid** | **String** | The SID of the recording source. For a Room Recording, this value is a &#x60;track_sid&#x60;. |  [optional] |
|**status** | **RecordingEnumStatus** |  |  [optional] |
|**statusCallback** | **URI** | The URL called using the &#x60;status_callback_method&#x60; to send status information on every recording event. |  [optional] |
|**statusCallbackMethod** | [**StatusCallbackMethodEnum**](#StatusCallbackMethodEnum) | The HTTP method used to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;, defaults to &#x60;POST&#x60;. |  [optional] |
|**trackName** | **String** | The name that was given to the source track of the recording. If no name is given, the &#x60;source_sid&#x60; is used. |  [optional] |
|**type** | **RecordingEnumType** |  |  [optional] |
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



