

# VariationsInner1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**itemId** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |
|**presentAtAllLocations** | **Boolean** |  |  [optional] |
|**priceAmount** | **BigDecimal** |  |  [optional] |
|**priceCurrency** | **Currency** |  |  [optional] |
|**pricingType** | [**PricingTypeEnum**](#PricingTypeEnum) |  |  [optional] |
|**sequence** | **BigDecimal** |  |  [optional] |
|**sku** | **String** |  |  [optional] |
|**stockable** | **Boolean** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**version** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: PricingTypeEnum

| Name | Value |
|---- | -----|
| FIXED | &quot;fixed&quot; |
| VARIABLE | &quot;variable&quot; |
| OTHER | &quot;other&quot; |



