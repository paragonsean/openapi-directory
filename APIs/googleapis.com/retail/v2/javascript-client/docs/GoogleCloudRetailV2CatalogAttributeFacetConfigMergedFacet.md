# VertexAiSearchForRetailApi.GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mergedFacetKey** | **String** | The merged facet key should be a valid facet key that is different than the facet key of the current catalog attribute. We refer this is merged facet key as the child of the current catalog attribute. This merged facet key can&#39;t be a parent of another facet key (i.e. no directed path of length 2). This merged facet key needs to be either a textual custom attribute or a numerical custom attribute. | [optional] 
**mergedFacetValues** | [**[GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacetValue]**](GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacetValue.md) | Each instance is a list of facet values that map into the same (possibly different) merged facet value. For the current attribute config, each facet value should map to at most one merged facet value. | [optional] 


