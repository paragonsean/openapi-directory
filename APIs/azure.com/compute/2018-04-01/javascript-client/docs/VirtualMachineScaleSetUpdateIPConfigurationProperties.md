# ComputeManagementClient.VirtualMachineScaleSetUpdateIPConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationGatewayBackendAddressPools** | [**[SubResource]**](SubResource.md) | The application gateway backend address pools. | [optional] 
**loadBalancerBackendAddressPools** | [**[SubResource]**](SubResource.md) | The load balancer backend address pools. | [optional] 
**loadBalancerInboundNatPools** | [**[SubResource]**](SubResource.md) | The load balancer inbound nat pools. | [optional] 
**primary** | **Boolean** | Specifies the primary IP Configuration in case the network interface has more than one IP Configuration. | [optional] 
**privateIPAddressVersion** | **String** | Available from Api-Version 2017-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4.  Possible values are: &#39;IPv4&#39; and &#39;IPv6&#39;. | [optional] 
**publicIPAddressConfiguration** | [**VirtualMachineScaleSetUpdatePublicIPAddressConfiguration**](VirtualMachineScaleSetUpdatePublicIPAddressConfiguration.md) |  | [optional] 
**subnet** | [**ApiEntityReference**](ApiEntityReference.md) |  | [optional] 



## Enum: PrivateIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)




