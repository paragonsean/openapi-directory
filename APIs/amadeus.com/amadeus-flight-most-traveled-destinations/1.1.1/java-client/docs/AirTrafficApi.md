# AirTrafficApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAirTraffic**](AirTrafficApi.md#getAirTraffic) | **GET** /travel/analytics/air-traffic/traveled | Returns a list of air traffic reports. |


<a id="getAirTraffic"></a>
# **getAirTraffic**
> Success getAirTraffic(originCityCode, period, max, fields, pageLimit, pageOffset, sort)

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
    String originCityCode = "MAD"; // String | Code for the origin city following IATA standard ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)). - e.g. BOS for Boston
    String period = "2017-01"; // String | period when consumers are traveling. * It can be a month only.  * [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format must be used - e.g. 2015-05.  * Period ranges are not supported.  * Only periods from 2011-01 up to previous month are valid.  * Future dates are not supported. 
    BigDecimal max = new BigDecimal("10.0"); // BigDecimal | maximum number of destinations in the response. Default value is **10** and maximum value is 50.
    String fields = "fields_example"; // String | list of attributes desired in the response or list of attributes to remove from the response (with \"-\" before fields)  * The attributes names must contain the whole path (except resource name) e.g. travelers
    Integer pageLimit = 10; // Integer | maximum items in one page
    Integer pageOffset = 0; // Integer | start index of the requested page
    String sort = "analytics.flights.score"; // String | defines on which attribute the sorting will be done: * **analytics.flights.score** - sort destination by flights score (decreasing) * **analytics.travelers.score** - sort destination by traveler's score (decreasing) 
    try {
      Success result = apiInstance.getAirTraffic(originCityCode, period, max, fields, pageLimit, pageOffset, sort);
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
| **originCityCode** | **String**| Code for the origin city following IATA standard ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)). - e.g. BOS for Boston | |
| **period** | **String**| period when consumers are traveling. * It can be a month only.  * [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format must be used - e.g. 2015-05.  * Period ranges are not supported.  * Only periods from 2011-01 up to previous month are valid.  * Future dates are not supported.  | |
| **max** | **BigDecimal**| maximum number of destinations in the response. Default value is **10** and maximum value is 50. | [optional] [default to 10.0] |
| **fields** | **String**| list of attributes desired in the response or list of attributes to remove from the response (with \&quot;-\&quot; before fields)  * The attributes names must contain the whole path (except resource name) e.g. travelers | [optional] |
| **pageLimit** | **Integer**| maximum items in one page | [optional] [default to 10] |
| **pageOffset** | **Integer**| start index of the requested page | [optional] [default to 0] |
| **sort** | **String**| defines on which attribute the sorting will be done: * **analytics.flights.score** - sort destination by flights score (decreasing) * **analytics.travelers.score** - sort destination by traveler&#39;s score (decreasing)  | [optional] [default to analytics.travelers.score] [enum: analytics.flights.score, analytics.travelers.score] |

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
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION 2781    | INVALID LENGTH 4926    | INVALID DATA RECEIVED                                32171   | MANDATORY DATA MISSING         |  -  |
| **0** | Unexpected Error |  -  |

