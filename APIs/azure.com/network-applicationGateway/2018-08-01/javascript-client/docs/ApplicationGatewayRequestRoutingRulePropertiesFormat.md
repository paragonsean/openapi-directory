# NetworkManagementClient.ApplicationGatewayRequestRoutingRulePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendAddressPool** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  | [optional] 
**backendHttpSettings** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  | [optional] 
**httpListener** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state of the request routing rule resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**redirectConfiguration** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  | [optional] 
**ruleType** | **String** | Rule type. | [optional] 
**urlPathMap** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  | [optional] 



## Enum: RuleTypeEnum


* `Basic` (value: `"Basic"`)

* `PathBasedRouting` (value: `"PathBasedRouting"`)




