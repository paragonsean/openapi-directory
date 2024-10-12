

# ReleaseRenderEvent

Payload proto for \"clouddeploy.googleapis.com/release_render\" Platform Log event that describes the render status change.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Debug message for when a render transition occurs. Provides further details as rendering progresses through render states. |  [optional] |
|**pipelineUid** | **String** | Unique identifier of the &#x60;DeliveryPipeline&#x60;. |  [optional] |
|**release** | **String** | The name of the release. release_uid is not in this log message because we write some of these log messages at release creation time, before we&#39;ve generated the uid. |  [optional] |
|**releaseRenderState** | [**ReleaseRenderStateEnum**](#ReleaseRenderStateEnum) | The state of the release render. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of this notification, e.g. for a release render state change event. |  [optional] |



## Enum: ReleaseRenderStateEnum

| Name | Value |
|---- | -----|
| RENDER_STATE_UNSPECIFIED | &quot;RENDER_STATE_UNSPECIFIED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |



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



