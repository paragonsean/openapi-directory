

# GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacetValue

Replaces a set of textual facet values by the same (possibly different) merged facet value. Each facet value should appear at most once as a value per CatalogAttribute. This feature is available only for textual custom attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mergedValue** | **String** | All the previous values are replaced by this merged facet value. This merged_value must be non-empty and can have up to 128 characters. |  [optional] |
|**values** | **List&lt;String&gt;** | All the facet values that are replaces by the same merged_value that follows. The maximum number of values per MergedFacetValue is 25. Each value can have up to 128 characters. |  [optional] |



