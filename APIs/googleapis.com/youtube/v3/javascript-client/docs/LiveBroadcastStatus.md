# YouTubeDataApiV3.LiveBroadcastStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifeCycleStatus** | **String** | The broadcast&#39;s status. The status can be updated using the API&#39;s liveBroadcasts.transition method. | [optional] 
**liveBroadcastPriority** | **String** | Priority of the live broadcast event (internal state). | [optional] 
**madeForKids** | **Boolean** | Whether the broadcast is made for kids or not, decided by YouTube instead of the creator. This field is read only. | [optional] 
**privacyStatus** | **String** | The broadcast&#39;s privacy status. Note that the broadcast represents exactly one YouTube video, so the privacy settings are identical to those supported for videos. In addition, you can set this field by modifying the broadcast resource or by setting the privacyStatus field of the corresponding video resource. | [optional] 
**recordingStatus** | **String** | The broadcast&#39;s recording status. | [optional] 
**selfDeclaredMadeForKids** | **Boolean** | This field will be set to True if the creator declares the broadcast to be kids only: go/live-cw-work. | [optional] 



## Enum: LifeCycleStatusEnum


* `lifeCycleStatusUnspecified` (value: `"lifeCycleStatusUnspecified"`)

* `created` (value: `"created"`)

* `ready` (value: `"ready"`)

* `testing` (value: `"testing"`)

* `live` (value: `"live"`)

* `complete` (value: `"complete"`)

* `revoked` (value: `"revoked"`)

* `testStarting` (value: `"testStarting"`)

* `liveStarting` (value: `"liveStarting"`)





## Enum: LiveBroadcastPriorityEnum


* `liveBroadcastPriorityUnspecified` (value: `"liveBroadcastPriorityUnspecified"`)

* `low` (value: `"low"`)

* `normal` (value: `"normal"`)

* `high` (value: `"high"`)





## Enum: PrivacyStatusEnum


* `public` (value: `"public"`)

* `unlisted` (value: `"unlisted"`)

* `private` (value: `"private"`)





## Enum: RecordingStatusEnum


* `liveBroadcastRecordingStatusUnspecified` (value: `"liveBroadcastRecordingStatusUnspecified"`)

* `notRecording` (value: `"notRecording"`)

* `recording` (value: `"recording"`)

* `recorded` (value: `"recorded"`)




