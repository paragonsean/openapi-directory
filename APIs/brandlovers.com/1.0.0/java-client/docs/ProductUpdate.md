

# ProductUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;ProductAttribute&gt;**](ProductAttribute.md) | List of &#x60;key&#x60; &#x60;value&#x60; attributes of this product. This is very important for search and SEO optmization. Include all relevant information |  [optional] |
|**brand** | **String** | Brand name |  [optional] |
|**categories** | **List&lt;String&gt;** | Array of categories associated with this product |  [optional] |
|**description** | **String** | Product text description. |  [optional] |
|**dimensions** | [**Dimensions**](Dimensions.md) |  |  [optional] |
|**giftWrap** | [**GiftWrap**](GiftWrap.md) |  |  [optional] |
|**gtin** | **List&lt;String&gt;** | Array of product EAN and/or ISBN and/or ASIN codes |  [optional] |
|**images** | **List&lt;String&gt;** | List of valid Product image URLs. HTTP or HTTPS are valid. HTTPS is prefered. |  [optional] |
|**price** | [**ProductPrice**](ProductPrice.md) |  |  [optional] |
|**productGroupId** | **String** | Unique Product Group ID. Products with the same &#x60;productGroupId&#x60; will be grouped and displayed as a unique entry. Use &#x60;productGroupId&#x60; to group diferent SKUs that represent diferent colors, sizes, capacities, etc.. |  [optional] |
|**productId** | **String** | Brand Lovers Product Id. Use this to recommend a product association |  [optional] |
|**skuSellerId** | **String** | Unique Product Id (SKU) in the seller system |  |
|**stock** | **Integer** | Number of products availble for sale from the seller. Each new successfull order will automatically reduce the number of products available. |  [optional] |
|**title** | **String** | Product name as advertised by manufacturer. This how the product will be displayed in the Marketplace |  [optional] |
|**videos** | **List&lt;String&gt;** | List of videos de URLs associated with this product. HTTP or HTTPS are valid. HTTPS is prefered. |  [optional] |



