

# ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesApplicationGatewayBackendAddressPoolsInnerPropertiesBackendIPConfigurationsInnerProperties

Properties of IP configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationGatewayBackendAddressPools** | **List&lt;Items&gt;** | The reference of ApplicationGatewayBackendAddressPool resource. |  [optional] |
|**loadBalancerBackendAddressPools** | **List&lt;Items&gt;** | The reference of LoadBalancerBackendAddressPool resource. |  [optional] |
|**loadBalancerInboundNatRules** | **List&lt;Items&gt;** | A list of references of LoadBalancerInboundNatRules. |  [optional] |
|**primary** | **Boolean** | Gets whether this is a primary customer address on the network interface. |  [optional] |
|**privateIPAddress** | **String** |  |  [optional] |
|**privateIPAddressVersion** | [**PrivateIPAddressVersionEnum**](#PrivateIPAddressVersionEnum) | Available from Api-Version 2016-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4.  Possible values are: &#39;IPv4&#39; and &#39;IPv6&#39;. |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | Defines how a private IP address is assigned. Possible values are: &#39;Static&#39; and &#39;Dynamic&#39;. |  [optional] |
|**provisioningState** | **String** |  |  [optional] |
|**publicIPAddress** | **PublicIPAddress** |  |  [optional] |
|**subnet** | **Subnet** |  |  [optional] |



## Enum: PrivateIPAddressVersionEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;IPv4&quot; |
| IPV6 | &quot;IPv6&quot; |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



