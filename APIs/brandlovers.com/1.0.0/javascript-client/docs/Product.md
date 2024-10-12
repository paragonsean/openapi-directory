# BrandLoversMarketplaceApiV1.Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[ProductAttribute]**](ProductAttribute.md) | List of &#x60;key&#x60; &#x60;value&#x60; attributes of this product. This is very important for search and SEO optmization. Include all relevant information | 
**brand** | **String** | Brand name | 
**categories** | **[String]** | Array of categories associated with this product | 
**description** | **String** | Product description. | 
**dimensions** | [**Dimensions**](Dimensions.md) |  | [optional] 
**giftWrap** | [**GiftWrap**](GiftWrap.md) |  | [optional] 
**gtin** | **[String]** | Array of product EAN and/or ISBN and/or ASIN codes | [optional] 
**images** | **[String]** | List of valid Product image URLs. HTTP or HTTPS are valid. HTTPS is prefered. | 
**price** | [**ProductPrice**](ProductPrice.md) |  | 
**productGroupId** | **String** | Unique Product Group ID. Products with the same &#x60;productGroupId&#x60; will be grouped and displayed as a unique entry. Use &#x60;productGroupId&#x60; to group diferent SKUs that represent diferent colors, sizes, capacities, etc.. | [optional] 
**productId** | **String** | Brand Lovers Product ID. Use this to suggest a product association. This field is optional. | [optional] 
**skuSellerId** | **String** | Unique Product Id (SKU) in the seller system | 
**stock** | **Number** | Number of products availble for sale from the seller. Each new successfull order will automatically reduce the number of products available. | 
**title** | **String** | Product name as advertised by manufacturer. This how the product will be displayed in the Marketplace | 
**videos** | **[String]** | List of videos de URLs associated with this product. HTTP or HTTPS are valid. HTTPS is prefered. | [optional] 


