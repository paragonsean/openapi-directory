

# VirtualMachineScaleSetReimageParameters

Describes a Virtual Machine Scale Set VM Reimage Parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceIds** | **List&lt;String&gt;** | The virtual machine scale set instance ids. Omitting the virtual machine scale set instance ids will result in the operation being performed on all virtual machines in the virtual machine scale set. |  [optional] |
|**tempDisk** | **Boolean** | Specifies whether to reimage temp disk. Default value: false. Note: This temp disk reimage parameter is only supported for VM/VMSS with Ephemeral OS disk. |  [optional] |



