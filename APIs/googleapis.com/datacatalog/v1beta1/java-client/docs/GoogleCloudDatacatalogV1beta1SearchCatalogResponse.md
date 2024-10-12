

# GoogleCloudDatacatalogV1beta1SearchCatalogResponse

Response message for SearchCatalog.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The token that can be used to retrieve the next page of results. |  [optional] |
|**results** | [**List&lt;GoogleCloudDatacatalogV1beta1SearchCatalogResult&gt;**](GoogleCloudDatacatalogV1beta1SearchCatalogResult.md) | Search results. |  [optional] |
|**totalSize** | **Integer** | The approximate total number of entries matched by the query. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Unreachable locations. Search result does not include data from those locations. Users can get additional information on the error by repeating the search request with a more restrictive parameter -- setting the value for &#x60;SearchDataCatalogRequest.scope.restricted_locations&#x60;. |  [optional] |



