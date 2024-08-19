

# VirtualMachineProperties

Describes the properties of a Virtual Machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilitySet** | [**SubResource**](SubResource.md) |  |  [optional] |
|**diagnosticsProfile** | [**DiagnosticsProfile**](DiagnosticsProfile.md) |  |  [optional] |
|**hardwareProfile** | [**HardwareProfile**](HardwareProfile.md) |  |  [optional] |
|**instanceView** | [**VirtualMachineInstanceView**](VirtualMachineInstanceView.md) |  |  [optional] |
|**licenseType** | **String** | Specifies that the image or disk that is being used was licensed on-premises. This element is only used for images that contain the Windows Server operating system. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; Windows_Client &lt;br&gt;&lt;br&gt; Windows_Server &lt;br&gt;&lt;br&gt; If this element is included in a request for an update, the value must match the initial value. This value cannot be updated. &lt;br&gt;&lt;br&gt; For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc&#x3D;%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) &lt;br&gt;&lt;br&gt; Minimum api-version: 2015-06-15 |  [optional] |
|**networkProfile** | [**NetworkProfile**](NetworkProfile.md) |  |  [optional] |
|**osProfile** | [**OSProfile**](OSProfile.md) |  |  [optional] |
|**provisioningState** | **String** | The provisioning state, which only appears in the response. |  [optional] [readonly] |
|**storageProfile** | [**StorageProfile**](StorageProfile.md) |  |  [optional] |



