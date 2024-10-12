

# GoogleCloudRetailV2SearchResponseFacetFacetValue

A facet value which contains value names and their count.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **String** | Number of items that have this facet value. |  [optional] |
|**interval** | [**GoogleCloudRetailV2Interval**](GoogleCloudRetailV2Interval.md) |  |  [optional] |
|**maxValue** | **Double** | The maximum value in the FacetValue.interval. Only supported on numerical facets and returned if SearchRequest.FacetSpec.FacetKey.return_min_max is true. |  [optional] |
|**minValue** | **Double** | The minimum value in the FacetValue.interval. Only supported on numerical facets and returned if SearchRequest.FacetSpec.FacetKey.return_min_max is true. |  [optional] |
|**value** | **String** | Text value of a facet, such as \&quot;Black\&quot; for facet \&quot;colorFamilies\&quot;. |  [optional] |



