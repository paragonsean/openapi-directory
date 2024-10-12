# TwilioInsights.InsightsV1ConferenceConferenceParticipant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique SID identifier of the Account. | [optional] 
**callDirection** | [**ConferenceParticipantEnumCallDirection**](ConferenceParticipantEnumCallDirection.md) |  | [optional] 
**callSid** | **String** | Unique SID identifier of the call that generated the Participant resource. | [optional] 
**callStatus** | [**ConferenceParticipantEnumCallStatus**](ConferenceParticipantEnumCallStatus.md) |  | [optional] 
**callType** | [**ConferenceParticipantEnumCallType**](ConferenceParticipantEnumCallType.md) |  | [optional] 
**coachedParticipants** | **[String]** | Call SIDs coached by this participant. | [optional] 
**conferenceRegion** | [**ConferenceParticipantEnumRegion**](ConferenceParticipantEnumRegion.md) |  | [optional] 
**conferenceSid** | **String** | The unique SID identifier of the Conference. | [optional] 
**countryCode** | **String** | ISO alpha-2 country code of the participant based on caller ID or called number. | [optional] 
**durationSeconds** | **Number** | Participant durations in seconds. | [optional] 
**events** | **Object** | Object containing information of actions taken by participants. Contains a dictionary of URL links to nested resources of this Conference Participant. | [optional] 
**from** | **String** | Caller ID of the calling party. | [optional] 
**isCoach** | **Boolean** | Boolean. Indicated whether participant was a coach. | [optional] 
**isModerator** | **Boolean** | Boolean. Indicates whether participant had startConferenceOnEnter&#x3D;true or endConferenceOnExit&#x3D;true. | [optional] 
**jitterBufferSize** | [**ConferenceParticipantEnumJitterBufferSize**](ConferenceParticipantEnumJitterBufferSize.md) |  | [optional] 
**joinTime** | **Date** | ISO 8601 timestamp of participant join event. | [optional] 
**label** | **String** | The user-specified label of this participant. | [optional] 
**leaveTime** | **Date** | ISO 8601 timestamp of participant leave event. | [optional] 
**metrics** | **Object** | Object. Contains participant call quality metrics. | [optional] 
**outboundQueueLength** | **Number** | Add Participant API only. Estimated time in queue at call creation. | [optional] 
**outboundTimeInQueue** | **Number** | Add Participant API only. Actual time in queue in seconds. | [optional] 
**participantRegion** | [**ConferenceParticipantEnumRegion**](ConferenceParticipantEnumRegion.md) |  | [optional] 
**participantSid** | **String** | SID for this participant. | [optional] 
**processingState** | [**ConferenceParticipantEnumProcessingState**](ConferenceParticipantEnumProcessingState.md) |  | [optional] 
**properties** | **Object** | Participant properties and metadata. | [optional] 
**to** | **String** | Called party. | [optional] 
**url** | **String** | The URL of this resource. | [optional] 


