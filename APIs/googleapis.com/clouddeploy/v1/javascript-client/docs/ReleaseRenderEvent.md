# CloudDeployApi.ReleaseRenderEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Debug message for when a render transition occurs. Provides further details as rendering progresses through render states. | [optional] 
**pipelineUid** | **String** | Unique identifier of the &#x60;DeliveryPipeline&#x60;. | [optional] 
**release** | **String** | The name of the release. release_uid is not in this log message because we write some of these log messages at release creation time, before we&#39;ve generated the uid. | [optional] 
**releaseRenderState** | **String** | The state of the release render. | [optional] 
**type** | **String** | Type of this notification, e.g. for a release render state change event. | [optional] 



## Enum: ReleaseRenderStateEnum


* `RENDER_STATE_UNSPECIFIED` (value: `"RENDER_STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)





## Enum: TypeEnum


* `UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `PUBSUB_NOTIFICATION_FAILURE` (value: `"TYPE_PUBSUB_NOTIFICATION_FAILURE"`)

* `RESOURCE_STATE_CHANGE` (value: `"TYPE_RESOURCE_STATE_CHANGE"`)

* `PROCESS_ABORTED` (value: `"TYPE_PROCESS_ABORTED"`)

* `RESTRICTION_VIOLATED` (value: `"TYPE_RESTRICTION_VIOLATED"`)

* `RESOURCE_DELETED` (value: `"TYPE_RESOURCE_DELETED"`)

* `ROLLOUT_UPDATE` (value: `"TYPE_ROLLOUT_UPDATE"`)

* `DEPLOY_POLICY_EVALUATION` (value: `"TYPE_DEPLOY_POLICY_EVALUATION"`)

* `RENDER_STATUES_CHANGE` (value: `"TYPE_RENDER_STATUES_CHANGE"`)




