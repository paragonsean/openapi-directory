# ManagementApi.APIKeyMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey**](APIKeyMerchantLevelApi.md#postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey) | **POST** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey | Generate new API key



## postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey

> GenerateApiKeyResponse postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey(merchantId, apiCredentialId)

Generate new API key

Returns a new API key for the API credential. You can use the new API key a few minutes after generating it. The old API key stops working 24 hours after generating a new one.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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

let apiInstance = new ManagementApi.APIKeyMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
apiInstance.postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey(merchantId, apiCredentialId, (error, data, response) => {
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

[**GenerateApiKeyResponse**](GenerateApiKeyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

