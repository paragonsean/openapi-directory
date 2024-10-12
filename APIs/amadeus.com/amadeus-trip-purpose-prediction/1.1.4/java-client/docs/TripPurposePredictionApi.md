# TripPurposePredictionApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTripPurposePrediction**](TripPurposePredictionApi.md#getTripPurposePrediction) | **GET** /travel/predictions/trip-purpose | Returns the forecast purpose of a trip |


<a id="getTripPurposePrediction"></a>
# **getTripPurposePrediction**
> Prediction getTripPurposePrediction(originLocationCode, destinationLocationCode, departureDate, returnDate, searchDate)

Returns the forecast purpose of a trip

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TripPurposePredictionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    TripPurposePredictionApi apiInstance = new TripPurposePredictionApi(defaultClient);
    String originLocationCode = "NYC"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler will depart, e.g. BOS for Boston
    String destinationLocationCode = "MAD"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris
    String departureDate = "2023-12-01"; // String | the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25
    String returnDate = "2023-12-12"; // String | the date on which the traveler will depart from the destination to return to the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28
    String searchDate = "searchDate_example"; // String | the date on which the traveler is performing the search. If this parameter is not specified, current date will be used. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28
    try {
      Prediction result = apiInstance.getTripPurposePrediction(originLocationCode, destinationLocationCode, departureDate, returnDate, searchDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TripPurposePredictionApi#getTripPurposePrediction");
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
| **originLocationCode** | **String**| city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler will depart, e.g. BOS for Boston | |
| **destinationLocationCode** | **String**| city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris | |
| **departureDate** | **String**| the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25 | |
| **returnDate** | **String**| the date on which the traveler will depart from the destination to return to the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28 | |
| **searchDate** | **String**| the date on which the traveler is performing the search. If this parameter is not specified, current date will be used. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28 | [optional] |

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

