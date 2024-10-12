# NetworkManagementClient.AzureFirewallApplicationRuleCollectionPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AzureFirewallRCAction**](AzureFirewallRCAction.md) |  | [optional] 
**priority** | **Number** | Priority of the application rule collection resource. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**rules** | [**[AzureFirewallApplicationRule]**](AzureFirewallApplicationRule.md) | Collection of rules used by a application rule collection. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




