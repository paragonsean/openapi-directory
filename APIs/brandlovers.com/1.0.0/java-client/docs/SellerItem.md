

# SellerItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;ProductAttribute&gt;**](ProductAttribute.md) |  |  |
|**brand** | **String** | Brand name |  |
|**dimensions** | [**Dimensions**](Dimensions.md) |  |  |
|**giftWrap** | [**GiftWrap**](GiftWrap.md) |  |  [optional] |
|**gtin** | **List&lt;String&gt;** | Array of product EAN and/or ISBN and/or ASIN codes |  [optional] |
|**images** | [**List&lt;Image&gt;**](Image.md) | List of valid Product image URLs. |  |
|**prices** | [**List&lt;ProductPrice&gt;**](ProductPrice.md) | Price information for each marketplace that this product is listed |  |
|**product** | [**ProductReference**](ProductReference.md) |  |  |
|**skuSellerId** | **String** | Unique Product Id (SKU) in the seller system |  |
|**status** | [**List&lt;SellerItemStatus&gt;**](SellerItemStatus.md) | Product status for each marketplace that this product is listed |  |
|**stocks** | [**List&lt;ControlledStock&gt;**](ControlledStock.md) | Invetory information for each marketplace that this product is listed |  |
|**title** | **String** | Product name as advertised by manufacturer. This how the product will be displayed in the Marketplace |  |
|**urls** | [**List&lt;ProductSiteReference&gt;**](ProductSiteReference.md) | List of URLs where the product is listed for sale |  [optional] |



