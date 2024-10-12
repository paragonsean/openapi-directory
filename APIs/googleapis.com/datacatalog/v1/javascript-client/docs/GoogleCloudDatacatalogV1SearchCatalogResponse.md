# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1SearchCatalogResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | Pagination token that can be used in subsequent calls to retrieve the next page of results. | [optional] 
**results** | [**[GoogleCloudDatacatalogV1SearchCatalogResult]**](GoogleCloudDatacatalogV1SearchCatalogResult.md) | Search results. | [optional] 
**totalSize** | **Number** | The approximate total number of entries matched by the query. | [optional] 
**unreachable** | **[String]** | Unreachable locations. Search results don&#39;t include data from those locations. To get additional information on an error, repeat the search request and restrict it to specific locations by setting the &#x60;SearchCatalogRequest.scope.restricted_locations&#x60; parameter. | [optional] 


