# PosApi.Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviation** | **String** |  | [optional] 
**absentAtLocationIds** | **[String]** | A list of locations where the object is not present, even if present_at_all_locations is true. This can include locations that are deactivated. | [optional] 
**available** | **Boolean** |  | [optional] 
**availableForPickup** | **Boolean** |  | [optional] 
**availableOnline** | **Boolean** |  | [optional] 
**categories** | [**[CategoriesInner]**](CategoriesInner.md) |  | [optional] 
**code** | **String** | Product code, e.g. UPC or EAN | [optional] 
**cost** | **Number** |  | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**deleted** | **Boolean** | Flag to indicate if the object is deleted. | [optional] 
**description** | **String** |  | [optional] 
**hidden** | **Boolean** |  | [optional] 
**id** | **String** |  | [optional] 
**idempotencyKey** | **String** | A value you specify that uniquely identifies this request among requests you have sent. | [optional] 
**isRevenue** | **Boolean** | True if this item should be counted as revenue. For example, gift cards and donations would not be counted as revenue. | [optional] 
**modifierGroups** | [**[VariationsInner]**](VariationsInner.md) |  | [optional] 
**name** | **String** |  | 
**options** | [**[ItemOptionsInner]**](ItemOptionsInner.md) | List of options pertaining to this item&#39;s attribute variation | [optional] 
**presentAtAllLocations** | **Boolean** |  | [optional] 
**priceAmount** | **Number** |  | [optional] 
**priceCurrency** | [**Currency**](Currency.md) |  | [optional] 
**pricingType** | **String** |  | [optional] 
**productType** | **String** |  | [optional] 
**sku** | **String** | SKU of the item | [optional] 
**taxIds** | **[String]** | A list of Tax IDs for the product. | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 
**useDefaultTaxRates** | **Boolean** |  | [optional] 
**variations** | [**[VariationsInner1]**](VariationsInner1.md) |  | [optional] 
**version** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: PricingTypeEnum


* `fixed` (value: `"fixed"`)

* `variable` (value: `"variable"`)

* `per_unit` (value: `"per_unit"`)

* `other` (value: `"other"`)





## Enum: ProductTypeEnum


* `regular` (value: `"regular"`)

* `other` (value: `"other"`)




