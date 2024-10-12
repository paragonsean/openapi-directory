

# ApplicationGatewayWebApplicationFirewallConfiguration

Application gateway web application firewall configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disabledRuleGroups** | [**List&lt;ApplicationGatewayFirewallDisabledRuleGroup&gt;**](ApplicationGatewayFirewallDisabledRuleGroup.md) | The disabled rule groups. |  [optional] |
|**enabled** | **Boolean** | Whether the web application firewall is enabled or not. |  |
|**firewallMode** | [**FirewallModeEnum**](#FirewallModeEnum) | Web application firewall mode. |  |
|**ruleSetType** | **String** | The type of the web application firewall rule set. Possible values are: &#39;OWASP&#39;. |  |
|**ruleSetVersion** | **String** | The version of the rule set type. |  |



## Enum: FirewallModeEnum

| Name | Value |
|---- | -----|
| DETECTION | &quot;Detection&quot; |
| PREVENTION | &quot;Prevention&quot; |



