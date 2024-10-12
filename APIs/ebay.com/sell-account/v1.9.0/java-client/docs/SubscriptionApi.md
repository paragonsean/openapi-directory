# SubscriptionApi

All URIs are relative to *https://api.ebay.com/sell/account/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSubscription**](SubscriptionApi.md#getSubscription) | **GET** /subscription |  |


<a id="getSubscription"></a>
# **getSubscription**
> SubscriptionResponse getSubscription(limit, continuationToken)



This method retrieves a list of subscriptions associated with the seller account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/account/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionApi apiInstance = new SubscriptionApi(defaultClient);
    String limit = "limit_example"; // String | This field is for future use.
    String continuationToken = "continuationToken_example"; // String | This field is for future use.
    try {
      SubscriptionResponse result = apiInstance.getSubscription(limit, continuationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionApi#getSubscription");
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
| **limit** | **String**| This field is for future use. | [optional] |
| **continuationToken** | **String**| This field is for future use. | [optional] |

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

