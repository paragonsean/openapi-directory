# CloudDeployApi.AdvanceRolloutRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**AutomationRuleCondition**](AutomationRuleCondition.md) |  | [optional] 
**id** | **String** | Required. ID of the rule. This id must be unique in the &#x60;Automation&#x60; resource to which this rule belongs. The format is &#x60;a-z{0,62}&#x60;. | [optional] 
**sourcePhases** | **[String]** | Optional. Proceeds only after phase name matched any one in the list. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: &#x60;^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$&#x60;. | [optional] 
**wait** | **String** | Optional. How long to wait after a rollout is finished. | [optional] 


