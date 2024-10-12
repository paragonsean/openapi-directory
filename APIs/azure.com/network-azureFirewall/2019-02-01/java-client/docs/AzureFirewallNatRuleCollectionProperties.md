

# AzureFirewallNatRuleCollectionProperties

Properties of the NAT rule collection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**AzureFirewallNatRCAction**](AzureFirewallNatRCAction.md) |  |  [optional] |
|**priority** | **Integer** | Priority of the NAT rule collection resource. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**rules** | [**List&lt;AzureFirewallNatRule&gt;**](AzureFirewallNatRule.md) | Collection of rules used by a NAT rule collection. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



