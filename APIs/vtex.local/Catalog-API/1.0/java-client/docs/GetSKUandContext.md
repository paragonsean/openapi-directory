

# GetSKUandContext


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateIdValues** | **List&lt;String&gt;** | Array with values of alternative SKU IDs. |  |
|**alternateIds** | [**AlternateIds**](AlternateIds.md) |  |  |
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Array with Attachments ID that are related to the SKU. |  |
|**brandId** | **String** | Product Brand ID. |  |
|**brandName** | **String** | Product Brand Name. |  |
|**csCIdentification** | **String** | SKU Seller identification. |  |
|**categories** | **List&lt;String&gt;** | Array with Categories from the related Product. |  |
|**collections** | **List&lt;String&gt;** | Array with Collections ID that are related to the Product. |  |
|**commercialConditionId** | **Integer** | SKU Commercial Condition ID. |  |
|**complementName** | **String** | Product Complement Name. |  [optional] |
|**detailUrl** | **String** | Product URL. |  |
|**dimension** | [**Dimension**](Dimension.md) |  |  |
|**estimatedDateArrival** | **String** | To add the product as pre-sale, enter the product estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format. You must take into consideration both the launch date and the freight calculation for the arrival date. |  |
|**id** | **Integer** | SKU ID. |  |
|**imageUrl** | **String** | SKU image URL. |  |
|**images** | [**List&lt;Image&gt;**](Image.md) | Array with SKU images. |  |
|**informationSource** | **String** | Information Source. |  |
|**isActive** | **Boolean** | Defines if the SKU is active or not. |  |
|**isGiftCardRecharge** | **Boolean** | Defines if the purchase will generate a reward. |  |
|**isInventoried** | **Boolean** |  |  |
|**isKit** | **Boolean** | Defines if the SKU is part of a bundle. |  |
|**isProductActive** | **Boolean** | Defines if the product is active or not. |  [optional] |
|**isTransported** | **Boolean** |  |  |
|**keyWords** | **String** | Keywords related to the product. |  [optional] |
|**kitItems** | **List&lt;String&gt;** | Array with SKU IDs of bundle components. |  |
|**manufacturerCode** | **String** | Product Supplier ID. |  |
|**measurementUnit** | **String** | SKU Measurement Unit. |  |
|**modalType** | **String** | Modal Type. |  |
|**nameComplete** | **String** | Product Name and SKU Name concatenated. |  |
|**productCategories** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Object containing product categories. Structure: \&quot;{CategoryID}\&quot;: \&quot;{CategoryName}\&quot;. |  |
|**productCategoryIds** | **String** | Category Hierarchy with Category IDs. |  |
|**productClustersIds** | **String** | Product Clusters IDs. |  |
|**productDescription** | **String** | Product Description. HTML is allowed. |  |
|**productFinalScore** | **Integer** | Product Final Score. |  [optional] |
|**productGlobalCategoryId** | **Integer** | Global Category ID. |  |
|**productId** | **Integer** | ID of the related Product. |  |
|**productIsVisible** | **Boolean** | Defines if the product is visible or not. |  [optional] |
|**productName** | **String** | Product Name. |  |
|**productRefId** | **String** | Reference ID of the related Product. |  [optional] |
|**productSpecifications** | [**List&lt;ProductSpecification&gt;**](ProductSpecification.md) | Array with related Product Specifications. |  |
|**realDimension** | [**RealDimension**](RealDimension.md) |  |  |
|**releaseDate** | **String** | Release date of the product. |  [optional] |
|**rewardValue** | **BigDecimal** | Reward value related to the SKU. |  |
|**salesChannels** | **List&lt;Integer&gt;** | Array with the ID of all the Sales Channels that are related to the product. |  |
|**services** | **List&lt;String&gt;** | Array with Service IDs that are related to the SKU. |  |
|**showIfNotAvailable** | **Boolean** | Defines if the product will be shown if it is not available. |  [optional] |
|**skuName** | **String** | SKU Name. |  |
|**skuSellers** | [**List&lt;SkuSeller&gt;**](SkuSeller.md) | Array with SKU Sellers data. |  |
|**skuSpecifications** | [**List&lt;SkuSpecification&gt;**](SkuSpecification.md) | Array with related SKU Specifications. |  |
|**taxCode** | **String** | SKU Tax Code. |  [optional] |
|**unitMultiplier** | **BigDecimal** | This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward. |  |



