

# SaveSuggestionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableQuantity** | **Integer** |  |  |
|**brandName** | **String** | Name of the brand to which this SKU belongs. It must match the brand created in the marketplace. |  |
|**categoryFullPath** | **String** | Full path to the SKU&#39;s category. It should be written as {department}/{category}. For example: if the department is **Appliances** and the category is **Oven**, the full path should be &#39;Appliances/Oven&#39;. |  |
|**EAN** | **String** | SKU reference code. Mandatory if the RefId is not informed. |  |
|**height** | **Integer** | Height of the SKU. |  |
|**images** | [**List&lt;Image&gt;**](Image.md) | Array containing the URLs and names the SKU images. |  |
|**length** | **Integer** | Length of the SKU. |  |
|**measurementUnit** | **String** | Measurement unit that should be used for this SKU. If this information doesn&#39;t apply, you should use the default value &#x60;un&#x60;. |  [optional] |
|**pricing** | [**SaveSuggestionRequestPricing**](SaveSuggestionRequestPricing.md) |  |  |
|**productDescription** | **String** | Product Description containing the main information about the product (not the SKU). |  |
|**productId** | **String** | Product ID in seller&#39;s account. |  |
|**productName** | **String** | Name of the suggested product. This field has a limit of 150 characters. |  |
|**productSpecifications** | [**List&lt;ProductSpecification&gt;**](ProductSpecification.md) | Array containing the names and values of the product specifications. |  [optional] |
|**refId** | **String** | SKU reference code. Mandotory if the EAN is not informed. |  |
|**sellerId** | **String** | ID of the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. |  |
|**sellerStockKeepingUnitId** | **Integer** | ID of the SKU registered in the seller. |  [optional] |
|**skuName** | **String** | Name of the suggested SKU. |  |
|**skuSpecifications** | [**List&lt;SkuSpecification&gt;**](SkuSpecification.md) | Array containing the names and values of the SKU specifications. |  [optional] |
|**unitMultiplier** | **Integer** | Unit multiplier for this SKU. If this information doesn&#39;t apply, you should use the default value &#x60;1&#x60;. |  [optional] |
|**weight** | **Integer** | Weight of the SKU in grams. |  |
|**width** | **Integer** | Width of the SKU. |  |



