# ManagementApi.APICredentialsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMerchantsMerchantIdApiCredentials**](APICredentialsMerchantLevelApi.md#getMerchantsMerchantIdApiCredentials) | **GET** /merchants/{merchantId}/apiCredentials | Get a list of API credentials
[**getMerchantsMerchantIdApiCredentialsApiCredentialId**](APICredentialsMerchantLevelApi.md#getMerchantsMerchantIdApiCredentialsApiCredentialId) | **GET** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Get an API credential
[**patchMerchantsMerchantIdApiCredentialsApiCredentialId**](APICredentialsMerchantLevelApi.md#patchMerchantsMerchantIdApiCredentialsApiCredentialId) | **PATCH** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Update an API credential
[**postMerchantsMerchantIdApiCredentials**](APICredentialsMerchantLevelApi.md#postMerchantsMerchantIdApiCredentials) | **POST** /merchants/{merchantId}/apiCredentials | Create an API credential



## getMerchantsMerchantIdApiCredentials

> ListMerchantApiCredentialsResponse getMerchantsMerchantIdApiCredentials(merchantId, opts)

Get a list of API credentials

Returns the list of [API credentials](https://docs.adyen.com/development-resources/api-credentials) for the merchant account. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.APICredentialsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56 // Number | The number of items to have on a page, maximum 100. The default is 10 items on a page.
};
apiInstance.getMerchantsMerchantIdApiCredentials(merchantId, opts, (error, data, response) => {
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
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 

### Return type

[**ListMerchantApiCredentialsResponse**](ListMerchantApiCredentialsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdApiCredentialsApiCredentialId

> ApiCredential getMerchantsMerchantIdApiCredentialsApiCredentialId(merchantId, apiCredentialId)

Get an API credential

Returns the [API credential](https://docs.adyen.com/development-resources/api-credentials) identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.APICredentialsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
apiInstance.getMerchantsMerchantIdApiCredentialsApiCredentialId(merchantId, apiCredentialId, (error, data, response) => {
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

[**ApiCredential**](ApiCredential.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchMerchantsMerchantIdApiCredentialsApiCredentialId

> ApiCredential patchMerchantsMerchantIdApiCredentialsApiCredentialId(merchantId, apiCredentialId, opts)

Update an API credential

Changes the API credential&#39;s roles, or allowed origins. The request has the new values for the fields you want to change. The response contains the full updated API credential, including the new values from the request.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.APICredentialsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
let opts = {
  'updateMerchantApiCredentialRequest': new ManagementApi.UpdateMerchantApiCredentialRequest() // UpdateMerchantApiCredentialRequest | 
};
apiInstance.patchMerchantsMerchantIdApiCredentialsApiCredentialId(merchantId, apiCredentialId, opts, (error, data, response) => {
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
 **updateMerchantApiCredentialRequest** | [**UpdateMerchantApiCredentialRequest**](UpdateMerchantApiCredentialRequest.md)|  | [optional] 

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdApiCredentials

> CreateApiCredentialResponse postMerchantsMerchantIdApiCredentials(merchantId, opts)

Create an API credential

Creates an [API credential](https://docs.adyen.com/development-resources/api-credentials) for the company account identified in the path. In the request, you can specify the roles and allowed origins for the new API credential.  The response includes the: * [API key](https://docs.adyen.com/development-resources/api-authentication#api-key-authentication): used for API request authentication. * [Client key](https://docs.adyen.com/development-resources/client-side-authentication#how-it-works): public key used for client-side authentication. * [Username and password](https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication): used for basic authentication.  &gt; Make sure you store the API key securely in your system. You won&#39;t be able to retrieve it later.  If your API key is lost or compromised, you need to [generate a new API key](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey).  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.APICredentialsMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'createMerchantApiCredentialRequest': new ManagementApi.CreateMerchantApiCredentialRequest() // CreateMerchantApiCredentialRequest | 
};
apiInstance.postMerchantsMerchantIdApiCredentials(merchantId, opts, (error, data, response) => {
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
 **createMerchantApiCredentialRequest** | [**CreateMerchantApiCredentialRequest**](CreateMerchantApiCredentialRequest.md)|  | [optional] 

### Return type

[**CreateApiCredentialResponse**](CreateApiCredentialResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

