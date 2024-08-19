

# VirtualMachineScaleSetExtensionProperties

Describes the properties of a Virtual Machine Scale Set Extension.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoUpgradeMinorVersion** | **Boolean** | Whether the extension handler should be automatically upgraded across minor versions. |  [optional] |
|**protectedSettings** | **Object** | Json formatted protected settings for the extension. |  [optional] |
|**provisioningState** | **String** | The provisioning state, which only appears in the response. |  [optional] [readonly] |
|**publisher** | **String** | The name of the extension handler publisher. |  [optional] |
|**settings** | **Object** | Json formatted public settings for the extension. |  [optional] |
|**type** | **String** | The type of the extension handler. |  [optional] |
|**typeHandlerVersion** | **String** | The type version of the extension handler. |  [optional] |



