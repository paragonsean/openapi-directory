# HostedOnboardingPageApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Hop/v5*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postGetOnboardingUrl**](HostedOnboardingPageApi.md#postGetOnboardingUrl) | **POST** /getOnboardingUrl | Get a link to a Adyen-hosted onboarding page |


<a id="postGetOnboardingUrl"></a>
# **postGetOnboardingUrl**
> GetOnboardingUrlResponse postGetOnboardingUrl(getOnboardingUrlRequest)

Get a link to a Adyen-hosted onboarding page

Returns a link to an Adyen-hosted onboarding page (HOP) that you can send to your account holder. For more information on how to use HOP, refer to [Hosted onboarding](https://docs.adyen.com/marketplaces-and-platforms/classic/collect-verification-details/hosted-onboarding-page). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostedOnboardingPageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Hop/v5");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    HostedOnboardingPageApi apiInstance = new HostedOnboardingPageApi(defaultClient);
    GetOnboardingUrlRequest getOnboardingUrlRequest = new GetOnboardingUrlRequest(); // GetOnboardingUrlRequest | 
    try {
      GetOnboardingUrlResponse result = apiInstance.postGetOnboardingUrl(getOnboardingUrlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostedOnboardingPageApi#postGetOnboardingUrl");
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
| **getOnboardingUrlRequest** | [**GetOnboardingUrlRequest**](GetOnboardingUrlRequest.md)|  | [optional] |

### Return type

[**GetOnboardingUrlResponse**](GetOnboardingUrlResponse.md)

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

