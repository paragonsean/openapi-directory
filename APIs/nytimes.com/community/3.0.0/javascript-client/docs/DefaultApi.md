# CommunityApi.DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/community/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETUserContentByDateJson**](DefaultApi.md#gETUserContentByDateJson) | **GET** /user-content/by-date.json | Comments by Date
[**gETUserContentRecentJson**](DefaultApi.md#gETUserContentRecentJson) | **GET** /user-content/recent.json | Recent User Comments
[**gETUserContentUrlJson**](DefaultApi.md#gETUserContentUrlJson) | **GET** /user-content/url.json | Comments by URL
[**gETUserContentUserJson**](DefaultApi.md#gETUserContentUserJson) | **GET** /user-content/user.json | Comments by User



## gETUserContentByDateJson

> GETUserContentByDateJson200Response gETUserContentByDateJson(opts)

Comments by Date



### Example

```javascript
import CommunityApi from 'community_api';
let defaultClient = CommunityApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new CommunityApi.DefaultApi();
let opts = {
  'date': "date_example" // String | 
};
apiInstance.gETUserContentByDateJson(opts, (error, data, response) => {
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
 **date** | **String**|  | [optional] 

### Return type

[**GETUserContentByDateJson200Response**](GETUserContentByDateJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETUserContentRecentJson

> GETUserContentRecentJson200Response gETUserContentRecentJson()

Recent User Comments



### Example

```javascript
import CommunityApi from 'community_api';
let defaultClient = CommunityApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new CommunityApi.DefaultApi();
apiInstance.gETUserContentRecentJson((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GETUserContentRecentJson200Response**](GETUserContentRecentJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETUserContentUrlJson

> GETUserContentUrlJson200Response gETUserContentUrlJson(opts)

Comments by URL



### Example

```javascript
import CommunityApi from 'community_api';
let defaultClient = CommunityApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new CommunityApi.DefaultApi();
let opts = {
  'url': "url_example" // String | 
};
apiInstance.gETUserContentUrlJson(opts, (error, data, response) => {
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
 **url** | **String**|  | [optional] 

### Return type

[**GETUserContentUrlJson200Response**](GETUserContentUrlJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETUserContentUserJson

> GETUserContentUserJson200Response gETUserContentUserJson(opts)

Comments by User



### Example

```javascript
import CommunityApi from 'community_api';
let defaultClient = CommunityApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new CommunityApi.DefaultApi();
let opts = {
  'userID': 56 // Number | 
};
apiInstance.gETUserContentUserJson(opts, (error, data, response) => {
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
 **userID** | **Number**|  | [optional] 

### Return type

[**GETUserContentUserJson200Response**](GETUserContentUserJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

