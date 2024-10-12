# ApiKeyMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey**](ApiKeyMerchantLevelApi.md#postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey) | **POST** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey | Generate new API key |


<a id="postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey"></a>
# **postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey**
> GenerateApiKeyResponse postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey(merchantId, apiCredentialId)

Generate new API key

Returns a new API key for the API credential. You can use the new API key a few minutes after generating it. The old API key stops working 24 hours after generating a new one.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiKeyMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApiKeyMerchantLevelApi apiInstance = new ApiKeyMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
    try {
      GenerateApiKeyResponse result = apiInstance.postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey(merchantId, apiCredentialId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeyMerchantLevelApi#postMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **apiCredentialId** | **String**| Unique identifier of the API credential. | |

### Return type

[**GenerateApiKeyResponse**](GenerateApiKeyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

