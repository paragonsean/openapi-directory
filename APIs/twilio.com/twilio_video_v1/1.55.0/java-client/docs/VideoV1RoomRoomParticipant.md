

# VideoV1RoomRoomParticipant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RoomParticipant resource. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**duration** | **Integer** | The duration in seconds that the participant was &#x60;connected&#x60;. Populated only after the participant is &#x60;disconnected&#x60;. |  [optional] |
|**endTime** | **OffsetDateTime** | The time when the participant disconnected from the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format. |  [optional] |
|**identity** | **String** | The application-defined string that uniquely identifies the resource&#39;s User within a Room. If a client joins with an existing Identity, the existing client is disconnected. See [access tokens](https://www.twilio.com/docs/video/tutorials/user-identity-access-tokens) and [limits](https://www.twilio.com/docs/video/programmable-video-limits) for more info.  |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**roomSid** | **String** | The SID of the participant&#39;s room. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the RoomParticipant resource. |  [optional] |
|**startTime** | **OffsetDateTime** | The time of participant connected to the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format. |  [optional] |
|**status** | **RoomParticipantEnumStatus** |  |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |



