# MarketplaceApi.GetMatchedOffersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brandId** | **Number** | Offer&#39;s brand ID that the product belongs to, configured in the Catalog. It should be the marketplace&#39;s brand chosen for the offer to be matched with. | [default to 2004291]
**categoryId** | **Number** | Offer&#39;s Category ID that the product belongs to, configured in the Catalog. It should be the marketplace&#39;s category chosen for the offer to be matched with. | [default to 1563]
**lastModified** | **String** | Last date the offer was modified. | [default to &#39;2021-05-06T21:37:24.262529&#39;]
**productId** | **String** | A string that identifies the seller&#39;s product. This is the ID that the marketplace will use for all references to this product. | [default to &#39;941947&#39;]
**productName** | **String** | Name of the offer&#39;s product. | [default to &#39;Name of the Product - 123&#39;]
**skus** | [**[Sku2]**](Sku2.md) | Array of SKUs in the offer. | 


