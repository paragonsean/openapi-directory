

# ApplicationGatewayRequestRoutingRulePropertiesFormat

Properties of request routing rule of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendAddressPool** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  |  [optional] |
|**backendHttpSettings** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  |  [optional] |
|**httpListener** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  |  [optional] |
|**provisioningState** | **String** | Provisioning state of the request routing rule resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | Rule type. Possible values are: &#39;Basic&#39; and &#39;PathBasedRouting&#39;. |  [optional] |
|**urlPathMap** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  |  [optional] |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| PATH_BASED_ROUTING | &quot;PathBasedRouting&quot; |



