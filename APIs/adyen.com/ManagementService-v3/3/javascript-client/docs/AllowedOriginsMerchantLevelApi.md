# ManagementApi.AllowedOriginsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId**](AllowedOriginsMerchantLevelApi.md#deleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId) | **DELETE** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Delete an allowed origin
[**getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins**](AllowedOriginsMerchantLevelApi.md#getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins) | **GET** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | Get a list of allowed origins
[**getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId**](AllowedOriginsMerchantLevelApi.md#getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId) | **GET** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Get an allowed origin
[**postMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins**](AllowedOriginsMerchantLevelApi.md#postMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins) | **POST** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | Create an allowed origin



## deleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId

> deleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId(merchantId, apiCredentialId, originId)

Delete an allowed origin

Removes the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path. As soon as an allowed origin is removed, we no longer accept client-side requests from that domain.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.AllowedOriginsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
let originId = "originId_example"; // String | Unique identifier of the allowed origin.
apiInstance.deleteMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId(merchantId, apiCredentialId, originId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **apiCredentialId** | **String**| Unique identifier of the API credential. | 
 **originId** | **String**| Unique identifier of the allowed origin. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins

> AllowedOriginsResponse getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins(merchantId, apiCredentialId)

Get a list of allowed origins

Returns the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.AllowedOriginsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
apiInstance.getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins(merchantId, apiCredentialId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **apiCredentialId** | **String**| Unique identifier of the API credential. | 

### Return type

[**AllowedOriginsResponse**](AllowedOriginsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId

> AllowedOrigin getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId(merchantId, apiCredentialId, originId)

Get an allowed origin

Returns the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.AllowedOriginsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
let originId = "originId_example"; // String | Unique identifier of the allowed origin.
apiInstance.getMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOriginsOriginId(merchantId, apiCredentialId, originId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **apiCredentialId** | **String**| Unique identifier of the API credential. | 
 **originId** | **String**| Unique identifier of the allowed origin. | 

### Return type

[**AllowedOrigin**](AllowedOrigin.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins

> AllowedOriginsResponse postMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins(merchantId, apiCredentialId, opts)

Create an allowed origin

Adds a new [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) to the API credential&#39;s list of allowed origins.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.AllowedOriginsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
let opts = {
  'allowedOrigin': new ManagementApi.AllowedOrigin() // AllowedOrigin | 
};
apiInstance.postMerchantsMerchantIdApiCredentialsApiCredentialIdAllowedOrigins(merchantId, apiCredentialId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **apiCredentialId** | **String**| Unique identifier of the API credential. | 
 **allowedOrigin** | [**AllowedOrigin**](AllowedOrigin.md)|  | [optional] 

### Return type

[**AllowedOriginsResponse**](AllowedOriginsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

