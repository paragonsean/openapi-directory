# TokenResetMobilePinApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tokenResetmobilepinPost**](TokenResetMobilePinApi.md#tokenResetmobilepinPost) | **POST** /token/resetmobilepin |  |


<a id="tokenResetmobilepinPost"></a>
# **tokenResetmobilepinPost**
> TokenResetMobilePinResponseSchema tokenResetmobilepinPost(tokenResetMobilePinRequestSchema)



Used to request that the Mobile PIN for a Mastercard Cloud-Based Payment token in a single issuer wallet is reset. The request is passed to the Credential Management System for processing. When the Mobile PIN is a token-level PIN (as opposed to a wallet-level PIN), the cardholder must choose a new PIN within 10 minutes of a Reset Mobile PIN action. Otherwise, the reset will need to be re-requested. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenResetMobilePinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    TokenResetMobilePinApi apiInstance = new TokenResetMobilePinApi(defaultClient);
    TokenResetMobilePinRequestSchema tokenResetMobilePinRequestSchema = new TokenResetMobilePinRequestSchema(); // TokenResetMobilePinRequestSchema | Contains the details of the request message.
    try {
      TokenResetMobilePinResponseSchema result = apiInstance.tokenResetmobilepinPost(tokenResetMobilePinRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenResetMobilePinApi#tokenResetmobilepinPost");
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
| **tokenResetMobilePinRequestSchema** | [**TokenResetMobilePinRequestSchema**](TokenResetMobilePinRequestSchema.md)| Contains the details of the request message. | [optional] |

### Return type

[**TokenResetMobilePinResponseSchema**](TokenResetMobilePinResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains the details of the response message. |  -  |
| **0** | unexpected error |  -  |

