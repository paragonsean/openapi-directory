# NetworkManagementClient.ApplicationGatewayRequestRoutingRulePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendAddressPool** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**backendHttpSettings** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**httpListener** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state of the request routing rule resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**redirectConfiguration** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**rewriteRuleSet** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**ruleType** | **String** | Rule type. | [optional] 
**urlPathMap** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 



## Enum: RuleTypeEnum


* `Basic` (value: `"Basic"`)

* `PathBasedRouting` (value: `"PathBasedRouting"`)




