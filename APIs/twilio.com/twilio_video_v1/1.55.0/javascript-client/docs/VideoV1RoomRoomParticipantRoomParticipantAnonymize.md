# TwilioVideo.VideoV1RoomRoomParticipantRoomParticipantAnonymize

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RoomParticipant resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**duration** | **Number** | The duration in seconds that the participant was &#x60;connected&#x60;. Populated only after the participant is &#x60;disconnected&#x60;. | [optional] 
**endTime** | **Date** | The time when the participant disconnected from the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format. | [optional] 
**identity** | **String** | The SID of the participant. | [optional] 
**roomSid** | **String** | The SID of the participant&#39;s room. | [optional] 
**sid** | **String** | The unique string that we created to identify the RoomParticipant resource. | [optional] 
**startTime** | **Date** | The time of participant connected to the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format. | [optional] 
**status** | [**RoomParticipantAnonymizeEnumStatus**](RoomParticipantAnonymizeEnumStatus.md) |  | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 


