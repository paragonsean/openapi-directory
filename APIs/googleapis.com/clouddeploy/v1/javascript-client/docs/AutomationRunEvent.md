# CloudDeployApi.AutomationRunEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automationId** | **String** | Identifier of the &#x60;Automation&#x60;. | [optional] 
**automationRun** | **String** | The name of the &#x60;AutomationRun&#x60;. | [optional] 
**destinationTargetId** | **String** | ID of the &#x60;Target&#x60; to which the &#x60;AutomationRun&#x60; is created. | [optional] 
**message** | **String** | Debug message for when there is an update on the AutomationRun. Provides further details about the resource creation or state change. | [optional] 
**pipelineUid** | **String** | Unique identifier of the &#x60;DeliveryPipeline&#x60;. | [optional] 
**ruleId** | **String** | Identifier of the &#x60;Automation&#x60; rule. | [optional] 
**type** | **String** | Type of this notification, e.g. for a Pub/Sub failure. | [optional] 



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




