# ComputeManagementClient.VirtualMachineScaleSetVMInstanceView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootDiagnostics** | [**BootDiagnosticsInstanceView**](BootDiagnosticsInstanceView.md) |  | [optional] 
**disks** | [**[DiskInstanceView]**](DiskInstanceView.md) | The disks information. | [optional] 
**extensions** | [**[VirtualMachineExtensionInstanceView]**](VirtualMachineExtensionInstanceView.md) | The extensions information. | [optional] 
**placementGroupId** | **String** | The placement group in which the VM is running. If the VM is deallocated it will not have a placementGroupId. | [optional] 
**platformFaultDomain** | **Number** | The Fault Domain count. | [optional] 
**platformUpdateDomain** | **Number** | The Update Domain count. | [optional] 
**rdpThumbPrint** | **String** | The Remote desktop certificate thumbprint. | [optional] 
**statuses** | [**[InstanceViewStatus]**](InstanceViewStatus.md) | The resource status information. | [optional] 
**vmAgent** | [**VirtualMachineAgentInstanceView**](VirtualMachineAgentInstanceView.md) |  | [optional] 


