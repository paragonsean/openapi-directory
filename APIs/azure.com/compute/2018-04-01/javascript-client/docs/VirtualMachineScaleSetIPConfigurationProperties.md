# ComputeManagementClient.VirtualMachineScaleSetIPConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationGatewayBackendAddressPools** | [**[SubResource]**](SubResource.md) | Specifies an array of references to backend address pools of application gateways. A scale set can reference backend address pools of multiple application gateways. Multiple scale sets cannot use the same application gateway. | [optional] 
**loadBalancerBackendAddressPools** | [**[SubResource]**](SubResource.md) | Specifies an array of references to backend address pools of load balancers. A scale set can reference backend address pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer. | [optional] 
**loadBalancerInboundNatPools** | [**[SubResource]**](SubResource.md) | Specifies an array of references to inbound Nat pools of the load balancers. A scale set can reference inbound nat pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer | [optional] 
**primary** | **Boolean** | Specifies the primary network interface in case the virtual machine has more than 1 network interface. | [optional] 
**privateIPAddressVersion** | **String** | Available from Api-Version 2017-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4.  Possible values are: &#39;IPv4&#39; and &#39;IPv6&#39;. | [optional] 
**publicIPAddressConfiguration** | [**VirtualMachineScaleSetPublicIPAddressConfiguration**](VirtualMachineScaleSetPublicIPAddressConfiguration.md) |  | [optional] 
**subnet** | [**ApiEntityReference**](ApiEntityReference.md) |  | [optional] 



## Enum: PrivateIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)




