# Apacta.IntegrationsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIntegrationsContactsSync**](IntegrationsApi.md#getIntegrationsContactsSync) | **GET** /integrations/contactsSync | Force Synchronization with ERP systems
[**getIntegrationsList**](IntegrationsApi.md#getIntegrationsList) | **GET** /integrations | Get integrations list
[**getIntegrationsView**](IntegrationsApi.md#getIntegrationsView) | **GET** /integrations/{integration_id} | View integration details
[**integrationsBillysAuthenticatePost**](IntegrationsApi.md#integrationsBillysAuthenticatePost) | **POST** /integrations/billysAuthenticate | Authenticate to Billys
[**integrationsProductsSyncGet**](IntegrationsApi.md#integrationsProductsSyncGet) | **GET** /integrations/productsSync | Sync products from erp integration



## getIntegrationsContactsSync

> GetIntegrationsList200Response getIntegrationsContactsSync()

Force Synchronization with ERP systems

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.IntegrationsApi();
apiInstance.getIntegrationsContactsSync((error, data, response) => {
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

[**GetIntegrationsList200Response**](GetIntegrationsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegrationsList

> GetIntegrationsList200Response getIntegrationsList()

Get integrations list

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.IntegrationsApi();
apiInstance.getIntegrationsList((error, data, response) => {
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

[**GetIntegrationsList200Response**](GetIntegrationsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegrationsView

> GetIntegrationsList200Response getIntegrationsView(integrationId)

View integration details

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.IntegrationsApi();
let integrationId = "integrationId_example"; // String | Automatically added
apiInstance.getIntegrationsView(integrationId, (error, data, response) => {
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
 **integrationId** | **String**| Automatically added | 

### Return type

[**GetIntegrationsList200Response**](GetIntegrationsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationsBillysAuthenticatePost

> IntegrationsBillysAuthenticatePost200Response integrationsBillysAuthenticatePost()

Authenticate to Billys

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.IntegrationsApi();
apiInstance.integrationsBillysAuthenticatePost((error, data, response) => {
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

[**IntegrationsBillysAuthenticatePost200Response**](IntegrationsBillysAuthenticatePost200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationsProductsSyncGet

> IntegrationsProductsSyncGet200Response integrationsProductsSyncGet()

Sync products from erp integration

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.IntegrationsApi();
apiInstance.integrationsProductsSyncGet((error, data, response) => {
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

[**IntegrationsProductsSyncGet200Response**](IntegrationsProductsSyncGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

