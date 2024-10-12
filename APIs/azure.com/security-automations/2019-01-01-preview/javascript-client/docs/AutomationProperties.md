# SecurityCenter.AutomationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[AutomationAction]**](AutomationAction.md) | A collection of the actions which are triggered if all the configured rules evaluations, within at least one rule set, are true. | [optional] 
**description** | **String** | The security automation description. | [optional] 
**isEnabled** | **Boolean** | Indicates whether the security automation is enabled. | [optional] 
**scopes** | [**[AutomationScope]**](AutomationScope.md) | A collection of scopes on which the security automations logic is applied. Supported scopes are the subscription itself or a resource group under that subscription. The automation will only apply on defined scopes. | [optional] 
**sources** | [**[AutomationSource]**](AutomationSource.md) | A collection of the source event types which evaluate the security automation set of rules. | [optional] 


