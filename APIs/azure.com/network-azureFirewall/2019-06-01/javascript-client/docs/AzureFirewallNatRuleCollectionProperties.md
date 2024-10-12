# NetworkManagementClient.AzureFirewallNatRuleCollectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AzureFirewallNatRCAction**](AzureFirewallNatRCAction.md) |  | [optional] 
**priority** | **Number** | Priority of the NAT rule collection resource. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**rules** | [**[AzureFirewallNatRule]**](AzureFirewallNatRule.md) | Collection of rules used by a NAT rule collection. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




