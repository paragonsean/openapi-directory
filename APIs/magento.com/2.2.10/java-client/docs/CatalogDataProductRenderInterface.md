

# CatalogDataProductRenderInterface

Represents Data Object which holds enough information to render product This information is put into part as Add To Cart or Add to Compare Data or Price Data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addToCartButton** | [**CatalogDataProductRenderButtonInterface**](CatalogDataProductRenderButtonInterface.md) |  |  |
|**addToCompareButton** | [**CatalogDataProductRenderButtonInterface**](CatalogDataProductRenderButtonInterface.md) |  |  |
|**currencyCode** | **String** | Current or desired currency code to product |  |
|**extensionAttributes** | [**CatalogDataProductRenderExtensionInterface**](CatalogDataProductRenderExtensionInterface.md) |  |  |
|**id** | **Integer** | Product identifier |  |
|**images** | [**List&lt;CatalogDataProductRenderImageInterface&gt;**](CatalogDataProductRenderImageInterface.md) | Enough information, that needed to render image on front |  |
|**isSalable** | **String** | Information about product saleability (In Stock) |  |
|**name** | **String** | Product name |  |
|**priceInfo** | [**CatalogDataProductRenderPriceInfoInterface**](CatalogDataProductRenderPriceInfoInterface.md) |  |  |
|**storeId** | **Integer** | Information about current store id or requested store id |  |
|**type** | **String** | Product type. Such as bundle, grouped, simple, etc... |  |
|**url** | **String** | Product url |  |



