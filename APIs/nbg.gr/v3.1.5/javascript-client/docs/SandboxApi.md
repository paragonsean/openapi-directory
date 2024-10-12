# AccountAndTransactionApiSpecificationUk.SandboxApi

All URIs are relative to *https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sandboxPost**](SandboxApi.md#sandboxPost) | **POST** /sandbox | Create Sandbox
[**sandboxPut**](SandboxApi.md#sandboxPut) | **PUT** /sandbox | Import Sandbox
[**sandboxSandboxIdDelete**](SandboxApi.md#sandboxSandboxIdDelete) | **DELETE** /sandbox/{sandboxId} | Delete Sandbox
[**sandboxSandboxIdGet**](SandboxApi.md#sandboxSandboxIdGet) | **GET** /sandbox/{sandboxId} | Export Sandbox



## sandboxPost

> Sandbox sandboxPost(opts)

Create Sandbox

Create Sandbox

### Example

```javascript
import AccountAndTransactionApiSpecificationUk from 'account_and_transaction_api_specification_uk';
let defaultClient = AccountAndTransactionApiSpecificationUk.ApiClient.instance;
// Configure OAuth2 access token for authorization: Authorization-Code-Token
let Authorization-Code-Token = defaultClient.authentications['Authorization-Code-Token'];
Authorization-Code-Token.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Client-Id
let Client-Id = defaultClient.authentications['Client-Id'];
Client-Id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Client-Id.apiKeyPrefix = 'Token';

let apiInstance = new AccountAndTransactionApiSpecificationUk.SandboxApi();
let opts = {
  'sandboxRequest': new AccountAndTransactionApiSpecificationUk.SandboxRequest() // SandboxRequest | SandboxRequest
};
apiInstance.sandboxPost(opts, (error, data, response) => {
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
 **sandboxRequest** | [**SandboxRequest**](SandboxRequest.md)| SandboxRequest | [optional] 

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

- **Content-Type**: application/json, application/json; charset=utf-8
- **Accept**: application/json, application/json; charset=utf-8


## sandboxPut

> sandboxPut(opts)

Import Sandbox

Import Sandbox

### Example

```javascript
import AccountAndTransactionApiSpecificationUk from 'account_and_transaction_api_specification_uk';
let defaultClient = AccountAndTransactionApiSpecificationUk.ApiClient.instance;
// Configure OAuth2 access token for authorization: Authorization-Code-Token
let Authorization-Code-Token = defaultClient.authentications['Authorization-Code-Token'];
Authorization-Code-Token.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Client-Id
let Client-Id = defaultClient.authentications['Client-Id'];
Client-Id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Client-Id.apiKeyPrefix = 'Token';

let apiInstance = new AccountAndTransactionApiSpecificationUk.SandboxApi();
let opts = {
  'sandbox': new AccountAndTransactionApiSpecificationUk.Sandbox() // Sandbox | Sandbox
};
apiInstance.sandboxPut(opts, (error, data, response) => {
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
 **sandbox** | [**Sandbox**](Sandbox.md)| Sandbox | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

- **Content-Type**: application/json, application/json; charset=utf-8
- **Accept**: application/json, application/json; charset=utf-8


## sandboxSandboxIdDelete

> sandboxSandboxIdDelete(sandboxId)

Delete Sandbox

Delete Sandbox

### Example

```javascript
import AccountAndTransactionApiSpecificationUk from 'account_and_transaction_api_specification_uk';
let defaultClient = AccountAndTransactionApiSpecificationUk.ApiClient.instance;
// Configure OAuth2 access token for authorization: Authorization-Code-Token
let Authorization-Code-Token = defaultClient.authentications['Authorization-Code-Token'];
Authorization-Code-Token.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Client-Id
let Client-Id = defaultClient.authentications['Client-Id'];
Client-Id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Client-Id.apiKeyPrefix = 'Token';

let apiInstance = new AccountAndTransactionApiSpecificationUk.SandboxApi();
let sandboxId = "sandboxId_example"; // String | Sandbox Id
apiInstance.sandboxSandboxIdDelete(sandboxId, (error, data, response) => {
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
 **sandboxId** | **String**| Sandbox Id | 

### Return type

null (empty response body)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; charset=utf-8


## sandboxSandboxIdGet

> Sandbox sandboxSandboxIdGet(sandboxId)

Export Sandbox

Export Sandbox

### Example

```javascript
import AccountAndTransactionApiSpecificationUk from 'account_and_transaction_api_specification_uk';
let defaultClient = AccountAndTransactionApiSpecificationUk.ApiClient.instance;
// Configure OAuth2 access token for authorization: Authorization-Code-Token
let Authorization-Code-Token = defaultClient.authentications['Authorization-Code-Token'];
Authorization-Code-Token.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Client-Id
let Client-Id = defaultClient.authentications['Client-Id'];
Client-Id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Client-Id.apiKeyPrefix = 'Token';

let apiInstance = new AccountAndTransactionApiSpecificationUk.SandboxApi();
let sandboxId = "sandboxId_example"; // String | Sandbox Id
apiInstance.sandboxSandboxIdGet(sandboxId, (error, data, response) => {
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
 **sandboxId** | **String**| Sandbox Id | 

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; charset=utf-8

