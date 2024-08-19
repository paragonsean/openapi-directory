# ComputeManagementClient.VirtualMachineInstanceView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootDiagnostics** | [**BootDiagnosticsInstanceView**](BootDiagnosticsInstanceView.md) |  | [optional] 
**disks** | [**[DiskInstanceView]**](DiskInstanceView.md) | The virtual machine disk information. | [optional] 
**extensions** | [**[VirtualMachineExtensionInstanceView]**](VirtualMachineExtensionInstanceView.md) | The extensions information. | [optional] 
**platformFaultDomain** | **Number** | Specifies the fault domain of the virtual machine. | [optional] 
**platformUpdateDomain** | **Number** | Specifies the update domain of the virtual machine. | [optional] 
**rdpThumbPrint** | **String** | The Remote desktop certificate thumbprint. | [optional] 
**statuses** | [**[InstanceViewStatus]**](InstanceViewStatus.md) | The resource status information. | [optional] 
**vmAgent** | [**VirtualMachineAgentInstanceView**](VirtualMachineAgentInstanceView.md) |  | [optional] 


