# AzureBridgeAdminClient.DownloadedProductsGet200ResponseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**galleryPackageBlobSasUri** | **String** | The URI to the .azpkg file that provides information required for showing product in the gallery. | [optional] [readonly] 
**legalTerms** | **String** | Legal terms for the product. | [optional] 
**links** | [**[DownloadedProductsGet200ResponsePropertiesLinksInner]**](DownloadedProductsGet200ResponsePropertiesLinksInner.md) | List of product links. | [optional] 
**privacyPolicy** | **String** | Privacy policy of the product. | [optional] 
**productDetailsProperties** | **Object** | Product information. | [optional] 
**provisioningState** | **String** | The provisioning state of the resource. | [optional] 
**vmExtensionType** | **String** | Extension type of the VM. | [optional] 



## Enum: ProvisioningStateEnum


* `Stopped` (value: `"Stopped"`)

* `Starting` (value: `"Starting"`)

* `Running` (value: `"Running"`)

* `Stopping` (value: `"Stopping"`)

* `Succeeded` (value: `"Succeeded"`)

* `Downloading` (value: `"Downloading"`)




