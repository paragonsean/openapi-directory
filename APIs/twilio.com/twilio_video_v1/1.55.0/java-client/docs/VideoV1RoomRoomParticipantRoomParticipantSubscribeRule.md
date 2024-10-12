

# VideoV1RoomRoomParticipantRoomParticipantSubscribeRule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**participantSid** | **String** | The SID of the Participant resource for the Subscribe Rules. |  [optional] |
|**roomSid** | **String** | The SID of the Room resource for the Subscribe Rules |  [optional] |
|**rules** | [**List&lt;VideoV1RoomRoomParticipantRoomParticipantSubscribeRuleRulesInner&gt;**](VideoV1RoomRoomParticipantRoomParticipantSubscribeRuleRulesInner.md) | A collection of Subscribe Rules that describe how to include or exclude matching tracks. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information. |  [optional] |



