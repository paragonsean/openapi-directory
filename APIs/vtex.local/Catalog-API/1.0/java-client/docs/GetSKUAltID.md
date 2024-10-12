

# GetSKUAltID


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateIdValues** | **List&lt;String&gt;** | Array with values of alternative SKU IDs. |  |
|**alternateIds** | [**AlternateIds**](AlternateIds.md) |  |  |
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Array with Attachments ID that are related to the SKU. |  |
|**brandId** | **String** | Brand ID. |  |
|**brandName** | **String** | Brand Name. |  |
|**csCIdentification** | **String** | SKU Seller Identification. |  |
|**categories** | **List&lt;String&gt;** | Categories of the related product. |  |
|**categoriesFullPath** | **List&lt;String&gt;** | Path of Categories of the related product. |  [optional] |
|**collections** | **List&lt;String&gt;** | Array with Collections IDs that are related to the Product. |  |
|**commercialConditionId** | **Integer** | SKU Commercial Condition ID. |  |
|**complementName** | **String** | Product Complement Name. |  [optional] |
|**detailUrl** | **String** | Product slug. |  |
|**dimension** | [**Dimension**](Dimension.md) |  |  |
|**estimatedDateArrival** | **String** | SKU estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the product is on pre-sale. You must take into consideration both the launch date and the freight calculation for the arrival date. |  |
|**id** | **Integer** | SKU ID. |  |
|**imageUrl** | **String** | SKU image URL. |  |
|**images** | [**List&lt;Image&gt;**](Image.md) | Array of objects with SKU image details. |  |
|**informationSource** | **String** | Information Source. |  |
|**isActive** | **Boolean** | Defines if the SKU is active or not. |  |
|**isDirectCategoryActive** | **Boolean** | Indicates if the direct Product Category is active or not. |  [optional] |
|**isGiftCardRecharge** | **Boolean** | Defines if the purchase of the SKU will generate reward value for the customer. |  |
|**isInventoried** | **Boolean** |  |  |
|**isKit** | **Boolean** | Defines if the SKU is part of a bundle. |  |
|**isProductActive** | **Boolean** | Defines if the product is active or not. |  [optional] |
|**isTransported** | **Boolean** |  |  |
|**keyWords** | **String** | Keywords related to the product. |  [optional] |
|**kitItems** | **List&lt;String&gt;** | Array with SKU IDs of bundle components. |  |
|**manufacturerCode** | **String** | Product Supplier ID. |  |
|**measurementUnit** | **String** | Measurement unit. |  |
|**modalType** | **String** | Links an unusual type of SKU to a carrier specialized in delivering it. This field should be filled in with the name of the modal (e.g. \&quot;Chemicals\&quot; or \&quot;Refrigerated products\&quot;). To learn more about this feature, read our articles [How the modal works](https://help.vtex.com/en/tutorial/how-does-the-modal-work--tutorials_125) and [Setting up modal for carriers](https://help.vtex.com/en/tutorial/configure-modal--3jhLqxuPhuiq24UoykCcqy). |  |
|**nameComplete** | **String** | Product Name and SKU Name combined. |  |
|**positionsInClusters** | **Map&lt;String, Map&lt;String, Integer&gt;&gt;** | Product Clusters position in each Cluster. Structure: \&quot;{Product Cluster ID}\&quot;: {Position}.  &#x60;{Product Cluster ID}&#x60; is a string, while &#x60;{Position}&#x60; is an integer. |  [optional] |
|**productCategories** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Object containing product categories. Structure: \&quot;{CategoryID}\&quot;: \&quot;{CategoryName}\&quot;. Both the key and the value are strings. |  |
|**productCategoryIds** | **String** | Category path composed by category IDs separated by &#x60;/&#x60;. |  |
|**productClusterHighlights** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Product Clusters Highlights. Structure: \&quot;{Product Cluster ID}\&quot;: \&quot;{Product Cluster Name}\&quot;. Both the key and the value are strings. |  [optional] |
|**productClusterNames** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Product Clusters Names. Structure: \&quot;{Product Cluster ID}\&quot;: \&quot;{Product Cluster Name}\&quot;. Both the key and the value are strings. |  [optional] |
|**productClustersIds** | **String** | Product Cluster IDs separated by comma (&#x60;,&#x60;). |  |
|**productDescription** | **String** | Product Description. HTML is allowed. |  |
|**productFinalScore** | **Integer** | Product Final Score. |  [optional] |
|**productGlobalCategoryId** | **Integer** | Product Global Category ID. |  |
|**productId** | **Integer** | Product ID. |  |
|**productIsVisible** | **Boolean** | Defines if the product is visible or not. |  [optional] |
|**productName** | **String** | Product Name. |  |
|**productRefId** | **String** | Product Reference ID. |  [optional] |
|**productSpecifications** | [**List&lt;ProductSpecification&gt;**](ProductSpecification.md) | Array with related Product Specifications. |  |
|**realDimension** | [**RealDimension**](RealDimension.md) |  |  |
|**releaseDate** | **String** | Release date of the product. |  [optional] |
|**rewardValue** | **BigDecimal** | Reward value related to the SKU. |  |
|**salesChannels** | **List&lt;Integer&gt;** | Array of trade policy IDs. |  |
|**services** | **List&lt;String&gt;** | Array with Service IDs that are related to the SKU. |  |
|**showIfNotAvailable** | **Boolean** | Defines if the product will be shown if it is not available. |  [optional] |
|**skuName** | **String** | SKU Name. |  |
|**skuSellers** | [**List&lt;SkuSeller&gt;**](SkuSeller.md) | Array with related Sellers data. |  |
|**skuSpecifications** | [**List&lt;SkuSpecification&gt;**](SkuSpecification.md) | Array with related SKU Specifications. |  |
|**taxCode** | **String** | SKU Tax Code. |  [optional] |
|**unitMultiplier** | **BigDecimal** | This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward. |  |



