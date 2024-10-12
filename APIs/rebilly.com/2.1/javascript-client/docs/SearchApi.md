# RebillyRestApi.SearchApi

All URIs are relative to *https://api-sandbox.rebilly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSearch**](SearchApi.md#getSearch) | **GET** /search | Search merchant data



## getSearch

> [Search] getSearch(opts)

Search merchant data

Search merchant&#39;s data to return resources such as customers, invoices, orders, transactions. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.SearchApi();
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'sort': ["null"], // [String] | The collection items sort field and order (prefix with \"-\" for descending sort).
  'limit': 56, // Number | The collection items limit.
  'offset': 56, // Number | The collection items offset.
  'q': "q_example" // String | The default search. It will search across resources and many fields.
};
apiInstance.getSearch(opts, (error, data, response) => {
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
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 
 **sort** | [**[String]**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] 
 **limit** | **Number**| The collection items limit. | [optional] 
 **offset** | **Number**| The collection items offset. | [optional] 
 **q** | **String**| The default search. It will search across resources and many fields. | [optional] 

### Return type

[**[Search]**](Search.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

