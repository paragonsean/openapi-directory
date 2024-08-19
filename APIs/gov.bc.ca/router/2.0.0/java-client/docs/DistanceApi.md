# DistanceApi

All URIs are relative to *https://router.api.gov.bc.ca*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**distanceBetweenPairsOutputFormatGet**](DistanceApi.md#distanceBetweenPairsOutputFormatGet) | **GET** /distance/betweenPairs.{outputFormat} | Get distance and travel time between each pair of geographic points |
| [**distanceBetweenPairsOutputFormatPost**](DistanceApi.md#distanceBetweenPairsOutputFormatPost) | **POST** /distance/betweenPairs.{outputFormat} | Get distance and travel time between each pair of geographic points |
| [**distanceOutputFormatGet**](DistanceApi.md#distanceOutputFormatGet) | **GET** /distance.{outputFormat} | Get distance and travel time between two geographic points |
| [**distanceOutputFormatPost**](DistanceApi.md#distanceOutputFormatPost) | **POST** /distance.{outputFormat} | Get distance and travel time between two geographic points |
| [**truckDistanceBetweenPairsOutputFormatGet**](DistanceApi.md#truckDistanceBetweenPairsOutputFormatGet) | **GET** /truck/distance/betweenPairs.{outputFormat} | Get distance and travel time between each pair of geographic points for a commercial vehicle |
| [**truckDistanceBetweenPairsOutputFormatPost**](DistanceApi.md#truckDistanceBetweenPairsOutputFormatPost) | **POST** /truck/distance/betweenPairs.{outputFormat} | Get distance and travel time between each pair of geographic points |
| [**truckDistanceOutputFormatGet**](DistanceApi.md#truckDistanceOutputFormatGet) | **GET** /truck/distance.{outputFormat} | Get distance and travel time between two geographic points for a commercial vehicle |
| [**truckDistanceOutputFormatPost**](DistanceApi.md#truckDistanceOutputFormatPost) | **POST** /truck/distance.{outputFormat} | Get distance and travel time between two geographic points |


<a id="distanceBetweenPairsOutputFormatGet"></a>
# **distanceBetweenPairsOutputFormatGet**
> distanceBetweenPairsOutputFormatGet(outputFormat, fromPoints, toPoints, outputSRS, criteria, distanceUnit, departure, correctSide, disable, routeDescription, maxPairs)

Get distance and travel time between each pair of geographic points

Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DistanceApi apiInstance = new DistanceApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String fromPoints = "-123.70794,48.77869,-123.53785,48.38200"; // String | A comma-separated list of origin points.  See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target='_blank'>fromPoints</a>
    String toPoints = "-124.972951,49.715181,-123.139464,49.704015"; // String | A comma-separated list of destination points. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target='_blank'>toPoints</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    Integer maxPairs = 56; // Integer | The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs=1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs=3 means return the 3 nearest toPoints to each fromPoint.
    try {
      apiInstance.distanceBetweenPairsOutputFormatGet(outputFormat, fromPoints, toPoints, outputSRS, criteria, distanceUnit, departure, correctSide, disable, routeDescription, maxPairs);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistanceApi#distanceBetweenPairsOutputFormatGet");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, html] |
| **fromPoints** | **String**| A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt; | |
| **toPoints** | **String**| A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |
| **maxPairs** | **Integer**| The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint. | [optional] |

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
| **200** | A list of routes and their route distances/times. |  -  |

<a id="distanceBetweenPairsOutputFormatPost"></a>
# **distanceBetweenPairsOutputFormatPost**
> distanceBetweenPairsOutputFormatPost(outputFormat, fromPoints, toPoints, outputSRS, criteria, distanceUnit, departure, correctSide, disable, routeDescription, maxPairs)

Get distance and travel time between each pair of geographic points

Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DistanceApi apiInstance = new DistanceApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String fromPoints = "-123.70794,48.77869,-123.53785,48.38200"; // String | A comma-separated list of origin points.  See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target='_blank'>fromPoints</a>
    String toPoints = "-124.972951,49.715181,-123.139464,49.704015"; // String | A comma-separated list of destination points. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target='_blank'>toPoints</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    Integer maxPairs = 56; // Integer | The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs=1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs=3 means return the 3 nearest toPoints to each fromPoint.
    try {
      apiInstance.distanceBetweenPairsOutputFormatPost(outputFormat, fromPoints, toPoints, outputSRS, criteria, distanceUnit, departure, correctSide, disable, routeDescription, maxPairs);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistanceApi#distanceBetweenPairsOutputFormatPost");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, html] |
| **fromPoints** | **String**| A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt; | |
| **toPoints** | **String**| A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |
| **maxPairs** | **Integer**| The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint. | [optional] |

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
| **200** | A list of routes and their route distances/times. |  -  |

<a id="distanceOutputFormatGet"></a>
# **distanceOutputFormatGet**
> distanceOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription)

Get distance and travel time between two geographic points

Represents the distance and time of the shortest or fastest path between given start and end points.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DistanceApi apiInstance = new DistanceApi(defaultClient);
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
      apiInstance.distanceOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistanceApi#distanceOutputFormatGet");
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
| **200** | Distance and time of the shortest or fastest route |  -  |

<a id="distanceOutputFormatPost"></a>
# **distanceOutputFormatPost**
> distanceOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription)

Get distance and travel time between two geographic points

Represents the distance and time of the shortest or fastest path between given start and end points.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DistanceApi apiInstance = new DistanceApi(defaultClient);
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
      apiInstance.distanceOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistanceApi#distanceOutputFormatPost");
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
| **200** | Distance and time of the shortest or fastest route |  -  |

<a id="truckDistanceBetweenPairsOutputFormatGet"></a>
# **truckDistanceBetweenPairsOutputFormatGet**
> truckDistanceBetweenPairsOutputFormatGet(outputFormat, fromPoints, toPoints, outputSRS, criteria, distanceUnit, departure, correctSide, disable, routeDescription, maxPairs)

Get distance and travel time between each pair of geographic points for a commercial vehicle

Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints for a commercial vehicle. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DistanceApi apiInstance = new DistanceApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String fromPoints = "-123.70794,48.77869,-123.53785,48.38200"; // String | A comma-separated list of origin points.  See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target='_blank'>fromPoints</a>
    String toPoints = "-124.972951,49.715181,-123.139464,49.704015"; // String | A comma-separated list of destination points. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target='_blank'>toPoints</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    Integer maxPairs = 56; // Integer | The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs=1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs=3 means return the 3 nearest toPoints to each fromPoint.
    try {
      apiInstance.truckDistanceBetweenPairsOutputFormatGet(outputFormat, fromPoints, toPoints, outputSRS, criteria, distanceUnit, departure, correctSide, disable, routeDescription, maxPairs);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistanceApi#truckDistanceBetweenPairsOutputFormatGet");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, html] |
| **fromPoints** | **String**| A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt; | |
| **toPoints** | **String**| A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |
| **maxPairs** | **Integer**| The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint. | [optional] |

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
| **200** | A list of routes and their route distances/times. |  -  |

<a id="truckDistanceBetweenPairsOutputFormatPost"></a>
# **truckDistanceBetweenPairsOutputFormatPost**
> truckDistanceBetweenPairsOutputFormatPost(outputFormat, fromPoints, toPoints, outputSRS, criteria, distanceUnit, departure, correctSide, disable, routeDescription, maxPairs)

Get distance and travel time between each pair of geographic points

Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DistanceApi apiInstance = new DistanceApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String fromPoints = "-123.70794,48.77869,-123.53785,48.38200"; // String | A comma-separated list of origin points.  See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target='_blank'>fromPoints</a>
    String toPoints = "-124.972951,49.715181,-123.139464,49.704015"; // String | A comma-separated list of destination points. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target='_blank'>toPoints</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    Integer maxPairs = 56; // Integer | The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs=1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs=3 means return the 3 nearest toPoints to each fromPoint.
    try {
      apiInstance.truckDistanceBetweenPairsOutputFormatPost(outputFormat, fromPoints, toPoints, outputSRS, criteria, distanceUnit, departure, correctSide, disable, routeDescription, maxPairs);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistanceApi#truckDistanceBetweenPairsOutputFormatPost");
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
| **outputFormat** | **String**| Format of representation | [default to json] [enum: json, html] |
| **fromPoints** | **String**| A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt; | |
| **toPoints** | **String**| A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt; | |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to shortest] [enum: shortest, fastest] |
| **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to km] [enum: km, mi] |
| **departure** | **OffsetDateTime**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] |
| **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false] |
| **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to sc,tf,ev,td] |
| **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to Routing results] |
| **maxPairs** | **Integer**| The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint. | [optional] |

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
| **200** | A list of routes and their route distances/times. |  -  |

<a id="truckDistanceOutputFormatGet"></a>
# **truckDistanceOutputFormatGet**
> truckDistanceOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, disable, routeDescription)

Get distance and travel time between two geographic points for a commercial vehicle

Represents the distance and time of the shortest or fastest path between given start and end points.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DistanceApi apiInstance = new DistanceApi(defaultClient);
    String outputFormat = "json"; // String | Format of representation
    String points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String criteria = "shortest"; // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    String distanceUnit = "km"; // String | distance unit of measure (e.g., km, mi). Default is km.
    Boolean roundTrip = false; // Boolean | If true, route ends at start point. Default is false.
    OffsetDateTime departure = OffsetDateTime.now(); // OffsetDateTime | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
    Boolean correctSide = false; // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
    Integer truckRouteMultiplier = 9; // Integer | The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
    String disable = "sc,tf,ev,td"; // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
    String routeDescription = "Routing results"; // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    try {
      apiInstance.truckDistanceOutputFormatGet(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, truckRouteMultiplier, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistanceApi#truckDistanceOutputFormatGet");
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
| **200** | Distance and time of the shortest or fastest route |  -  |

<a id="truckDistanceOutputFormatPost"></a>
# **truckDistanceOutputFormatPost**
> truckDistanceOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription)

Get distance and travel time between two geographic points

Represents the distance and time of the shortest or fastest path between given start and end points.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://router.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DistanceApi apiInstance = new DistanceApi(defaultClient);
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
      apiInstance.truckDistanceOutputFormatPost(outputFormat, points, outputSRS, criteria, distanceUnit, roundTrip, departure, correctSide, disable, routeDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistanceApi#truckDistanceOutputFormatPost");
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
| **200** | Distance and time of the shortest or fastest route |  -  |

