# ReservationMergeApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationMerge**](ReservationMergeApi.md#reservationMerge) | **POST** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/merge | Merges two &#x60;Reservation&#x60;s. |


<a id="reservationMerge"></a>
# **reservationMerge**
> List&lt;ReservationResponse&gt; reservationMerge(reservationOrderId, apiVersion, body)

Merges two &#x60;Reservation&#x60;s.

Merge the specified &#x60;Reservation&#x60;s into a new &#x60;Reservation&#x60;. The two &#x60;Reservation&#x60;s being merged must have same properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationMergeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationMergeApi apiInstance = new ReservationMergeApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    MergeRequest body = new MergeRequest(); // MergeRequest | Information needed for commercial request for a reservation
    try {
      List<ReservationResponse> result = apiInstance.reservationMerge(reservationOrderId, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationMergeApi#reservationMerge");
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
| **reservationOrderId** | **String**| Order Id of the reservation | |
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |
| **body** | [**MergeRequest**](MergeRequest.md)| Information needed for commercial request for a reservation | |

### Return type

[**List&lt;ReservationResponse&gt;**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the &#x60;Reservation&#x60; created after the merge. |  -  |
| **202** | The request is accepted and is being processed |  -  |
| **0** | Unexpected error |  -  |

