# PriceMetricsApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getItineraryPriceMetrics**](PriceMetricsApi.md#getItineraryPriceMetrics) | **GET** /analytics/itinerary-price-metrics | GET itinerary price metric |


<a id="getItineraryPriceMetrics"></a>
# **getItineraryPriceMetrics**
> GetItineraryPriceMetrics200Response getItineraryPriceMetrics(originIataCode, destinationIataCode, departureDate, currencyCode, oneWay)

GET itinerary price metric



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceMetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    PriceMetricsApi apiInstance = new PriceMetricsApi(defaultClient);
    String originIataCode = "MAD"; // String | airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), from which the traveler will depart 
    String destinationIataCode = "CDG"; // String | airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), to which the traveler is going.
    String departureDate = "2021-03-21"; // String | The date on which the traveler will depart from the origin to go to the destination.   Dates are specified in the[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format.
    String currencyCode = "EUR"; // String | the preferred currency for display. Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro
    Boolean oneWay = false; // Boolean | true to get price metrics for a one way trip, false to get price metrics for a round trip
    try {
      GetItineraryPriceMetrics200Response result = apiInstance.getItineraryPriceMetrics(originIataCode, destinationIataCode, departureDate, currencyCode, oneWay);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceMetricsApi#getItineraryPriceMetrics");
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
| **originIataCode** | **String**| airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), from which the traveler will depart  | |
| **destinationIataCode** | **String**| airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), to which the traveler is going. | |
| **departureDate** | **String**| The date on which the traveler will depart from the origin to go to the destination.   Dates are specified in the[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format. | |
| **currencyCode** | **String**| the preferred currency for display. Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro | [optional] [default to EUR] |
| **oneWay** | **Boolean**| true to get price metrics for a one way trip, false to get price metrics for a round trip | [optional] [default to false] |

### Return type

[**GetItineraryPriceMetrics200Response**](GetItineraryPriceMetrics200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful reply |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION                             32171   | MANDATORY DATA MISSING  |  -  |
| **500** | Internal Server Error |  -  |

