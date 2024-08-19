# DirectionsApi

All URIs are relative to *https://router.api.gov.bc.ca*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**directionsOutputFormatGet**](DirectionsApi.md#directionsOutputFormatGet) | **GET** /directions.{outputFormat} | Get the directions, path, distance and travel time between a series of geographic points |
| [**directionsOutputFormatPost**](DirectionsApi.md#directionsOutputFormatPost) | **POST** /directions.{outputFormat} | Get the directions, path, distance and travel time between a series of geographic points |
| [**optimalDirectionsOutputFormatGet**](DirectionsApi.md#optimalDirectionsOutputFormatGet) | **GET** /optimalDirections.{outputFormat} | Get the directions, optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time. |
| [**optimalDirectionsOutputFormatPost**](DirectionsApi.md#optimalDirectionsOutputFormatPost) | **POST** /optimalDirections.{outputFormat} | Get the directions, optimal path, distance and travel time between a start point and one or more end points which are reordered to minimize total distance or time. |
| [**truckDirectionsOutputFormatGet**](DirectionsApi.md#truckDirectionsOutputFormatGet) | **GET** /truck/directions.{outputFormat} | Get the directions, path, distance and travel time between a series of geographic points for a commercial vehicle |
| [**truckDirectionsOutputFormatPost**](DirectionsApi.md#truckDirectionsOutputFormatPost) | **POST** /truck/directions.{outputFormat} | Get the directions, path, distance and travel time between a series of geographic points |
| [**truckOptimalDirectionsOutputFormatGet**](DirectionsApi.md#truckOptimalDirectionsOutputFormatGet) | **GET** /truck/optimalDirections.{outputFormat} | Get the directions, optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time for a commercial vehicle |
| [**truckOptimalDirectionsOutputFormatPost**](DirectionsApi.md#truckOptimalDirectionsOutputFormatPost) | **POST** /truck/optimalDirections.{outputFormat} | Get the directions, optimal path, distance and travel time between a start point and one or more end points which are reordered to minimize total distance or time. |


<a id="directionsOutputFormatGet"></a>
# **directionsOutputFormatGet**
> directionsOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription)

Get the directions, path, distance and travel time between a series of geographic points

Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between given start and end points

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DirectionsApi apiInstance = new DirectionsApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    Boolean roundTrip = false; // Boolean | If true, route ends at start point. Default is false.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start/end point.Default is false.
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    try {
      apiInstance.directionsOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectionsApi#directionsOutputFormatGet");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, kml, html] |
| **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start/end point.Default is false. | [optional] [default to false] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | turn-by-turn directions, geometry, distance, and time of the shortest or fastest route |  -  |

<a id="directionsOutputFormatPost"></a>
# **directionsOutputFormatPost**
> directionsOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription)

Get the directions, path, distance and travel time between a series of geographic points

Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between given start and end points

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DirectionsApi apiInstance = new DirectionsApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    Boolean roundTrip = false; // Boolean | If true, route ends at start point. Default is false.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start/end point.Default is false.
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    try {
      apiInstance.directionsOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectionsApi#directionsOutputFormatPost");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, kml, html] |
| **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start/end point.Default is false. | [optional] [default to false] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | turn-by-turn directions, geometry, distance, and time of the shortest or fastest route |  -  |

<a id="optimalDirectionsOutputFormatGet"></a>
# **optimalDirectionsOutputFormatGet**
> optimalDirectionsOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription)

Get the directions, optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.

Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between a start point and a series of end points which are reordered to minimize distance/time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DirectionsApi apiInstance = new DirectionsApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    Boolean roundTrip = false; // Boolean | If true, route ends at start point. Default is false.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    try {
      apiInstance.optimalDirectionsOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectionsApi#optimalDirectionsOutputFormatGet");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, kml, html] |
| **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | turn-by-turn directions, geometry, distance, and time of the shortest or fastest route. End points are reordered to minimize total distance or time. |  -  |

<a id="optimalDirectionsOutputFormatPost"></a>
# **optimalDirectionsOutputFormatPost**
> optimalDirectionsOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription)

Get the directions, optimal path, distance and travel time between a start point and one or more end points which are reordered to minimize total distance or time.

Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between a start point and one or more end points which are reordered to minimize distance or time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DirectionsApi apiInstance = new DirectionsApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    Boolean roundTrip = false; // Boolean | If true, route ends at start point. Default is false.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    try {
      apiInstance.optimalDirectionsOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectionsApi#optimalDirectionsOutputFormatPost");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, kml, html] |
| **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | turn-by-turn directions, geometry, distance, and time of the shortest or fastest route. End points are reordered to minimize total distance or time. |  -  |

<a id="truckDirectionsOutputFormatGet"></a>
# **truckDirectionsOutputFormatGet**
> truckDirectionsOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, partition, disable, routeDescription)

Get the directions, path, distance and travel time between a series of geographic points for a commercial vehicle

Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between given start and end points for a commercial vehicle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DirectionsApi apiInstance = new DirectionsApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    Boolean roundTrip = false; // Boolean | If true, route ends at start point. Default is false.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start/end point.Default is false.
    Integer truckRouteMultiplier = 9; // Integer | The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
    String partition = ""; // String | A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. <br><br>Partition values:<br> isTruckRoute – Distinguish between truck route sections and non-truck route sections <br> isFerry – Distinguish between ferry sections and non-ferry sections <br> locality – Include the locality name for the route partition
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    try {
      apiInstance.truckDirectionsOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, partition, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectionsApi#truckDirectionsOutputFormatGet");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, kml, html] |
| **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start/end point.Default is false. | [optional] [default to false] |
| **truckRouteMultiplier** | **Integer**| The truck route multiplier value is used to multiply the cost of using roads that are not truck routes. | [optional] [default to 9] |
| **partition** | **String**| A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition | [optional] [default to ] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | turn-by-turn directions, geometry, distance, and time of the shortest or fastest route |  -  |

<a id="truckDirectionsOutputFormatPost"></a>
# **truckDirectionsOutputFormatPost**
> truckDirectionsOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, partition, disable, routeDescription)

Get the directions, path, distance and travel time between a series of geographic points

Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between given start and end points

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DirectionsApi apiInstance = new DirectionsApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    Boolean roundTrip = false; // Boolean | If true, route ends at start point. Default is false.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start/end point.Default is false.
    Integer truckRouteMultiplier = 9; // Integer | The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
    String partition = ""; // String | A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. <br><br>Partition values:<br> isTruckRoute – Distinguish between truck route sections and non-truck route sections <br> isFerry – Distinguish between ferry sections and non-ferry sections <br> locality – Include the locality name for the route partition
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    try {
      apiInstance.truckDirectionsOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, partition, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectionsApi#truckDirectionsOutputFormatPost");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, kml, html] |
| **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start/end point.Default is false. | [optional] [default to false] |
| **truckRouteMultiplier** | **Integer**| The truck route multiplier value is used to multiply the cost of using roads that are not truck routes. | [optional] [default to 9] |
| **partition** | **String**| A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition | [optional] [default to ] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | turn-by-turn directions, geometry, distance, and time of the shortest or fastest route |  -  |

<a id="truckOptimalDirectionsOutputFormatGet"></a>
# **truckOptimalDirectionsOutputFormatGet**
> truckOptimalDirectionsOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, partition, disable, routeDescription)

Get the directions, optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time for a commercial vehicle

Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between a start point and a series of end points which are reordered to minimize distance/time for a commercial vehicle.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DirectionsApi apiInstance = new DirectionsApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    Boolean roundTrip = false; // Boolean | If true, route ends at start point. Default is false.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
    Integer truckRouteMultiplier = 9; // Integer | The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
    String partition = ""; // String | A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. <br><br>Partition values:<br> isTruckRoute – Distinguish between truck route sections and non-truck route sections <br> isFerry – Distinguish between ferry sections and non-ferry sections <br> locality – Include the locality name for the route partition
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    try {
      apiInstance.truckOptimalDirectionsOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, partition, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectionsApi#truckOptimalDirectionsOutputFormatGet");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, kml, html] |
| **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false] |
| **truckRouteMultiplier** | **Integer**| The truck route multiplier value is used to multiply the cost of using roads that are not truck routes. | [optional] [default to 9] |
| **partition** | **String**| A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition | [optional] [default to ] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | turn-by-turn directions, geometry, distance, and time of the shortest or fastest route. End points are reordered to minimize total distance or time. |  -  |

<a id="truckOptimalDirectionsOutputFormatPost"></a>
# **truckOptimalDirectionsOutputFormatPost**
> truckOptimalDirectionsOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, partition, disable, routeDescription)

Get the directions, optimal path, distance and travel time between a start point and one or more end points which are reordered to minimize total distance or time.

Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between a start point and one or more end points which are reordered to minimize distance or time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DirectionsApi apiInstance = new DirectionsApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    Boolean roundTrip = false; // Boolean | If true, route ends at start point. Default is false.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
    Integer truckRouteMultiplier = 9; // Integer | The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
    String partition = ""; // String | A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. <br><br>Partition values:<br> isTruckRoute – Distinguish between truck route sections and non-truck route sections <br> isFerry – Distinguish between ferry sections and non-ferry sections <br> locality – Include the locality name for the route partition
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    try {
      apiInstance.truckOptimalDirectionsOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, partition, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectionsApi#truckOptimalDirectionsOutputFormatPost");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, kml, html] |
| **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false] |
| **truckRouteMultiplier** | **Integer**| The truck route multiplier value is used to multiply the cost of using roads that are not truck routes. | [optional] [default to 9] |
| **partition** | **String**| A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition | [optional] [default to ] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | turn-by-turn directions, geometry, distance, and time of the shortest or fastest route. End points are reordered to minimize total distance or time. |  -  |

