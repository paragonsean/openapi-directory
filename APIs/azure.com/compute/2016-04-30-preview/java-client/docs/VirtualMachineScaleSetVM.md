

# VirtualMachineScaleSetVM

Describes a virtual machine scale set virtual machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceId** | **String** | The virtual machine instance ID. |  [optional] [readonly] |
|**plan** | [**Plan**](Plan.md) |  |  [optional] |
|**properties** | [**VirtualMachineScaleSetVMProperties**](VirtualMachineScaleSetVMProperties.md) |  |  [optional] |
|**resources** | [**List&lt;VirtualMachineExtension&gt;**](VirtualMachineExtension.md) | The virtual machine child extension resources. |  [optional] [readonly] |
|**sku** | [**Sku**](Sku.md) |  |  [optional] |
|**id** | **String** | Resource Id |  [optional] [readonly] |
|**location** | **String** | Resource location |  |
|**name** | **String** | Resource name |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Resource tags |  [optional] |
|**type** | **String** | Resource type |  [optional] [readonly] |



