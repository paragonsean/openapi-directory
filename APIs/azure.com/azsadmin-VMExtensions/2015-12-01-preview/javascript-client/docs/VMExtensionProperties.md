# ComputeAdminClient.VMExtensionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computeRole** | **String** | Compute role | [optional] 
**isSystemExtension** | **Boolean** | Indicates if the extension is for the system. | [optional] 
**provisioningState** | **String** | The provisioning state of the resource. | [optional] 
**sourceBlob** | [**AzureBlob**](AzureBlob.md) |  | [optional] 
**supportMultipleExtensions** | **Boolean** | True if supports multiple extensions. | [optional] 
**vmOsType** | **String** | Operating system type. | [optional] 
**vmScaleSetEnabled** | **Boolean** | Value indicating whether the extension is enabled for virtual machine scale set support. | [optional] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Failed` (value: `"Failed"`)

* `Succeeded` (value: `"Succeeded"`)

* `Canceled` (value: `"Canceled"`)





## Enum: VmOsTypeEnum


* `Unknown` (value: `"Unknown"`)

* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)




