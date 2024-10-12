# BcRoutePlannerRestApi.RouteApi

All URIs are relative to *https://router.api.gov.bc.ca*

Method | HTTP request | Description
------------- | ------------- | -------------
[**optimalRouteOutputFormatGet**](RouteApi.md#optimalRouteOutputFormatGet) | **GET** /optimalRoute.{outputFormat} | Get the optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.
[**optimalRouteOutputFormatPost**](RouteApi.md#optimalRouteOutputFormatPost) | **POST** /optimalRoute.{outputFormat} | Get the path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.
[**routeOutputFormatGet**](RouteApi.md#routeOutputFormatGet) | **GET** /route.{outputFormat} | Get the path, distance and travel time between a series of geographic points
[**routeOutputFormatPost**](RouteApi.md#routeOutputFormatPost) | **POST** /route.{outputFormat} | Get the path, distance and travel time between a series of geographic points
[**truckOptimalRouteOutputFormatGet**](RouteApi.md#truckOptimalRouteOutputFormatGet) | **GET** /truck/optimalRoute.{outputFormat} | Get the optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time for a commercial vehicle
[**truckOptimalRouteOutputFormatPost**](RouteApi.md#truckOptimalRouteOutputFormatPost) | **POST** /truck/optimalRoute.{outputFormat} | Get the path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.
[**truckRouteOutputFormatGet**](RouteApi.md#truckRouteOutputFormatGet) | **GET** /truck/route.{outputFormat} | Get the path, distance and travel time between a series of geographic points for a commercial vehicle
[**truckRouteOutputFormatPost**](RouteApi.md#truckRouteOutputFormatPost) | **POST** /truck/route.{outputFormat} | Get the path, distance and travel time between a series of geographic points



## optimalRouteOutputFormatGet

> optimalRouteOutputFormatGet(outputFormat, points, opts)

Get the optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.

Represents the geometry, distance, and time of the shortest or fastest path between a start point and a series of end points which are reordered to minimize distance or time

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.RouteApi();
let outputFormat = "json"; // String | Format of representation
let points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'roundTrip': false, // Boolean | If true, route ends at start point. Default is false.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'" // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
};
apiInstance.optimalRouteOutputFormatGet(outputFormat, points, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Format of representation | [default to &#39;json&#39;]
 **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## optimalRouteOutputFormatPost

> optimalRouteOutputFormatPost(outputFormat, points, opts)

Get the path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.

Represents the geometry, distance, and time of the shortest or fastest path between a start point and a series of end points which are reordered to minimize total distance or time.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.RouteApi();
let outputFormat = "json"; // String | Format of representation
let points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'roundTrip': false, // Boolean | If true, route ends at start point. Default is false.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'" // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
};
apiInstance.optimalRouteOutputFormatPost(outputFormat, points, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Format of representation | [default to &#39;json&#39;]
 **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## routeOutputFormatGet

> routeOutputFormatGet(outputFormat, points, opts)

Get the path, distance and travel time between a series of geographic points

Represents the geometry, distance, and time of the shortest or fastest path between given start and end points.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.RouteApi();
let outputFormat = "json"; // String | Format of representation
let points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'roundTrip': false, // Boolean | If true, route ends at start point. Default is false.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start/end point.Default is false.
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br> Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'" // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
};
apiInstance.routeOutputFormatGet(outputFormat, points, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Format of representation | [default to &#39;json&#39;]
 **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start/end point.Default is false. | [optional] [default to false]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt; Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## routeOutputFormatPost

> routeOutputFormatPost(outputFormat, points, opts)

Get the path, distance and travel time between a series of geographic points

Represents the geometry, distance, and time of the shortest or fastest path between given start and end points.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.RouteApi();
let outputFormat = "json"; // String | Format of representation
let points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'roundTrip': false, // Boolean | If true, route ends at start point. Default is false.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start/end point.Default is false.
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'" // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
};
apiInstance.routeOutputFormatPost(outputFormat, points, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Format of representation | [default to &#39;json&#39;]
 **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start/end point.Default is false. | [optional] [default to false]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## truckOptimalRouteOutputFormatGet

> truckOptimalRouteOutputFormatGet(outputFormat, points, opts)

Get the optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time for a commercial vehicle

Represents the geometry, distance, and time of the shortest or fastest path between a start point and a series of end points which are reordered to minimize distance or time for a commercial vehicle.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.RouteApi();
let outputFormat = "json"; // String | Format of representation
let points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'roundTrip': false, // Boolean | If true, route ends at start point. Default is false.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
  'truckRouteMultiplier': 9, // Number | The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
  'partition': "''", // String | A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. <br><br>Partition values:<br> isTruckRoute – Distinguish between truck route sections and non-truck route sections <br> isFerry – Distinguish between ferry sections and non-ferry sections <br> locality – Include the locality name for the route partition
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'" // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
};
apiInstance.truckOptimalRouteOutputFormatGet(outputFormat, points, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Format of representation | [default to &#39;json&#39;]
 **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false]
 **truckRouteMultiplier** | **Number**| The truck route multiplier value is used to multiply the cost of using roads that are not truck routes. | [optional] [default to 9]
 **partition** | **String**| A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition | [optional] [default to &#39;&#39;]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## truckOptimalRouteOutputFormatPost

> truckOptimalRouteOutputFormatPost(outputFormat, points, opts)

Get the path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.

Represents the geometry, distance, and time of the shortest or fastest path between a start point and a series of end points which are reordered to minimize total distance or time.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.RouteApi();
let outputFormat = "json"; // String | Format of representation
let points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'roundTrip': false, // Boolean | If true, route ends at start point. Default is false.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
  'truckRouteMultiplier': 9, // Number | The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
  'partition': "''", // String | A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. <br><br>Partition values:<br> isTruckRoute – Distinguish between truck route sections and non-truck route sections <br> isFerry – Distinguish between ferry sections and non-ferry sections <br> locality – Include the locality name for the route partition
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'" // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
};
apiInstance.truckOptimalRouteOutputFormatPost(outputFormat, points, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Format of representation | [default to &#39;json&#39;]
 **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false]
 **truckRouteMultiplier** | **Number**| The truck route multiplier value is used to multiply the cost of using roads that are not truck routes. | [optional] [default to 9]
 **partition** | **String**| A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition | [optional] [default to &#39;&#39;]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## truckRouteOutputFormatGet

> truckRouteOutputFormatGet(outputFormat, points, opts)

Get the path, distance and travel time between a series of geographic points for a commercial vehicle

Represents the geometry, distance, and time of the shortest or fastest path between given start and end points for a commercial vehicle.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.RouteApi();
let outputFormat = "json"; // String | Format of representation
let points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'roundTrip': false, // Boolean | If true, route ends at start point. Default is false.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start/end point.Default is false.
  'truckRouteMultiplier': 9, // Number | The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
  'partition': "''", // String | A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. <br><br>Partition values:<br> isTruckRoute – Distinguish between truck route sections and non-truck route sections <br> isFerry – Distinguish between ferry sections and non-ferry sections <br> locality – Include the locality name for the route partition
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br> Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'" // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
};
apiInstance.truckRouteOutputFormatGet(outputFormat, points, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Format of representation | [default to &#39;json&#39;]
 **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start/end point.Default is false. | [optional] [default to false]
 **truckRouteMultiplier** | **Number**| The truck route multiplier value is used to multiply the cost of using roads that are not truck routes. | [optional] [default to 9]
 **partition** | **String**| A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition | [optional] [default to &#39;&#39;]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt; Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## truckRouteOutputFormatPost

> truckRouteOutputFormatPost(outputFormat, points, opts)

Get the path, distance and travel time between a series of geographic points

Represents the geometry, distance, and time of the shortest or fastest path between given start and end points.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.RouteApi();
let outputFormat = "json"; // String | Format of representation
let points = "-123.70794,48.77869,-123.53785,48.38200"; // String | A list of any number of route points in start to end order. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target='_blank'>points</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'roundTrip': false, // Boolean | If true, route ends at start point. Default is false.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start/end point.Default is false.
  'truckRouteMultiplier': 9, // Number | The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
  'partition': "''", // String | A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. <br><br>Partition values:<br> isTruckRoute – Distinguish between truck route sections and non-truck route sections <br> isFerry – Distinguish between ferry sections and non-ferry sections <br> locality – Include the locality name for the route partition
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'" // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
};
apiInstance.truckRouteOutputFormatPost(outputFormat, points, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Format of representation | [default to &#39;json&#39;]
 **points** | **String**| A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **roundTrip** | **Boolean**| If true, route ends at start point. Default is false. | [optional] [default to false]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start/end point.Default is false. | [optional] [default to false]
 **truckRouteMultiplier** | **Number**| The truck route multiplier value is used to multiply the cost of using roads that are not truck routes. | [optional] [default to 9]
 **partition** | **String**| A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition | [optional] [default to &#39;&#39;]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

