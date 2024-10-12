# BrandLoversMarketplaceApiV1.SellerItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[ProductAttribute]**](ProductAttribute.md) |  | 
**brand** | **String** | Brand name | 
**dimensions** | [**Dimensions**](Dimensions.md) |  | 
**giftWrap** | [**GiftWrap**](GiftWrap.md) |  | [optional] 
**gtin** | **[String]** | Array of product EAN and/or ISBN and/or ASIN codes | [optional] 
**images** | [**[Image]**](Image.md) | List of valid Product image URLs. | 
**prices** | [**[ProductPrice]**](ProductPrice.md) | Price information for each marketplace that this product is listed | 
**product** | [**ProductReference**](ProductReference.md) |  | 
**skuSellerId** | **String** | Unique Product Id (SKU) in the seller system | 
**status** | [**[SellerItemStatus]**](SellerItemStatus.md) | Product status for each marketplace that this product is listed | 
**stocks** | [**[ControlledStock]**](ControlledStock.md) | Invetory information for each marketplace that this product is listed | 
**title** | **String** | Product name as advertised by manufacturer. This how the product will be displayed in the Marketplace | 
**urls** | [**[ProductSiteReference]**](ProductSiteReference.md) | List of URLs where the product is listed for sale | [optional] 


