# VertexAiSearchForRetailApi.GoogleCloudRetailV2betaSearchResponseFacetFacetValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **String** | Number of items that have this facet value. | [optional] 
**interval** | [**GoogleCloudRetailV2betaInterval**](GoogleCloudRetailV2betaInterval.md) |  | [optional] 
**maxValue** | **Number** | The maximum value in the FacetValue.interval. Only supported on numerical facets and returned if SearchRequest.FacetSpec.FacetKey.return_min_max is true. | [optional] 
**minValue** | **Number** | The minimum value in the FacetValue.interval. Only supported on numerical facets and returned if SearchRequest.FacetSpec.FacetKey.return_min_max is true. | [optional] 
**value** | **String** | Text value of a facet, such as \&quot;Black\&quot; for facet \&quot;colorFamilies\&quot;. | [optional] 


