# ManagementApi.ClientKeyCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKey**](ClientKeyCompanyLevelApi.md#postCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKey) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey | Generate new client key



## postCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKey

> GenerateClientKeyResponse postCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKey(companyId, apiCredentialId)

Generate new client key

Returns a new [client key](https://docs.adyen.com/development-resources/client-side-authentication#how-it-works) for the API credential identified in the path. You can use the new client key a few minutes after generating it. The old client key stops working 24 hours after generating a new one.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.ClientKeyCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
apiInstance.postCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKey(companyId, apiCredentialId, (error, data, response) => {
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

[**GenerateClientKeyResponse**](GenerateClientKeyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

