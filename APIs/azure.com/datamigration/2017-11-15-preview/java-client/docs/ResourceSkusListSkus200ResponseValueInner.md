

# ResourceSkusListSkus200ResponseValueInner

Describes an available DMS SKU.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersions** | **List&lt;String&gt;** | The api versions that support this SKU. |  [optional] [readonly] |
|**capabilities** | [**List&lt;ResourceSkusListSkus200ResponseValueInnerCapabilitiesInner&gt;**](ResourceSkusListSkus200ResponseValueInnerCapabilitiesInner.md) | A name value pair to describe the capability. |  [optional] [readonly] |
|**capacity** | [**ResourceSkusListSkus200ResponseValueInnerCapacity**](ResourceSkusListSkus200ResponseValueInnerCapacity.md) |  |  [optional] |
|**costs** | [**List&lt;ResourceSkusListSkus200ResponseValueInnerCostsInner&gt;**](ResourceSkusListSkus200ResponseValueInnerCostsInner.md) | Metadata for retrieving price info. |  [optional] [readonly] |
|**family** | **String** | The Family of this particular SKU. |  [optional] [readonly] |
|**kind** | **String** | The Kind of resources that are supported in this SKU. |  [optional] [readonly] |
|**locations** | **List&lt;String&gt;** | The set of locations that the SKU is available. |  [optional] [readonly] |
|**name** | **String** | The name of SKU. |  [optional] [readonly] |
|**resourceType** | **String** | The type of resource the SKU applies to. |  [optional] [readonly] |
|**restrictions** | [**List&lt;ResourceSkusListSkus200ResponseValueInnerRestrictionsInner&gt;**](ResourceSkusListSkus200ResponseValueInnerRestrictionsInner.md) | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |  [optional] [readonly] |
|**size** | **String** | The Size of the SKU. |  [optional] [readonly] |
|**tier** | **String** | Specifies the tier of DMS in a scale set. |  [optional] [readonly] |



