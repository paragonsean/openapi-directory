

# VirtualMachineScaleSetUpdateOSProfile

Describes a virtual machine scale set OS profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customData** | **String** | A base-64 encoded string of custom data. |  [optional] |
|**linuxConfiguration** | [**LinuxConfiguration**](LinuxConfiguration.md) |  |  [optional] |
|**secrets** | [**List&lt;VaultSecretGroup&gt;**](VaultSecretGroup.md) | The List of certificates for addition to the VM. |  [optional] |
|**windowsConfiguration** | [**WindowsConfiguration**](WindowsConfiguration.md) |  |  [optional] |



