

# FacetResult

Source specific facet response

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buckets** | [**List&lt;FacetBucket&gt;**](FacetBucket.md) | FacetBuckets for values in response containing at least a single result with the corresponding filter. |  [optional] |
|**objectType** | **String** | Object type for which facet results are returned. Can be empty. |  [optional] |
|**operatorName** | **String** | The name of the operator chosen for faceting. @see cloudsearch.SchemaPropertyOptions |  [optional] |
|**sourceName** | **String** | Source name for which facet results are returned. Will not be empty. |  [optional] |



