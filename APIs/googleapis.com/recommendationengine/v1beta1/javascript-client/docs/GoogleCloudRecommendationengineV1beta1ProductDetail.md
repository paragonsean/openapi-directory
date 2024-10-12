# RecommendationsAiBeta.GoogleCloudRecommendationengineV1beta1ProductDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableQuantity** | **Number** | Optional. Quantity of the products in stock when a user event happens. Optional. If provided, this overrides the available quantity in Catalog for this event. and can only be set if &#x60;stock_status&#x60; is set to &#x60;IN_STOCK&#x60;. Note that if an item is out of stock, you must set the &#x60;stock_state&#x60; field to be &#x60;OUT_OF_STOCK&#x60;. Leaving this field unspecified / as zero is not sufficient to mark the item out of stock. | [optional] 
**currencyCode** | **String** | Optional. Currency code for price/costs. Use three-character ISO-4217 code. Required only if originalPrice or displayPrice is set. | [optional] 
**displayPrice** | **Number** | Optional. Display price of the product (e.g. discounted price). If provided, this will override the display price in Catalog for this product. | [optional] 
**id** | **String** | Required. Catalog item ID. UTF-8 encoded string with a length limit of 128 characters. | [optional] 
**itemAttributes** | [**GoogleCloudRecommendationengineV1beta1FeatureMap**](GoogleCloudRecommendationengineV1beta1FeatureMap.md) |  | [optional] 
**originalPrice** | **Number** | Optional. Original price of the product. If provided, this will override the original price in Catalog for this product. | [optional] 
**quantity** | **Number** | Optional. Quantity of the product associated with the user event. For example, this field will be 2 if two products are added to the shopping cart for &#x60;add-to-cart&#x60; event. Required for &#x60;add-to-cart&#x60;, &#x60;add-to-list&#x60;, &#x60;remove-from-cart&#x60;, &#x60;checkout-start&#x60;, &#x60;purchase-complete&#x60;, &#x60;refund&#x60; event types. | [optional] 
**stockState** | **String** | Optional. Item stock state. If provided, this overrides the stock state in Catalog for items in this event. | [optional] 



## Enum: StockStateEnum


* `STOCK_STATE_UNSPECIFIED` (value: `"STOCK_STATE_UNSPECIFIED"`)

* `IN_STOCK` (value: `"IN_STOCK"`)

* `OUT_OF_STOCK` (value: `"OUT_OF_STOCK"`)

* `PREORDER` (value: `"PREORDER"`)

* `BACKORDER` (value: `"BACKORDER"`)




