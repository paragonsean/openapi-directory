# BeezUpMerchantApi.ChannelCatalogProductInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**productExists** | **Boolean** | Indicates if the product still exists in your catalog | 
**productId** | **String** | The product identifier | 
**productImageUrl** | **String** | The product image Url | [optional] 
**productSku** | **String** | The product SKU | 
**productTitle** | **String** | The product tile | 
**disabled** | **Boolean** | Indicates if the product has been disabled or not | [default to false]
**excluded** | **Boolean** | Indicates if the product has been excluded by a exclusion filter | [default to false]
**excludedBy** | **[String]** |  | [optional] 
**links** | [**ChannelCatalogProductInfoLinks**](ChannelCatalogProductInfoLinks.md) |  | 
**overrides** | [**{String: ProductOverrideWithCatalogValue}**](ProductOverrideWithCatalogValue.md) | The key is the channel column identifier | 
**uncategorized** | **Boolean** | Indicates if the product&#39;s category has been NOT mapped to a channel category | 


