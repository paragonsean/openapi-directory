# RequestBasketsApi.BasketsApi

All URIs are relative to *https://rbaskets.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiBasketsGet**](BasketsApi.md#apiBasketsGet) | **GET** /api/baskets | Get baskets
[**apiBasketsNameDelete**](BasketsApi.md#apiBasketsNameDelete) | **DELETE** /api/baskets/{name} | Delete basket
[**apiBasketsNameGet**](BasketsApi.md#apiBasketsNameGet) | **GET** /api/baskets/{name} | Get basket settings
[**apiBasketsNamePost**](BasketsApi.md#apiBasketsNamePost) | **POST** /api/baskets/{name} | Create new basket
[**apiBasketsNamePut**](BasketsApi.md#apiBasketsNamePut) | **PUT** /api/baskets/{name} | Update basket settings
[**apiStatsGet**](BasketsApi.md#apiStatsGet) | **GET** /api/stats | Get baskets statistics
[**basketsGet**](BasketsApi.md#basketsGet) | **GET** /baskets | Get baskets
[**basketsNameDelete**](BasketsApi.md#basketsNameDelete) | **DELETE** /baskets/{name} | Delete basket
[**basketsNameGet**](BasketsApi.md#basketsNameGet) | **GET** /baskets/{name} | Get basket settings
[**basketsNamePost**](BasketsApi.md#basketsNamePost) | **POST** /baskets/{name} | Create new basket
[**basketsNamePut**](BasketsApi.md#basketsNamePut) | **PUT** /baskets/{name} | Update basket settings



## apiBasketsGet

> Baskets apiBasketsGet(opts)

Get baskets

Fetches a list of basket names managed by service. Require master token.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: service_token
let service_token = defaultClient.authentications['service_token'];
service_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//service_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.BasketsApi();
let opts = {
  'max': 56, // Number | Maximum number of basket names to return; default 20
  'skip': 56, // Number | Number of basket names to skip; default 0
  'q': "q_example" // String | Query string to filter result, only those basket names that match the query will be included in response
};
apiInstance.apiBasketsGet(opts, (error, data, response) => {
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
 **max** | **Number**| Maximum number of basket names to return; default 20 | [optional] 
 **skip** | **Number**| Number of basket names to skip; default 0 | [optional] 
 **q** | **String**| Query string to filter result, only those basket names that match the query will be included in response | [optional] 

### Return type

[**Baskets**](Baskets.md)

### Authorization

[service_token](../README.md#service_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiBasketsNameDelete

> apiBasketsNameDelete(name)

Delete basket

Permanently deletes this basket and all collected requests.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.BasketsApi();
let name = "name_example"; // String | The basket name
apiInstance.apiBasketsNameDelete(name, (error, data, response) => {
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


## apiBasketsNameGet

> Config apiBasketsNameGet(name)

Get basket settings

Retrieves configuration settings of this basket.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.BasketsApi();
let name = "name_example"; // String | The basket name
apiInstance.apiBasketsNameGet(name, (error, data, response) => {
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

### Return type

[**Config**](Config.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiBasketsNamePost

> Token apiBasketsNamePost(name, opts)

Create new basket

Creates a new basket with this name.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';

let apiInstance = new RequestBasketsApi.BasketsApi();
let name = "name_example"; // String | The name of new basket
let opts = {
  'config': new RequestBasketsApi.Config() // Config | Basket configuration
};
apiInstance.apiBasketsNamePost(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of new basket | 
 **config** | [**Config**](Config.md)| Basket configuration | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiBasketsNamePut

> apiBasketsNamePut(name, config)

Update basket settings

Updates configuration settings of this basket.  Special configuration parameters for request forwarding:   * &#x60;insecure_tls&#x60; controls certificate verification when forwarding requests. Setting this parameter to &#x60;true&#x60;   allows to forward collected HTTP requests via HTTPS protocol even if the forward end-point is configured with   self-signed TLS/SSL certificate. **Warning:** enabling this feature has known security implications.   * &#x60;expand_path&#x60; changes the logic of constructing taget URL when forwarding requests. If this parameter is   set to &#x60;true&#x60; the forward URL path will be expanded when original HTTP request contains compound path. For   example, a basket with name **server1** is configured to forward all requests to &#x60;http://server1.intranet:8001/myservice&#x60;   and it has received an HTTP request like &#x60;GET http://baskets.example.com/server1/component/123/events?status&#x3D;OK&#x60;   then depending on &#x60;expand_path&#x60; settings the request will be forwarded to:     * &#x60;true&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice/component/123/events?status&#x3D;OK&#x60;     * &#x60;false&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice?status&#x3D;OK&#x60; 

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.BasketsApi();
let name = "name_example"; // String | The basket name
let config = new RequestBasketsApi.Config(); // Config | New configuration to apply
apiInstance.apiBasketsNamePut(name, config, (error, data, response) => {
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
 **config** | [**Config**](Config.md)| New configuration to apply | 

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiStatsGet

> ServiceStats apiStatsGet(opts)

Get baskets statistics

Get service statistics about baskets and collected HTTP requests. Require master token.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: service_token
let service_token = defaultClient.authentications['service_token'];
service_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//service_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.BasketsApi();
let opts = {
  'max': 56 // Number | Maximum number of basket names to return; default 5
};
apiInstance.apiStatsGet(opts, (error, data, response) => {
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
 **max** | **Number**| Maximum number of basket names to return; default 5 | [optional] 

### Return type

[**ServiceStats**](ServiceStats.md)

### Authorization

[service_token](../README.md#service_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## basketsGet

> Baskets basketsGet(opts)

Get baskets

Fetches a list of basket names managed by service. Require master token.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: service_token
let service_token = defaultClient.authentications['service_token'];
service_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//service_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.BasketsApi();
let opts = {
  'max': 56, // Number | Maximum number of basket names to return; default 20
  'skip': 56, // Number | Number of basket names to skip; default 0
  'q': "q_example" // String | Query string to filter result, only those basket names that match the query will be included in response
};
apiInstance.basketsGet(opts, (error, data, response) => {
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
 **max** | **Number**| Maximum number of basket names to return; default 20 | [optional] 
 **skip** | **Number**| Number of basket names to skip; default 0 | [optional] 
 **q** | **String**| Query string to filter result, only those basket names that match the query will be included in response | [optional] 

### Return type

[**Baskets**](Baskets.md)

### Authorization

[service_token](../README.md#service_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## basketsNameDelete

> basketsNameDelete(name)

Delete basket

Permanently deletes this basket and all collected requests.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.BasketsApi();
let name = "name_example"; // String | The basket name
apiInstance.basketsNameDelete(name, (error, data, response) => {
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


## basketsNameGet

> Config basketsNameGet(name)

Get basket settings

Retrieves configuration settings of this basket.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.BasketsApi();
let name = "name_example"; // String | The basket name
apiInstance.basketsNameGet(name, (error, data, response) => {
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

### Return type

[**Config**](Config.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## basketsNamePost

> Token basketsNamePost(name, opts)

Create new basket

Creates a new basket with this name.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';

let apiInstance = new RequestBasketsApi.BasketsApi();
let name = "name_example"; // String | The name of new basket
let opts = {
  'config': new RequestBasketsApi.Config() // Config | Basket configuration
};
apiInstance.basketsNamePost(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of new basket | 
 **config** | [**Config**](Config.md)| Basket configuration | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## basketsNamePut

> basketsNamePut(name, config)

Update basket settings

Updates configuration settings of this basket.  Special configuration parameters for request forwarding:   * &#x60;insecure_tls&#x60; controls certificate verification when forwarding requests. Setting this parameter to &#x60;true&#x60;   allows to forward collected HTTP requests via HTTPS protocol even if the forward end-point is configured with   self-signed TLS/SSL certificate. **Warning:** enabling this feature has known security implications.   * &#x60;expand_path&#x60; changes the logic of constructing taget URL when forwarding requests. If this parameter is   set to &#x60;true&#x60; the forward URL path will be expanded when original HTTP request contains compound path. For   example, a basket with name **server1** is configured to forward all requests to &#x60;http://server1.intranet:8001/myservice&#x60;   and it has received an HTTP request like &#x60;GET http://baskets.example.com/server1/component/123/events?status&#x3D;OK&#x60;   then depending on &#x60;expand_path&#x60; settings the request will be forwarded to:     * &#x60;true&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice/component/123/events?status&#x3D;OK&#x60;     * &#x60;false&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice?status&#x3D;OK&#x60; 

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';
let defaultClient = RequestBasketsApi.ApiClient.instance;
// Configure API key authorization: basket_token
let basket_token = defaultClient.authentications['basket_token'];
basket_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//basket_token.apiKeyPrefix = 'Token';

let apiInstance = new RequestBasketsApi.BasketsApi();
let name = "name_example"; // String | The basket name
let config = new RequestBasketsApi.Config(); // Config | New configuration to apply
apiInstance.basketsNamePut(name, config, (error, data, response) => {
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
 **config** | [**Config**](Config.md)| New configuration to apply | 

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

