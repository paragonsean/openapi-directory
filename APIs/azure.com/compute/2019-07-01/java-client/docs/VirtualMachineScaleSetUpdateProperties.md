

# VirtualMachineScaleSetUpdateProperties

Describes the properties of a Virtual Machine Scale Set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalCapabilities** | [**AdditionalCapabilities**](AdditionalCapabilities.md) |  |  [optional] |
|**automaticRepairsPolicy** | [**AutomaticRepairsPolicy**](AutomaticRepairsPolicy.md) |  |  [optional] |
|**doNotRunExtensionsOnOverprovisionedVMs** | **Boolean** | When Overprovision is enabled, extensions are launched only on the requested number of VMs which are finally kept. This property will hence ensure that the extensions do not run on the extra overprovisioned VMs. |  [optional] |
|**overprovision** | **Boolean** | Specifies whether the Virtual Machine Scale Set should be overprovisioned. |  [optional] |
|**proximityPlacementGroup** | [**SubResource**](SubResource.md) |  |  [optional] |
|**scaleInPolicy** | [**ScaleInPolicy**](ScaleInPolicy.md) |  |  [optional] |
|**singlePlacementGroup** | **Boolean** | When true this limits the scale set to a single placement group, of max size 100 virtual machines. |  [optional] |
|**upgradePolicy** | [**UpgradePolicy**](UpgradePolicy.md) |  |  [optional] |
|**virtualMachineProfile** | [**VirtualMachineScaleSetUpdateVMProfile**](VirtualMachineScaleSetUpdateVMProfile.md) |  |  [optional] |



