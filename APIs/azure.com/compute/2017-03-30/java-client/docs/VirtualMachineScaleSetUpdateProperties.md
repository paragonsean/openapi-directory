

# VirtualMachineScaleSetUpdateProperties

Describes the properties of a Virtual Machine Scale Set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**overprovision** | **Boolean** | Specifies whether the Virtual Machine Scale Set should be overprovisioned. |  [optional] |
|**singlePlacementGroup** | **Boolean** | When true this limits the scale set to a single placement group, of max size 100 virtual machines. |  [optional] |
|**upgradePolicy** | [**UpgradePolicy**](UpgradePolicy.md) |  |  [optional] |
|**virtualMachineProfile** | [**VirtualMachineScaleSetUpdateVMProfile**](VirtualMachineScaleSetUpdateVMProfile.md) |  |  [optional] |



