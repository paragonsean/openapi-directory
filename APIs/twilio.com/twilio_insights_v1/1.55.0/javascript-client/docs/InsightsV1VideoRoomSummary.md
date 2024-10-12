# TwilioInsights.InsightsV1VideoRoomSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | Account SID associated with this room. | [optional] 
**codecs** | [**[VideoRoomSummaryEnumCodec]**](VideoRoomSummaryEnumCodec.md) | Codecs used by participants in the room. Can be &#x60;VP8&#x60;, &#x60;H264&#x60;, or &#x60;VP9&#x60;. | [optional] 
**concurrentParticipants** | **Number** | Actual number of concurrent participants. | [optional] 
**createTime** | **Date** | Creation time of the room. | [optional] 
**createdMethod** | [**VideoRoomSummaryEnumCreatedMethod**](VideoRoomSummaryEnumCreatedMethod.md) |  | [optional] 
**durationSec** | **Number** | Total room duration from create time to end time. | [optional] 
**edgeLocation** | [**VideoRoomSummaryEnumEdgeLocation**](VideoRoomSummaryEnumEdgeLocation.md) |  | [optional] 
**endReason** | [**VideoRoomSummaryEnumEndReason**](VideoRoomSummaryEnumEndReason.md) |  | [optional] 
**endTime** | **Date** | End time for the room. | [optional] 
**links** | **Object** | Room subresources. | [optional] 
**maxConcurrentParticipants** | **Number** | Maximum number of participants allowed in the room at the same time allowed by the application settings. | [optional] 
**maxParticipants** | **Number** | Max number of total participants allowed by the application settings. | [optional] 
**mediaRegion** | [**VideoRoomSummaryEnumTwilioRealm**](VideoRoomSummaryEnumTwilioRealm.md) |  | [optional] 
**processingState** | [**VideoRoomSummaryEnumProcessingState**](VideoRoomSummaryEnumProcessingState.md) |  | [optional] 
**recordingEnabled** | **Boolean** | Boolean indicating if recording is enabled for the room. | [optional] 
**roomName** | **String** | Room friendly name. | [optional] 
**roomSid** | **String** | Unique identifier for the room. | [optional] 
**roomStatus** | [**VideoRoomSummaryEnumRoomStatus**](VideoRoomSummaryEnumRoomStatus.md) |  | [optional] 
**roomType** | [**VideoRoomSummaryEnumRoomType**](VideoRoomSummaryEnumRoomType.md) |  | [optional] 
**statusCallback** | **String** | Webhook provided for status callbacks. | [optional] 
**statusCallbackMethod** | **String** | HTTP method provided for status callback URL. | [optional] 
**totalParticipantDurationSec** | **Number** | Combined amount of participant time in the room. | [optional] 
**totalRecordingDurationSec** | **Number** | Combined amount of recorded seconds for participants in the room. | [optional] 
**uniqueParticipantIdentities** | **Number** | Unique number of participant identities. | [optional] 
**uniqueParticipants** | **Number** | Number of participants. May include duplicate identities for participants who left and rejoined. | [optional] 
**url** | **String** | URL for the room resource. | [optional] 



## Enum: StatusCallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)




