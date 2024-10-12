# ComputeManagementClient.VirtualMachineScaleSetProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalCapabilities** | [**AdditionalCapabilities**](AdditionalCapabilities.md) |  | [optional] 
**automaticRepairsPolicy** | [**AutomaticRepairsPolicy**](AutomaticRepairsPolicy.md) |  | [optional] 
**doNotRunExtensionsOnOverprovisionedVMs** | **Boolean** | When Overprovision is enabled, extensions are launched only on the requested number of VMs which are finally kept. This property will hence ensure that the extensions do not run on the extra overprovisioned VMs. | [optional] 
**overprovision** | **Boolean** | Specifies whether the Virtual Machine Scale Set should be overprovisioned. | [optional] 
**platformFaultDomainCount** | **Number** | Fault Domain count for each placement group. | [optional] 
**provisioningState** | **String** | The provisioning state, which only appears in the response. | [optional] [readonly] 
**proximityPlacementGroup** | [**SubResource**](SubResource.md) |  | [optional] 
**scaleInPolicy** | [**ScaleInPolicy**](ScaleInPolicy.md) |  | [optional] 
**singlePlacementGroup** | **Boolean** | When true this limits the scale set to a single placement group, of max size 100 virtual machines. | [optional] 
**uniqueId** | **String** | Specifies the ID which uniquely identifies a Virtual Machine Scale Set. | [optional] [readonly] 
**upgradePolicy** | [**UpgradePolicy**](UpgradePolicy.md) |  | [optional] 
**virtualMachineProfile** | [**VirtualMachineScaleSetVMProfile**](VirtualMachineScaleSetVMProfile.md) |  | [optional] 
**zoneBalance** | **Boolean** | Whether to force strictly even Virtual Machine distribution cross x-zones in case there is zone outage. | [optional] 


