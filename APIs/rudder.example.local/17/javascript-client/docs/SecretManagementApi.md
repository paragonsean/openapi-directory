# RudderApi.SecretManagementApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSecret**](SecretManagementApi.md#addSecret) | **PUT** /secret | Create a secret
[**deleteSecret**](SecretManagementApi.md#deleteSecret) | **DELETE** /secret/{name} | Delete a secret
[**getAllSecrets**](SecretManagementApi.md#getAllSecrets) | **GET** /secret | List all secrets
[**getSecret**](SecretManagementApi.md#getSecret) | **GET** /secret/{name} | Get one secret
[**updateSecret**](SecretManagementApi.md#updateSecret) | **POST** /secret | Update a secret



## addSecret

> AddSecret200Response addSecret(secrets)

Create a secret

Add a secret

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SecretManagementApi();
let secrets = new RudderApi.Secrets(); // Secrets | 
apiInstance.addSecret(secrets, (error, data, response) => {
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
 **secrets** | [**Secrets**](Secrets.md)|  | 

### Return type

[**AddSecret200Response**](AddSecret200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSecret

> DeleteSecret200Response deleteSecret(name)

Delete a secret

Remove the secret by his unique name

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SecretManagementApi();
let name = "name_example"; // String | Unique name of the secret
apiInstance.deleteSecret(name, (error, data, response) => {
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
 **name** | **String**| Unique name of the secret | 

### Return type

[**DeleteSecret200Response**](DeleteSecret200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllSecrets

> GetAllSecrets200Response getAllSecrets()

List all secrets

Get the list of all secrets without their value

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SecretManagementApi();
apiInstance.getAllSecrets((error, data, response) => {
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

[**GetAllSecrets200Response**](GetAllSecrets200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSecret

> GetSecret200Response getSecret(name)

Get one secret

Get one secret by his unique name

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SecretManagementApi();
let name = "name_example"; // String | Unique name of the secret
apiInstance.getSecret(name, (error, data, response) => {
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
 **name** | **String**| Unique name of the secret | 

### Return type

[**GetSecret200Response**](GetSecret200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSecret

> UpdateSecret200Response updateSecret(secrets)

Update a secret

Update a secret and override the value, the name cannot be overridden

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SecretManagementApi();
let secrets = new RudderApi.Secrets(); // Secrets | 
apiInstance.updateSecret(secrets, (error, data, response) => {
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
 **secrets** | [**Secrets**](Secrets.md)|  | 

### Return type

[**UpdateSecret200Response**](UpdateSecret200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

