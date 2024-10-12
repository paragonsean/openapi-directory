# ReservationPurchaseApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationOrderPurchase**](ReservationPurchaseApi.md#reservationOrderPurchase) | **PUT** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId} | Purchase &#x60;ReservationOrder&#x60; |


<a id="reservationOrderPurchase"></a>
# **reservationOrderPurchase**
> ReservationOrderResponse reservationOrderPurchase(reservationOrderId, apiVersion, body)

Purchase &#x60;ReservationOrder&#x60;

Purchase &#x60;ReservationOrder&#x60; and create resource under the specified URI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationPurchaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationPurchaseApi apiInstance = new ReservationPurchaseApi(defaultClient);
    String reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    PurchaseRequest body = new PurchaseRequest(); // PurchaseRequest | Information needed for calculate or purchase reservation
    try {
      ReservationOrderResponse result = apiInstance.reservationOrderPurchase(reservationOrderId, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationPurchaseApi#reservationOrderPurchase");
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
| **body** | [**PurchaseRequest**](PurchaseRequest.md)| Information needed for calculate or purchase reservation | |

### Return type

[**ReservationOrderResponse**](ReservationOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource has been created |  -  |
| **202** | The request is accepted and is being processed. Operation result link is in location header. |  -  |
| **0** | Unexpected error |  -  |

