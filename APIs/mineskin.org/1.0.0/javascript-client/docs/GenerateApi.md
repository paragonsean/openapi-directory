# MineSkinApi.GenerateApi

All URIs are relative to *https://api.mineskin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generateUploadPost**](GenerateApi.md#generateUploadPost) | **POST** /generate/upload | 
[**generateUrlPost**](GenerateApi.md#generateUrlPost) | **POST** /generate/url | 
[**generateUserPost**](GenerateApi.md#generateUserPost) | **POST** /generate/user | 



## generateUploadPost

> GenerateUploadPost200Response generateUploadPost(userAgent, opts)



### Example

```javascript
import MineSkinApi from 'mine_skin_api';
let defaultClient = MineSkinApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MineSkinApi.GenerateApi();
let userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
let opts = {
  'model': "'steve'", // String | 
  'name': "name_example", // String | 
  'variant': "variant_example", // String | Skin variant - automatically determined based on the image if not specified
  'visibility': 0, // Number | Visibility of the generated skin. 0 for public, 1 for private
  'file': "/path/to/file" // File | 
};
apiInstance.generateUploadPost(userAgent, opts, (error, data, response) => {
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
 **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | 
 **model** | **String**|  | [optional] [default to &#39;steve&#39;]
 **name** | **String**|  | [optional] 
 **variant** | **String**| Skin variant - automatically determined based on the image if not specified | [optional] 
 **visibility** | **Number**| Visibility of the generated skin. 0 for public, 1 for private | [optional] [default to 0]
 **file** | **File**|  | [optional] 

### Return type

[**GenerateUploadPost200Response**](GenerateUploadPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## generateUrlPost

> GenerateUploadPost200Response generateUrlPost(userAgent, generateUrlPostRequest)



### Example

```javascript
import MineSkinApi from 'mine_skin_api';
let defaultClient = MineSkinApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MineSkinApi.GenerateApi();
let userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
let generateUrlPostRequest = new MineSkinApi.GenerateUrlPostRequest(); // GenerateUrlPostRequest | 
apiInstance.generateUrlPost(userAgent, generateUrlPostRequest, (error, data, response) => {
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
 **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | 
 **generateUrlPostRequest** | [**GenerateUrlPostRequest**](GenerateUrlPostRequest.md)|  | 

### Return type

[**GenerateUploadPost200Response**](GenerateUploadPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## generateUserPost

> GenerateUploadPost200Response generateUserPost(userAgent, generateUserPostRequest)



### Example

```javascript
import MineSkinApi from 'mine_skin_api';
let defaultClient = MineSkinApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MineSkinApi.GenerateApi();
let userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
let generateUserPostRequest = new MineSkinApi.GenerateUserPostRequest(); // GenerateUserPostRequest | 
apiInstance.generateUserPost(userAgent, generateUserPostRequest, (error, data, response) => {
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
 **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | 
 **generateUserPostRequest** | [**GenerateUserPostRequest**](GenerateUserPostRequest.md)|  | 

### Return type

[**GenerateUploadPost200Response**](GenerateUploadPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

