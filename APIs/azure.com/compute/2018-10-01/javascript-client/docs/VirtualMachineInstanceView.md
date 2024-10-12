# ComputeManagementClient.VirtualMachineInstanceView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootDiagnostics** | [**BootDiagnosticsInstanceView**](BootDiagnosticsInstanceView.md) |  | [optional] 
**computerName** | **String** | The computer name assigned to the virtual machine. | [optional] 
**disks** | [**[DiskInstanceView]**](DiskInstanceView.md) | The virtual machine disk information. | [optional] 
**extensions** | [**[VirtualMachineExtensionInstanceView]**](VirtualMachineExtensionInstanceView.md) | The extensions information. | [optional] 
**maintenanceRedeployStatus** | [**MaintenanceRedeployStatus**](MaintenanceRedeployStatus.md) |  | [optional] 
**osName** | **String** | The Operating System running on the virtual machine. | [optional] 
**osVersion** | **String** | The version of Operating System running on the virtual machine. | [optional] 
**platformFaultDomain** | **Number** | Specifies the fault domain of the virtual machine. | [optional] 
**platformUpdateDomain** | **Number** | Specifies the update domain of the virtual machine. | [optional] 
**rdpThumbPrint** | **String** | The Remote desktop certificate thumbprint. | [optional] 
**statuses** | [**[InstanceViewStatus]**](InstanceViewStatus.md) | The resource status information. | [optional] 
**vmAgent** | [**VirtualMachineAgentInstanceView**](VirtualMachineAgentInstanceView.md) |  | [optional] 


