# NetworkManagementClient.FirewallPolicyPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basePolicy** | [**FirewallPolicyPropertiesFormatBasePolicy**](FirewallPolicyPropertiesFormatBasePolicy.md) |  | [optional] 
**childPolicies** | [**[FirewallPolicyPropertiesFormatBasePolicy]**](FirewallPolicyPropertiesFormatBasePolicy.md) | List of references to Child Firewall Policies | [optional] [readonly] 
**firewalls** | [**[FirewallPolicyPropertiesFormatBasePolicy]**](FirewallPolicyPropertiesFormatBasePolicy.md) | List of references to Azure Firewalls that this Firewall Policy is associated with | [optional] [readonly] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**ruleGroups** | [**[FirewallPolicyPropertiesFormatBasePolicy]**](FirewallPolicyPropertiesFormatBasePolicy.md) | List of references to FirewallPolicyRuleGroups | [optional] [readonly] 
**threatIntelMode** | **String** | The operation mode for Threat Intel. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)





## Enum: ThreatIntelModeEnum


* `Alert` (value: `"Alert"`)

* `Deny` (value: `"Deny"`)

* `Off` (value: `"Off"`)




