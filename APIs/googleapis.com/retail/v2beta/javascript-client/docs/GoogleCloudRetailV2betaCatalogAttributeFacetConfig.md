# VertexAiSearchForRetailApi.GoogleCloudRetailV2betaCatalogAttributeFacetConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facetIntervals** | [**[GoogleCloudRetailV2betaInterval]**](GoogleCloudRetailV2betaInterval.md) | If you don&#39;t set the facet SearchRequest.FacetSpec.FacetKey.intervals in the request to a numerical attribute, then we use the computed intervals with rounded bounds obtained from all its product numerical attribute values. The computed intervals might not be ideal for some attributes. Therefore, we give you the option to overwrite them with the facet_intervals field. The maximum of facet intervals per CatalogAttribute is 40. Each interval must have a lower bound or an upper bound. If both bounds are provided, then the lower bound must be smaller or equal than the upper bound. | [optional] 
**ignoredFacetValues** | [**[GoogleCloudRetailV2betaCatalogAttributeFacetConfigIgnoredFacetValues]**](GoogleCloudRetailV2betaCatalogAttributeFacetConfigIgnoredFacetValues.md) | Each instance represents a list of attribute values to ignore as facet values for a specific time range. The maximum number of instances per CatalogAttribute is 25. | [optional] 
**mergedFacet** | [**GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacet**](GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacet.md) |  | [optional] 
**mergedFacetValues** | [**[GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacetValue]**](GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacetValue.md) | Each instance replaces a list of facet values by a merged facet value. If a facet value is not in any list, then it will stay the same. To avoid conflicts, only paths of length 1 are accepted. In other words, if \&quot;dark_blue\&quot; merged into \&quot;BLUE\&quot;, then the latter can&#39;t merge into \&quot;blues\&quot; because this would create a path of length 2. The maximum number of instances of MergedFacetValue per CatalogAttribute is 100. This feature is available only for textual custom attributes. | [optional] 
**rerankConfig** | [**GoogleCloudRetailV2betaCatalogAttributeFacetConfigRerankConfig**](GoogleCloudRetailV2betaCatalogAttributeFacetConfigRerankConfig.md) |  | [optional] 


