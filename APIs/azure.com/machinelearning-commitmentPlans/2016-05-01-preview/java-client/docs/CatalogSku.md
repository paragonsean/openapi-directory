

# CatalogSku

Details of a commitment plan SKU.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**List&lt;SkuCapability&gt;**](SkuCapability.md) | The capability information for the specified SKU. |  [optional] [readonly] |
|**capacity** | [**SkuCapacity**](SkuCapacity.md) |  |  [optional] |
|**costs** | [**List&lt;SkuCost&gt;**](SkuCost.md) | The cost information for the specified SKU. |  [optional] [readonly] |
|**locations** | **List&lt;String&gt;** | Regions where the SKU is available. |  [optional] [readonly] |
|**name** | **String** | SKU name |  [optional] [readonly] |
|**resourceType** | **String** | Resource type name |  [optional] [readonly] |
|**restrictions** | [**List&lt;SkuRestrictions&gt;**](SkuRestrictions.md) | Restrictions which would prevent a SKU from being used. This is empty if there are no restrictions. |  [optional] [readonly] |
|**tier** | **String** | SKU tier |  [optional] [readonly] |



