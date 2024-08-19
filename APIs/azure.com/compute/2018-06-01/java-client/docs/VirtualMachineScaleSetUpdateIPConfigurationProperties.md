

# VirtualMachineScaleSetUpdateIPConfigurationProperties

Describes a virtual machine scale set network profile's IP configuration properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationGatewayBackendAddressPools** | [**List&lt;SubResource&gt;**](SubResource.md) | The application gateway backend address pools. |  [optional] |
|**applicationSecurityGroups** | [**List&lt;SubResource&gt;**](SubResource.md) | Specifies an array of references to application security group. |  [optional] |
|**loadBalancerBackendAddressPools** | [**List&lt;SubResource&gt;**](SubResource.md) | The load balancer backend address pools. |  [optional] |
|**loadBalancerInboundNatPools** | [**List&lt;SubResource&gt;**](SubResource.md) | The load balancer inbound nat pools. |  [optional] |
|**primary** | **Boolean** | Specifies the primary IP Configuration in case the network interface has more than one IP Configuration. |  [optional] |
|**privateIPAddressVersion** | [**PrivateIPAddressVersionEnum**](#PrivateIPAddressVersionEnum) | Available from Api-Version 2017-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4.  Possible values are: &#39;IPv4&#39; and &#39;IPv6&#39;. |  [optional] |
|**publicIPAddressConfiguration** | [**VirtualMachineScaleSetUpdatePublicIPAddressConfiguration**](VirtualMachineScaleSetUpdatePublicIPAddressConfiguration.md) |  |  [optional] |
|**subnet** | [**ApiEntityReference**](ApiEntityReference.md) |  |  [optional] |



## Enum: PrivateIPAddressVersionEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;IPv4&quot; |
| IPV6 | &quot;IPv6&quot; |



