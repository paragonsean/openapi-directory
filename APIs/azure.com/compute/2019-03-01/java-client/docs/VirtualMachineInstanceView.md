

# VirtualMachineInstanceView

The instance view of a virtual machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootDiagnostics** | [**BootDiagnosticsInstanceView**](BootDiagnosticsInstanceView.md) |  |  [optional] |
|**computerName** | **String** | The computer name assigned to the virtual machine. |  [optional] |
|**disks** | [**List&lt;DiskInstanceView&gt;**](DiskInstanceView.md) | The virtual machine disk information. |  [optional] |
|**extensions** | [**List&lt;VirtualMachineExtensionInstanceView&gt;**](VirtualMachineExtensionInstanceView.md) | The extensions information. |  [optional] |
|**hyperVGeneration** | [**HyperVGenerationEnum**](#HyperVGenerationEnum) | Specifies the HyperVGeneration Type associated with a resource |  [optional] |
|**maintenanceRedeployStatus** | [**MaintenanceRedeployStatus**](MaintenanceRedeployStatus.md) |  |  [optional] |
|**osName** | **String** | The Operating System running on the virtual machine. |  [optional] |
|**osVersion** | **String** | The version of Operating System running on the virtual machine. |  [optional] |
|**platformFaultDomain** | **Integer** | Specifies the fault domain of the virtual machine. |  [optional] |
|**platformUpdateDomain** | **Integer** | Specifies the update domain of the virtual machine. |  [optional] |
|**rdpThumbPrint** | **String** | The Remote desktop certificate thumbprint. |  [optional] |
|**statuses** | [**List&lt;InstanceViewStatus&gt;**](InstanceViewStatus.md) | The resource status information. |  [optional] |
|**vmAgent** | [**VirtualMachineAgentInstanceView**](VirtualMachineAgentInstanceView.md) |  |  [optional] |



## Enum: HyperVGenerationEnum

| Name | Value |
|---- | -----|
| V1 | &quot;V1&quot; |
| V2 | &quot;V2&quot; |



