# BookingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelFlightOrder**](BookingApi.md#cancelFlightOrder) | **DELETE** /booking/flight-orders/{flight-orderId} | Cancel a given flight order |
| [**getFlightOrder**](BookingApi.md#getFlightOrder) | **GET** /booking/flight-orders/{flight-orderId} | Retrieve a given flight order |


<a id="cancelFlightOrder"></a>
# **cancelFlightOrder**
> cancelFlightOrder(flightOrderId)

Cancel a given flight order

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
    String flightOrderId = "flightOrderId_example"; // String | identifier of the flight order
    try {
      apiInstance.cancelFlightOrder(flightOrderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingApi#cancelFlightOrder");
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
| **flightOrderId** | **String**| identifier of the flight order | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully Deleted |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  4926    | INVALID DATA RECEIVED 32171   | MANDATORY DATA MISSING  |  -  |
| **404** | Not Found |  -  |
| **0** | Unexpected error |  -  |

<a id="getFlightOrder"></a>
# **getFlightOrder**
> SuccessBooking getFlightOrder(flightOrderId)

Retrieve a given flight order

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
    String flightOrderId = "flightOrderId_example"; // String | identifier of the flight order
    try {
      SuccessBooking result = apiInstance.getFlightOrder(flightOrderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingApi#getFlightOrder");
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
| **flightOrderId** | **String**| identifier of the flight order | |

### Return type

[**SuccessBooking**](SuccessBooking.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 4926    | INVALID DATA RECEIVED 32171   | MANDATORY DATA MISSING  |  -  |
| **404** | Not Found |  -  |
| **0** | Unexpected error |  -  |

