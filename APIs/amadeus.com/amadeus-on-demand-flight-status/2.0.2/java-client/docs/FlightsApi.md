# FlightsApi

All URIs are relative to *https://test.api.amadeus.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFlightsStatus**](FlightsApi.md#getFlightsStatus) | **GET** /schedule/flights | Retrieves a unique flight by search criteria. |


<a id="getFlightsStatus"></a>
# **getFlightsStatus**
> SuccessFlights getFlightsStatus(carrierCode, flightNumber, scheduledDepartureDate, operationalSuffix)

Retrieves a unique flight by search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v2");

    FlightsApi apiInstance = new FlightsApi(defaultClient);
    String carrierCode = "TP"; // String | 2 to 3-character IATA carrier code ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)). 
    String flightNumber = "487"; // String | 1 to 4-digit number of the flight. e.g. 4537
    LocalDate scheduledDepartureDate = LocalDate.parse("2023-08-01"); // LocalDate | scheduled departure date of the flight, local to the departure airport, format YYYY-MM-DD.
    String operationalSuffix = "operationalSuffix_example"; // String | 1-letter operational suffix assigned by the carrier to differentiate flight in case of delay changing the departure date e.g. A 
    try {
      SuccessFlights result = apiInstance.getFlightsStatus(carrierCode, flightNumber, scheduledDepartureDate, operationalSuffix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlightsApi#getFlightsStatus");
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
| **carrierCode** | **String**| 2 to 3-character IATA carrier code ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)).  | |
| **flightNumber** | **String**| 1 to 4-digit number of the flight. e.g. 4537 | |
| **scheduledDepartureDate** | **LocalDate**| scheduled departure date of the flight, local to the departure airport, format YYYY-MM-DD. | |
| **operationalSuffix** | **String**| 1-letter operational suffix assigned by the carrier to differentiate flight in case of delay changing the departure date e.g. A  | [optional] |

### Return type

[**SuccessFlights**](SuccessFlights.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of dated flights |  -  |
| **400** | code    | title ------- | ------------------------------------- 477     | INVALID FORMAT 572     | INVALID OPTION 2781    | INVALID LENGTH 4926    | INVALID DATA RECEIVED 32171   | MANDATORY DATA MISSING  |  -  |
| **401** | Unauthorized |  -  |
| **0** | Unexpected Error |  -  |

