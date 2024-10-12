# RecommendationsAiBeta.GoogleCloudRecommendationengineV1beta1ProductCatalogItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableQuantity** | **String** | Optional. The available quantity of the item. | [optional] 
**canonicalProductUri** | **String** | Optional. Canonical URL directly linking to the item detail page with a length limit of 5 KiB.. | [optional] 
**costs** | **{String: Number}** | Optional. A map to pass the costs associated with the product. For example: {\&quot;manufacturing\&quot;: 45.5} The profit of selling this item is computed like so: * If &#39;exactPrice&#39; is provided, profit &#x3D; displayPrice - sum(costs) * If &#39;priceRange&#39; is provided, profit &#x3D; minPrice - sum(costs) | [optional] 
**currencyCode** | **String** | Optional. Only required if the price is set. Currency code for price/costs. Use three-character ISO-4217 code. | [optional] 
**exactPrice** | [**GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice**](GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice.md) |  | [optional] 
**images** | [**[GoogleCloudRecommendationengineV1beta1Image]**](GoogleCloudRecommendationengineV1beta1Image.md) | Optional. Product images for the catalog item. | [optional] 
**priceRange** | [**GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange**](GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange.md) |  | [optional] 
**stockState** | **String** | Optional. Online stock state of the catalog item. Default is &#x60;IN_STOCK&#x60;. | [optional] 



## Enum: StockStateEnum


* `STOCK_STATE_UNSPECIFIED` (value: `"STOCK_STATE_UNSPECIFIED"`)

* `IN_STOCK` (value: `"IN_STOCK"`)

* `OUT_OF_STOCK` (value: `"OUT_OF_STOCK"`)

* `PREORDER` (value: `"PREORDER"`)

* `BACKORDER` (value: `"BACKORDER"`)




