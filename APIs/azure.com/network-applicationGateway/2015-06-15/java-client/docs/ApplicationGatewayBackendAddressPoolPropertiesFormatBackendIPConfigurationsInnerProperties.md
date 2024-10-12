

# ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerProperties

Properties of IP configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**loadBalancerBackendAddressPools** | [**List&lt;ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesLoadBalancerBackendAddressPoolsInner&gt;**](ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesLoadBalancerBackendAddressPoolsInner.md) | The reference of LoadBalancerBackendAddressPool resource. |  [optional] |
|**loadBalancerInboundNatRules** | [**List&lt;ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesLoadBalancerInboundNatRulesInner&gt;**](ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesLoadBalancerInboundNatRulesInner.md) | A list of references of LoadBalancerInboundNatRules. |  [optional] |
|**primary** | **Boolean** | Gets whether this is a primary customer address on the network interface. |  [optional] |
|**privateIPAddress** | **String** |  |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | Defines how a private IP address is assigned. Possible values are: &#39;Static&#39; and &#39;Dynamic&#39;. |  [optional] |
|**provisioningState** | **String** |  |  [optional] |
|**publicIPAddress** | [**ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesPublicIPAddress**](ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesPublicIPAddress.md) |  |  [optional] |
|**subnet** | [**ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnet**](ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnet.md) |  |  [optional] |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



