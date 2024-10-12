# FlightDelayPredictionApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFlightDelayPrediction**](FlightDelayPredictionApi.md#getFlightDelayPrediction) | **GET** /travel/predictions/flight-delay | Return the delay segment where the flight is likely to lay. |


<a id="getFlightDelayPrediction"></a>
# **getFlightDelayPrediction**
> Prediction getFlightDelayPrediction(originLocationCode, destinationLocationCode, departureDate, departureTime, arrivalDate, arrivalTime, aircraftCode, carrierCode, flightNumber, duration)

Return the delay segment where the flight is likely to lay.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlightDelayPredictionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    FlightDelayPredictionApi apiInstance = new FlightDelayPredictionApi(defaultClient);
    String originLocationCode = "NCE"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler is departing, e.g. PAR for Paris
    String destinationLocationCode = "IST"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris
    LocalDate departureDate = LocalDate.parse("2020-08-01"); // LocalDate | the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
    String departureTime = "66000"; // String | local time relative to originLocationCode on which the traveler will depart from the origin. Time respects ISO 8601 standard. e.g. 13:22:00
    LocalDate arrivalDate = LocalDate.parse("2020-08-01"); // LocalDate | the date on which the traveler will arrive to the destination from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
    String arrivalTime = "80100"; // String | local time relative to destinationLocationCode on which the traveler will arrive to destination. Time respects ISO 8601 standard. e.g. 13:22:00
    String aircraftCode = "321"; // String | IATA aircraft code (http://www.flugzeuginfo.net/table_accodes_iata_en.php)
    String carrierCode = "TK"; // String | airline / carrier code
    String flightNumber = "1816"; // String | flight number as assigned by the carrier
    String duration = "PT31H10M"; // String | flight duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
    try {
      Prediction result = apiInstance.getFlightDelayPrediction(originLocationCode, destinationLocationCode, departureDate, departureTime, arrivalDate, arrivalTime, aircraftCode, carrierCode, flightNumber, duration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlightDelayPredictionApi#getFlightDelayPrediction");
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
| **originLocationCode** | **String**| city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler is departing, e.g. PAR for Paris | |
| **destinationLocationCode** | **String**| city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris | |
| **departureDate** | **LocalDate**| the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25 | |
| **departureTime** | **String**| local time relative to originLocationCode on which the traveler will depart from the origin. Time respects ISO 8601 standard. e.g. 13:22:00 | |
| **arrivalDate** | **LocalDate**| the date on which the traveler will arrive to the destination from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25 | |
| **arrivalTime** | **String**| local time relative to destinationLocationCode on which the traveler will arrive to destination. Time respects ISO 8601 standard. e.g. 13:22:00 | |
| **aircraftCode** | **String**| IATA aircraft code (http://www.flugzeuginfo.net/table_accodes_iata_en.php) | |
| **carrierCode** | **String**| airline / carrier code | |
| **flightNumber** | **String**| flight number as assigned by the carrier | |
| **duration** | **String**| flight duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M | |

### Return type

[**Prediction**](Prediction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION 4926    | INVALID DATA RECEIVED                32171   | MANDATORY DATA MISSING         |  -  |
| **0** | Unexpected Error |  -  |

