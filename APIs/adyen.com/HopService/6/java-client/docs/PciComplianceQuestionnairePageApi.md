# PciComplianceQuestionnairePageApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Hop/v6*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postGetPciQuestionnaireUrl**](PciComplianceQuestionnairePageApi.md#postGetPciQuestionnaireUrl) | **POST** /getPciQuestionnaireUrl | Get a link to a PCI compliance questionnaire |


<a id="postGetPciQuestionnaireUrl"></a>
# **postGetPciQuestionnaireUrl**
> GetPciUrlResponse postGetPciQuestionnaireUrl(getPciUrlRequest)

Get a link to a PCI compliance questionnaire

Returns a link to a PCI compliance questionnaire that you can send to your account holder.  &gt; You should only use this endpoint if you have a [partner platform setup](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-partners).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PciComplianceQuestionnairePageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Hop/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PciComplianceQuestionnairePageApi apiInstance = new PciComplianceQuestionnairePageApi(defaultClient);
    GetPciUrlRequest getPciUrlRequest = new GetPciUrlRequest(); // GetPciUrlRequest | 
    try {
      GetPciUrlResponse result = apiInstance.postGetPciQuestionnaireUrl(getPciUrlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PciComplianceQuestionnairePageApi#postGetPciQuestionnaireUrl");
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
| **getPciUrlRequest** | [**GetPciUrlRequest**](GetPciUrlRequest.md)|  | [optional] |

### Return type

[**GetPciUrlResponse**](GetPciUrlResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

