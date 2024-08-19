

# VirtualMachineScaleSetProperties

Describes the properties of a Virtual Machine Scale Set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**overProvision** | **Boolean** | Specifies whether the Virtual Machine Scale Set should be overprovisioned. |  [optional] |
|**provisioningState** | **String** | The provisioning state, which only appears in the response. |  [optional] [readonly] |
|**singlePlacementGroup** | **Boolean** | When true this limits the scale set to a single placement group, of max size 100 virtual machines. |  [optional] |
|**upgradePolicy** | [**UpgradePolicy**](UpgradePolicy.md) |  |  [optional] |
|**virtualMachineProfile** | [**VirtualMachineScaleSetVMProfile**](VirtualMachineScaleSetVMProfile.md) |  |  [optional] |



