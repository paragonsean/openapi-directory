# VRealizeNetworkInsightApiReference.SearchApi

All URIs are relative to *http://vmware.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchEntities**](SearchApi.md#searchEntities) | **POST** /search | Search entities



## searchEntities

> PagedListResponseWithTime searchEntities(opts)

Search entities

Using search API you can search vRealize Network Insight entities by specifying entity type and filter expression. A filter expression is a predicate expression (similar to SQL where clause) used to define the search criteria. Please refer to API Guide on details of how to construct filter expression. A successful search request will return a list of entity ids that matches the search criteria.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.SearchApi();
let opts = {
  'searchRequest': new VRealizeNetworkInsightApiReference.SearchRequest() // SearchRequest | Search Request
};
apiInstance.searchEntities(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchRequest** | [**SearchRequest**](SearchRequest.md)| Search Request | [optional] 

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

