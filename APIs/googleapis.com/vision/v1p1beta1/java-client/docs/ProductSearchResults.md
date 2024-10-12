

# ProductSearchResults

Results for a product search request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**indexTime** | **String** | Timestamp of the index which provided these results. Products added to the product set and products removed from the product set after this time are not reflected in the current results. |  [optional] |
|**productGroupedResults** | [**List&lt;GroupedResult&gt;**](GroupedResult.md) | List of results grouped by products detected in the query image. Each entry corresponds to one bounding polygon in the query image, and contains the matching products specific to that region. There may be duplicate product matches in the union of all the per-product results. |  [optional] |
|**results** | [**List&lt;Result&gt;**](Result.md) | List of results, one for each product match. |  [optional] |



