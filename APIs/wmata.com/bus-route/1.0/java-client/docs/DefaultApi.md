# DefaultApi

All URIs are relative to *http://api.wmata.com/Bus.svc*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**call5476362a281d830c946a3d68**](DefaultApi.md#call5476362a281d830c946a3d68) | **GET** /json/jBusPositions | JSON - Bus Position |
| [**call5476362a281d830c946a3d69**](DefaultApi.md#call5476362a281d830c946a3d69) | **GET** /json/jRouteDetails | JSON - Path Details |
| [**call5476362a281d830c946a3d6a**](DefaultApi.md#call5476362a281d830c946a3d6a) | **GET** /json/jRoutes | JSON - Routes |
| [**call5476362a281d830c946a3d6b**](DefaultApi.md#call5476362a281d830c946a3d6b) | **GET** /json/jRouteSchedule | JSON - Schedule |
| [**call5476362a281d830c946a3d6c**](DefaultApi.md#call5476362a281d830c946a3d6c) | **GET** /json/jStopSchedule | JSON - Schedule at Stop |
| [**call5476362a281d830c946a3d6d**](DefaultApi.md#call5476362a281d830c946a3d6d) | **GET** /json/jStops | JSON - Stop Search |
| [**call5476362a281d830c946a3d6e**](DefaultApi.md#call5476362a281d830c946a3d6e) | **GET** /BusPositions | XML - Bus Position |
| [**call5476362a281d830c946a3d6f**](DefaultApi.md#call5476362a281d830c946a3d6f) | **GET** /RouteDetails | XML - Path Details |
| [**call5476362a281d830c946a3d70**](DefaultApi.md#call5476362a281d830c946a3d70) | **GET** /Routes | XML - Routes |
| [**call5476362a281d830c946a3d71**](DefaultApi.md#call5476362a281d830c946a3d71) | **GET** /RouteSchedule | XML - Schedule |
| [**call5476362a281d830c946a3d72**](DefaultApi.md#call5476362a281d830c946a3d72) | **GET** /StopSchedule | XML - Schedule at Stop |
| [**call5476362a281d830c946a3d73**](DefaultApi.md#call5476362a281d830c946a3d73) | **GET** /Stops | XML - Stop Search |


<a id="call5476362a281d830c946a3d68"></a>
# **call5476362a281d830c946a3d68**
> call5476362a281d830c946a3d68(routeID, lat, lon, radius)

JSON - Bus Position

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;  &lt;p&gt;Returns bus positions for the given route, with an optional search radius. If no parameters are specified, all bus positions are returned.&lt;/p&gt;  &lt;p&gt;Note that the RouteID parameter accepts only base route names and no variations, i.e.: use 10A instead of 10Av1 or 10Av2.&lt;/p&gt;  &lt;p&gt;Bus positions are refreshed approximately every &lt;span style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;20 to 30&lt;/span&gt; 7 to 10 seconds.&lt;/p&gt;  &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;  &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt; &lt;thead&gt; &lt;tr&gt; &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;  &lt;th&gt;Description&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt;  &lt;tbody&gt; &lt;tr&gt; &lt;td&gt;BusPositions&lt;/td&gt;  &lt;td&gt; Array containing bus position information (&lt;a href&#x3D; \&quot;#BusPosition\&quot;&gt;BusPositions&lt;/a&gt;). &lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td colspan&#x3D;\&quot;2\&quot;&gt; &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt; &lt;a id&#x3D;\&quot;BusPosition\&quot; name&#x3D;\&quot;BusPosition\&quot;&gt;BusPosition Elements&lt;/a&gt; &lt;/div&gt; &lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;DateTime&lt;/td&gt;  &lt;td&gt;Date and time (Eastern Standard Time) of last position update. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T13:23:40).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;Deviation&lt;/td&gt;  &lt;td&gt;Deviation, in minutes, from schedule. Positive values indicate that the bus is running late while negative ones are for buses running ahead of schedule.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DirectionNum&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; Use the DirectionText for a customer-friendly description of direction.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;DirectionText&lt;/td&gt;  &lt;td&gt;General direction of the trip, not the bus itself (e.g.: NORTH, SOUTH, EAST, WEST).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;Lat&lt;/td&gt;  &lt;td&gt;Last reported Latitude of the bus.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;Lon&lt;/td&gt;  &lt;td&gt;Last reported Longitude of the bus.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;RouteID&lt;/td&gt;  &lt;td&gt;Base route name as shown on the bus. Note that the base route name could also refer to any variant, so a RouteID of 10A could refer to 10A, 10Av1, 10Av2, etc.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;TripEndTime&lt;/td&gt;  &lt;td&gt;Scheduled end date and time (Eastern Standard Time) of the bus&#39;s current trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T13:17:00).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;TripHeadsign&lt;/td&gt;  &lt;td&gt;Destination of the bus.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;TripID&lt;/td&gt;  &lt;td&gt;Unique trip ID. This can be correlated with the data returned from the schedule-related methods.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;TripStartTime&lt;/td&gt;  &lt;td&gt;Scheduled start date and time (Eastern Standard Time) of the bus&#39;s current trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T12:40:00).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;VehicleID&lt;/td&gt;  &lt;td&gt;Unique identifier for the bus. This is usually visible on the bus itself.&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String routeID = "70"; // String | Base bus route, e.g.: 70, 10A.
    BigDecimal lat = new BigDecimal(78); // BigDecimal | Center point Latitude, required if Longitude and Radius are specified.
    BigDecimal lon = new BigDecimal(78); // BigDecimal | Center point Longitude, required if Latitude and Radius are specified.
    BigDecimal radius = new BigDecimal(78); // BigDecimal | Radius (meters) to include in the search area, required if Latitude and Longitude are specified.
    try {
      apiInstance.call5476362a281d830c946a3d68(routeID, lat, lon, radius);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d68");
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
| **routeID** | **String**| Base bus route, e.g.: 70, 10A. | [optional] [default to 70] [enum: 70] |
| **lat** | **BigDecimal**| Center point Latitude, required if Longitude and Radius are specified. | [optional] |
| **lon** | **BigDecimal**| Center point Longitude, required if Latitude and Radius are specified. | [optional] |
| **radius** | **BigDecimal**| Radius (meters) to include in the search area, required if Latitude and Longitude are specified. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default return code. |  -  |

<a id="call5476362a281d830c946a3d69"></a>
# **call5476362a281d830c946a3d69**
> call5476362a281d830c946a3d69(routeID, date)

JSON - Path Details

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;For a given date, returns the set of ordered latitude/longitude points along  a route variant along with the list of stops served.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Direction0/Direction1&lt;/td&gt;    &lt;td&gt;  Structures describing &lt;a href&#x3D;\&quot;#Direction\&quot;&gt;path/stop&lt;/a&gt;  information.&lt;br&gt;  &lt;br&gt;  Most routes will return content in both Direction0 and  Direction1 elements, though a few will return NULL for Direction0 or for Direction1.&lt;br&gt;  &lt;br&gt;  0 or 1 are binary properties. There is no specific mapping to  direction, but a different value for the same route signifies  that the route is in an opposite direction.  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Descriptive name for the route.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Bus route variant (e.g.: 10A, 10Av1, etc.).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Direction\&quot; name&#x3D;\&quot;Direction\&quot;&gt;Direction0/Direction1  Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DirectionNum&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; Use the  DirectionText element to denote the general direction of the route  variant.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionText&lt;/td&gt;    &lt;td&gt;General direction of the route variant (NORTH, SOUTH, EAST,  WEST, LOOP, etc.).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Shape&lt;/td&gt;    &lt;td&gt;  Array containing shape point information (&lt;a href&#x3D;  \&quot;#ShapePoint\&quot;&gt;ShapePoint&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Stops&lt;/td&gt;    &lt;td&gt;  Array containing stop information (&lt;a href&#x3D;\&quot;#Stop\&quot;&gt;Stop&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripHeadsign&lt;/td&gt;    &lt;td&gt;Descriptive text of where the bus is headed. This is similar,  but not necessarily identical, to what is displayed on the  bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;ShapePoint\&quot; name&#x3D;\&quot;ShapePoint\&quot;&gt;ShapePoint  Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lat&lt;/td&gt;    &lt;td&gt;Latitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lon&lt;/td&gt;    &lt;td&gt;Longitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;SeqNum&lt;/td&gt;    &lt;td&gt;Order of the point in the sequence of ShapePoints.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Stop\&quot; name&#x3D;\&quot;Stop\&quot;&gt;Stop Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lat&lt;/td&gt;    &lt;td&gt;Latitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lon&lt;/td&gt;    &lt;td&gt;Longitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Stop name. May be slightly different from what is spoken or  displayed in the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Routes&lt;/td&gt;    &lt;td&gt;String array of route variants which provide service at this  stop. Note that these are not date-specific; any route variant  which stops at this stop on any day will be listed.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopID&lt;/td&gt;    &lt;td&gt;7-digit regional ID which can be used in various bus-related  methods. If unavailable, the StopID will be 0 or NULL.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String routeID = "70"; // String | Bus route variant, e.g.: 70, 10A, 10Av1.
    String date = "date_example"; // String | Date in YYYY-MM-DD format for which to retrieve route and stop information.  Defaults to today's date unless specified.
    try {
      apiInstance.call5476362a281d830c946a3d69(routeID, date);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d69");
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
| **routeID** | **String**| Bus route variant, e.g.: 70, 10A, 10Av1. | [default to 70] [enum: 70] |
| **date** | **String**| Date in YYYY-MM-DD format for which to retrieve route and stop information.  Defaults to today&#39;s date unless specified. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

<a id="call5476362a281d830c946a3d6a"></a>
# **call5476362a281d830c946a3d6a**
> call5476362a281d830c946a3d6a()

JSON - Routes

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns a list of all bus route variants (patterns). For example, the 10A  and 10Av1 are the same route, but may stop at slightly different locations.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Routes&lt;/td&gt;    &lt;td&gt;  Array containing route variant information (&lt;a href&#x3D;  \&quot;#Route\&quot;&gt;Route&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Route\&quot; name&#x3D;\&quot;Route\&quot;&gt;Route Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Descriptive name of the route variant.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Unique identifier for a given route variant. Can be used in  various other bus-related methods.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;LineDescription&lt;/td&gt;    &lt;td&gt;Denotes the route variant’s grouping – lines are a combination of routes which lie in the same corridor and which have significant portions of their paths along the same roadways.&lt;/td&gt;  &lt;/tr&gt;   &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.call5476362a281d830c946a3d6a();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d6a");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response type. |  -  |

<a id="call5476362a281d830c946a3d6b"></a>
# **call5476362a281d830c946a3d6b**
> call5476362a281d830c946a3d6b(routeID, date, includingVariations)

JSON - Schedule

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns schedules for a given route variant for a given date.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Direction0/Direction1&lt;/td&gt;    &lt;td&gt;  Arrays containing trip information (&lt;a href&#x3D;  \&quot;#Trip\&quot;&gt;Trip&lt;/a&gt;).&lt;br&gt;  &lt;br&gt;  Most routes will return content in both Direction0 and  Direction1 elements, though a few (especially ones which run in  a loop, such as the U8) will return content only for Direction0  and NULL content for Direction1.&lt;br&gt;  &lt;br&gt;  0 or 1 are binary properties. There is no specific mapping to  direction, but a different value for the same route signifies  that the route is in an opposite direction.  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Descriptive name for the route.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Trip\&quot; name&#x3D;\&quot;Trip\&quot;&gt;Trip Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DirectionNum&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; Use the  TripDirectionText element to denote the general direction of the  trip.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;EndTime&lt;/td&gt;    &lt;td&gt;Scheduled end date and time (Eastern Standard Time) for this  trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Bus route variant. This can be used in several other bus  methods which accept variants.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StartTime&lt;/td&gt;    &lt;td&gt;Scheduled start date and time (Eastern Standard Time) for this  trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopTimes&lt;/td&gt;    &lt;td&gt;  Array containing location and time information (&lt;a href&#x3D;  \&quot;#StopTime\&quot;&gt;StopTime&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripDirectionText&lt;/td&gt;    &lt;td&gt;General direction of the trip (NORTH, SOUTH, EAST, WEST, LOOP,  etc.).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripHeadsign&lt;/td&gt;    &lt;td&gt;Descriptive text of where the bus is headed. This is similar,  but not necessarily identical, to what is displayed on the  bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripID&lt;/td&gt;    &lt;td&gt;Unique trip ID. This can be correlated with the data returned  from the schedule-related methods.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;StopTime\&quot; name&#x3D;\&quot;StopTime\&quot;&gt;StopTime Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopID&lt;/td&gt;    &lt;td&gt;7-digit regional ID which can be used in various bus-related  methods. If unavailable, the StopID will be 0 or NULL.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopName&lt;/td&gt;    &lt;td&gt;Stop name. May be slightly different from what is spoken or  displayed in the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopSeq&lt;/td&gt;    &lt;td&gt;Order of the stop in the sequence of StopTimes.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Time&lt;/td&gt;    &lt;td&gt;Scheduled departure date and time (Eastern Standard Time) from  this stop. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String routeID = "70"; // String | Bus route variant, e.g.: 70, 10A, 10Av1, etc.
    String date = "date_example"; // String | Date in YYYY-MM-DD format for which to retrieve schedule.  Defaults to today's date unless specified.
    Boolean includingVariations = false; // Boolean | Whether or not to include variations if a base route is specified in RouteID.  For example, if B30 is specified and IncludingVariations is set to true, data for all variations of B30 such as B30v1, B30v2, etc. will be returned.
    try {
      apiInstance.call5476362a281d830c946a3d6b(routeID, date, includingVariations);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d6b");
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
| **routeID** | **String**| Bus route variant, e.g.: 70, 10A, 10Av1, etc. | [default to 70] [enum: 70] |
| **date** | **String**| Date in YYYY-MM-DD format for which to retrieve schedule.  Defaults to today&#39;s date unless specified. | [optional] |
| **includingVariations** | **Boolean**| Whether or not to include variations if a base route is specified in RouteID.  For example, if B30 is specified and IncludingVariations is set to true, data for all variations of B30 such as B30v1, B30v2, etc. will be returned. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

<a id="call5476362a281d830c946a3d6c"></a>
# **call5476362a281d830c946a3d6c**
> call5476362a281d830c946a3d6c(stopID, date)

JSON - Schedule at Stop

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns a set of buses scheduled at a stop for a given date.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;ScheduleArrivals&lt;/td&gt;    &lt;td&gt;  Array containing scheduled arrival information (&lt;a href&#x3D;  \&quot;#ScheduleArrival\&quot;&gt;ScheduleArrival&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Stop&lt;/td&gt;    &lt;td&gt;  Structure describing &lt;a href&#x3D;\&quot;#Stop\&quot;&gt;stop&lt;/a&gt; information.  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;ScheduleArrival\&quot; name&#x3D;  \&quot;ScheduleArrival\&quot;&gt;ScheduleArrival Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionNum&lt;/td&gt;    &lt;td&gt;Denotes a binary direction (0 or 1) of the bus. There is no  specific mapping to direction, but a different value for the same  route signifies that the buses are traveling in opposite  directions. Use the TripDirectionText element to show the actual  destination of the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;EndTime&lt;/td&gt;    &lt;td&gt;Scheduled end date and time (Eastern Standard Time) for this  trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Bus route variant identifier (pattern). This variant can be  used in several other bus methods which accept variants. Note that  customers will never see anything other than the base route name,  so variants 10A, 10Av1, 10Av2, etc. will be displayed as 10A on the  bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;ScheduleTime&lt;/td&gt;    &lt;td&gt;Date and time (Eastern Standard Time) when the bus is scheduled  to stop at this location. Will be in YYYY-MM-DDTHH:mm:ss format  (e.g.: 2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StartTime&lt;/td&gt;    &lt;td&gt;Scheduled start date and time (Eastern Standard Time) for this  trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripDirectionText&lt;/td&gt;    &lt;td&gt;General direction of the trip (e.g.: NORTH, SOUTH, EAST,  WEST).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripHeadsign&lt;/td&gt;    &lt;td&gt;Destination of the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripID&lt;/td&gt;    &lt;td&gt;Trip identifier. This can be correlated with the data in our  bus schedule information as well as bus positions.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Stop\&quot; name&#x3D;\&quot;Stop\&quot;&gt;Stop Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lat&lt;/td&gt;    &lt;td&gt;Latitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lon&lt;/td&gt;    &lt;td&gt;Longitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Stop name. May be slightly different from what is spoken or  displayed in the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Routes&lt;/td&gt;    &lt;td&gt;String array of route variants which provide service at this  stop. Note that these are not date-specific; any route variant  which stops at this stop on any day will be listed.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopID&lt;/td&gt;    &lt;td&gt;7-digit regional ID which can be used in various bus-related  methods. If unavailable, the StopID will be 0 or NULL.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String stopID = "1001195"; // String | 7-digit regional stop ID.
    String date = "date_example"; // String | Date in YYYY-MM-DD format for which to retrieve schedule.  Defaults to today's date unless specified.
    try {
      apiInstance.call5476362a281d830c946a3d6c(stopID, date);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d6c");
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
| **stopID** | **String**| 7-digit regional stop ID. | [default to 1001195] [enum: 1001195] |
| **date** | **String**| Date in YYYY-MM-DD format for which to retrieve schedule.  Defaults to today&#39;s date unless specified. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

<a id="call5476362a281d830c946a3d6d"></a>
# **call5476362a281d830c946a3d6d**
> call5476362a281d830c946a3d6d(lat, lon, radius)

JSON - Stop Search

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns a list of nearby bus stops based on latitude, longitude, and radius.  Omit all parameters to retrieve a list of all stops.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Stops&lt;/td&gt;    &lt;td&gt;  Array containing stop information (&lt;a href&#x3D;\&quot;#Stop\&quot;&gt;Stop&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Stop\&quot; name&#x3D;\&quot;Stop\&quot;&gt;Stop Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lat&lt;/td&gt;    &lt;td&gt;Latitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lon&lt;/td&gt;    &lt;td&gt;Longitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Stop name. May be slightly different from what is spoken or  displayed in the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Routes&lt;/td&gt;    &lt;td&gt;String array of route variants which provide service at this  stop. Note that these are not date-specific; any route variant  which stops at this stop on any day will be listed.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopID&lt;/td&gt;    &lt;td&gt;7-digit regional ID which can be used in various bus-related  methods. If unavailable, the StopID will be 0 or NULL.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BigDecimal lat = new BigDecimal("38.878586"); // BigDecimal | Center point Latitude, required if Longitude and Radius are specified.
    BigDecimal lon = new BigDecimal("-76.989626"); // BigDecimal | Center point Longitude, required if Latitude and Radius are specified.
    BigDecimal radius = new BigDecimal("500"); // BigDecimal | Radius (meters) to include in the search area, required if Latitude and Longitude are specified.
    try {
      apiInstance.call5476362a281d830c946a3d6d(lat, lon, radius);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d6d");
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
| **lat** | **BigDecimal**| Center point Latitude, required if Longitude and Radius are specified. | [optional] [enum: 38.878586] |
| **lon** | **BigDecimal**| Center point Longitude, required if Latitude and Radius are specified. | [optional] [enum: -76.989626] |
| **radius** | **BigDecimal**| Radius (meters) to include in the search area, required if Latitude and Longitude are specified. | [optional] [enum: 500] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

<a id="call5476362a281d830c946a3d6e"></a>
# **call5476362a281d830c946a3d6e**
> call5476362a281d830c946a3d6e(routeID, lat, lon, radius)

XML - Bus Position

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;  &lt;p&gt;Returns bus positions for the given route, with an optional search radius. If no parameters are specified, all bus positions are returned.&lt;/p&gt;  &lt;p&gt;Note that the RouteID parameter accepts only base route names and no variations, i.e.: use 10A instead of 10Av1 or 10Av2.&lt;/p&gt;  &lt;p&gt;Bus positions are refreshed approximately every &lt;span style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;20 to 30&lt;/span&gt; 7 to 10 seconds.&lt;/p&gt;  &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;  &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt; &lt;thead&gt; &lt;tr&gt; &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;  &lt;th&gt;Description&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt;  &lt;tbody&gt; &lt;tr&gt; &lt;td&gt;BusPositions&lt;/td&gt;  &lt;td&gt; Array containing bus position information (&lt;a href&#x3D; \&quot;#BusPosition\&quot;&gt;BusPositions&lt;/a&gt;). &lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td colspan&#x3D;\&quot;2\&quot;&gt; &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt; &lt;a id&#x3D;\&quot;BusPosition\&quot; name&#x3D;\&quot;BusPosition\&quot;&gt;BusPosition Elements&lt;/a&gt; &lt;/div&gt; &lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;DateTime&lt;/td&gt;  &lt;td&gt;Date and time (Eastern Standard Time) of last position update. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T13:23:40).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;Deviation&lt;/td&gt;  &lt;td&gt;Deviation, in minutes, from schedule. Positive values indicate that the bus is running late while negative ones are for buses running ahead of schedule.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DirectionNum&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; Use the DirectionText for a customer-friendly description of direction.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;DirectionText&lt;/td&gt;  &lt;td&gt;General direction of the trip, not the bus itself (e.g.: NORTH, SOUTH, EAST, WEST).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;Lat&lt;/td&gt;  &lt;td&gt;Last reported Latitude of the bus.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;Lon&lt;/td&gt;  &lt;td&gt;Last reported Longitude of the bus.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;RouteID&lt;/td&gt;  &lt;td&gt;Base route name as shown on the bus. Note that the base route name could also refer to any variant, so a RouteID of 10A could refer to 10A, 10Av1, 10Av2, etc.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;TripEndTime&lt;/td&gt;  &lt;td&gt;Scheduled end date and time (Eastern Standard Time) of the bus&#39;s current trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T13:17:00).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;TripHeadsign&lt;/td&gt;  &lt;td&gt;Destination of the bus.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;TripID&lt;/td&gt;  &lt;td&gt;Unique trip ID. This can be correlated with the data returned from the schedule-related methods.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;TripStartTime&lt;/td&gt;  &lt;td&gt;Scheduled start date and time (Eastern Standard Time) of the bus&#39;s current trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T12:40:00).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;VehicleID&lt;/td&gt;  &lt;td&gt;Unique identifier for the bus. This is usually visible on the bus itself.&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String routeID = "70"; // String | Bus route, e.g.: 70, 10A.
    String lat = "lat_example"; // String | Center point Latitude, required if Longitude and Radius are specified.
    String lon = "lon_example"; // String | Center point Longitude, required if Latitude and Radius are specified.
    String radius = "radius_example"; // String | Radius (meters) to include in the search area, required if Latitude and Longitude are specified.
    try {
      apiInstance.call5476362a281d830c946a3d6e(routeID, lat, lon, radius);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d6e");
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
| **routeID** | **String**| Bus route, e.g.: 70, 10A. | [optional] [default to 70] [enum: 70] |
| **lat** | **String**| Center point Latitude, required if Longitude and Radius are specified. | [optional] |
| **lon** | **String**| Center point Longitude, required if Latitude and Radius are specified. | [optional] |
| **radius** | **String**| Radius (meters) to include in the search area, required if Latitude and Longitude are specified. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

<a id="call5476362a281d830c946a3d6f"></a>
# **call5476362a281d830c946a3d6f**
> call5476362a281d830c946a3d6f(routeID, date)

XML - Path Details

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;  &lt;p&gt;For a given date, returns the set of ordered latitude/longitude points along route variant along with the list of stops served.&lt;/p&gt;  &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;  &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;  &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;  &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Direction0/Direction1&lt;/td&gt;  &lt;td&gt;  Structures describing &lt;a href&#x3D;\&quot;#Direction\&quot;&gt;path/stop&lt;/a&gt;information.&lt;br&gt;  &lt;br&gt;  Most routes will return content in both Direction0 and Direction1 elements, though a few will return NULL for Direction0 or for Direction1.&lt;br&gt;  &lt;br&gt;  0 or 1 are binary properties. There is no specific mapping to direction, but a different value for the same route signifies that the route is in an opposite direction.  &lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;  &lt;td&gt;Descriptive name for the route.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;  &lt;td&gt;Bus route variant (e.g.: 10A, 10Av1, etc.).&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Direction\&quot; name&#x3D;\&quot;Direction\&quot;&gt;Direction0/Direction1 Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DirectionNum&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; Use the DirectionText element to denote the general direction of the route variant.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;DirectionText&lt;/td&gt;  &lt;td&gt;General direction of the route variant (NORTH, SOUTH, EAST, WEST, LOOP, etc.).&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;Shape&lt;/td&gt;  &lt;td&gt;  Array containing shape point information (&lt;a href&#x3D;\&quot;#ShapePoint\&quot;&gt;ShapePoint&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;Stops&lt;/td&gt;  &lt;td&gt;  Array containing stop information (&lt;a href&#x3D;\&quot;#Stop\&quot;&gt;Stop&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;TripHeadsign&lt;/td&gt;  &lt;td&gt;Descriptive text of where the bus is headed. This is similar, but not necessarily identical, to what is displayed on the bus.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;ShapePoint\&quot; name&#x3D;\&quot;ShapePoint\&quot;&gt;ShapePoint Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;Lat&lt;/td&gt;  &lt;td&gt;Latitude.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;Lon&lt;/td&gt;  &lt;td&gt;Longitude.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;SeqNum&lt;/td&gt;  &lt;td&gt;Order of the point in the sequence of ShapePoints.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;   &lt;a id&#x3D;\&quot;Stop\&quot; name&#x3D;\&quot;Stop\&quot;&gt;Stop Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;Lat&lt;/td&gt;  &lt;td&gt;Latitude.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;Lon&lt;/td&gt;  &lt;td&gt;Longitude.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;  &lt;td&gt;Stop name. May be slightly different from what is spoken or displayed in the bus.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;Routes&lt;/td&gt;  &lt;td&gt;String array of route variants which provide service at this stop. Note that these are not date-specific; any route variant which stops at this stop on any day will be listed.&lt;/td&gt;  &lt;/tr&gt;  &lt;tr&gt;  &lt;td&gt;StopID&lt;/td&gt;  &lt;td&gt;7-digit regional ID which can be used in various bus-related methods. If unavailable, the StopID will be 0 or NULL.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String routeID = "70"; // String | Bus route variant, e.g.: 70, 10A, 10Av1.
    String date = "date_example"; // String | Date in YYYY-MM-DD format for which to retrieve route and stop information.  Defaults to today's date unless specified.
    try {
      apiInstance.call5476362a281d830c946a3d6f(routeID, date);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d6f");
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
| **routeID** | **String**| Bus route variant, e.g.: 70, 10A, 10Av1. | [default to 70] [enum: 70] |
| **date** | **String**| Date in YYYY-MM-DD format for which to retrieve route and stop information.  Defaults to today&#39;s date unless specified. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

<a id="call5476362a281d830c946a3d70"></a>
# **call5476362a281d830c946a3d70**
> call5476362a281d830c946a3d70()

XML - Routes

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns a list of all bus route variants (patterns). For example, the 10A  and 10Av1 are the same route, but may stop at slightly different locations.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Routes&lt;/td&gt;    &lt;td&gt;  Array containing route variant information (&lt;a href&#x3D;  \&quot;#Route\&quot;&gt;Route&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Route\&quot; name&#x3D;\&quot;Route\&quot;&gt;Route Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Descriptive name of the route variant.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Unique identifier for a given route variant. Can be used in  various other bus-related methods.&lt;/td&gt;  &lt;/tr&gt;      &lt;tr&gt;  &lt;td&gt;LineDescription&lt;/td&gt;    &lt;td&gt;Denotes the route variant’s grouping – lines are a combination of routes which lie in the same corridor and which have significant portions of their paths along the same roadways.&lt;/td&gt;  &lt;/tr&gt;   &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.call5476362a281d830c946a3d70();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d70");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

<a id="call5476362a281d830c946a3d71"></a>
# **call5476362a281d830c946a3d71**
> call5476362a281d830c946a3d71(routeID, date, includingVariations)

XML - Schedule

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns schedules for a given route variant for a given date.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Direction0/Direction1&lt;/td&gt;    &lt;td&gt;  Arrays containing trip information (&lt;a href&#x3D;  \&quot;#Trip\&quot;&gt;Trip&lt;/a&gt;).&lt;br&gt;  &lt;br&gt;  Most routes will return content in both Direction0 and  Direction1 elements, though a few (especially ones which run in  a loop, such as the U8) will return content only for Direction0  and NULL content for Direction1.&lt;br&gt;  &lt;br&gt;  0 or 1 are binary properties. There is no specific mapping to  direction, but a different value for the same route signifies  that the route is in an opposite direction.  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Descriptive name for the route.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Trip\&quot; name&#x3D;\&quot;Trip\&quot;&gt;Trip Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DirectionNum&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; Use the  TripDirectionText element to denote the general direction of the  trip.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;EndTime&lt;/td&gt;    &lt;td&gt;Scheduled end date and time (Eastern Standard Time) for this  trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Bus route variant. This can be used in several other bus  methods which accept variants.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StartTime&lt;/td&gt;    &lt;td&gt;Scheduled start date and time (Eastern Standard Time) for this  trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopTimes&lt;/td&gt;    &lt;td&gt;  Array containing location and time information (&lt;a href&#x3D;  \&quot;#StopTime\&quot;&gt;StopTime&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripDirectionText&lt;/td&gt;    &lt;td&gt;General direction of the trip (NORTH, SOUTH, EAST, WEST, LOOP,  etc.).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripHeadsign&lt;/td&gt;    &lt;td&gt;Descriptive text of where the bus is headed. This is similar,  but not necessarily identical, to what is displayed on the  bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripID&lt;/td&gt;    &lt;td&gt;Unique trip ID. This can be correlated with the data returned  from the schedule-related methods.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;StopTime\&quot; name&#x3D;\&quot;StopTime\&quot;&gt;StopTime Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopID&lt;/td&gt;    &lt;td&gt;7-digit regional ID which can be used in various bus-related  methods. If unavailable, the StopID will be 0 or NULL.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopName&lt;/td&gt;    &lt;td&gt;Stop name. May be slightly different from what is spoken or  displayed in the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopSeq&lt;/td&gt;    &lt;td&gt;Order of the stop in the sequence of StopTimes.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Time&lt;/td&gt;    &lt;td&gt;Scheduled departure date and time (Eastern Standard Time) from  this stop. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String routeID = "70"; // String | Bus route variant, e.g.: 70, 10A, 10Av1.
    String date = "date_example"; // String | Date in YYYY-MM-DD format for which to retrieve schedule.  Defaults to today's date unless specified.
    Boolean includingVariations = false; // Boolean | Whether or not to include variations.  For example, if B30 is specified, include all variations such as B30v1, B30v2, etc.
    try {
      apiInstance.call5476362a281d830c946a3d71(routeID, date, includingVariations);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d71");
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
| **routeID** | **String**| Bus route variant, e.g.: 70, 10A, 10Av1. | [default to 70] [enum: 70] |
| **date** | **String**| Date in YYYY-MM-DD format for which to retrieve schedule.  Defaults to today&#39;s date unless specified. | [optional] |
| **includingVariations** | **Boolean**| Whether or not to include variations.  For example, if B30 is specified, include all variations such as B30v1, B30v2, etc. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

<a id="call5476362a281d830c946a3d72"></a>
# **call5476362a281d830c946a3d72**
> call5476362a281d830c946a3d72(stopID, date)

XML - Schedule at Stop

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns a set of buses scheduled at a stop for a given date.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;ScheduleArrivals&lt;/td&gt;    &lt;td&gt;  Array containing scheduled arrival information (&lt;a href&#x3D;  \&quot;#ScheduleArrival\&quot;&gt;ScheduleArrival&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Stop&lt;/td&gt;    &lt;td&gt;  Structure describing &lt;a href&#x3D;\&quot;#Stop\&quot;&gt;stop&lt;/a&gt; information.  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;ScheduleArrival\&quot; name&#x3D;  \&quot;ScheduleArrival\&quot;&gt;ScheduleArrival Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionNum&lt;/td&gt;    &lt;td&gt;Denotes a binary direction (0 or 1) of the bus. There is no  specific mapping to direction, but a different value for the same  route signifies that the buses are traveling in opposite  directions. Use the TripDirectionText element to show the actual  destination of the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;EndTime&lt;/td&gt;    &lt;td&gt;Scheduled end date and time (Eastern Standard Time) for this  trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Bus route variant identifier (pattern). This variant can be  used in several other bus methods which accept variants. Note that  customers will never see anything other than the base route name,  so variants 10A, 10Av1, 10Av2, etc. will be displayed as 10A on the  bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;ScheduleTime&lt;/td&gt;    &lt;td&gt;Date and time (Eastern Standard Time) when the bus is scheduled  to stop at this location. Will be in YYYY-MM-DDTHH:mm:ss format  (e.g.: 2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StartTime&lt;/td&gt;    &lt;td&gt;Scheduled start date and time (Eastern Standard Time) for this  trip. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.:  2014-10-27T13:17:00).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripDirectionText&lt;/td&gt;    &lt;td&gt;General direction of the trip (e.g.: NORTH, SOUTH, EAST,  WEST).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripHeadsign&lt;/td&gt;    &lt;td&gt;Destination of the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripID&lt;/td&gt;    &lt;td&gt;Trip identifier. This can be correlated with the data in our  bus schedule information as well as bus positions.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Stop\&quot; name&#x3D;\&quot;Stop\&quot;&gt;Stop Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lat&lt;/td&gt;    &lt;td&gt;Latitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lon&lt;/td&gt;    &lt;td&gt;Longitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Stop name. May be slightly different from what is spoken or  displayed in the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Routes&lt;/td&gt;    &lt;td&gt;String array of route variants which provide service at this  stop. Note that these are not date-specific; any route variant  which stops at this stop on any day will be listed.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopID&lt;/td&gt;    &lt;td&gt;7-digit regional ID which can be used in various bus-related  methods. If unavailable, the StopID will be 0 or NULL.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String stopID = "1001195"; // String | 7-digit regional stop ID.
    String date = "date_example"; // String | Date in YYYY-MM-DD format for which to retrieve schedule.  Defaults to today's date unless specified.
    try {
      apiInstance.call5476362a281d830c946a3d72(stopID, date);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d72");
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
| **stopID** | **String**| 7-digit regional stop ID. | [default to 1001195] [enum: 1001195] |
| **date** | **String**| Date in YYYY-MM-DD format for which to retrieve schedule.  Defaults to today&#39;s date unless specified. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

<a id="call5476362a281d830c946a3d73"></a>
# **call5476362a281d830c946a3d73**
> call5476362a281d830c946a3d73(lat, lon, radius)

XML - Stop Search

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns a list of nearby bus stops based on latitude, longitude, and radius.  Omit all parameters to retrieve a list of all stops.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Stops&lt;/td&gt;    &lt;td&gt;  Array containing stop information (&lt;a href&#x3D;\&quot;#Stop\&quot;&gt;Stop&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Stop\&quot; name&#x3D;\&quot;Stop\&quot;&gt;Stop Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lat&lt;/td&gt;    &lt;td&gt;Latitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Lon&lt;/td&gt;    &lt;td&gt;Longitude.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Name&lt;/td&gt;    &lt;td&gt;Stop name. May be slightly different from what is spoken or  displayed in the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Routes&lt;/td&gt;    &lt;td&gt;String array of route variants which provide service at this  stop. Note that these are not date-specific; any route variant  which stops at this stop on any day will be listed.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopID&lt;/td&gt;    &lt;td&gt;7-digit regional ID which can be used in various bus-related  methods. If unavailable, the StopID will be 0 or NULL.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/Bus.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String lat = "38.878586"; // String | Center point Latitude, required if Longitude and Radius are specified.
    String lon = "-76.989626"; // String | Center point Longitude, required if Latitude and Radius are specified.
    String radius = "500"; // String | Radius (feet) to include in the search area, required if Latitude and Longitude are specified.
    try {
      apiInstance.call5476362a281d830c946a3d73(lat, lon, radius);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476362a281d830c946a3d73");
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
| **lat** | **String**| Center point Latitude, required if Longitude and Radius are specified. | [optional] [enum: 38.878586] |
| **lon** | **String**| Center point Longitude, required if Latitude and Radius are specified. | [optional] [enum: -76.989626] |
| **radius** | **String**| Radius (feet) to include in the search area, required if Latitude and Longitude are specified. | [optional] [enum: 500] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |

