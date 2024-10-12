

# VirtualMachineScaleSetExtensionProperties

Describes the properties of a Virtual Machine Scale Set Extension.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoUpgradeMinorVersion** | **Boolean** | Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true. |  [optional] |
|**protectedSettings** | **Object** | The extension can contain either protectedSettings or protectedSettingsFromKeyVault or no protected settings at all. |  [optional] |
|**provisioningState** | **String** | The provisioning state, which only appears in the response. |  [optional] [readonly] |
|**publisher** | **String** | The name of the extension handler publisher. |  [optional] |
|**settings** | **Object** | Json formatted public settings for the extension. |  [optional] |
|**type** | **String** | Specifies the type of the extension; an example is \&quot;CustomScriptExtension\&quot;. |  [optional] |
|**typeHandlerVersion** | **String** | Specifies the version of the script handler. |  [optional] |



