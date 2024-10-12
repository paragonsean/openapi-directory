# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1beta1SearchCatalogResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | The token that can be used to retrieve the next page of results. | [optional] 
**results** | [**[GoogleCloudDatacatalogV1beta1SearchCatalogResult]**](GoogleCloudDatacatalogV1beta1SearchCatalogResult.md) | Search results. | [optional] 
**totalSize** | **Number** | The approximate total number of entries matched by the query. | [optional] 
**unreachable** | **[String]** | Unreachable locations. Search result does not include data from those locations. Users can get additional information on the error by repeating the search request with a more restrictive parameter -- setting the value for &#x60;SearchDataCatalogRequest.scope.restricted_locations&#x60;. | [optional] 


