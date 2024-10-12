# AirTrafficApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAirTraffic**](AirTrafficApi.md#getAirTraffic) | **GET** /travel/analytics/air-traffic/busiest-period | Returns a list of air traffic reports. |


<a id="getAirTraffic"></a>
# **getAirTraffic**
> Success getAirTraffic(cityCode, period, direction)

Returns a list of air traffic reports.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirTrafficApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    AirTrafficApi apiInstance = new AirTrafficApi(defaultClient);
    String cityCode = "MAD"; // String | Code for the city following IATA standard. [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. BOS for Boston
    String period = "2017"; // String | time period (year) of the statistics.  Year for which the statistic are requested following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 
    String direction = "ARRIVING"; // String | Use ARRIVING to have statistics on travelers coming to the city or DEPARTING for statistics on travelers leaving the city.  By default, statistics are given on travelers ARRIVING the city. 
    try {
      Success result = apiInstance.getAirTraffic(cityCode, period, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirTrafficApi#getAirTraffic");
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
| **cityCode** | **String**| Code for the city following IATA standard. [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. BOS for Boston | |
| **period** | **String**| time period (year) of the statistics.  Year for which the statistic are requested following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)  | |
| **direction** | **String**| Use ARRIVING to have statistics on travelers coming to the city or DEPARTING for statistics on travelers leaving the city.  By default, statistics are given on travelers ARRIVING the city.  | [optional] [default to ARRIVING] [enum: ARRIVING, DEPARTING] |

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
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION 2781    | INVALID LENGTH 4926    | INVALID DATA RECEIVED 32171   | MANDATORY DATA MISSING  |  -  |
| **0** | Unexpected Error |  -  |

