# CloudDeployApi.RepairRolloutRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**AutomationRuleCondition**](AutomationRuleCondition.md) |  | [optional] 
**id** | **String** | Required. ID of the rule. This id must be unique in the &#x60;Automation&#x60; resource to which this rule belongs. The format is &#x60;a-z{0,62}&#x60;. | [optional] 
**jobs** | **[String]** | Optional. Jobs to repair. Proceeds only after job name matched any one in the list, or for all jobs if unspecified or empty. The phase that includes the job must match the phase ID specified in &#x60;source_phase&#x60;. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: &#x60;^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$&#x60;. | [optional] 
**repairModes** | [**[RepairMode]**](RepairMode.md) | Required. Defines the types of automatic repair actions for failed jobs. | [optional] 
**sourcePhases** | **[String]** | Optional. Phases within which jobs are subject to automatic repair actions on failure. Proceeds only after phase name matched any one in the list, or for all phases if unspecified. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: &#x60;^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$&#x60;. | [optional] 


