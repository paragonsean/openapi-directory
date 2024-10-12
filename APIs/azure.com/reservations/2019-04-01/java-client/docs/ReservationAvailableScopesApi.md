# ReservationAvailableScopesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationAvailableScopes**](ReservationAvailableScopesApi.md#reservationAvailableScopes) | **POST** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}/availableScopes | Get Available Scopes for &#x60;Reservation&#x60;. |


<a id="reservationAvailableScopes"></a>
# **reservationAvailableScopes**
> Properties reservationAvailableScopes(reservationOrderId, reservationId, apiVersion, body)

Get Available Scopes for &#x60;Reservation&#x60;.

Get Available Scopes for &#x60;Reservation&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationAvailableScopesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationAvailableScopesApi apiInstance = new ReservationAvailableScopesApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String reservationId = "reservationId_example"; // String | Id of the Reservation Item
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    List<String> body = Arrays.asList(); // List<String> | 
    try {
      Properties result = apiInstance.reservationAvailableScopes(reservationOrderId, reservationId, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationAvailableScopesApi#reservationAvailableScopes");
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
| **reservationId** | **String**| Id of the Reservation Item | |
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |
| **body** | [**List&lt;String&gt;**](String.md)|  | |

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of &#x60;Subscription&#x60;s created after the filter. |  -  |
| **0** | Unexpected error |  -  |

