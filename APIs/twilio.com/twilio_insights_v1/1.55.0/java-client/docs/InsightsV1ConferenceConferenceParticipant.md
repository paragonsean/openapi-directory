

# InsightsV1ConferenceConferenceParticipant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique SID identifier of the Account. |  [optional] |
|**callDirection** | **ConferenceParticipantEnumCallDirection** |  |  [optional] |
|**callSid** | **String** | Unique SID identifier of the call that generated the Participant resource. |  [optional] |
|**callStatus** | **ConferenceParticipantEnumCallStatus** |  |  [optional] |
|**callType** | **ConferenceParticipantEnumCallType** |  |  [optional] |
|**coachedParticipants** | **List&lt;String&gt;** | Call SIDs coached by this participant. |  [optional] |
|**conferenceRegion** | **ConferenceParticipantEnumRegion** |  |  [optional] |
|**conferenceSid** | **String** | The unique SID identifier of the Conference. |  [optional] |
|**countryCode** | **String** | ISO alpha-2 country code of the participant based on caller ID or called number. |  [optional] |
|**durationSeconds** | **Integer** | Participant durations in seconds. |  [optional] |
|**events** | **Object** | Object containing information of actions taken by participants. Contains a dictionary of URL links to nested resources of this Conference Participant. |  [optional] |
|**from** | **String** | Caller ID of the calling party. |  [optional] |
|**isCoach** | **Boolean** | Boolean. Indicated whether participant was a coach. |  [optional] |
|**isModerator** | **Boolean** | Boolean. Indicates whether participant had startConferenceOnEnter&#x3D;true or endConferenceOnExit&#x3D;true. |  [optional] |
|**jitterBufferSize** | **ConferenceParticipantEnumJitterBufferSize** |  |  [optional] |
|**joinTime** | **OffsetDateTime** | ISO 8601 timestamp of participant join event. |  [optional] |
|**label** | **String** | The user-specified label of this participant. |  [optional] |
|**leaveTime** | **OffsetDateTime** | ISO 8601 timestamp of participant leave event. |  [optional] |
|**metrics** | **Object** | Object. Contains participant call quality metrics. |  [optional] |
|**outboundQueueLength** | **Integer** | Add Participant API only. Estimated time in queue at call creation. |  [optional] |
|**outboundTimeInQueue** | **Integer** | Add Participant API only. Actual time in queue in seconds. |  [optional] |
|**participantRegion** | **ConferenceParticipantEnumRegion** |  |  [optional] |
|**participantSid** | **String** | SID for this participant. |  [optional] |
|**processingState** | **ConferenceParticipantEnumProcessingState** |  |  [optional] |
|**properties** | **Object** | Participant properties and metadata. |  [optional] |
|**to** | **String** | Called party. |  [optional] |
|**url** | **URI** | The URL of this resource. |  [optional] |



