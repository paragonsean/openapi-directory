

# TargetNotificationEvent

Payload proto for \"clouddeploy.googleapis.com/target_notification\" Platform Log event that describes the failure to send target status change Pub/Sub notification.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Debug message for when a notification fails to send. |  [optional] |
|**target** | **String** | The name of the &#x60;Target&#x60;. |  [optional] |
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



