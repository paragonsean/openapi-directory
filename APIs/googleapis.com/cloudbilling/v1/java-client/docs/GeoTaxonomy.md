

# GeoTaxonomy

Encapsulates the geographic taxonomy data for a sku.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**regions** | **List&lt;String&gt;** | The list of regions associated with a sku. Empty for Global skus, which are associated with all Google Cloud regions. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of Geo Taxonomy: GLOBAL, REGIONAL, or MULTI_REGIONAL. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| GLOBAL | &quot;GLOBAL&quot; |
| REGIONAL | &quot;REGIONAL&quot; |
| MULTI_REGIONAL | &quot;MULTI_REGIONAL&quot; |



