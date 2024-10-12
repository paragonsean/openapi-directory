

# GoogleCloudRetailV2CatalogAttributeFacetConfigRerankConfig

Options to rerank based on facet values engaged by the user for the current key. That key needs to be a custom textual key and facetable. To use this control, you also need to pass all the facet keys engaged by the user in the request using the field [SearchRequest.FacetSpec]. In particular, if you don't pass the facet keys engaged that you want to rerank on, this control won't be effective. Moreover, to obtain better results, the facet values that you want to rerank on should be close to English (ideally made of words, underscores, and spaces).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**facetValues** | **List&lt;String&gt;** | If empty, rerank on all facet values for the current key. Otherwise, will rerank on the facet values from this list only. |  [optional] |
|**rerankFacet** | **Boolean** | If set to true, then we also rerank the dynamic facets based on the facet values engaged by the user for the current attribute key during serving. |  [optional] |



