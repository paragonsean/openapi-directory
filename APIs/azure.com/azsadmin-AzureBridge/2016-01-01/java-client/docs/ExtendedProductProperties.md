

# ExtendedProductProperties

Product information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeRole** | **ComputeRole** |  |  [optional] |
|**isSystemExtension** | **Boolean** | Specifies if product is a Virtual Machine Extension. |  [optional] [readonly] |
|**sourceBlob** | [**Uri**](Uri.md) |  |  [optional] |
|**supportMultipleExtensions** | **Boolean** | Indicates if specified product supports multiple extensions. |  [optional] [readonly] |
|**version** | **String** | Specifies product version. |  [optional] [readonly] |
|**vmOsType** | **OperatingSystem** |  |  [optional] |
|**vmScaleSetEnabled** | **Boolean** | Indicates if virtual machine Scale Set is enabled in the specified product. |  [optional] [readonly] |
|**dataDiskImages** | [**List&lt;DataDiskImage&gt;**](DataDiskImage.md) | List of attached data disks. |  [optional] [readonly] |
|**osDiskImage** | [**OsDiskImage**](OsDiskImage.md) |  |  [optional] |



