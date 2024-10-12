

# AutomationProperties

A set of properties that defines the behavior of the automation configuration. To learn more about the supported security events data models schemas - please visit https://aka.ms/ASCAutomationSchemas.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;AutomationAction&gt;**](AutomationAction.md) | A collection of the actions which are triggered if all the configured rules evaluations, within at least one rule set, are true. |  [optional] |
|**description** | **String** | The security automation description. |  [optional] |
|**isEnabled** | **Boolean** | Indicates whether the security automation is enabled. |  [optional] |
|**scopes** | [**List&lt;AutomationScope&gt;**](AutomationScope.md) | A collection of scopes on which the security automations logic is applied. Supported scopes are the subscription itself or a resource group under that subscription. The automation will only apply on defined scopes. |  [optional] |
|**sources** | [**List&lt;AutomationSource&gt;**](AutomationSource.md) | A collection of the source event types which evaluate the security automation set of rules. |  [optional] |



