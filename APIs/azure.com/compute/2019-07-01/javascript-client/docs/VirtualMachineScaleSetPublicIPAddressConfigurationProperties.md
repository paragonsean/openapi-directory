# ComputeManagementClient.VirtualMachineScaleSetPublicIPAddressConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsSettings** | [**VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings**](VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings.md) |  | [optional] 
**idleTimeoutInMinutes** | **Number** | The idle timeout of the public IP address. | [optional] 
**ipTags** | [**[VirtualMachineScaleSetIpTag]**](VirtualMachineScaleSetIpTag.md) | The list of IP tags associated with the public IP address. | [optional] 
**publicIPAddressVersion** | **String** | Available from Api-Version 2019-07-01 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4. Possible values are: &#39;IPv4&#39; and &#39;IPv6&#39;. | [optional] 
**publicIPPrefix** | [**SubResource**](SubResource.md) |  | [optional] 



## Enum: PublicIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)




