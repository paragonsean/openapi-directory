# CloudSearchApi.FacetOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integerFacetingOptions** | [**IntegerFacetingOptions**](IntegerFacetingOptions.md) |  | [optional] 
**numFacetBuckets** | **Number** | Maximum number of facet buckets that should be returned for this facet. Defaults to 10. Maximum value is 100. | [optional] 
**objectType** | **String** | If object_type is set, only those objects of that type will be used to compute facets. If empty, then all objects will be used to compute facets. | [optional] 
**operatorName** | **String** | The name of the operator chosen for faceting. @see cloudsearch.SchemaPropertyOptions | [optional] 
**sourceName** | **String** | Source name to facet on. Format: datasources/{source_id} If empty, all data sources will be used. | [optional] 


