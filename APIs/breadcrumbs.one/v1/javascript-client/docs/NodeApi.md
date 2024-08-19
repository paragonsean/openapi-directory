# BreadcrumbsOne.NodeApi

All URIs are relative to *https://api.breadcrumbs.one*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nodePost**](NodeApi.md#nodePost) | **POST** /node | Shows the incoming and outgoing transactions from blockchain address



## nodePost

> BreadcrumbsAPIModelsNodeNodeResponse nodePost(opts)

Shows the incoming and outgoing transactions from blockchain address

### Example

```javascript
import BreadcrumbsOne from 'breadcrumbs_one';
let defaultClient = BreadcrumbsOne.ApiClient.instance;
// Configure API key authorization: X-API-KEY
let X-API-KEY = defaultClient.authentications['X-API-KEY'];
X-API-KEY.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-API-KEY.apiKeyPrefix = 'Token';

let apiInstance = new BreadcrumbsOne.NodeApi();
let opts = {
  'breadcrumbsAPIModelsNodeNodeRequest': new BreadcrumbsOne.BreadcrumbsAPIModelsNodeNodeRequest() // BreadcrumbsAPIModelsNodeNodeRequest | 
};
apiInstance.nodePost(opts, (error, data, response) => {
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
 **breadcrumbsAPIModelsNodeNodeRequest** | [**BreadcrumbsAPIModelsNodeNodeRequest**](BreadcrumbsAPIModelsNodeNodeRequest.md)|  | [optional] 

### Return type

[**BreadcrumbsAPIModelsNodeNodeResponse**](BreadcrumbsAPIModelsNodeNodeResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json

