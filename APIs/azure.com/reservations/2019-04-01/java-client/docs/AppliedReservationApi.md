# AppliedReservationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAppliedReservationList**](AppliedReservationApi.md#getAppliedReservationList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Capacity/appliedReservations | Get list of applicable &#x60;Reservation&#x60;s. |


<a id="getAppliedReservationList"></a>
# **getAppliedReservationList**
> AppliedReservations getAppliedReservationList(apiVersion, subscriptionId)

Get list of applicable &#x60;Reservation&#x60;s.

Get applicable &#x60;Reservation&#x60;s that are applied to this subscription or a resource group under this subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppliedReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AppliedReservationApi apiInstance = new AppliedReservationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    String subscriptionId = "subscriptionId_example"; // String | Id of the subscription
    try {
      AppliedReservations result = apiInstance.getAppliedReservationList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppliedReservationApi#getAppliedReservationList");
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
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |
| **subscriptionId** | **String**| Id of the subscription | |

### Return type

[**AppliedReservations**](AppliedReservations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Applicable &#x60;Reservation&#x60;s. |  -  |
| **0** | Unexpected error |  -  |

