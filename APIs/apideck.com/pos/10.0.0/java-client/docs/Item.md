

# Item


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abbreviation** | **String** |  |  [optional] |
|**absentAtLocationIds** | **List&lt;String&gt;** | A list of locations where the object is not present, even if present_at_all_locations is true. This can include locations that are deactivated. |  [optional] |
|**available** | **Boolean** |  |  [optional] |
|**availableForPickup** | **Boolean** |  |  [optional] |
|**availableOnline** | **Boolean** |  |  [optional] |
|**categories** | [**List&lt;CategoriesInner&gt;**](CategoriesInner.md) |  |  [optional] |
|**code** | **String** | Product code, e.g. UPC or EAN |  [optional] |
|**cost** | **BigDecimal** |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**deleted** | **Boolean** | Flag to indicate if the object is deleted. |  [optional] |
|**description** | **String** |  |  [optional] |
|**hidden** | **Boolean** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**idempotencyKey** | **String** | A value you specify that uniquely identifies this request among requests you have sent. |  [optional] |
|**isRevenue** | **Boolean** | True if this item should be counted as revenue. For example, gift cards and donations would not be counted as revenue. |  [optional] |
|**modifierGroups** | [**List&lt;VariationsInner&gt;**](VariationsInner.md) |  |  [optional] |
|**name** | **String** |  |  |
|**options** | [**List&lt;ItemOptionsInner&gt;**](ItemOptionsInner.md) | List of options pertaining to this item&#39;s attribute variation |  [optional] |
|**presentAtAllLocations** | **Boolean** |  |  [optional] |
|**priceAmount** | **BigDecimal** |  |  [optional] |
|**priceCurrency** | **Currency** |  |  [optional] |
|**pricingType** | [**PricingTypeEnum**](#PricingTypeEnum) |  |  [optional] |
|**productType** | [**ProductTypeEnum**](#ProductTypeEnum) |  |  [optional] |
|**sku** | **String** | SKU of the item |  [optional] |
|**taxIds** | **List&lt;String&gt;** | A list of Tax IDs for the product. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |
|**useDefaultTaxRates** | **Boolean** |  |  [optional] |
|**variations** | [**List&lt;VariationsInner1&gt;**](VariationsInner1.md) |  |  [optional] |
|**version** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: PricingTypeEnum

| Name | Value |
|---- | -----|
| FIXED | &quot;fixed&quot; |
| VARIABLE | &quot;variable&quot; |
| PER_UNIT | &quot;per_unit&quot; |
| OTHER | &quot;other&quot; |



## Enum: ProductTypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;regular&quot; |
| OTHER | &quot;other&quot; |



