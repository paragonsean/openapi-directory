# ApplyScopeApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationUpdate_0**](ApplyScopeApi.md#reservationUpdate_0) | **PATCH** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId} | Updates a &#x60;Reservation&#x60;. |


<a id="reservationUpdate_0"></a>
# **reservationUpdate_0**
> ReservationResponse reservationUpdate_0(reservationOrderId, reservationId, apiVersion, parameters)

Updates a &#x60;Reservation&#x60;.

Updates the applied scopes of the &#x60;Reservation&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplyScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ApplyScopeApi apiInstance = new ApplyScopeApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation 
    String reservationId = "reservationId_example"; // String | Id of the Reservation Item
    String apiVersion = "apiVersion_example"; // String | Supported version.
    Patch parameters = new Patch(); // Patch | Information needed to patch a reservation item
    try {
      ReservationResponse result = apiInstance.reservationUpdate_0(reservationOrderId, reservationId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplyScopeApi#reservationUpdate_0");
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
| **reservationOrderId** | **String**| Order Id of the reservation  | |
| **reservationId** | **String**| Id of the Reservation Item | |
| **apiVersion** | **String**| Supported version. | |
| **parameters** | [**Patch**](Patch.md)| Information needed to patch a reservation item | |

### Return type

[**ReservationResponse**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the updated &#x60;Reservation&#x60;. |  -  |
| **202** | The request is accepted and is being processed |  -  |
| **0** | Unexpected error |  -  |

