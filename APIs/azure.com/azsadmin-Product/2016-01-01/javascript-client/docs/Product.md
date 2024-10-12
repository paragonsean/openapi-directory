# AzureBridgeAdminClient.Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legalTerms** | **String** | Legal terms for the product. | [optional] 
**links** | **[Object]** | List of product links. | [optional] 
**privacyPolicy** | **String** | Privacy policy of the product. | [optional] 
**provisioningState** | **String** | The provisioning state of the resource. | [optional] 
**vmExtensionType** | **String** | Extension type of the VM. | [optional] 
**billingPartNumber** | **String** | Billing part number. | [optional] 
**compatibility** | [**ProductAllOfCompatibility**](ProductAllOfCompatibility.md) |  | [optional] 
**description** | **String** | Description of the product. | [optional] 
**displayName** | **String** | Name displayed for the product. | [optional] 
**galleryItemIdentity** | **String** | Gallery item identity. | [optional] 
**iconUris** | [**ProductAllOfIconUris**](ProductAllOfIconUris.md) |  | [optional] 
**offer** | **String** | Offer name. | [optional] 
**offerVersion** | **String** | Offer version. | [optional] 
**payloadLength** | **Number** | Size in bytes. | [optional] 
**productKind** | **String** | The kind. E.g. VirtualMachineProductProperties.ProductKind or WebApp, SolutionTemplate. | [optional] 
**productProperties** | [**ProductAllOfProductProperties**](ProductAllOfProductProperties.md) |  | [optional] 
**publisherDisplayName** | **String** | Name of publisher. | [optional] 
**publisherIdentifier** | **String** | Publisher identifier. | [optional] 
**sku** | **String** | Product SKU. | [optional] 



## Enum: ProvisioningStateEnum


* `Stopped` (value: `"Stopped"`)

* `Starting` (value: `"Starting"`)

* `Running` (value: `"Running"`)

* `Stopping` (value: `"Stopping"`)

* `Succeeded` (value: `"Succeeded"`)

* `Downloading` (value: `"Downloading"`)




