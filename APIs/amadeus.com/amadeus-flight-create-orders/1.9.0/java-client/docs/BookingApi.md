# BookingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFligtOrders**](BookingApi.md#createFligtOrders) | **POST** /booking/flight-orders | Create Order associated to the Flight offers. |


<a id="createFligtOrders"></a>
# **createFligtOrders**
> SuccessBooking createFligtOrders(body)

Create Order associated to the Flight offers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    BookingApi apiInstance = new BookingApi(defaultClient);
    FlightOrderQuery body = new FlightOrderQuery(); // FlightOrderQuery | list of element needed to book a flight Order
    try {
      SuccessBooking result = apiInstance.createFligtOrders(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingApi#createFligtOrders");
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
| **body** | [**FlightOrderQuery**](FlightOrderQuery.md)| list of element needed to book a flight Order | |

### Return type

[**SuccessBooking**](SuccessBooking.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.amadeus+json
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 1304    | CREDIT CARD NOT ACCEPTED 2781    | INVALID LENGTH 4926    | INVALID DATA RECEIVED 9112    | TICKETING - TKT 2668    | PARAMETER COMBINATION INVALID/RESTRICTED 32171   | MANDATORY DATA MISSING 34107   | NOT APPLICABLE FARE 34651   | SEGMENT SELL FAILURE 34733   | VIRTUAL CARD CREATION FAILED 36870   | BOOKING FAILED 37200   | PRICE DISCREPANCY 38034   | ONE OR MORE SERVICES ARE NOT AVAILABLE  |  -  |
| **0** | Unexpected error |  -  |

