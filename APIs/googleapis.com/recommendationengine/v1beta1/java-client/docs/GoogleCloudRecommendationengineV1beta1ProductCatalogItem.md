

# GoogleCloudRecommendationengineV1beta1ProductCatalogItem

ProductCatalogItem captures item metadata specific to retail products.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableQuantity** | **String** | Optional. The available quantity of the item. |  [optional] |
|**canonicalProductUri** | **String** | Optional. Canonical URL directly linking to the item detail page with a length limit of 5 KiB.. |  [optional] |
|**costs** | **Map&lt;String, Float&gt;** | Optional. A map to pass the costs associated with the product. For example: {\&quot;manufacturing\&quot;: 45.5} The profit of selling this item is computed like so: * If &#39;exactPrice&#39; is provided, profit &#x3D; displayPrice - sum(costs) * If &#39;priceRange&#39; is provided, profit &#x3D; minPrice - sum(costs) |  [optional] |
|**currencyCode** | **String** | Optional. Only required if the price is set. Currency code for price/costs. Use three-character ISO-4217 code. |  [optional] |
|**exactPrice** | [**GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice**](GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice.md) |  |  [optional] |
|**images** | [**List&lt;GoogleCloudRecommendationengineV1beta1Image&gt;**](GoogleCloudRecommendationengineV1beta1Image.md) | Optional. Product images for the catalog item. |  [optional] |
|**priceRange** | [**GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange**](GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange.md) |  |  [optional] |
|**stockState** | [**StockStateEnum**](#StockStateEnum) | Optional. Online stock state of the catalog item. Default is &#x60;IN_STOCK&#x60;. |  [optional] |



## Enum: StockStateEnum

| Name | Value |
|---- | -----|
| STOCK_STATE_UNSPECIFIED | &quot;STOCK_STATE_UNSPECIFIED&quot; |
| IN_STOCK | &quot;IN_STOCK&quot; |
| OUT_OF_STOCK | &quot;OUT_OF_STOCK&quot; |
| PREORDER | &quot;PREORDER&quot; |
| BACKORDER | &quot;BACKORDER&quot; |



