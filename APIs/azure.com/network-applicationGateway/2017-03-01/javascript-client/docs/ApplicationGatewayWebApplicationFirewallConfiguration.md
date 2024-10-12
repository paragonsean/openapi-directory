# NetworkManagementClient.ApplicationGatewayWebApplicationFirewallConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabledRuleGroups** | [**[ApplicationGatewayFirewallDisabledRuleGroup]**](ApplicationGatewayFirewallDisabledRuleGroup.md) | The disabled rule groups. | [optional] 
**enabled** | **Boolean** | Whether the web application firewall is enabled or not. | 
**firewallMode** | **String** | Web application firewall mode. | 
**ruleSetType** | **String** | The type of the web application firewall rule set. Possible values are: &#39;OWASP&#39;. | 
**ruleSetVersion** | **String** | The version of the rule set type. | 



## Enum: FirewallModeEnum


* `Detection` (value: `"Detection"`)

* `Prevention` (value: `"Prevention"`)




