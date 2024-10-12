# NetworkManagementClient.AzureFirewallNetworkRuleCollectionPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AzureFirewallRCAction**](AzureFirewallRCAction.md) |  | [optional] 
**priority** | **Number** | Priority of the network rule collection resource. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**rules** | [**[AzureFirewallNetworkRule]**](AzureFirewallNetworkRule.md) | Collection of rules used by a network rule collection. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




