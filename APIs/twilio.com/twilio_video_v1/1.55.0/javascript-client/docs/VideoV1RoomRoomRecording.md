# TwilioVideo.VideoV1RoomRoomRecording

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RoomRecording resource. | [optional] 
**codec** | [**RoomRecordingEnumCodec**](RoomRecordingEnumCodec.md) |  | [optional] 
**containerFormat** | [**RoomRecordingEnumFormat**](RoomRecordingEnumFormat.md) |  | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**duration** | **Number** | The duration of the recording rounded to the nearest second. Sub-second duration tracks have a &#x60;duration&#x60; of 1 second | [optional] 
**groupingSids** | **Object** | A list of SIDs related to the Recording. Includes the &#x60;room_sid&#x60; and &#x60;participant_sid&#x60;. | [optional] 
**links** | **Object** | The URLs of related resources. | [optional] 
**mediaExternalLocation** | **String** | The URL of the media file associated with the recording when stored externally. See [External S3 Recordings](/docs/video/api/external-s3-recordings) for more details. | [optional] 
**offset** | **Number** | The time in milliseconds elapsed between an arbitrary point in time, common to all group rooms, and the moment when the source room of this track started. This information provides a synchronization mechanism for recordings belonging to the same room. | [optional] 
**roomSid** | **String** | The SID of the Room resource the recording is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the RoomRecording resource. | [optional] 
**size** | **Number** | The size of the recorded track in bytes. | [optional] 
**sourceSid** | **String** | The SID of the recording source. For a Room Recording, this value is a &#x60;track_sid&#x60;. | [optional] 
**status** | [**RoomRecordingEnumStatus**](RoomRecordingEnumStatus.md) |  | [optional] 
**trackName** | **String** | The name that was given to the source track of the recording. If no name is given, the &#x60;source_sid&#x60; is used. | [optional] 
**type** | [**RoomRecordingEnumType**](RoomRecordingEnumType.md) |  | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 


