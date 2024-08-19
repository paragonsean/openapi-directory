

# VirtualMachineScaleSetUpdateNetworkConfigurationProperties

Describes a virtual machine scale set updatable network profile's IP configuration.Use this object for updating network profile's IP Configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsSettings** | [**VirtualMachineScaleSetNetworkConfigurationDnsSettings**](VirtualMachineScaleSetNetworkConfigurationDnsSettings.md) |  |  [optional] |
|**enableAcceleratedNetworking** | **Boolean** | Specifies whether the network interface is accelerated networking-enabled. |  [optional] |
|**ipConfigurations** | [**List&lt;VirtualMachineScaleSetUpdateIPConfiguration&gt;**](VirtualMachineScaleSetUpdateIPConfiguration.md) | The virtual machine scale set IP Configuration. |  [optional] |
|**networkSecurityGroup** | [**SubResource**](SubResource.md) |  |  [optional] |
|**primary** | **Boolean** | Whether this is a primary NIC on a virtual machine. |  [optional] |



