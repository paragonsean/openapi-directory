# AirportOntimePredictionApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAirportOnTimePrediction**](AirportOntimePredictionApi.md#getAirportOnTimePrediction) | **GET** /airport/predictions/on-time | Returns a percentage of on-time flight departures from a given airport. |


<a id="getAirportOnTimePrediction"></a>
# **getAirportOnTimePrediction**
> Prediction getAirportOnTimePrediction(airportCode, date)

Returns a percentage of on-time flight departures from a given airport.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirportOntimePredictionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    AirportOntimePredictionApi apiInstance = new AirportOntimePredictionApi(defaultClient);
    String airportCode = "JFK"; // String | airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx), e.g. BOS for Boston
    LocalDate date = LocalDate.parse("2023-11-12"); // LocalDate | the date on which the traveler will depart from the give airport. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
    try {
      Prediction result = apiInstance.getAirportOnTimePrediction(airportCode, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirportOntimePredictionApi#getAirportOnTimePrediction");
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
| **airportCode** | **String**| airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx), e.g. BOS for Boston | |
| **date** | **LocalDate**| the date on which the traveler will depart from the give airport. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25 | |

### Return type

[**Prediction**](Prediction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION 4926    | INVALID DATA RECEIVED                32171   | MANDATORY DATA MISSING         |  -  |
| **0** | Unexpected Error |  -  |

