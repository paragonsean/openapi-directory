# CatalogApi.GetSKUandContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateIdValues** | **[String]** | Array with values of alternative SKU IDs. | 
**alternateIds** | [**AlternateIds**](AlternateIds.md) |  | 
**attachments** | [**[Attachment]**](Attachment.md) | Array with Attachments ID that are related to the SKU. | 
**brandId** | **String** | Product Brand ID. | 
**brandName** | **String** | Product Brand Name. | 
**cSCIdentification** | **String** | SKU Seller identification. | 
**categories** | **[String]** | Array with Categories from the related Product. | 
**collections** | **[String]** | Array with Collections ID that are related to the Product. | 
**commercialConditionId** | **Number** | SKU Commercial Condition ID. | 
**complementName** | **String** | Product Complement Name. | [optional] 
**detailUrl** | **String** | Product URL. | 
**dimension** | [**Dimension**](Dimension.md) |  | 
**estimatedDateArrival** | **String** | To add the product as pre-sale, enter the product estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format. You must take into consideration both the launch date and the freight calculation for the arrival date. | 
**id** | **Number** | SKU ID. | 
**imageUrl** | **String** | SKU image URL. | 
**images** | [**[Image]**](Image.md) | Array with SKU images. | 
**informationSource** | **String** | Information Source. | 
**isActive** | **Boolean** | Defines if the SKU is active or not. | 
**isGiftCardRecharge** | **Boolean** | Defines if the purchase will generate a reward. | 
**isInventoried** | **Boolean** |  | 
**isKit** | **Boolean** | Defines if the SKU is part of a bundle. | 
**isProductActive** | **Boolean** | Defines if the product is active or not. | [optional] 
**isTransported** | **Boolean** |  | 
**keyWords** | **String** | Keywords related to the product. | [optional] 
**kitItems** | **[String]** | Array with SKU IDs of bundle components. | 
**manufacturerCode** | **String** | Product Supplier ID. | 
**measurementUnit** | **String** | SKU Measurement Unit. | 
**modalType** | **String** | Modal Type. | 
**nameComplete** | **String** | Product Name and SKU Name concatenated. | 
**productCategories** | **{String: {String: String}}** | Object containing product categories. Structure: \&quot;{CategoryID}\&quot;: \&quot;{CategoryName}\&quot;. | 
**productCategoryIds** | **String** | Category Hierarchy with Category IDs. | 
**productClustersIds** | **String** | Product Clusters IDs. | 
**productDescription** | **String** | Product Description. HTML is allowed. | 
**productFinalScore** | **Number** | Product Final Score. | [optional] 
**productGlobalCategoryId** | **Number** | Global Category ID. | 
**productId** | **Number** | ID of the related Product. | 
**productIsVisible** | **Boolean** | Defines if the product is visible or not. | [optional] 
**productName** | **String** | Product Name. | 
**productRefId** | **String** | Reference ID of the related Product. | [optional] 
**productSpecifications** | [**[ProductSpecification]**](ProductSpecification.md) | Array with related Product Specifications. | 
**realDimension** | [**RealDimension**](RealDimension.md) |  | 
**releaseDate** | **String** | Release date of the product. | [optional] 
**rewardValue** | **Number** | Reward value related to the SKU. | 
**salesChannels** | **[Number]** | Array with the ID of all the Sales Channels that are related to the product. | 
**services** | **[String]** | Array with Service IDs that are related to the SKU. | 
**showIfNotAvailable** | **Boolean** | Defines if the product will be shown if it is not available. | [optional] 
**skuName** | **String** | SKU Name. | 
**skuSellers** | [**[SkuSeller]**](SkuSeller.md) | Array with SKU Sellers data. | 
**skuSpecifications** | [**[SkuSpecification]**](SkuSpecification.md) | Array with related SKU Specifications. | 
**taxCode** | **String** | SKU Tax Code. | [optional] 
**unitMultiplier** | **Number** | This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward. | 


