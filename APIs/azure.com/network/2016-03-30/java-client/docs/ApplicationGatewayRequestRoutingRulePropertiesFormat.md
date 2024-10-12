

# ApplicationGatewayRequestRoutingRulePropertiesFormat

Properties of Request routing rule of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendAddressPool** | [**SubResource**](SubResource.md) |  |  [optional] |
|**backendHttpSettings** | [**SubResource**](SubResource.md) |  |  [optional] |
|**httpListener** | [**SubResource**](SubResource.md) |  |  [optional] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the request routing rule resource Updating/Deleting/Failed |  [optional] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | Gets or sets the rule type |  [optional] |
|**urlPathMap** | [**SubResource**](SubResource.md) |  |  [optional] |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| PATH_BASED_ROUTING | &quot;PathBasedRouting&quot; |



