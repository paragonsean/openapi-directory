

# ApplicationGatewayRequestRoutingRulePropertiesFormat

Properties of request routing rule of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendAddressPool** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  |  [optional] |
|**backendHttpSettings** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  |  [optional] |
|**httpListener** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  |  [optional] |
|**provisioningState** | **String** | Provisioning state of the request routing rule resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**redirectConfiguration** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  |  [optional] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | Rule type. |  [optional] |
|**urlPathMap** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  |  [optional] |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| PATH_BASED_ROUTING | &quot;PathBasedRouting&quot; |



