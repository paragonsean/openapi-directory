

# GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacet

The current facet key (i.e. attribute config) maps into the merged_facet_key. A facet key can have at most one child. The current facet key and the merged facet key need both to be textual custom attributes or both numerical custom attributes (same type).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mergedFacetKey** | **String** | The merged facet key should be a valid facet key that is different than the facet key of the current catalog attribute. We refer this is merged facet key as the child of the current catalog attribute. This merged facet key can&#39;t be a parent of another facet key (i.e. no directed path of length 2). This merged facet key needs to be either a textual custom attribute or a numerical custom attribute. |  [optional] |
|**mergedFacetValues** | [**List&lt;GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacetValue&gt;**](GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacetValue.md) | Each instance is a list of facet values that map into the same (possibly different) merged facet value. For the current attribute config, each facet value should map to at most one merged facet value. |  [optional] |



