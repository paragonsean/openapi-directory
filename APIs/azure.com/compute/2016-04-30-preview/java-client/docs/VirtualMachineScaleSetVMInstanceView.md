

# VirtualMachineScaleSetVMInstanceView

The instance view of a virtual machine scale set VM.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootDiagnostics** | [**BootDiagnosticsInstanceView**](BootDiagnosticsInstanceView.md) |  |  [optional] |
|**disks** | [**List&lt;DiskInstanceView&gt;**](DiskInstanceView.md) | The disks information. |  [optional] |
|**extensions** | [**List&lt;VirtualMachineExtensionInstanceView&gt;**](VirtualMachineExtensionInstanceView.md) | The extensions information. |  [optional] |
|**placementGroupId** | **String** | The placement group in which the VM is running. If the VM is deallocated it will not have a placementGroupId. |  [optional] |
|**platformFaultDomain** | **Integer** | The Fault Domain count. |  [optional] |
|**platformUpdateDomain** | **Integer** | The Update Domain count. |  [optional] |
|**rdpThumbPrint** | **String** | The Remote desktop certificate thumbprint. |  [optional] |
|**statuses** | [**List&lt;InstanceViewStatus&gt;**](InstanceViewStatus.md) | The resource status information. |  [optional] |
|**vmAgent** | [**VirtualMachineAgentInstanceView**](VirtualMachineAgentInstanceView.md) |  |  [optional] |



