# RoutingApiApi

All URIs are relative to *https://graphhopper.com/api/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRoute**](RoutingApiApi.md#getRoute) | **GET** /route | GET Route Endpoint |
| [**postRoute**](RoutingApiApi.md#postRoute) | **POST** /route | POST Route Endpoint |
| [**routeInfoGet**](RoutingApiApi.md#routeInfoGet) | **GET** /route/info | Coverage information |


<a id="getRoute"></a>
# **getRoute**
> RouteResponse getRoute(point, pointHint, snapPrevention, vehicle, curbside, turnCosts, locale, elevation, details, optimize, instructions, calcPoints, debug, pointsEncoded, chDisable, weighting, heading, headingPenalty, passThrough, blockArea, avoid, algorithm, roundTripDistance, roundTripSeed, alternativeRouteMaxPaths, alternativeRouteMaxWeightFactor, alternativeRouteMaxShareFactor)

GET Route Endpoint

The GET request is the most simple one: just specify the parameter in the URL and you are done. Can be tried directly in every browser. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RoutingApiApi apiInstance = new RoutingApiApi(defaultClient);
    List<String> point = Arrays.asList(); // List<String> | The points for which the route should be calculated. Format: `[latitude,longitude]`. Specify at least an origin and a destination. Via points are possible. The maximum number depends on your plan. 
    List<String> pointHint = Arrays.asList(); // List<String> | The `point_hint` is typically a road name to which the associated `point` parameter should be snapped to. Specify no `point_hint` parameter or the same number as you have `point` parameters. 
    List<String> snapPrevention = Arrays.asList(); // List<String> | Optional parameter to avoid snapping to a certain road class or road environment. Currently supported values are `motorway`, `trunk`, `ferry`, `tunnel`, `bridge` and `ford`. Multiple values are specified like `snap_prevention=ferry&snap_prevention=motorway`. 
    VehicleProfileId vehicle = VehicleProfileId.fromValue("car"); // VehicleProfileId | The vehicle profile for which the route should be calculated. 
    List<String> curbside = Arrays.asList(); // List<String> | Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap. 
    Boolean turnCosts = false; // Boolean | Specifies if turn restrictions should be considered. Enabling this option increases the route computation time. Only supported for motor vehicles and OpenStreetMap. 
    String locale = "en"; // String | The locale of the resulting turn instructions. E.g. `pt_PT` for Portuguese or `de` for German. 
    Boolean elevation = false; // Boolean | If `true`, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the `points` and `snapped_waypoints` fields of the response, in both their encodings. Unless you switch off the `points_encoded` parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile. 
    List<String> details = Arrays.asList(); // List<String> | Optional parameter to retrieve path details. You can request additional details for the route: `street_name`,  `time`, `distance`, `max_speed`, `toll`, `road_class`, `road_class_link`, `road_access`, `road_environment`, `lanes`, and `surface`. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539). 
    String optimize = "false"; // String | Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to `\"true\"` and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits. 
    Boolean instructions = true; // Boolean | If instructions should be calculated and returned 
    Boolean calcPoints = true; // Boolean | If the points for the route should be calculated at all. 
    Boolean debug = false; // Boolean | If `true`, the output will be formatted. 
    Boolean pointsEncoded = true; // Boolean | Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to `false` to switch the encoding to simple coordinate pairs like `[lon,lat]`, or `[lon,lat,elevation]`. See the description of the response format for more information. 
    Boolean chDisable = false; // Boolean | Use this parameter in combination with one or more parameters from below. 
    String weighting = "fastest"; // String | Determines the way the \"best\" route is calculated. Besides `fastest` you can use `short_fastest` which finds a reasonable balance between the distance influence (`shortest`) and the time (`fastest`). You could also use `shortest` but is deprecated and not recommended for motor vehicles. All except `fastest` require `ch.disable=true`. 
    List<Integer> heading = Arrays.asList(); // List<Integer> | Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with `algorithm=round_trip` and forces the initial direction.  Requires `ch.disable=true`. 
    Integer headingPenalty = 120; // Integer | Time penalty in seconds for not obeying a specified heading. Requires `ch.disable=true`. 
    Boolean passThrough = false; // Boolean | If `true`, u-turns are avoided at via-points with regard to the `heading_penalty`. Requires `ch.disable=true`. 
    String blockArea = "blockArea_example"; // String | Block road access by specifying a point close to the road segment to be blocked, with the format `lat,lon`. You can also block all road segments crossing a geometric shape. Specify a circle using the format `lat,lon,radius`, or a polygon using the format `lat1,lon1,lat2,lon2,...,latN,lonN`. You can specify several shapes, separating them with `;`. Requires `ch.disable=true`. 
    String avoid = "avoid_example"; // String | Specify which road classes and environments you would like to avoid.  Possible values are `motorway`, `steps`, `track`, `toll`, `ferry`, `tunnel` and `bridge`. Separate several values with `;`. Obviously not all the values make sense for all vehicle profiles e.g. `bike` is already forbidden on a `motorway`. Requires `ch.disable=true`. 
    String algorithm = "round_trip"; // String | Rather than looking for the shortest or fastest path, this parameter lets you solve two different problems related to routing: With `alternative_route`, we give you not one but several routes that are close to optimal, but not too similar to each other.  With `round_trip`, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. The `round_trip` option requires `ch.disable=true`. You can control both of these features with additional parameters, see below.  
    Integer roundTripDistance = 10000; // Integer | If `algorithm=round_trip`, this parameter configures approximative length of the resulting round trip. Requires `ch.disable=true`. 
    Long roundTripSeed = 56L; // Long | If `algorithm=round_trip`, this sets the random seed. Change this to get a different tour for each value. 
    Integer alternativeRouteMaxPaths = 2; // Integer | If `algorithm=alternative_route`, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives. 
    BigDecimal alternativeRouteMaxWeightFactor = new BigDecimal("1.4"); // BigDecimal | If `algorithm=alternative_route`, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives. 
    BigDecimal alternativeRouteMaxShareFactor = new BigDecimal("0.6"); // BigDecimal | If `algorithm=alternative_route`, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives. 
    try {
      RouteResponse result = apiInstance.getRoute(point, pointHint, snapPrevention, vehicle, curbside, turnCosts, locale, elevation, details, optimize, instructions, calcPoints, debug, pointsEncoded, chDisable, weighting, heading, headingPenalty, passThrough, blockArea, avoid, algorithm, roundTripDistance, roundTripSeed, alternativeRouteMaxPaths, alternativeRouteMaxWeightFactor, alternativeRouteMaxShareFactor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApiApi#getRoute");
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
| **point** | [**List&lt;String&gt;**](String.md)| The points for which the route should be calculated. Format: &#x60;[latitude,longitude]&#x60;. Specify at least an origin and a destination. Via points are possible. The maximum number depends on your plan.  | |
| **pointHint** | [**List&lt;String&gt;**](String.md)| The &#x60;point_hint&#x60; is typically a road name to which the associated &#x60;point&#x60; parameter should be snapped to. Specify no &#x60;point_hint&#x60; parameter or the same number as you have &#x60;point&#x60; parameters.  | [optional] |
| **snapPrevention** | [**List&lt;String&gt;**](String.md)| Optional parameter to avoid snapping to a certain road class or road environment. Currently supported values are &#x60;motorway&#x60;, &#x60;trunk&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60;, &#x60;bridge&#x60; and &#x60;ford&#x60;. Multiple values are specified like &#x60;snap_prevention&#x3D;ferry&amp;snap_prevention&#x3D;motorway&#x60;.  | [optional] |
| **vehicle** | [**VehicleProfileId**](.md)| The vehicle profile for which the route should be calculated.  | [optional] [default to car] [enum: car, bike, foot, hike, mtb, racingbike, scooter, truck, small_truck] |
| **curbside** | [**List&lt;String&gt;**](String.md)| Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.  | [optional] [enum: any, right, left] |
| **turnCosts** | **Boolean**| Specifies if turn restrictions should be considered. Enabling this option increases the route computation time. Only supported for motor vehicles and OpenStreetMap.  | [optional] [default to false] |
| **locale** | **String**| The locale of the resulting turn instructions. E.g. &#x60;pt_PT&#x60; for Portuguese or &#x60;de&#x60; for German.  | [optional] [default to en] |
| **elevation** | **Boolean**| If &#x60;true&#x60;, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the &#x60;points&#x60; and &#x60;snapped_waypoints&#x60; fields of the response, in both their encodings. Unless you switch off the &#x60;points_encoded&#x60; parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile.  | [optional] [default to false] |
| **details** | [**List&lt;String&gt;**](String.md)| Optional parameter to retrieve path details. You can request additional details for the route: &#x60;street_name&#x60;,  &#x60;time&#x60;, &#x60;distance&#x60;, &#x60;max_speed&#x60;, &#x60;toll&#x60;, &#x60;road_class&#x60;, &#x60;road_class_link&#x60;, &#x60;road_access&#x60;, &#x60;road_environment&#x60;, &#x60;lanes&#x60;, and &#x60;surface&#x60;. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539).  | [optional] |
| **optimize** | **String**| Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to &#x60;\&quot;true\&quot;&#x60; and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits.  | [optional] [default to false] |
| **instructions** | **Boolean**| If instructions should be calculated and returned  | [optional] [default to true] |
| **calcPoints** | **Boolean**| If the points for the route should be calculated at all.  | [optional] [default to true] |
| **debug** | **Boolean**| If &#x60;true&#x60;, the output will be formatted.  | [optional] [default to false] |
| **pointsEncoded** | **Boolean**| Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to &#x60;false&#x60; to switch the encoding to simple coordinate pairs like &#x60;[lon,lat]&#x60;, or &#x60;[lon,lat,elevation]&#x60;. See the description of the response format for more information.  | [optional] [default to true] |
| **chDisable** | **Boolean**| Use this parameter in combination with one or more parameters from below.  | [optional] [default to false] |
| **weighting** | **String**| Determines the way the \&quot;best\&quot; route is calculated. Besides &#x60;fastest&#x60; you can use &#x60;short_fastest&#x60; which finds a reasonable balance between the distance influence (&#x60;shortest&#x60;) and the time (&#x60;fastest&#x60;). You could also use &#x60;shortest&#x60; but is deprecated and not recommended for motor vehicles. All except &#x60;fastest&#x60; require &#x60;ch.disable&#x3D;true&#x60;.  | [optional] [default to fastest] |
| **heading** | [**List&lt;Integer&gt;**](Integer.md)| Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with &#x60;algorithm&#x3D;round_trip&#x60; and forces the initial direction.  Requires &#x60;ch.disable&#x3D;true&#x60;.  | [optional] |
| **headingPenalty** | **Integer**| Time penalty in seconds for not obeying a specified heading. Requires &#x60;ch.disable&#x3D;true&#x60;.  | [optional] [default to 120] |
| **passThrough** | **Boolean**| If &#x60;true&#x60;, u-turns are avoided at via-points with regard to the &#x60;heading_penalty&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  | [optional] [default to false] |
| **blockArea** | **String**| Block road access by specifying a point close to the road segment to be blocked, with the format &#x60;lat,lon&#x60;. You can also block all road segments crossing a geometric shape. Specify a circle using the format &#x60;lat,lon,radius&#x60;, or a polygon using the format &#x60;lat1,lon1,lat2,lon2,...,latN,lonN&#x60;. You can specify several shapes, separating them with &#x60;;&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  | [optional] |
| **avoid** | **String**| Specify which road classes and environments you would like to avoid.  Possible values are &#x60;motorway&#x60;, &#x60;steps&#x60;, &#x60;track&#x60;, &#x60;toll&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60; and &#x60;bridge&#x60;. Separate several values with &#x60;;&#x60;. Obviously not all the values make sense for all vehicle profiles e.g. &#x60;bike&#x60; is already forbidden on a &#x60;motorway&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  | [optional] |
| **algorithm** | **String**| Rather than looking for the shortest or fastest path, this parameter lets you solve two different problems related to routing: With &#x60;alternative_route&#x60;, we give you not one but several routes that are close to optimal, but not too similar to each other.  With &#x60;round_trip&#x60;, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. The &#x60;round_trip&#x60; option requires &#x60;ch.disable&#x3D;true&#x60;. You can control both of these features with additional parameters, see below.   | [optional] [enum: round_trip, alternative_route] |
| **roundTripDistance** | **Integer**| If &#x60;algorithm&#x3D;round_trip&#x60;, this parameter configures approximative length of the resulting round trip. Requires &#x60;ch.disable&#x3D;true&#x60;.  | [optional] [default to 10000] |
| **roundTripSeed** | **Long**| If &#x60;algorithm&#x3D;round_trip&#x60;, this sets the random seed. Change this to get a different tour for each value.  | [optional] |
| **alternativeRouteMaxPaths** | **Integer**| If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives.  | [optional] [default to 2] |
| **alternativeRouteMaxWeightFactor** | **BigDecimal**| If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives.  | [optional] [default to 1.4] |
| **alternativeRouteMaxShareFactor** | **BigDecimal**| If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives.  | [optional] [default to 0.6] |

### Return type

[**RouteResponse**](RouteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Routing Result |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **400** | Your request is not valid. For example, you specified too few or too many points. |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **401** | Authentication necessary |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **429** | API limit reached. |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **500** | Internal server error. We get notified automatically and fix this asap. |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **501** | Only a special list of vehicles is supported. |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |

<a id="postRoute"></a>
# **postRoute**
> RouteResponse postRoute(routeRequest)

POST Route Endpoint

Please see the [GET endpoint](#operation/getRoute) for a simpler method on how to get started. If you are familiar with POST requests and JSON then do not hesitate to continue here.  Especially when you use many locations you should get familiar with this POST endpoint as the GET endpoint has an URL length limitation. Additionally the request of this POST endpoint can be compressed and can slightly speed up the request.  To do a request you send JSON data. Both request scenarios GET and POST are identical except that all singular parameter names are named as their plural for a POST request. The effected parameters are: &#x60;points&#x60;, &#x60;point_hints&#x60; and &#x60;snap_preventions&#x60;.  **Please note that in opposite to the GET endpoint, points are specified in the order of &#x60;longitude, latitude&#x60;**.  For example &#x60;point&#x3D;10,11&amp;point&#x3D;20,22&#x60; will be converted to the &#x60;points&#x60; array (plural): &#x60;&#x60;&#x60;json { \&quot;points\&quot;: [[11,10], [22,20]] } &#x60;&#x60;&#x60; Note again that also the order changes from &#x60;[latitude,longitude]&#x60; to &#x60;[longitude,latitude]&#x60; similar to [GeoJson](http://geojson.org/geojson-spec.html#examples).  Example: &#x60;&#x60;&#x60;bash curl -X POST -H \&quot;Content-Type: application/json\&quot; \&quot;https://graphhopper.com/api/1/route?key&#x3D;[YOUR_KEY]\&quot; -d &#39;{\&quot;elevation\&quot;:false,\&quot;points\&quot;:[[-0.087891,51.534377],[-0.090637,51.467697]],\&quot;vehicle\&quot;:\&quot;car\&quot;}&#39; &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RoutingApiApi apiInstance = new RoutingApiApi(defaultClient);
    RouteRequest routeRequest = new RouteRequest(); // RouteRequest | 
    try {
      RouteResponse result = apiInstance.postRoute(routeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApiApi#postRoute");
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
| **routeRequest** | [**RouteRequest**](RouteRequest.md)|  | [optional] |

### Return type

[**RouteResponse**](RouteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Routing Result |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **400** | Your request is not valid. For example, you specified too few or too many points. |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **401** | Authentication necessary |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **429** | API limit reached. |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **500** | Internal server error. We get notified automatically and fix this asap. |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **501** | Only a special list of vehicles is supported. |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |

<a id="routeInfoGet"></a>
# **routeInfoGet**
> InfoResponse routeInfoGet()

Coverage information

Use this to find out details about the supported vehicle profiles and features, or if you just need to ping the server. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RoutingApiApi apiInstance = new RoutingApiApi(defaultClient);
    try {
      InfoResponse result = apiInstance.routeInfoGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApiApi#routeInfoGet");
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

[**InfoResponse**](InfoResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Coverage Information |  -  |

