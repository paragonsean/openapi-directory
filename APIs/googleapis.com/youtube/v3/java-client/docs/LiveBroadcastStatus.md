

# LiveBroadcastStatus

Live broadcast state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lifeCycleStatus** | [**LifeCycleStatusEnum**](#LifeCycleStatusEnum) | The broadcast&#39;s status. The status can be updated using the API&#39;s liveBroadcasts.transition method. |  [optional] |
|**liveBroadcastPriority** | [**LiveBroadcastPriorityEnum**](#LiveBroadcastPriorityEnum) | Priority of the live broadcast event (internal state). |  [optional] |
|**madeForKids** | **Boolean** | Whether the broadcast is made for kids or not, decided by YouTube instead of the creator. This field is read only. |  [optional] |
|**privacyStatus** | [**PrivacyStatusEnum**](#PrivacyStatusEnum) | The broadcast&#39;s privacy status. Note that the broadcast represents exactly one YouTube video, so the privacy settings are identical to those supported for videos. In addition, you can set this field by modifying the broadcast resource or by setting the privacyStatus field of the corresponding video resource. |  [optional] |
|**recordingStatus** | [**RecordingStatusEnum**](#RecordingStatusEnum) | The broadcast&#39;s recording status. |  [optional] |
|**selfDeclaredMadeForKids** | **Boolean** | This field will be set to True if the creator declares the broadcast to be kids only: go/live-cw-work. |  [optional] |



## Enum: LifeCycleStatusEnum

| Name | Value |
|---- | -----|
| LIFE_CYCLE_STATUS_UNSPECIFIED | &quot;lifeCycleStatusUnspecified&quot; |
| CREATED | &quot;created&quot; |
| READY | &quot;ready&quot; |
| TESTING | &quot;testing&quot; |
| LIVE | &quot;live&quot; |
| COMPLETE | &quot;complete&quot; |
| REVOKED | &quot;revoked&quot; |
| TEST_STARTING | &quot;testStarting&quot; |
| LIVE_STARTING | &quot;liveStarting&quot; |



## Enum: LiveBroadcastPriorityEnum

| Name | Value |
|---- | -----|
| LIVE_BROADCAST_PRIORITY_UNSPECIFIED | &quot;liveBroadcastPriorityUnspecified&quot; |
| LOW | &quot;low&quot; |
| NORMAL | &quot;normal&quot; |
| HIGH | &quot;high&quot; |



## Enum: PrivacyStatusEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| UNLISTED | &quot;unlisted&quot; |
| PRIVATE | &quot;private&quot; |



## Enum: RecordingStatusEnum

| Name | Value |
|---- | -----|
| LIVE_BROADCAST_RECORDING_STATUS_UNSPECIFIED | &quot;liveBroadcastRecordingStatusUnspecified&quot; |
| NOT_RECORDING | &quot;notRecording&quot; |
| RECORDING | &quot;recording&quot; |
| RECORDED | &quot;recorded&quot; |



