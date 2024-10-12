

# ApplicationGatewayFirewallRuleSetPropertiesFormat

Properties of the web application firewall rule set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**ruleGroups** | [**List&lt;ApplicationGatewayFirewallRuleGroup&gt;**](ApplicationGatewayFirewallRuleGroup.md) | The rule groups of the web application firewall rule set. |  |
|**ruleSetType** | **String** | The type of the web application firewall rule set. |  |
|**ruleSetVersion** | **String** | The version of the web application firewall rule set type. |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



