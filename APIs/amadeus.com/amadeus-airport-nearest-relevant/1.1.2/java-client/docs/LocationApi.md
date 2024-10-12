# LocationApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNearestRelevantAirports**](LocationApi.md#getNearestRelevantAirports) | **GET** /reference-data/locations/airports | Returns a list of relevant airports near to a given point. |


<a id="getNearestRelevantAirports"></a>
# **getNearestRelevantAirports**
> Success getNearestRelevantAirports(latitude, longitude, radius, pageLimit, pageOffset, sort)

Returns a list of relevant airports near to a given point.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    LocationApi apiInstance = new LocationApi(defaultClient);
    Double latitude = 51.57285D; // Double | latitude location to be at the center of the search circle
    Double longitude = -0.44161D; // Double | longitude location to be at the center of the search circle
    Integer radius = 500; // Integer | radius of the search in Kilometer. Can be from 0 to 500, default value is 500 Km.
    Integer pageLimit = 10; // Integer | maximum items in one page
    Integer pageOffset = 0; // Integer | start index of the requested page
    String sort = "relevance"; // String | defines on which attribute the sorting will be done from the best option to the worst one: * **relevance** - Score value calculated based on distance and traffic analytics * **distance** - Distance from the location to the geo-code given in API request parameters * **analytics.flights.score** - Approximate score for ranking purposes calculated based on estimated number of flights from/to airport in one reference year (last year) * **analytics.travelers.score** - Approximate score for ranking purposes calculated based on estimated number of travelers in the airport for one reference year (last year) 
    try {
      Success result = apiInstance.getNearestRelevantAirports(latitude, longitude, radius, pageLimit, pageOffset, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#getNearestRelevantAirports");
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
| **latitude** | **Double**| latitude location to be at the center of the search circle | |
| **longitude** | **Double**| longitude location to be at the center of the search circle | |
| **radius** | **Integer**| radius of the search in Kilometer. Can be from 0 to 500, default value is 500 Km. | [optional] [default to 500] |
| **pageLimit** | **Integer**| maximum items in one page | [optional] [default to 10] |
| **pageOffset** | **Integer**| start index of the requested page | [optional] [default to 0] |
| **sort** | **String**| defines on which attribute the sorting will be done from the best option to the worst one: * **relevance** - Score value calculated based on distance and traffic analytics * **distance** - Distance from the location to the geo-code given in API request parameters * **analytics.flights.score** - Approximate score for ranking purposes calculated based on estimated number of flights from/to airport in one reference year (last year) * **analytics.travelers.score** - Approximate score for ranking purposes calculated based on estimated number of travelers in the airport for one reference year (last year)  | [optional] [default to relevance] [enum: relevance, distance, analytics.flights.score, analytics.travelers.score] |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION 4926    | INVALID DATA RECEIVED                32171   | MANDATORY DATA MISSING         |  -  |
| **0** | Unexpected Error |  -  |

