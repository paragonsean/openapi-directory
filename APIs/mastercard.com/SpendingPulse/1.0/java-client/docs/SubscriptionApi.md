# SubscriptionApi

All URIs are relative to *https://api.mastercard.com/spendingpulse/v1/spulse.svc*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionGet**](SubscriptionApi.md#subscriptionGet) | **GET** /subscription | Returns a list of all reports one is currently subscribed to. |


<a id="subscriptionGet"></a>
# **subscriptionGet**
> SubscriptionListResponse subscriptionGet(currentRow, offset)

Returns a list of all reports one is currently subscribed to.

Returns a list of all reports one is currently subscribed to. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/spendingpulse/v1/spulse.svc");

    SubscriptionApi apiInstance = new SubscriptionApi(defaultClient);
    String currentRow = "1"; // String | Starting record number to return.
    String offset = "25"; // String | Used to restrict the number of records returned if needed to be less than max.
    try {
      SubscriptionListResponse result = apiInstance.subscriptionGet(currentRow, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionApi#subscriptionGet");
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
| **currentRow** | **String**| Starting record number to return. | [optional] |
| **offset** | **String**| Used to restrict the number of records returned if needed to be less than max. | [optional] |

### Return type

[**SubscriptionListResponse**](SubscriptionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of subscriptions. |  -  |
| **0** | Unexpected errors |  -  |

