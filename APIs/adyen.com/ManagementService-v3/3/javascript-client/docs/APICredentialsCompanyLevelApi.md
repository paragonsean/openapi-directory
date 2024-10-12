# ManagementApi.APICredentialsCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompaniesCompanyIdApiCredentials**](APICredentialsCompanyLevelApi.md#getCompaniesCompanyIdApiCredentials) | **GET** /companies/{companyId}/apiCredentials | Get a list of API credentials
[**getCompaniesCompanyIdApiCredentialsApiCredentialId**](APICredentialsCompanyLevelApi.md#getCompaniesCompanyIdApiCredentialsApiCredentialId) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId} | Get an API credential
[**patchCompaniesCompanyIdApiCredentialsApiCredentialId**](APICredentialsCompanyLevelApi.md#patchCompaniesCompanyIdApiCredentialsApiCredentialId) | **PATCH** /companies/{companyId}/apiCredentials/{apiCredentialId} | Update an API credential.
[**postCompaniesCompanyIdApiCredentials**](APICredentialsCompanyLevelApi.md#postCompaniesCompanyIdApiCredentials) | **POST** /companies/{companyId}/apiCredentials | Create an API credential.



## getCompaniesCompanyIdApiCredentials

> ListCompanyApiCredentialsResponse getCompaniesCompanyIdApiCredentials(companyId, opts)

Get a list of API credentials

Returns the list of [API credentials](https://docs.adyen.com/development-resources/api-credentials) for the company account. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.APICredentialsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56 // Number | The number of items to have on a page, maximum 100. The default is 10 items on a page.
};
apiInstance.getCompaniesCompanyIdApiCredentials(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 

### Return type

[**ListCompanyApiCredentialsResponse**](ListCompanyApiCredentialsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdApiCredentialsApiCredentialId

> CompanyApiCredential getCompaniesCompanyIdApiCredentialsApiCredentialId(companyId, apiCredentialId)

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

let apiInstance = new ManagementApi.APICredentialsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
apiInstance.getCompaniesCompanyIdApiCredentialsApiCredentialId(companyId, apiCredentialId, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **apiCredentialId** | **String**| Unique identifier of the API credential. | 

### Return type

[**CompanyApiCredential**](CompanyApiCredential.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchCompaniesCompanyIdApiCredentialsApiCredentialId

> CompanyApiCredential patchCompaniesCompanyIdApiCredentialsApiCredentialId(companyId, apiCredentialId, opts)

Update an API credential.

Changes the API credential&#39;s roles, merchant account access, or allowed origins. The request has the new values for the fields you want to change. The response contains the full updated API credential, including the new values from the request.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.APICredentialsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
let opts = {
  'updateCompanyApiCredentialRequest': new ManagementApi.UpdateCompanyApiCredentialRequest() // UpdateCompanyApiCredentialRequest | 
};
apiInstance.patchCompaniesCompanyIdApiCredentialsApiCredentialId(companyId, apiCredentialId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **apiCredentialId** | **String**| Unique identifier of the API credential. | 
 **updateCompanyApiCredentialRequest** | [**UpdateCompanyApiCredentialRequest**](UpdateCompanyApiCredentialRequest.md)|  | [optional] 

### Return type

[**CompanyApiCredential**](CompanyApiCredential.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCompaniesCompanyIdApiCredentials

> CreateCompanyApiCredentialResponse postCompaniesCompanyIdApiCredentials(companyId, opts)

Create an API credential.

Creates an [API credential](https://docs.adyen.com/development-resources/api-credentials) for the company account identified in the path. In the request, you can specify which merchant accounts the new API credential will have access to, as well as its roles and allowed origins.  The response includes several types of authentication details: * [API key](https://docs.adyen.com/development-resources/api-authentication#api-key-authentication): used for API request authentication. * [Client key](https://docs.adyen.com/development-resources/client-side-authentication#how-it-works): public key used for client-side authentication. * [Username and password](https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication): used for basic authentication.  &gt; Make sure you store the API key securely in your system. You won&#39;t be able to retrieve it later.  If your API key is lost or compromised, you need to [generate a new API key](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/apiCredentials/{apiCredentialId}/generateApiKey).  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.APICredentialsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'createCompanyApiCredentialRequest': new ManagementApi.CreateCompanyApiCredentialRequest() // CreateCompanyApiCredentialRequest | 
};
apiInstance.postCompaniesCompanyIdApiCredentials(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **createCompanyApiCredentialRequest** | [**CreateCompanyApiCredentialRequest**](CreateCompanyApiCredentialRequest.md)|  | [optional] 

### Return type

[**CreateCompanyApiCredentialResponse**](CreateCompanyApiCredentialResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

