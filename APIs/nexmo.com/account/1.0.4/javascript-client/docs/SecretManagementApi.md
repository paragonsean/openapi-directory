# AccountApi.SecretManagementApi

All URIs are relative to *https://api.nexmo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAPISecret**](SecretManagementApi.md#createAPISecret) | **POST** /accounts/{api_key}/secrets | Create API Secret
[**retrieveAPISecret**](SecretManagementApi.md#retrieveAPISecret) | **GET** /accounts/{api_key}/secrets/{secret_id} | Retrieve one API Secret
[**retrieveAPISecrets**](SecretManagementApi.md#retrieveAPISecrets) | **GET** /accounts/{api_key}/secrets | Retrieve API Secrets
[**revokeAPISecret**](SecretManagementApi.md#revokeAPISecret) | **DELETE** /accounts/{api_key}/secrets/{secret_id} | Revoke an API Secret



## createAPISecret

> SecretInfo createAPISecret(apiKey, createSecretRequest)

Create API Secret

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new AccountApi.SecretManagementApi();
let apiKey = "abcd1234"; // String | The API key to manage secrets for
let createSecretRequest = new AccountApi.CreateSecretRequest(); // CreateSecretRequest | 
apiInstance.createAPISecret(apiKey, createSecretRequest, (error, data, response) => {
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
 **apiKey** | **String**| The API key to manage secrets for | 
 **createSecretRequest** | [**CreateSecretRequest**](CreateSecretRequest.md)|  | 

### Return type

[**SecretInfo**](SecretInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## retrieveAPISecret

> SecretInfo retrieveAPISecret(apiKey, secretId)

Retrieve one API Secret

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new AccountApi.SecretManagementApi();
let apiKey = "abcd1234"; // String | The API key to manage secrets for
let secretId = "01234567-aaaa-bbbb-cccc-defdefdefdef"; // String | ID of the API Secret
apiInstance.retrieveAPISecret(apiKey, secretId, (error, data, response) => {
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
 **apiKey** | **String**| The API key to manage secrets for | 
 **secretId** | **String**| ID of the API Secret | 

### Return type

[**SecretInfo**](SecretInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAPISecrets

> RetrieveAPISecrets200Response retrieveAPISecrets(apiKey)

Retrieve API Secrets

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new AccountApi.SecretManagementApi();
let apiKey = "abcd1234"; // String | The API key to manage secrets for
apiInstance.retrieveAPISecrets(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| The API key to manage secrets for | 

### Return type

[**RetrieveAPISecrets200Response**](RetrieveAPISecrets200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## revokeAPISecret

> revokeAPISecret(apiKey, secretId)

Revoke an API Secret

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new AccountApi.SecretManagementApi();
let apiKey = "abcd1234"; // String | The API key to manage secrets for
let secretId = "01234567-aaaa-bbbb-cccc-defdefdefdef"; // String | ID of the API Secret
apiInstance.revokeAPISecret(apiKey, secretId, (error, data, response) => {
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
 **apiKey** | **String**| The API key to manage secrets for | 
 **secretId** | **String**| ID of the API Secret | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

