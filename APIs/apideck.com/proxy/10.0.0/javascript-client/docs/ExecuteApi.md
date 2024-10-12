# ProxyApi.ExecuteApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteProxy**](ExecuteApi.md#deleteProxy) | **DELETE** /proxy | DELETE
[**getProxy**](ExecuteApi.md#getProxy) | **GET** /proxy | GET
[**optionsProxy**](ExecuteApi.md#optionsProxy) | **OPTIONS** /proxy | OPTIONS
[**patchProxy**](ExecuteApi.md#patchProxy) | **PATCH** /proxy | PATCH
[**postProxy**](ExecuteApi.md#postProxy) | **POST** /proxy | POST
[**putProxy**](ExecuteApi.md#putProxy) | **PUT** /proxy | PUT



## deleteProxy

> Object deleteProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts)

DELETE

Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example

```javascript
import ProxyApi from 'proxy_api';
let defaultClient = ProxyApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ProxyApi.ExecuteApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
let xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
let opts = {
  'xApideckDownstreamAuthorization': "Bearer XXXXXXXXXXXXXXXXX" // String | Downstream authorization header. This will skip the Vault token injection.
};
apiInstance.deleteProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | 
 **xApideckDownstreamUrl** | **String**| Downstream URL | 
 **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProxy

> Object getProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts)

GET

Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example

```javascript
import ProxyApi from 'proxy_api';
let defaultClient = ProxyApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ProxyApi.ExecuteApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
let xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
let opts = {
  'xApideckDownstreamAuthorization': "Bearer XXXXXXXXXXXXXXXXX" // String | Downstream authorization header. This will skip the Vault token injection.
};
apiInstance.getProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | 
 **xApideckDownstreamUrl** | **String**| Downstream URL | 
 **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## optionsProxy

> Object optionsProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts)

OPTIONS

Proxies a downstream OPTION request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example

```javascript
import ProxyApi from 'proxy_api';
let defaultClient = ProxyApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ProxyApi.ExecuteApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
let xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
let opts = {
  'xApideckDownstreamAuthorization': "Bearer XXXXXXXXXXXXXXXXX" // String | Downstream authorization header. This will skip the Vault token injection.
};
apiInstance.optionsProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | 
 **xApideckDownstreamUrl** | **String**| Downstream URL | 
 **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchProxy

> Object patchProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts)

PATCH

Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example

```javascript
import ProxyApi from 'proxy_api';
let defaultClient = ProxyApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ProxyApi.ExecuteApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
let xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
let opts = {
  'xApideckDownstreamAuthorization': "Bearer XXXXXXXXXXXXXXXXX", // String | Downstream authorization header. This will skip the Vault token injection.
  'postProxyRequest': new ProxyApi.PostProxyRequest() // PostProxyRequest | Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.
};
apiInstance.patchProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | 
 **xApideckDownstreamUrl** | **String**| Downstream URL | 
 **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] 
 **postProxyRequest** | [**PostProxyRequest**](PostProxyRequest.md)| Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postProxy

> Object postProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts)

POST

Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example

```javascript
import ProxyApi from 'proxy_api';
let defaultClient = ProxyApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ProxyApi.ExecuteApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
let xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
let opts = {
  'xApideckDownstreamAuthorization': "Bearer XXXXXXXXXXXXXXXXX", // String | Downstream authorization header. This will skip the Vault token injection.
  'postProxyRequest': new ProxyApi.PostProxyRequest() // PostProxyRequest | Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.
};
apiInstance.postProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | 
 **xApideckDownstreamUrl** | **String**| Downstream URL | 
 **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] 
 **postProxyRequest** | [**PostProxyRequest**](PostProxyRequest.md)| Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putProxy

> Object putProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts)

PUT

Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example

```javascript
import ProxyApi from 'proxy_api';
let defaultClient = ProxyApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new ProxyApi.ExecuteApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
let xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
let opts = {
  'xApideckDownstreamAuthorization': "Bearer XXXXXXXXXXXXXXXXX", // String | Downstream authorization header. This will skip the Vault token injection.
  'putProxyRequest': new ProxyApi.PutProxyRequest() // PutProxyRequest | Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.
};
apiInstance.putProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | 
 **xApideckDownstreamUrl** | **String**| Downstream URL | 
 **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] 
 **putProxyRequest** | [**PutProxyRequest**](PutProxyRequest.md)| Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

