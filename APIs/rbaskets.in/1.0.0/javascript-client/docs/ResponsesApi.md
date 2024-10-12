# RequestBasketsApi.ResponsesApi

All URIs are relative to *https://rbaskets.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiBasketsNameResponsesMethodGet**](ResponsesApi.md#apiBasketsNameResponsesMethodGet) | **GET** /api/baskets/{name}/responses/{method} | Get response settings
[**apiBasketsNameResponsesMethodPut**](ResponsesApi.md#apiBasketsNameResponsesMethodPut) | **PUT** /api/baskets/{name}/responses/{method} | Update response settings
[**basketsNameResponsesMethodGet**](ResponsesApi.md#basketsNameResponsesMethodGet) | **GET** /baskets/{name}/responses/{method} | Get response settings
[**basketsNameResponsesMethodPut**](ResponsesApi.md#basketsNameResponsesMethodPut) | **PUT** /baskets/{name}/responses/{method} | Update response settings



## apiBasketsNameResponsesMethodGet

> Response apiBasketsNameResponsesMethodGet(name, method)

Get response settings

Retrieves information about configured response of the basket. Service will reply with this response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.ResponsesApi();
let name = "name_example"; // String | The basket name
let method = "method_example"; // String | The HTTP method this response is configured for
apiInstance.apiBasketsNameResponsesMethodGet(name, method, (error, data, response) => {
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
 **method** | **String**| The HTTP method this response is configured for | 

### Return type

[**Response**](Response.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiBasketsNameResponsesMethodPut

> apiBasketsNameResponsesMethodPut(name, method, response)

Update response settings

Allows to configure HTTP response of this basket. The service will reply with configured response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.ResponsesApi();
let name = "name_example"; // String | The basket name
let method = "method_example"; // String | The HTTP method this response is configured for
let response = new RequestBasketsApi.Response(); // Response | HTTP response configuration
apiInstance.apiBasketsNameResponsesMethodPut(name, method, response, (error, data, response) => {
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
 **method** | **String**| The HTTP method this response is configured for | 
 **response** | [**Response**](Response.md)| HTTP response configuration | 

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## basketsNameResponsesMethodGet

> Response basketsNameResponsesMethodGet(name, method)

Get response settings

Retrieves information about configured response of the basket. Service will reply with this response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.ResponsesApi();
let name = "name_example"; // String | The basket name
let method = "method_example"; // String | The HTTP method this response is configured for
apiInstance.basketsNameResponsesMethodGet(name, method, (error, data, response) => {
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
 **method** | **String**| The HTTP method this response is configured for | 

### Return type

[**Response**](Response.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## basketsNameResponsesMethodPut

> basketsNameResponsesMethodPut(name, method, response)

Update response settings

Allows to configure HTTP response of this basket. The service will reply with configured response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.ResponsesApi();
let name = "name_example"; // String | The basket name
let method = "method_example"; // String | The HTTP method this response is configured for
let response = new RequestBasketsApi.Response(); // Response | HTTP response configuration
apiInstance.basketsNameResponsesMethodPut(name, method, response, (error, data, response) => {
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
 **method** | **String**| The HTTP method this response is configured for | 
 **response** | [**Response**](Response.md)| HTTP response configuration | 

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

