

# ApplicationGatewayRequestRoutingRulePropertiesFormat

Properties of request routing rule of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendAddressPool** | **Model0** |  |  [optional] |
|**backendHttpSettings** | **Model0** |  |  [optional] |
|**httpListener** | **Model0** |  |  [optional] |
|**provisioningState** | **String** | Provisioning state of the request routing rule resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**redirectConfiguration** | **Model0** |  |  [optional] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | Rule type. |  [optional] |
|**urlPathMap** | **Model0** |  |  [optional] |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| PATH_BASED_ROUTING | &quot;PathBasedRouting&quot; |



