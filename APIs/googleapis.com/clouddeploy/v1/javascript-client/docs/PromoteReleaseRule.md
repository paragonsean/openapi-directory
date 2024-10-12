# CloudDeployApi.PromoteReleaseRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**AutomationRuleCondition**](AutomationRuleCondition.md) |  | [optional] 
**destinationPhase** | **String** | Optional. The starting phase of the rollout created by this operation. Default to the first phase. | [optional] 
**destinationTargetId** | **String** | Optional. The ID of the stage in the pipeline to which this &#x60;Release&#x60; is deploying. If unspecified, default it to the next stage in the promotion flow. The value of this field could be one of the following: * The last segment of a target name. It only needs the ID to determine if the target is one of the stages in the promotion sequence defined in the pipeline. * \&quot;@next\&quot;, the next target in the promotion sequence. | [optional] 
**id** | **String** | Required. ID of the rule. This id must be unique in the &#x60;Automation&#x60; resource to which this rule belongs. The format is &#x60;a-z{0,62}&#x60;. | [optional] 
**wait** | **String** | Optional. How long the release need to be paused until being promoted to the next target. | [optional] 


