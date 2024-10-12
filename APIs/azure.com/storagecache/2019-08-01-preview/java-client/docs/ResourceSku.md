

# ResourceSku

A resource SKU

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**List&lt;ResourceSkuCapabilities&gt;**](ResourceSkuCapabilities.md) | A list of capabilities of this SKU, such as throughput or ops/sec |  [optional] |
|**locationInfo** | [**List&lt;ResourceSkuLocationInfo&gt;**](ResourceSkuLocationInfo.md) | The set of locations that the SKU is available. |  [optional] |
|**locations** | **List&lt;String&gt;** | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). |  [optional] [readonly] |
|**name** | **String** | The name of this sku. |  [optional] |
|**resourceType** | **String** | The type of resource the sku applies to. |  [optional] [readonly] |
|**restrictions** | [**List&lt;Restriction&gt;**](Restriction.md) | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |  [optional] |



