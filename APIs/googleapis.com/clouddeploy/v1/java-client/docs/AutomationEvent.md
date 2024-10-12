

# AutomationEvent

Payload proto for \"clouddeploy.googleapis.com/automation\" Platform Log event that describes the Automation related events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automation** | **String** | The name of the &#x60;AutomationRun&#x60;. |  [optional] |
|**message** | **String** | Debug message for when there is an update on the AutomationRun. Provides further details about the resource creation or state change. |  [optional] |
|**pipelineUid** | **String** | Unique identifier of the &#x60;DeliveryPipeline&#x60;. |  [optional] |
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



