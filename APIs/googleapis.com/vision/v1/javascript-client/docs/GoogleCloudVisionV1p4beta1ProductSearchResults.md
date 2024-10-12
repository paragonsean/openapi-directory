# CloudVisionApi.GoogleCloudVisionV1p4beta1ProductSearchResults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexTime** | **String** | Timestamp of the index which provided these results. Products added to the product set and products removed from the product set after this time are not reflected in the current results. | [optional] 
**productGroupedResults** | [**[GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult]**](GoogleCloudVisionV1p4beta1ProductSearchResultsGroupedResult.md) | List of results grouped by products detected in the query image. Each entry corresponds to one bounding polygon in the query image, and contains the matching products specific to that region. There may be duplicate product matches in the union of all the per-product results. | [optional] 
**results** | [**[GoogleCloudVisionV1p4beta1ProductSearchResultsResult]**](GoogleCloudVisionV1p4beta1ProductSearchResultsResult.md) | List of results, one for each product match. | [optional] 


