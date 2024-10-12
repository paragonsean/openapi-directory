# DisplaySeatMapsApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSeatmapFromFlightOffer**](DisplaySeatMapsApi.md#getSeatmapFromFlightOffer) | **POST** /shopping/seatmaps | Returns all the seat maps of a given flightOffer. |
| [**getSeatmapFromOrder**](DisplaySeatMapsApi.md#getSeatmapFromOrder) | **GET** /shopping/seatmaps | Returns all the seat maps of a given order. |


<a id="getSeatmapFromFlightOffer"></a>
# **getSeatmapFromFlightOffer**
> SeatMapReply getSeatmapFromFlightOffer(xHTTPMethodOverride, body)

Returns all the seat maps of a given flightOffer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisplaySeatMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    DisplaySeatMapsApi apiInstance = new DisplaySeatMapsApi(defaultClient);
    String xHTTPMethodOverride = "GET"; // String | the HTTP method to apply
    FlightOffers body = new FlightOffers(); // FlightOffers | 
    try {
      SeatMapReply result = apiInstance.getSeatmapFromFlightOffer(xHTTPMethodOverride, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisplaySeatMapsApi#getSeatmapFromFlightOffer");
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
| **xHTTPMethodOverride** | **String**| the HTTP method to apply | [default to GET] |
| **body** | [**FlightOffers**](FlightOffers.md)|  | |

### Return type

[**SeatMapReply**](SeatMapReply.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.amadeus+json
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title ------- | ------------------------------------- 477     | INVALID FORMAT 2781    | INVALID LENGHT 572     | INVALID OPTION 4481    | FLIGHT DOES NOT OPERATE ON DATE REQUESTED 8791    | SEAT MAP DISPLAY REQUEST IS OUTSIDE SYSTEM DATE RANGE 32171   | MANDATORY DATA MISSING  |  -  |
| **0** | Unexpected Error |  -  |

<a id="getSeatmapFromOrder"></a>
# **getSeatmapFromOrder**
> SeatMapReply getSeatmapFromOrder(flightOrderId, flightOrderId2)

Returns all the seat maps of a given order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisplaySeatMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    DisplaySeatMapsApi apiInstance = new DisplaySeatMapsApi(defaultClient);
    String flightOrderId = "flightOrderId_example"; // String | identifier of the order
    String flightOrderId2 = "flightOrderId_example"; // String | DEPRECATED identifier of the order , kept for backward compatibility
    try {
      SeatMapReply result = apiInstance.getSeatmapFromOrder(flightOrderId, flightOrderId2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisplaySeatMapsApi#getSeatmapFromOrder");
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
| **flightOrderId** | **String**| identifier of the order | [optional] |
| **flightOrderId2** | **String**| DEPRECATED identifier of the order , kept for backward compatibility | [optional] |

### Return type

[**SeatMapReply**](SeatMapReply.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title ------- | ------------------------------------- 477     | INVALID FORMAT 572     | INVALID OPTION 4481    | FLIGHT DOES NOT OPERATE ON DATE REQUESTED 8791    | SEAT MAP DISPLAY REQUEST IS OUTSIDE SYSTEM DATE RANGE 32171   | MANDATORY DATA MISSING  |  -  |
| **404** | Not Found |  -  |
| **0** | Unexpected Error |  -  |

