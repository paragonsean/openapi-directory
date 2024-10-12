# SnykApi.DependenciesApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listAllDependencies**](DependenciesApi.md#listAllDependencies) | **POST** /org/{orgId}/dependencies | List all dependencies



## listAllDependencies

> ListAllDependencies200Response listAllDependencies(orgId, opts)

List all dependencies



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.DependenciesApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
let opts = {
  'sortBy': "dependency", // String | The field to sort results by.
  'order': "'asc'", // String | The direction to sort results by.
  'page': 1, // Number | The page of results to fetch.
  'perPage': 20, // Number | The number of results to fetch per page (maximum is 1000).
  'listAllDependenciesRequest': new SnykApi.ListAllDependenciesRequest() // ListAllDependenciesRequest | 
};
apiInstance.listAllDependencies(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **sortBy** | **String**| The field to sort results by. | [optional] [default to &#39;dependency&#39;]
 **order** | **String**| The direction to sort results by. | [optional] [default to &#39;asc&#39;]
 **page** | **Number**| The page of results to fetch. | [optional] [default to 1]
 **perPage** | **Number**| The number of results to fetch per page (maximum is 1000). | [optional] [default to 20]
 **listAllDependenciesRequest** | [**ListAllDependenciesRequest**](ListAllDependenciesRequest.md)|  | [optional] 

### Return type

[**ListAllDependencies200Response**](ListAllDependencies200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

