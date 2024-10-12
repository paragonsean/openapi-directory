# NetworkManagementClient.ApplicationGatewayWebApplicationFirewallConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabledRuleGroups** | [**[ApplicationGatewayFirewallDisabledRuleGroup]**](ApplicationGatewayFirewallDisabledRuleGroup.md) | The disabled rule groups. | [optional] 
**enabled** | **Boolean** | Whether the web application firewall is enabled or not. | 
**exclusions** | [**[ApplicationGatewayFirewallExclusion]**](ApplicationGatewayFirewallExclusion.md) | The exclusion list. | [optional] 
**fileUploadLimitInMb** | **Number** | Maximum file upload size in Mb for WAF. | [optional] 
**firewallMode** | **String** | Web application firewall mode. | 
**maxRequestBodySize** | **Number** | Maximum request body size for WAF. | [optional] 
**maxRequestBodySizeInKb** | **Number** | Maximum request body size in Kb for WAF. | [optional] 
**requestBodyCheck** | **Boolean** | Whether allow WAF to check request Body. | [optional] 
**ruleSetType** | **String** | The type of the web application firewall rule set. Possible values are: &#39;OWASP&#39;. | 
**ruleSetVersion** | **String** | The version of the rule set type. | 



## Enum: FirewallModeEnum


* `Detection` (value: `"Detection"`)

* `Prevention` (value: `"Prevention"`)




