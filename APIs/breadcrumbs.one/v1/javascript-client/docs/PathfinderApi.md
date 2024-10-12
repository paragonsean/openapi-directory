# BreadcrumbsOne.PathfinderApi

All URIs are relative to *https://api.breadcrumbs.one*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pathfinderPost**](PathfinderApi.md#pathfinderPost) | **POST** /pathfinder | Automatically find path between crypto addresses



## pathfinderPost

> BreadcrumbsAPIModelsPathfinderPathfinderResponse pathfinderPost(opts)

Automatically find path between crypto addresses

### Example

```javascript
import BreadcrumbsOne from 'breadcrumbs_one';
let defaultClient = BreadcrumbsOne.ApiClient.instance;
// Configure API key authorization: X-API-KEY
let X-API-KEY = defaultClient.authentications['X-API-KEY'];
X-API-KEY.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-API-KEY.apiKeyPrefix = 'Token';

let apiInstance = new BreadcrumbsOne.PathfinderApi();
let opts = {
  'breadcrumbsAPIModelsPathfinderPathfinderRequest': new BreadcrumbsOne.BreadcrumbsAPIModelsPathfinderPathfinderRequest() // BreadcrumbsAPIModelsPathfinderPathfinderRequest | 
};
apiInstance.pathfinderPost(opts, (error, data, response) => {
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
 **breadcrumbsAPIModelsPathfinderPathfinderRequest** | [**BreadcrumbsAPIModelsPathfinderPathfinderRequest**](BreadcrumbsAPIModelsPathfinderPathfinderRequest.md)|  | [optional] 

### Return type

[**BreadcrumbsAPIModelsPathfinderPathfinderResponse**](BreadcrumbsAPIModelsPathfinderPathfinderResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json

