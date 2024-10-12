# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1beta1SearchCatalogRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orderBy** | **String** | Specifies the ordering of results, currently supported case-sensitive choices are: * &#x60;relevance&#x60;, only supports descending * &#x60;last_modified_timestamp [asc|desc]&#x60;, defaults to descending if not specified * &#x60;default&#x60; that can only be descending If not specified, defaults to &#x60;relevance&#x60; descending. | [optional] 
**pageSize** | **Number** | Number of results in the search page. If &lt;&#x3D;0 then defaults to 10. Max limit for page_size is 1000. Throws an invalid argument for page_size &gt; 1000. | [optional] 
**pageToken** | **String** | Optional. Pagination token returned in an earlier SearchCatalogResponse.next_page_token, which indicates that this is a continuation of a prior SearchCatalogRequest call, and that the system should return the next page of data. If empty, the first page is returned. | [optional] 
**query** | **String** | Optional. The query string in search query syntax. An empty query string will result in all data assets (in the specified scope) that the user has access to. Query strings can be simple as \&quot;x\&quot; or more qualified as: * name:x * column:x * description:y Note: Query tokens need to have a minimum of 3 characters for substring matching to work correctly. See [Data Catalog Search Syntax](https://cloud.google.com/data-catalog/docs/how-to/search-reference) for more information. | [optional] 
**scope** | [**GoogleCloudDatacatalogV1beta1SearchCatalogRequestScope**](GoogleCloudDatacatalogV1beta1SearchCatalogRequestScope.md) |  | [optional] 


