# TokenActivateApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tokenActivatePost**](TokenActivateApi.md#tokenActivatePost) | **POST** /token/activate |  |


<a id="tokenActivatePost"></a>
# **tokenActivatePost**
> TokenActivateResponseSchema tokenActivatePost(tokenActivateRequestSchema)



Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation. If the provisioning was not completed successfully, activation cannot be accomplished using Customer Service API. It is expected that a cardholder will complete the authentication process using an issuer&#39;s call center or using an issuer-supplied mobile application, and only then should the issuer use this API to activate the token. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenActivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    TokenActivateApi apiInstance = new TokenActivateApi(defaultClient);
    TokenActivateRequestSchema tokenActivateRequestSchema = new TokenActivateRequestSchema(); // TokenActivateRequestSchema | Contains the details of the request message.
    try {
      TokenActivateResponseSchema result = apiInstance.tokenActivatePost(tokenActivateRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenActivateApi#tokenActivatePost");
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
| **tokenActivateRequestSchema** | [**TokenActivateRequestSchema**](TokenActivateRequestSchema.md)| Contains the details of the request message. | [optional] |

### Return type

[**TokenActivateResponseSchema**](TokenActivateResponseSchema.md)

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

