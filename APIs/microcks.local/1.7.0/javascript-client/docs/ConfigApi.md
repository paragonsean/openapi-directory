# MicrocksApiV17.ConfigApi

All URIs are relative to *http://microcks.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSecret**](ConfigApi.md#createSecret) | **POST** /secrets | Create a new Secret
[**deleteSecret**](ConfigApi.md#deleteSecret) | **DELETE** /secrets/{id} | Delete Secret
[**getFeaturesConfiguration**](ConfigApi.md#getFeaturesConfiguration) | **GET** /features/config | Get features configuration
[**getKeycloakConfig**](ConfigApi.md#getKeycloakConfig) | **GET** /keycloak/config | Get authentification configuration
[**getSecret**](ConfigApi.md#getSecret) | **GET** /secrets/{id} | Get Secret
[**getSecrets**](ConfigApi.md#getSecrets) | **GET** /secrets | Get Secrets
[**getSecretsCounter**](ConfigApi.md#getSecretsCounter) | **GET** /secrets/count | Get the Secrets counter
[**updateSecret**](ConfigApi.md#updateSecret) | **PUT** /secrets/{id} | Update Secret



## createSecret

> Secret createSecret(opts)

Create a new Secret

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.ConfigApi();
let opts = {
  'secret': new MicrocksApiV17.Secret() // Secret | 
};
apiInstance.createSecret(opts, (error, data, response) => {
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
 **secret** | [**Secret**](Secret.md)|  | [optional] 

### Return type

[**Secret**](Secret.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSecret

> deleteSecret(id)

Delete Secret

Delete a Secret

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.ConfigApi();
let id = "id_example"; // String | Unique identifier of Secret to manage
apiInstance.deleteSecret(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of Secret to manage | 

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFeaturesConfiguration

> getFeaturesConfiguration()

Get features configuration

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.ConfigApi();
apiInstance.getFeaturesConfiguration((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKeycloakConfig

> KeycloakConfig getKeycloakConfig()

Get authentification configuration

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.ConfigApi();
apiInstance.getKeycloakConfig((error, data, response) => {
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

[**KeycloakConfig**](KeycloakConfig.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSecret

> Secret getSecret(id)

Get Secret

Retrieve a Secret

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.ConfigApi();
let id = "id_example"; // String | Unique identifier of Secret to manage
apiInstance.getSecret(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of Secret to manage | 

### Return type

[**Secret**](Secret.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSecrets

> [Secret] getSecrets(opts)

Get Secrets

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.ConfigApi();
let opts = {
  'page': 56, // Number | Page of Secrets to retrieve (starts at and defaults to 0)
  'size': 56 // Number | Size of a page. Maximum number of Secrets to include in a response (defaults to 20)
};
apiInstance.getSecrets(opts, (error, data, response) => {
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
 **page** | **Number**| Page of Secrets to retrieve (starts at and defaults to 0) | [optional] 
 **size** | **Number**| Size of a page. Maximum number of Secrets to include in a response (defaults to 20) | [optional] 

### Return type

[**[Secret]**](Secret.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSecretsCounter

> Counter getSecretsCounter()

Get the Secrets counter

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.ConfigApi();
apiInstance.getSecretsCounter((error, data, response) => {
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

[**Counter**](Counter.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSecret

> updateSecret(id)

Update Secret

Update a Secret

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.ConfigApi();
let id = "id_example"; // String | Unique identifier of Secret to manage
apiInstance.updateSecret(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of Secret to manage | 

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

