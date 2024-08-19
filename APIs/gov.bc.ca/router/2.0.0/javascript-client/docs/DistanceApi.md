# BcRoutePlannerRestApi.DistanceApi

All URIs are relative to *https://router.api.gov.bc.ca*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distanceBetweenPairsOutputFormatGet**](DistanceApi.md#distanceBetweenPairsOutputFormatGet) | **GET** /distance/betweenPairs.{outputFormat} | Get distance and travel time between each pair of geographic points
[**distanceBetweenPairsOutputFormatPost**](DistanceApi.md#distanceBetweenPairsOutputFormatPost) | **POST** /distance/betweenPairs.{outputFormat} | Get distance and travel time between each pair of geographic points
[**distanceOutputFormatGet**](DistanceApi.md#distanceOutputFormatGet) | **GET** /distance.{outputFormat} | Get distance and travel time between two geographic points
[**distanceOutputFormatPost**](DistanceApi.md#distanceOutputFormatPost) | **POST** /distance.{outputFormat} | Get distance and travel time between two geographic points
[**truckDistanceBetweenPairsOutputFormatGet**](DistanceApi.md#truckDistanceBetweenPairsOutputFormatGet) | **GET** /truck/distance/betweenPairs.{outputFormat} | Get distance and travel time between each pair of geographic points for a commercial vehicle
[**truckDistanceBetweenPairsOutputFormatPost**](DistanceApi.md#truckDistanceBetweenPairsOutputFormatPost) | **POST** /truck/distance/betweenPairs.{outputFormat} | Get distance and travel time between each pair of geographic points
[**truckDistanceOutputFormatGet**](DistanceApi.md#truckDistanceOutputFormatGet) | **GET** /truck/distance.{outputFormat} | Get distance and travel time between two geographic points for a commercial vehicle
[**truckDistanceOutputFormatPost**](DistanceApi.md#truckDistanceOutputFormatPost) | **POST** /truck/distance.{outputFormat} | Get distance and travel time between two geographic points



## distanceBetweenPairsOutputFormatGet

> distanceBetweenPairsOutputFormatGet(outputFormat, fromPoints, toPoints, opts)

Get distance and travel time between each pair of geographic points

Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.DistanceApi();
let outputFormat = "json"; // String | Format of representation
let fromPoints = "-123.70794,48.77869,-123.53785,48.38200"; // String | A comma-separated list of origin points.  See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target='_blank'>fromPoints</a>
let toPoints = "-124.972951,49.715181,-123.139464,49.704015"; // String | A comma-separated list of destination points. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target='_blank'>toPoints</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'", // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
  'maxPairs': 56 // Number | The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs=1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs=3 means return the 3 nearest toPoints to each fromPoint.
};
apiInstance.distanceBetweenPairsOutputFormatGet(outputFormat, fromPoints, toPoints, opts, (error, data, response) => {
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
 **fromPoints** | **String**| A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt; | 
 **toPoints** | **String**| A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]
 **maxPairs** | **Number**| The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint. | [optional] 

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## distanceBetweenPairsOutputFormatPost

> distanceBetweenPairsOutputFormatPost(outputFormat, fromPoints, toPoints, opts)

Get distance and travel time between each pair of geographic points

Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.DistanceApi();
let outputFormat = "json"; // String | Format of representation
let fromPoints = "-123.70794,48.77869,-123.53785,48.38200"; // String | A comma-separated list of origin points.  See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target='_blank'>fromPoints</a>
let toPoints = "-124.972951,49.715181,-123.139464,49.704015"; // String | A comma-separated list of destination points. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target='_blank'>toPoints</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'", // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
  'maxPairs': 56 // Number | The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs=1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs=3 means return the 3 nearest toPoints to each fromPoint.
};
apiInstance.distanceBetweenPairsOutputFormatPost(outputFormat, fromPoints, toPoints, opts, (error, data, response) => {
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
 **fromPoints** | **String**| A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt; | 
 **toPoints** | **String**| A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]
 **maxPairs** | **Number**| The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint. | [optional] 

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## distanceOutputFormatGet

> distanceOutputFormatGet(outputFormat, points, opts)

Get distance and travel time between two geographic points

Represents the distance and time of the shortest or fastest path between given start and end points.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.DistanceApi();
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
apiInstance.distanceOutputFormatGet(outputFormat, points, opts, (error, data, response) => {
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


## distanceOutputFormatPost

> distanceOutputFormatPost(outputFormat, points, opts)

Get distance and travel time between two geographic points

Represents the distance and time of the shortest or fastest path between given start and end points.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.DistanceApi();
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
apiInstance.distanceOutputFormatPost(outputFormat, points, opts, (error, data, response) => {
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


## truckDistanceBetweenPairsOutputFormatGet

> truckDistanceBetweenPairsOutputFormatGet(outputFormat, fromPoints, toPoints, opts)

Get distance and travel time between each pair of geographic points for a commercial vehicle

Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints for a commercial vehicle. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.DistanceApi();
let outputFormat = "json"; // String | Format of representation
let fromPoints = "-123.70794,48.77869,-123.53785,48.38200"; // String | A comma-separated list of origin points.  See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target='_blank'>fromPoints</a>
let toPoints = "-124.972951,49.715181,-123.139464,49.704015"; // String | A comma-separated list of destination points. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target='_blank'>toPoints</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'", // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
  'maxPairs': 56 // Number | The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs=1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs=3 means return the 3 nearest toPoints to each fromPoint.
};
apiInstance.truckDistanceBetweenPairsOutputFormatGet(outputFormat, fromPoints, toPoints, opts, (error, data, response) => {
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
 **fromPoints** | **String**| A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt; | 
 **toPoints** | **String**| A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]
 **maxPairs** | **Number**| The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint. | [optional] 

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## truckDistanceBetweenPairsOutputFormatPost

> truckDistanceBetweenPairsOutputFormatPost(outputFormat, fromPoints, toPoints, opts)

Get distance and travel time between each pair of geographic points

Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.DistanceApi();
let outputFormat = "json"; // String | Format of representation
let fromPoints = "-123.70794,48.77869,-123.53785,48.38200"; // String | A comma-separated list of origin points.  See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target='_blank'>fromPoints</a>
let toPoints = "-124.972951,49.715181,-123.139464,49.704015"; // String | A comma-separated list of destination points. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target='_blank'>toPoints</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'criteria': "'shortest'", // String | Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
  'distanceUnit': "'km'", // String | distance unit of measure (e.g., km, mi). Default is km.
  'departure': new Date("2013-10-20T19:20:30+01:00"), // Date | departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);<br> Ignored if time-dependency modules are disabled
  'correctSide': false, // Boolean | If true, route starts and ends on same side of road as start and end points.Default is false.
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'", // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
  'maxPairs': 56 // Number | The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs=1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs=3 means return the 3 nearest toPoints to each fromPoint.
};
apiInstance.truckDistanceBetweenPairsOutputFormatPost(outputFormat, fromPoints, toPoints, opts, (error, data, response) => {
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
 **fromPoints** | **String**| A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt; | 
 **toPoints** | **String**| A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **criteria** | **String**| Routing criteria to optimize (e.g., shortest, fastest). Default is shortest. | [optional] [default to &#39;shortest&#39;]
 **distanceUnit** | **String**| distance unit of measure (e.g., km, mi). Default is km. | [optional] [default to &#39;km&#39;]
 **departure** | **Date**| departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled | [optional] 
 **correctSide** | **Boolean**| If true, route starts and ends on same side of road as start and end points.Default is false. | [optional] [default to false]
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]
 **maxPairs** | **Number**| The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint. | [optional] 

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## truckDistanceOutputFormatGet

> truckDistanceOutputFormatGet(outputFormat, points, opts)

Get distance and travel time between two geographic points for a commercial vehicle

Represents the distance and time of the shortest or fastest path between given start and end points.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.DistanceApi();
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
  'disable': "'sc,tf,ev,td'", // String | A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).<br><br>Module names include:<br> sc – ferry schedules; disabled by default; disabled by default and only suitable for demos<br>tf – historic traffic congestion; disabled by default and only suitable for demos<br>ev – road events; disabled by default and only suitable for demos<br>td – time-dependency; disabling this disables sc, tf, and ev modules<br>tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored<br>tc - turn costs (e.g., left turns take longer than right turns)
  'routeDescription': "'Routing results'" // String | Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
};
apiInstance.truckDistanceOutputFormatGet(outputFormat, points, opts, (error, data, response) => {
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
 **disable** | **String**| A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns) | [optional] [default to &#39;sc,tf,ev,td&#39;]
 **routeDescription** | **String**| Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster) | [optional] [default to &#39;Routing results&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## truckDistanceOutputFormatPost

> truckDistanceOutputFormatPost(outputFormat, points, opts)

Get distance and travel time between two geographic points

Represents the distance and time of the shortest or fastest path between given start and end points.

### Example

```javascript
import BcRoutePlannerRestApi from 'bc_route_planner_rest_api';
let defaultClient = BcRoutePlannerRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new BcRoutePlannerRestApi.DistanceApi();
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
apiInstance.truckDistanceOutputFormatPost(outputFormat, points, opts, (error, data, response) => {
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

