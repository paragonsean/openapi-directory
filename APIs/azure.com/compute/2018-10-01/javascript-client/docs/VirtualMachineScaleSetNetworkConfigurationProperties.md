# ComputeManagementClient.VirtualMachineScaleSetNetworkConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsSettings** | [**VirtualMachineScaleSetNetworkConfigurationDnsSettings**](VirtualMachineScaleSetNetworkConfigurationDnsSettings.md) |  | [optional] 
**enableAcceleratedNetworking** | **Boolean** | Specifies whether the network interface is accelerated networking-enabled. | [optional] 
**enableIPForwarding** | **Boolean** | Whether IP forwarding enabled on this NIC. | [optional] 
**ipConfigurations** | [**[VirtualMachineScaleSetIPConfiguration]**](VirtualMachineScaleSetIPConfiguration.md) | Specifies the IP configurations of the network interface. | 
**networkSecurityGroup** | [**SubResource**](SubResource.md) |  | [optional] 
**primary** | **Boolean** | Specifies the primary network interface in case the virtual machine has more than 1 network interface. | [optional] 


