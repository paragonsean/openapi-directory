

# VirtualMachineScaleSetVMProfile

Describes a virtual machine scale set virtual machine profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingProfile** | [**BillingProfile**](BillingProfile.md) |  |  [optional] |
|**diagnosticsProfile** | [**DiagnosticsProfile**](DiagnosticsProfile.md) |  |  [optional] |
|**evictionPolicy** | **EvictionPolicy** |  |  [optional] |
|**extensionProfile** | [**VirtualMachineScaleSetExtensionProfile**](VirtualMachineScaleSetExtensionProfile.md) |  |  [optional] |
|**licenseType** | **String** | Specifies that the image or disk that is being used was licensed on-premises. This element is only used for images that contain the Windows Server operating system. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; Windows_Client &lt;br&gt;&lt;br&gt; Windows_Server &lt;br&gt;&lt;br&gt; If this element is included in a request for an update, the value must match the initial value. This value cannot be updated. &lt;br&gt;&lt;br&gt; For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc&#x3D;%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) &lt;br&gt;&lt;br&gt; Minimum api-version: 2015-06-15 |  [optional] |
|**networkProfile** | [**VirtualMachineScaleSetNetworkProfile**](VirtualMachineScaleSetNetworkProfile.md) |  |  [optional] |
|**osProfile** | [**VirtualMachineScaleSetOSProfile**](VirtualMachineScaleSetOSProfile.md) |  |  [optional] |
|**priority** | **Priority** |  |  [optional] |
|**scheduledEventsProfile** | [**ScheduledEventsProfile**](ScheduledEventsProfile.md) |  |  [optional] |
|**storageProfile** | [**VirtualMachineScaleSetStorageProfile**](VirtualMachineScaleSetStorageProfile.md) |  |  [optional] |



