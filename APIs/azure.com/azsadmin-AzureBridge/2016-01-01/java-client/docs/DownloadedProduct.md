

# DownloadedProduct

Properties for aggregate usage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**galleryPackageBlobSasUri** | **String** | The URI to the .azpkg file that provides information required for showing product in the gallery. |  [optional] [readonly] |
|**legalTerms** | **String** | Legal terms for the product. |  [optional] |
|**links** | [**List&lt;Object&gt;**](Object.md) | List of product links. |  [optional] |
|**privacyPolicy** | **String** | Privacy policy of the product. |  [optional] |
|**productDetailsProperties** | [**ExtendedProductProperties**](ExtendedProductProperties.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] |
|**vmExtensionType** | **String** | Extension type of the VM. |  [optional] |
|**billingPartNumber** | **String** | Billing part number. |  [optional] |
|**compatibility** | [**DownloadedProductAllOfCompatibility**](DownloadedProductAllOfCompatibility.md) |  |  [optional] |
|**description** | **String** | Description of the product. |  [optional] |
|**displayName** | **String** | Name displayed for the product. |  [optional] |
|**galleryItemIdentity** | **String** | Gallery item identity. |  [optional] |
|**iconUris** | [**DownloadedProductAllOfIconUris**](DownloadedProductAllOfIconUris.md) |  |  [optional] |
|**offer** | **String** | Offer name. |  [optional] |
|**offerVersion** | **String** | Offer version. |  [optional] |
|**payloadLength** | **Long** | Size in bytes. |  [optional] |
|**productKind** | **String** | The kind. E.g. VirtualMachineProductProperties.ProductKind or WebApp, SolutionTemplate. |  [optional] |
|**productProperties** | [**DownloadedProductAllOfProductProperties**](DownloadedProductAllOfProductProperties.md) |  |  [optional] |
|**publisherDisplayName** | **String** | Name of publisher. |  [optional] |
|**publisherIdentifier** | **String** | Publisher identifier. |  [optional] |
|**sku** | **String** | Product SKU. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| DOWNLOADING | &quot;Downloading&quot; |



