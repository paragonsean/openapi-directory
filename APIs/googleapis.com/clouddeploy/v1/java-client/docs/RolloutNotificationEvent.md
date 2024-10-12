

# RolloutNotificationEvent

Payload proto for \"clouddeploy.googleapis.com/rollout_notification\" Platform Log event that describes the failure to send rollout status change Pub/Sub notification.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Debug message for when a notification fails to send. |  [optional] |
|**pipelineUid** | **String** | Unique identifier of the &#x60;DeliveryPipeline&#x60;. |  [optional] |
|**release** | **String** | The name of the &#x60;Release&#x60;. |  [optional] |
|**releaseUid** | **String** | Unique identifier of the &#x60;Release&#x60;. |  [optional] |
|**rollout** | **String** | The name of the &#x60;Rollout&#x60;. |  [optional] |
|**rolloutUid** | **String** | Unique identifier of the &#x60;Rollout&#x60;. |  [optional] |
|**targetId** | **String** | ID of the &#x60;Target&#x60; that the rollout is deployed to. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of this notification, e.g. for a Pub/Sub failure. |  [optional] |



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



