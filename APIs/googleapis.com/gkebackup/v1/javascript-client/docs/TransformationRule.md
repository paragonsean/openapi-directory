# BackupForGkeApi.TransformationRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Optional. The description is a user specified string description of the transformation rule. | [optional] 
**fieldActions** | [**[TransformationRuleAction]**](TransformationRuleAction.md) | Required. A list of transformation rule actions to take against candidate resources. Actions are executed in order defined - this order matters, as they could potentially interfere with each other and the first operation could affect the outcome of the second operation. | [optional] 
**resourceFilter** | [**ResourceFilter**](ResourceFilter.md) |  | [optional] 


