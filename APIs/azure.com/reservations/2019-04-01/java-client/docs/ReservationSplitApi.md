# ReservationSplitApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationSplit**](ReservationSplitApi.md#reservationSplit) | **POST** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/split | Split the &#x60;Reservation&#x60;. |


<a id="reservationSplit"></a>
# **reservationSplit**
> List&lt;ReservationResponse&gt; reservationSplit(reservationOrderId, apiVersion, body)

Split the &#x60;Reservation&#x60;.

Split a &#x60;Reservation&#x60; into two &#x60;Reservation&#x60;s with specified quantity distribution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationSplitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationSplitApi apiInstance = new ReservationSplitApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    SplitRequest body = new SplitRequest(); // SplitRequest | Information needed to Split a reservation item
    try {
      List<ReservationResponse> result = apiInstance.reservationSplit(reservationOrderId, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationSplitApi#reservationSplit");
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
| **body** | [**SplitRequest**](SplitRequest.md)| Information needed to Split a reservation item | |

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
| **200** | List of &#x60;Reservation&#x60;s created after the split operation. |  -  |
| **202** | The request is accepted and is being processed |  -  |
| **0** | Unexpected error |  -  |

