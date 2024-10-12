# VectaraRestApi.QueryServiceApi

All URIs are relative to *https://api.vectara.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](QueryServiceApi.md#query) | **POST** /v1/query | 
[**streamQuery**](QueryServiceApi.md#streamQuery) | **POST** /v1/stream-query | 



## query

> ServingBatchQueryResponse query(customerId, servingBatchQueryRequest)



Query

### Example

```javascript
import VectaraRestApi from 'vectara_rest_api';
let defaultClient = VectaraRestApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oAuth
let oAuth = defaultClient.authentications['oAuth'];
oAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VectaraRestApi.QueryServiceApi();
let customerId = 56; // Number | The Customer ID to use for the request.
let servingBatchQueryRequest = new VectaraRestApi.ServingBatchQueryRequest(); // ServingBatchQueryRequest | 
apiInstance.query(customerId, servingBatchQueryRequest, (error, data, response) => {
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
 **customerId** | **Number**| The Customer ID to use for the request. | 
 **servingBatchQueryRequest** | [**ServingBatchQueryRequest**](ServingBatchQueryRequest.md)|  | 

### Return type

[**ServingBatchQueryResponse**](ServingBatchQueryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## streamQuery

> StreamResultOfServingResponseSet streamQuery(customerId, servingBatchQueryRequest)



Stream Query

### Example

```javascript
import VectaraRestApi from 'vectara_rest_api';
let defaultClient = VectaraRestApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oAuth
let oAuth = defaultClient.authentications['oAuth'];
oAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VectaraRestApi.QueryServiceApi();
let customerId = 56; // Number | The Customer ID to use for the request.
let servingBatchQueryRequest = new VectaraRestApi.ServingBatchQueryRequest(); // ServingBatchQueryRequest | 
apiInstance.streamQuery(customerId, servingBatchQueryRequest, (error, data, response) => {
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
 **customerId** | **Number**| The Customer ID to use for the request. | 
 **servingBatchQueryRequest** | [**ServingBatchQueryRequest**](ServingBatchQueryRequest.md)|  | 

### Return type

[**StreamResultOfServingResponseSet**](StreamResultOfServingResponseSet.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

