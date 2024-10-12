

# RolloutUpdateEvent

Payload proto for \"clouddeploy.googleapis.com/rollout_update\" Platform Log event that describes the rollout update event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Debug message for when a rollout update event occurs. |  [optional] |
|**pipelineUid** | **String** | Unique identifier of the pipeline. |  [optional] |
|**release** | **String** | The name of the &#x60;Release&#x60;. |  [optional] |
|**releaseUid** | **String** | Unique identifier of the release. |  [optional] |
|**rollout** | **String** | The name of the rollout. rollout_uid is not in this log message because we write some of these log messages at rollout creation time, before we&#39;ve generated the uid. |  [optional] |
|**rolloutUpdateType** | [**RolloutUpdateTypeEnum**](#RolloutUpdateTypeEnum) | The type of the rollout update. |  [optional] |
|**targetId** | **String** | ID of the target. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of this notification, e.g. for a rollout update event. |  [optional] |



## Enum: RolloutUpdateTypeEnum

| Name | Value |
|---- | -----|
| ROLLOUT_UPDATE_TYPE_UNSPECIFIED | &quot;ROLLOUT_UPDATE_TYPE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| PENDING_RELEASE | &quot;PENDING_RELEASE&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| HALTED | &quot;HALTED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| APPROVAL_REQUIRED | &quot;APPROVAL_REQUIRED&quot; |
| APPROVED | &quot;APPROVED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| ADVANCE_REQUIRED | &quot;ADVANCE_REQUIRED&quot; |
| ADVANCED | &quot;ADVANCED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| PUBSUB_NOTIFICATION_FAILURE | &quot;TYPE_PUBSUB_NOTIFICATION_FAILURE&quot; |
| RESOURCE_STATE_CHANGE | &quot;TYPE_RESOURCE_STATE_CHANGE&quot; |
| PROCESS_ABORTED | &quot;TYPE_PROCESS_ABORTED&quot; |
| RESTRICTION_VIOLATED | &quot;TYPE_RESTRICTION_VIOLATED&quot; |
| RESOURCE_DELETED | &quot;TYPE_RESOURCE_DELETED&quot; |
| ROLLOUT_UPDATE | &quot;TYPE_ROLLOUT_UPDATE&quot; |
| DEPLOY_POLICY_EVALUATION | &quot;TYPE_DEPLOY_POLICY_EVALUATION&quot; |
| RENDER_STATUES_CHANGE | &quot;TYPE_RENDER_STATUES_CHANGE&quot; |



