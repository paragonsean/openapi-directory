

# InsightsV1VideoRoomSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | Account SID associated with this room. |  [optional] |
|**codecs** | **List&lt;VideoRoomSummaryEnumCodec&gt;** | Codecs used by participants in the room. Can be &#x60;VP8&#x60;, &#x60;H264&#x60;, or &#x60;VP9&#x60;. |  [optional] |
|**concurrentParticipants** | **Integer** | Actual number of concurrent participants. |  [optional] |
|**createTime** | **OffsetDateTime** | Creation time of the room. |  [optional] |
|**createdMethod** | **VideoRoomSummaryEnumCreatedMethod** |  |  [optional] |
|**durationSec** | **Long** | Total room duration from create time to end time. |  [optional] |
|**edgeLocation** | **VideoRoomSummaryEnumEdgeLocation** |  |  [optional] |
|**endReason** | **VideoRoomSummaryEnumEndReason** |  |  [optional] |
|**endTime** | **OffsetDateTime** | End time for the room. |  [optional] |
|**links** | **Object** | Room subresources. |  [optional] |
|**maxConcurrentParticipants** | **Integer** | Maximum number of participants allowed in the room at the same time allowed by the application settings. |  [optional] |
|**maxParticipants** | **Integer** | Max number of total participants allowed by the application settings. |  [optional] |
|**mediaRegion** | **VideoRoomSummaryEnumTwilioRealm** |  |  [optional] |
|**processingState** | **VideoRoomSummaryEnumProcessingState** |  |  [optional] |
|**recordingEnabled** | **Boolean** | Boolean indicating if recording is enabled for the room. |  [optional] |
|**roomName** | **String** | Room friendly name. |  [optional] |
|**roomSid** | **String** | Unique identifier for the room. |  [optional] |
|**roomStatus** | **VideoRoomSummaryEnumRoomStatus** |  |  [optional] |
|**roomType** | **VideoRoomSummaryEnumRoomType** |  |  [optional] |
|**statusCallback** | **URI** | Webhook provided for status callbacks. |  [optional] |
|**statusCallbackMethod** | [**StatusCallbackMethodEnum**](#StatusCallbackMethodEnum) | HTTP method provided for status callback URL. |  [optional] |
|**totalParticipantDurationSec** | **Long** | Combined amount of participant time in the room. |  [optional] |
|**totalRecordingDurationSec** | **Long** | Combined amount of recorded seconds for participants in the room. |  [optional] |
|**uniqueParticipantIdentities** | **Integer** | Unique number of participant identities. |  [optional] |
|**uniqueParticipants** | **Integer** | Number of participants. May include duplicate identities for participants who left and rejoined. |  [optional] |
|**url** | **URI** | URL for the room resource. |  [optional] |



## Enum: StatusCallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



