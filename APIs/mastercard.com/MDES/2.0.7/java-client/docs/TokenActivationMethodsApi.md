# TokenActivationMethodsApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tokenActivationmethodsPost**](TokenActivationMethodsApi.md#tokenActivationmethodsPost) | **POST** /token/activationmethods |  |


<a id="tokenActivationmethodsPost"></a>
# **tokenActivationmethodsPost**
> TokenActivationMethodsResponseSchema tokenActivationmethodsPost(tokenActivationMethodsRequestSchema)



Used to retrieve the available Activation Methods for a token that is awaiting activation. Activation Methods are the means by which a cardholder may complete cardholder authentication with the issuer beyond the scope of MDES. It is possible that there are no Activation Methods for a token when an issuer did not provide any cardholder-specific information with the Tokenization Authorization Request (TAR) pre-digitization network message response. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenActivationMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    TokenActivationMethodsApi apiInstance = new TokenActivationMethodsApi(defaultClient);
    TokenActivationMethodsRequestSchema tokenActivationMethodsRequestSchema = new TokenActivationMethodsRequestSchema(); // TokenActivationMethodsRequestSchema | Contains the details of the request message.
    try {
      TokenActivationMethodsResponseSchema result = apiInstance.tokenActivationmethodsPost(tokenActivationMethodsRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenActivationMethodsApi#tokenActivationmethodsPost");
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
| **tokenActivationMethodsRequestSchema** | [**TokenActivationMethodsRequestSchema**](TokenActivationMethodsRequestSchema.md)| Contains the details of the request message. | [optional] |

### Return type

[**TokenActivationMethodsResponseSchema**](TokenActivationMethodsResponseSchema.md)

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

