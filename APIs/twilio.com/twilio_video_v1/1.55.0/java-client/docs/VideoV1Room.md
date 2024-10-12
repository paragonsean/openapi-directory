

# VideoV1Room


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Room resource. |  [optional] |
|**audioOnly** | **Boolean** | When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**duration** | **Integer** | The duration of the room in seconds. |  [optional] |
|**emptyRoomTimeout** | **Integer** | Specifies how long (in minutes) a room will remain active after last participant leaves. Can be configured when creating a room via REST API. For Ad-Hoc rooms this value cannot be changed. |  [optional] |
|**enableTurn** | **Boolean** | Deprecated, now always considered to be true. |  [optional] |
|**endTime** | **OffsetDateTime** | The UTC end time of the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format. |  [optional] |
|**largeRoom** | **Boolean** | Indicates if this is a large room. |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**maxConcurrentPublishedTracks** | **Integer** | The maximum number of published audio, video, and data tracks all participants combined are allowed to publish in the room at the same time. Check [Programmable Video Limits](https://www.twilio.com/docs/video/programmable-video-limits) for more details. If it is set to 0 it means unconstrained. |  [optional] |
|**maxParticipantDuration** | **Integer** | The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours). |  [optional] |
|**maxParticipants** | **Integer** | The maximum number of concurrent Participants allowed in the room.  |  [optional] |
|**mediaRegion** | **String** | The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-addresses#media-servers). ***This feature is not available in &#x60;peer-to-peer&#x60; rooms.*** |  [optional] |
|**recordParticipantsOnConnect** | **Boolean** | Whether to start recording when Participants connect. ***This feature is not available in &#x60;peer-to-peer&#x60; rooms.*** |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Room resource. |  [optional] |
|**status** | **RoomEnumRoomStatus** |  |  [optional] |
|**statusCallback** | **URI** | The URL we call using the &#x60;status_callback_method&#x60; to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info. |  [optional] |
|**statusCallbackMethod** | [**StatusCallbackMethodEnum**](#StatusCallbackMethodEnum) | The HTTP method we use to call &#x60;status_callback&#x60;. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and defaults to &#x60;POST&#x60;. |  [optional] |
|**type** | **RoomEnumRoomType** |  |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used as a &#x60;room_sid&#x60; in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for &#x60;in-progress&#x60; rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is &#x60;in-progress&#x60;. |  [optional] |
|**unusedRoomTimeout** | **Integer** | Specifies how long (in minutes) a room will remain active if no one joins. Can be configured when creating a room via REST API. For Ad-Hoc rooms this value cannot be changed. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |
|**videoCodecs** | **List&lt;RoomEnumVideoCodec&gt;** | An array of the video codecs that are supported when publishing a track in the room.  Can be: &#x60;VP8&#x60; and &#x60;H264&#x60;.  ***This feature is not available in &#x60;peer-to-peer&#x60; rooms*** |  [optional] |



## Enum: StatusCallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



