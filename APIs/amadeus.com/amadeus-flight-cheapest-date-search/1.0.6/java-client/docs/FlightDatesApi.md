# FlightDatesApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFlightDates**](FlightDatesApi.md#getFlightDates) | **GET** /shopping/flight-dates | Find the cheapest flight dates from an origin to a destination. |


<a id="getFlightDates"></a>
# **getFlightDates**
> FlightDates getFlightDates(origin, destination, departureDate, oneWay, duration, nonStop, maxPrice, viewBy)

Find the cheapest flight dates from an origin to a destination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlightDatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    FlightDatesApi apiInstance = new FlightDatesApi(defaultClient);
    String origin = "MAD"; // String | IATA code of the city from which the flight will depart  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. MAD for Madrid 
    String destination = "MUC"; // String | IATA code of the city to which the flight is going.  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. MUC for Munich 
    String departureDate = "departureDate_example"; // String | the date, or range of dates, on which the flight will depart from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25. Ranges are specified with a comma and are inclusive
    Boolean oneWay = false; // Boolean | if this parameter is set to true, only one-way flights are considered. If this parameter is not set or set to false, only round-trip flights are considered
    String duration = "duration_example"; // String | exact duration or range of durations of the travel, in days. This parameter must not be set if oneWay is true. Ranges are specified with a comma and are inclusive, e.g. 2,8
    Boolean nonStop = false; // Boolean | if this parameter is set to true, only flights going from the origin to the destination with no stop in-between are considered
    Long maxPrice = 56L; // Long | defines the price limit for each offer returned. The value should be a positive number, without decimals
    String viewBy = "DATE"; // String | view the flight dates by DATE, DURATION, or WEEK. View by DATE (default when oneWay is true) to get the cheapest flight dates for every departure date in the given range. View by DURATION (default when oneWay is false) to get the cheapest flight dates for every departure date and for every duration in the given ranges. View by WEEK to get the cheapest flight destination for every week in the given range of departure dates. Note that specifying a detailed view but large ranges may result in a huge number of flight dates being returned. For some very large numbers of flight dates, the API may refuse to provide a response
    try {
      FlightDates result = apiInstance.getFlightDates(origin, destination, departureDate, oneWay, duration, nonStop, maxPrice, viewBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlightDatesApi#getFlightDates");
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
| **origin** | **String**| IATA code of the city from which the flight will depart  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. MAD for Madrid  | |
| **destination** | **String**| IATA code of the city to which the flight is going.  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. MUC for Munich  | |
| **departureDate** | **String**| the date, or range of dates, on which the flight will depart from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25. Ranges are specified with a comma and are inclusive | [optional] |
| **oneWay** | **Boolean**| if this parameter is set to true, only one-way flights are considered. If this parameter is not set or set to false, only round-trip flights are considered | [optional] [default to false] |
| **duration** | **String**| exact duration or range of durations of the travel, in days. This parameter must not be set if oneWay is true. Ranges are specified with a comma and are inclusive, e.g. 2,8 | [optional] |
| **nonStop** | **Boolean**| if this parameter is set to true, only flights going from the origin to the destination with no stop in-between are considered | [optional] [default to false] |
| **maxPrice** | **Long**| defines the price limit for each offer returned. The value should be a positive number, without decimals | [optional] |
| **viewBy** | **String**| view the flight dates by DATE, DURATION, or WEEK. View by DATE (default when oneWay is true) to get the cheapest flight dates for every departure date in the given range. View by DURATION (default when oneWay is false) to get the cheapest flight dates for every departure date and for every duration in the given ranges. View by WEEK to get the cheapest flight destination for every week in the given range of departure dates. Note that specifying a detailed view but large ranges may result in a huge number of flight dates being returned. For some very large numbers of flight dates, the API may refuse to provide a response | [optional] [enum: DATE, DURATION, WEEK] |

### Return type

[**FlightDates**](FlightDates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  425     | INVALID DATE 477     | INVALID FORMAT 2668    | PARAMETER COMBINATION INVALID/RESTRICTED 4926    | INVALID DATA RECEIVED 32171   | MANDATORY DATA MISSING  |  -  |
| **404** | code    | title                                  ------- | -------------------------------------  6003    | ITEM/DATA NOT FOUND OR DATA NOT EXISTING  |  -  |
| **500** | Unexpected error |  -  |

