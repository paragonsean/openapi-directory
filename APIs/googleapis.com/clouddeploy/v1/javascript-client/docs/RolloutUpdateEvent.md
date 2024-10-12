# CloudDeployApi.RolloutUpdateEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Debug message for when a rollout update event occurs. | [optional] 
**pipelineUid** | **String** | Unique identifier of the pipeline. | [optional] 
**release** | **String** | The name of the &#x60;Release&#x60;. | [optional] 
**releaseUid** | **String** | Unique identifier of the release. | [optional] 
**rollout** | **String** | The name of the rollout. rollout_uid is not in this log message because we write some of these log messages at rollout creation time, before we&#39;ve generated the uid. | [optional] 
**rolloutUpdateType** | **String** | The type of the rollout update. | [optional] 
**targetId** | **String** | ID of the target. | [optional] 
**type** | **String** | Type of this notification, e.g. for a rollout update event. | [optional] 



## Enum: RolloutUpdateTypeEnum


* `ROLLOUT_UPDATE_TYPE_UNSPECIFIED` (value: `"ROLLOUT_UPDATE_TYPE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `PENDING_RELEASE` (value: `"PENDING_RELEASE"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `HALTED` (value: `"HALTED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `APPROVAL_REQUIRED` (value: `"APPROVAL_REQUIRED"`)

* `APPROVED` (value: `"APPROVED"`)

* `REJECTED` (value: `"REJECTED"`)

* `ADVANCE_REQUIRED` (value: `"ADVANCE_REQUIRED"`)

* `ADVANCED` (value: `"ADVANCED"`)





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




