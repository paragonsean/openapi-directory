# ManagementApi.MyAPICredentialApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMeAllowedOriginsOriginId**](MyAPICredentialApi.md#deleteMeAllowedOriginsOriginId) | **DELETE** /me/allowedOrigins/{originId} | Remove allowed origin
[**getMe**](MyAPICredentialApi.md#getMe) | **GET** /me | Get API credential details
[**getMeAllowedOrigins**](MyAPICredentialApi.md#getMeAllowedOrigins) | **GET** /me/allowedOrigins | Get allowed origins
[**getMeAllowedOriginsOriginId**](MyAPICredentialApi.md#getMeAllowedOriginsOriginId) | **GET** /me/allowedOrigins/{originId} | Get allowed origin details
[**postMeAllowedOrigins**](MyAPICredentialApi.md#postMeAllowedOrigins) | **POST** /me/allowedOrigins | Add allowed origin
[**postMeGenerateClientKey**](MyAPICredentialApi.md#postMeGenerateClientKey) | **POST** /me/generateClientKey | Generate a client key



## deleteMeAllowedOriginsOriginId

> deleteMeAllowedOriginsOriginId(originId)

Remove allowed origin

Removes the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) specified in the path. The API key from the request is used to identify the [API credential](https://docs.adyen.com/development-resources/api-credentials).  You can make this request with any of the Management API roles.

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.MyAPICredentialApi();
let originId = "originId_example"; // String | Unique identifier of the allowed origin.
apiInstance.deleteMeAllowedOriginsOriginId(originId, (error, data, response) => {
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
 **originId** | **String**| Unique identifier of the allowed origin. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMe

> MeApiCredential getMe()

Get API credential details

Returns your [API credential](https://docs.adyen.com/development-resources/api-credentials) details based on the API Key you used in the request.  You can make this request with any of the Management API roles.

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.MyAPICredentialApi();
apiInstance.getMe((error, data, response) => {
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

[**MeApiCredential**](MeApiCredential.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMeAllowedOrigins

> AllowedOriginsResponse getMeAllowedOrigins()

Get allowed origins

Returns the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) of your [API credential](https://docs.adyen.com/development-resources/api-credentials) based on the API key you used in the request.  You can make this request with any of the Management API roles.

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.MyAPICredentialApi();
apiInstance.getMeAllowedOrigins((error, data, response) => {
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

[**AllowedOriginsResponse**](AllowedOriginsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMeAllowedOriginsOriginId

> AllowedOrigin getMeAllowedOriginsOriginId(originId)

Get allowed origin details

Returns the details of the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) specified in the path. The API key from the request is used to identify the [API credential](https://docs.adyen.com/development-resources/api-credentials).  You can make this request with any of the Management API roles.

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.MyAPICredentialApi();
let originId = "originId_example"; // String | Unique identifier of the allowed origin.
apiInstance.getMeAllowedOriginsOriginId(originId, (error, data, response) => {
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
 **originId** | **String**| Unique identifier of the allowed origin. | 

### Return type

[**AllowedOrigin**](AllowedOrigin.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postMeAllowedOrigins

> AllowedOrigin postMeAllowedOrigins(opts)

Add allowed origin

Adds an allowed origin to the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) of your API credential. The API key from the request is used to identify the [API credential](https://docs.adyen.com/development-resources/api-credentials).  You can make this request with any of the Management API roles.

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.MyAPICredentialApi();
let opts = {
  'createAllowedOriginRequest': new ManagementApi.CreateAllowedOriginRequest() // CreateAllowedOriginRequest | 
};
apiInstance.postMeAllowedOrigins(opts, (error, data, response) => {
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
 **createAllowedOriginRequest** | [**CreateAllowedOriginRequest**](CreateAllowedOriginRequest.md)|  | [optional] 

### Return type

[**AllowedOrigin**](AllowedOrigin.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMeGenerateClientKey

> GenerateClientKeyResponse postMeGenerateClientKey()

Generate a client key

Generates a new [client key](https://docs.adyen.com/development-resources/client-side-authentication/) used to authenticate requests from your payment environment. You can use the new client key a few minutes after generating it. The old client key stops working 24 hours after generating a new one.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.MyAPICredentialApi();
apiInstance.postMeGenerateClientKey((error, data, response) => {
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

[**GenerateClientKeyResponse**](GenerateClientKeyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

