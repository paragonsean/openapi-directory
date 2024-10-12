# RequestBasketsApi.RequestsApi

All URIs are relative to *https://rbaskets.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiBasketsNameRequestsDelete**](RequestsApi.md#apiBasketsNameRequestsDelete) | **DELETE** /api/baskets/{name}/requests | Delete all requests
[**apiBasketsNameRequestsGet**](RequestsApi.md#apiBasketsNameRequestsGet) | **GET** /api/baskets/{name}/requests | Get collected requests
[**basketsNameRequestsDelete**](RequestsApi.md#basketsNameRequestsDelete) | **DELETE** /baskets/{name}/requests | Delete all requests
[**basketsNameRequestsGet**](RequestsApi.md#basketsNameRequestsGet) | **GET** /baskets/{name}/requests | Get collected requests



## apiBasketsNameRequestsDelete

> apiBasketsNameRequestsDelete(name)

Delete all requests

Deletes all requests collected by this basket.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.RequestsApi();
let name = "name_example"; // String | The basket name
apiInstance.apiBasketsNameRequestsDelete(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The basket name | 

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiBasketsNameRequestsGet

> Requests apiBasketsNameRequestsGet(name, opts)

Get collected requests

Fetches collection of requests collected by this basket.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.RequestsApi();
let name = "name_example"; // String | The basket name
let opts = {
  'max': 56, // Number | Maximum number of requests to return; default 20
  'skip': 56, // Number | Number of requests to skip; default 0
  'q': "q_example", // String | Query string to filter result, only requests that match the query will be included in response
  '_in': "_in_example" // String | Defines what is taken into account when filtering is applied: `body` - search in content body of collected requests, `query` - search among query parameters of collected requests, `headers` - search among request header values, `any` - search anywhere; default `any` 
};
apiInstance.apiBasketsNameRequestsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The basket name | 
 **max** | **Number**| Maximum number of requests to return; default 20 | [optional] 
 **skip** | **Number**| Number of requests to skip; default 0 | [optional] 
 **q** | **String**| Query string to filter result, only requests that match the query will be included in response | [optional] 
 **_in** | **String**| Defines what is taken into account when filtering is applied: &#x60;body&#x60; - search in content body of collected requests, &#x60;query&#x60; - search among query parameters of collected requests, &#x60;headers&#x60; - search among request header values, &#x60;any&#x60; - search anywhere; default &#x60;any&#x60;  | [optional] 

### Return type

[**Requests**](Requests.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## basketsNameRequestsDelete

> basketsNameRequestsDelete(name)

Delete all requests

Deletes all requests collected by this basket.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.RequestsApi();
let name = "name_example"; // String | The basket name
apiInstance.basketsNameRequestsDelete(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The basket name | 

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## basketsNameRequestsGet

> Requests basketsNameRequestsGet(name, opts)

Get collected requests

Fetches collection of requests collected by this basket.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.RequestsApi();
let name = "name_example"; // String | The basket name
let opts = {
  'max': 56, // Number | Maximum number of requests to return; default 20
  'skip': 56, // Number | Number of requests to skip; default 0
  'q': "q_example", // String | Query string to filter result, only requests that match the query will be included in response
  '_in': "_in_example" // String | Defines what is taken into account when filtering is applied: `body` - search in content body of collected requests, `query` - search among query parameters of collected requests, `headers` - search among request header values, `any` - search anywhere; default `any` 
};
apiInstance.basketsNameRequestsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The basket name | 
 **max** | **Number**| Maximum number of requests to return; default 20 | [optional] 
 **skip** | **Number**| Number of requests to skip; default 0 | [optional] 
 **q** | **String**| Query string to filter result, only requests that match the query will be included in response | [optional] 
 **_in** | **String**| Defines what is taken into account when filtering is applied: &#x60;body&#x60; - search in content body of collected requests, &#x60;query&#x60; - search among query parameters of collected requests, &#x60;headers&#x60; - search among request header values, &#x60;any&#x60; - search anywhere; default &#x60;any&#x60;  | [optional] 

### Return type

[**Requests**](Requests.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

