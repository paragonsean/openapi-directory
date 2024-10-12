

# ApplicationGatewayFrontendIPConfigurationPropertiesFormat

Properties of Frontend IP configuration of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateIPAddress** | **String** | PrivateIPAddress of the network interface IP Configuration. |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | IP address allocation method. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicIPAddress** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |
|**subnet** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



