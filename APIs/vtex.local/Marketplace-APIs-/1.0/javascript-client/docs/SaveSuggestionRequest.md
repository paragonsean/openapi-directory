# Suggestions.SaveSuggestionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableQuantity** | **Number** |  | 
**brandName** | **String** | Name of the brand to which this SKU belongs. It must match the brand created in the marketplace. | 
**categoryFullPath** | **String** | Full path to the SKU&#39;s category. It should be written as {department}/{category}. For example: if the department is **Appliances** and the category is **Oven**, the full path should be &#39;Appliances/Oven&#39;. | 
**EAN** | **String** | SKU reference code. Mandatory if the RefId is not informed. | [default to &#39;EAN10&#39;]
**height** | **Number** | Height of the SKU. | [default to 10]
**images** | [**[Image]**](Image.md) | Array containing the URLs and names the SKU images. | 
**length** | **Number** | Length of the SKU. | [default to 10]
**measurementUnit** | **String** | Measurement unit that should be used for this SKU. If this information doesn&#39;t apply, you should use the default value &#x60;un&#x60;. | [optional] 
**pricing** | [**SaveSuggestionRequestPricing**](SaveSuggestionRequestPricing.md) |  | 
**productDescription** | **String** | Product Description containing the main information about the product (not the SKU). | 
**productId** | **String** | Product ID in seller&#39;s account. | [default to &#39;1234&#39;]
**productName** | **String** | Name of the suggested product. This field has a limit of 150 characters. | [default to &#39;&#39;]
**productSpecifications** | [**[ProductSpecification]**](ProductSpecification.md) | Array containing the names and values of the product specifications. | [optional] 
**refId** | **String** | SKU reference code. Mandotory if the EAN is not informed. | [default to &#39;REF10&#39;]
**sellerId** | **String** | ID of the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to &#39;1&#39;]
**sellerStockKeepingUnitId** | **Number** | ID of the SKU registered in the seller. | [optional] 
**skuName** | **String** | Name of the suggested SKU. | 
**skuSpecifications** | [**[SkuSpecification]**](SkuSpecification.md) | Array containing the names and values of the SKU specifications. | [optional] 
**unitMultiplier** | **Number** | Unit multiplier for this SKU. If this information doesn&#39;t apply, you should use the default value &#x60;1&#x60;. | [optional] 
**weight** | **Number** | Weight of the SKU in grams. | [default to 100]
**width** | **Number** | Width of the SKU. | [default to 10]


