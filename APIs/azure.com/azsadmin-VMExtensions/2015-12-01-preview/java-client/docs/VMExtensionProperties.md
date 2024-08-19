

# VMExtensionProperties

Properties of a Virtual Machine Extension Image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeRole** | **String** | Compute role |  [optional] |
|**isSystemExtension** | **Boolean** | Indicates if the extension is for the system. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] |
|**sourceBlob** | [**AzureBlob**](AzureBlob.md) |  |  [optional] |
|**supportMultipleExtensions** | **Boolean** | True if supports multiple extensions. |  [optional] |
|**vmOsType** | [**VmOsTypeEnum**](#VmOsTypeEnum) | Operating system type. |  [optional] |
|**vmScaleSetEnabled** | **Boolean** | Value indicating whether the extension is enabled for virtual machine scale set support. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: VmOsTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



