

# FirewallPolicyRuleGroupProperties

Properties of the rule group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**priority** | **Integer** | Priority of the Firewall Policy Rule Group resource. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**rules** | [**List&lt;FirewallPolicyRule&gt;**](FirewallPolicyRule.md) | Group of Firewall Policy rules. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



