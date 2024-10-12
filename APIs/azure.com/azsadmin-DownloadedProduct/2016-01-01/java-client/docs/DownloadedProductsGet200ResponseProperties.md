

# DownloadedProductsGet200ResponseProperties

Properties for aggregate usage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**galleryPackageBlobSasUri** | **String** | The URI to the .azpkg file that provides information required for showing product in the gallery. |  [optional] [readonly] |
|**legalTerms** | **String** | Legal terms for the product. |  [optional] |
|**links** | [**List&lt;DownloadedProductsGet200ResponsePropertiesLinksInner&gt;**](DownloadedProductsGet200ResponsePropertiesLinksInner.md) | List of product links. |  [optional] |
|**privacyPolicy** | **String** | Privacy policy of the product. |  [optional] |
|**productDetailsProperties** | **Object** | Product information. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] |
|**vmExtensionType** | **String** | Extension type of the VM. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| DOWNLOADING | &quot;Downloading&quot; |



