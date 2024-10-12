# TwilioInsights.InsightsV1VideoRoomSummaryVideoParticipantSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | Account SID associated with the room. | [optional] 
**codecs** | [**[VideoParticipantSummaryEnumCodec]**](VideoParticipantSummaryEnumCodec.md) | Codecs detected from the participant. Can be &#x60;VP8&#x60;, &#x60;H264&#x60;, or &#x60;VP9&#x60;. | [optional] 
**durationSec** | **Number** | Amount of time in seconds the participant was in the room. | [optional] 
**edgeLocation** | [**VideoParticipantSummaryEnumEdgeLocation**](VideoParticipantSummaryEnumEdgeLocation.md) |  | [optional] 
**endReason** | **String** | Reason the participant left the room. See [the list of possible values here](https://www.twilio.com/docs/video/troubleshooting/video-log-analyzer-api#end_reason). | [optional] 
**errorCode** | **Number** | Errors encountered by the participant. | [optional] 
**errorCodeUrl** | **String** | Twilio error code dictionary link. | [optional] 
**joinTime** | **Date** | When the participant joined the room. | [optional] 
**leaveTime** | **Date** | When the participant left the room. | [optional] 
**mediaRegion** | [**VideoParticipantSummaryEnumTwilioRealm**](VideoParticipantSummaryEnumTwilioRealm.md) |  | [optional] 
**participantIdentity** | **String** | The application-defined string that uniquely identifies the participant within a Room. | [optional] 
**participantSid** | **String** | Unique identifier for the participant. | [optional] 
**properties** | **Object** | Object containing information about the participant&#39;s data from the room. See [below](https://www.twilio.com/docs/video/troubleshooting/video-log-analyzer-api#properties) for more information. | [optional] 
**publisherInfo** | **Object** | Object containing information about the SDK name and version. See [below](https://www.twilio.com/docs/video/troubleshooting/video-log-analyzer-api#publisher_info) for more information. | [optional] 
**roomSid** | **String** | Unique identifier for the room. | [optional] 
**status** | [**VideoParticipantSummaryEnumRoomStatus**](VideoParticipantSummaryEnumRoomStatus.md) |  | [optional] 
**url** | **String** | URL of the participant resource. | [optional] 


