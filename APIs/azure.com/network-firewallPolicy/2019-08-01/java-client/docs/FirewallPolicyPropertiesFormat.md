

# FirewallPolicyPropertiesFormat

Firewall Policy definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basePolicy** | [**FirewallPolicyPropertiesFormatBasePolicy**](FirewallPolicyPropertiesFormatBasePolicy.md) |  |  [optional] |
|**childPolicies** | [**List&lt;FirewallPolicyPropertiesFormatBasePolicy&gt;**](FirewallPolicyPropertiesFormatBasePolicy.md) | List of references to Child Firewall Policies. |  [optional] [readonly] |
|**firewalls** | [**List&lt;FirewallPolicyPropertiesFormatBasePolicy&gt;**](FirewallPolicyPropertiesFormatBasePolicy.md) | List of references to Azure Firewalls that this Firewall Policy is associated with. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**ruleGroups** | [**List&lt;FirewallPolicyPropertiesFormatBasePolicy&gt;**](FirewallPolicyPropertiesFormatBasePolicy.md) | List of references to FirewallPolicyRuleGroups. |  [optional] [readonly] |
|**threatIntelMode** | [**ThreatIntelModeEnum**](#ThreatIntelModeEnum) | The operation mode for Threat Intel. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: ThreatIntelModeEnum

| Name | Value |
|---- | -----|
| ALERT | &quot;Alert&quot; |
| DENY | &quot;Deny&quot; |
| OFF | &quot;Off&quot; |



