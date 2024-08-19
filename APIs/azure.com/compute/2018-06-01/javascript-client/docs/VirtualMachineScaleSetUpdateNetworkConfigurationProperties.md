# ComputeManagementClient.VirtualMachineScaleSetUpdateNetworkConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsSettings** | [**VirtualMachineScaleSetNetworkConfigurationDnsSettings**](VirtualMachineScaleSetNetworkConfigurationDnsSettings.md) |  | [optional] 
**enableAcceleratedNetworking** | **Boolean** | Specifies whether the network interface is accelerated networking-enabled. | [optional] 
**enableIPForwarding** | **Boolean** | Whether IP forwarding enabled on this NIC. | [optional] 
**ipConfigurations** | [**[VirtualMachineScaleSetUpdateIPConfiguration]**](VirtualMachineScaleSetUpdateIPConfiguration.md) | The virtual machine scale set IP Configuration. | [optional] 
**networkSecurityGroup** | [**SubResource**](SubResource.md) |  | [optional] 
**primary** | **Boolean** | Whether this is a primary NIC on a virtual machine. | [optional] 


