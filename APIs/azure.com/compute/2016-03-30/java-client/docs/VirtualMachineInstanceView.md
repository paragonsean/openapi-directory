

# VirtualMachineInstanceView

The instance view of a virtual machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootDiagnostics** | [**BootDiagnosticsInstanceView**](BootDiagnosticsInstanceView.md) |  |  [optional] |
|**disks** | [**List&lt;DiskInstanceView&gt;**](DiskInstanceView.md) | The virtual machine disk information. |  [optional] |
|**extensions** | [**List&lt;VirtualMachineExtensionInstanceView&gt;**](VirtualMachineExtensionInstanceView.md) | The extensions information. |  [optional] |
|**platformFaultDomain** | **Integer** | Specifies the fault domain of the virtual machine. |  [optional] |
|**platformUpdateDomain** | **Integer** | Specifies the update domain of the virtual machine. |  [optional] |
|**rdpThumbPrint** | **String** | The Remote desktop certificate thumbprint. |  [optional] |
|**statuses** | [**List&lt;InstanceViewStatus&gt;**](InstanceViewStatus.md) | The resource status information. |  [optional] |
|**vmAgent** | [**VirtualMachineAgentInstanceView**](VirtualMachineAgentInstanceView.md) |  |  [optional] |



