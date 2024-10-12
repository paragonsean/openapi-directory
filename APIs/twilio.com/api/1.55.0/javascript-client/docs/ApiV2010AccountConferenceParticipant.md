# TwilioApi.ApiV2010AccountConferenceParticipant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resource. | [optional] 
**callSid** | **String** | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Participant resource is associated with. | [optional] 
**callSidToCoach** | **String** | The SID of the participant who is being &#x60;coached&#x60;. The participant being coached is the only participant who can hear the participant who is &#x60;coaching&#x60;. | [optional] 
**coaching** | **Boolean** | Whether the participant is coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;. If not present, defaults to &#x60;false&#x60; unless &#x60;call_sid_to_coach&#x60; is defined. If &#x60;true&#x60;, &#x60;call_sid_to_coach&#x60; must be defined. | [optional] 
**conferenceSid** | **String** | The SID of the conference the participant is in. | [optional] 
**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**endConferenceOnExit** | **Boolean** | Whether the conference ends when the participant leaves. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. If &#x60;true&#x60;, the conference ends and all other participants drop out when the participant leaves. | [optional] 
**hold** | **Boolean** | Whether the participant is on hold. Can be &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
**label** | **String** | The user-specified label of this participant, if one was given when the participant was created. This may be used to fetch, update or delete the participant. | [optional] 
**muted** | **Boolean** | Whether the participant is muted. Can be &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
**startConferenceOnEnter** | **Boolean** | Whether the conference starts when the participant joins the conference, if it has not already started. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference. | [optional] 
**status** | [**ParticipantEnumStatus**](ParticipantEnumStatus.md) |  | [optional] 
**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 


