# InstantPayoutsApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payout/v40*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postPayout**](InstantPayoutsApi.md#postPayout) | **POST** /payout | Make an instant card payout |


<a id="postPayout"></a>
# **postPayout**
> PayoutResponse postPayout(payoutRequest)

Make an instant card payout

With this call, you can pay out to your customers, and funds will be made available within 30 minutes on the cardholder&#39;s bank account (this is dependent on whether the issuer supports this functionality). Instant card payouts are only supported for Visa and Mastercard cards.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstantPayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/Payout/v40");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    InstantPayoutsApi apiInstance = new InstantPayoutsApi(defaultClient);
    PayoutRequest payoutRequest = new PayoutRequest(); // PayoutRequest | 
    try {
      PayoutResponse result = apiInstance.postPayout(payoutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstantPayoutsApi#postPayout");
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
| **payoutRequest** | [**PayoutRequest**](PayoutRequest.md)|  | [optional] |

### Return type

[**PayoutResponse**](PayoutResponse.md)

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

