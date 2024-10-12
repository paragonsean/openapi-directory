# CatalogApi.GetSKUAltID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateIdValues** | **[String]** | Array with values of alternative SKU IDs. | 
**alternateIds** | [**AlternateIds**](AlternateIds.md) |  | 
**attachments** | [**[Attachment]**](Attachment.md) | Array with Attachments ID that are related to the SKU. | 
**brandId** | **String** | Brand ID. | 
**brandName** | **String** | Brand Name. | 
**cSCIdentification** | **String** | SKU Seller Identification. | 
**categories** | **[String]** | Categories of the related product. | 
**categoriesFullPath** | **[String]** | Path of Categories of the related product. | [optional] 
**collections** | **[String]** | Array with Collections IDs that are related to the Product. | 
**commercialConditionId** | **Number** | SKU Commercial Condition ID. | 
**complementName** | **String** | Product Complement Name. | [optional] 
**detailUrl** | **String** | Product slug. | 
**dimension** | [**Dimension**](Dimension.md) |  | 
**estimatedDateArrival** | **String** | SKU estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the product is on pre-sale. You must take into consideration both the launch date and the freight calculation for the arrival date. | 
**id** | **Number** | SKU ID. | 
**imageUrl** | **String** | SKU image URL. | 
**images** | [**[Image]**](Image.md) | Array of objects with SKU image details. | 
**informationSource** | **String** | Information Source. | 
**isActive** | **Boolean** | Defines if the SKU is active or not. | 
**isDirectCategoryActive** | **Boolean** | Indicates if the direct Product Category is active or not. | [optional] 
**isGiftCardRecharge** | **Boolean** | Defines if the purchase of the SKU will generate reward value for the customer. | 
**isInventoried** | **Boolean** |  | 
**isKit** | **Boolean** | Defines if the SKU is part of a bundle. | 
**isProductActive** | **Boolean** | Defines if the product is active or not. | [optional] 
**isTransported** | **Boolean** |  | 
**keyWords** | **String** | Keywords related to the product. | [optional] 
**kitItems** | **[String]** | Array with SKU IDs of bundle components. | 
**manufacturerCode** | **String** | Product Supplier ID. | 
**measurementUnit** | **String** | Measurement unit. | 
**modalType** | **String** | Links an unusual type of SKU to a carrier specialized in delivering it. This field should be filled in with the name of the modal (e.g. \&quot;Chemicals\&quot; or \&quot;Refrigerated products\&quot;). To learn more about this feature, read our articles [How the modal works](https://help.vtex.com/en/tutorial/how-does-the-modal-work--tutorials_125) and [Setting up modal for carriers](https://help.vtex.com/en/tutorial/configure-modal--3jhLqxuPhuiq24UoykCcqy). | 
**nameComplete** | **String** | Product Name and SKU Name combined. | 
**positionsInClusters** | **{String: {String: Number}}** | Product Clusters position in each Cluster. Structure: \&quot;{Product Cluster ID}\&quot;: {Position}.  &#x60;{Product Cluster ID}&#x60; is a string, while &#x60;{Position}&#x60; is an integer. | [optional] 
**productCategories** | **{String: {String: String}}** | Object containing product categories. Structure: \&quot;{CategoryID}\&quot;: \&quot;{CategoryName}\&quot;. Both the key and the value are strings. | 
**productCategoryIds** | **String** | Category path composed by category IDs separated by &#x60;/&#x60;. | 
**productClusterHighlights** | **{String: {String: String}}** | Product Clusters Highlights. Structure: \&quot;{Product Cluster ID}\&quot;: \&quot;{Product Cluster Name}\&quot;. Both the key and the value are strings. | [optional] 
**productClusterNames** | **{String: {String: String}}** | Product Clusters Names. Structure: \&quot;{Product Cluster ID}\&quot;: \&quot;{Product Cluster Name}\&quot;. Both the key and the value are strings. | [optional] 
**productClustersIds** | **String** | Product Cluster IDs separated by comma (&#x60;,&#x60;). | 
**productDescription** | **String** | Product Description. HTML is allowed. | 
**productFinalScore** | **Number** | Product Final Score. | [optional] 
**productGlobalCategoryId** | **Number** | Product Global Category ID. | 
**productId** | **Number** | Product ID. | 
**productIsVisible** | **Boolean** | Defines if the product is visible or not. | [optional] 
**productName** | **String** | Product Name. | 
**productRefId** | **String** | Product Reference ID. | [optional] 
**productSpecifications** | [**[ProductSpecification]**](ProductSpecification.md) | Array with related Product Specifications. | 
**realDimension** | [**RealDimension**](RealDimension.md) |  | 
**releaseDate** | **String** | Release date of the product. | [optional] 
**rewardValue** | **Number** | Reward value related to the SKU. | 
**salesChannels** | **[Number]** | Array of trade policy IDs. | 
**services** | **[String]** | Array with Service IDs that are related to the SKU. | 
**showIfNotAvailable** | **Boolean** | Defines if the product will be shown if it is not available. | [optional] 
**skuName** | **String** | SKU Name. | 
**skuSellers** | [**[SkuSeller]**](SkuSeller.md) | Array with related Sellers data. | 
**skuSpecifications** | [**[SkuSpecification]**](SkuSpecification.md) | Array with related SKU Specifications. | 
**taxCode** | **String** | SKU Tax Code. | [optional] 
**unitMultiplier** | **Number** | This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward. | 


