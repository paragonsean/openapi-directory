# AirspaceApi

All URIs are relative to *https://dflight-api.ljaero.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aspByDistanceUsV1AirspaceDistanceQueryPost**](AirspaceApi.md#aspByDistanceUsV1AirspaceDistanceQueryPost) | **POST** /us/v1/airspace/distance-query | Retrieve all requested types of airspace located within given distance of location. |
| [**aspByPolyUsV1AirspacePolygonQueryPost**](AirspaceApi.md#aspByPolyUsV1AirspacePolygonQueryPost) | **POST** /us/v1/airspace/polygon-query | Retrieve all requested types of airspace located within given GeoJSON Polygon. |
| [**aspByRouteUsV1AirspaceRouteQueryPost**](AirspaceApi.md#aspByRouteUsV1AirspaceRouteQueryPost) | **POST** /us/v1/airspace/route-query | Retrieve all requested types of airspace traversed by route. |


<a id="aspByDistanceUsV1AirspaceDistanceQueryPost"></a>
# **aspByDistanceUsV1AirspaceDistanceQueryPost**
> AirspaceDistanceResponse aspByDistanceUsV1AirspaceDistanceQueryPost(airspaceByDistance, xApiKey)

Retrieve all requested types of airspace located within given distance of location.

Retrieve selected types of airspace existing within given distance from a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000) * asptypes:  list of one or more airspace types you wish to retrieve. Allowed values are &#39;CAS&#39;, &#39;SUA&#39;, &#39;MAA&#39;, and &#39;MTR&#39;.  Successful requests return a list of GeoJSON FeatureCollections, one for each Airspace type indicated in the request. Within each feature collection, there will be a separate Feature for each Airspace instance found. All Features will include a property indicating the *airspace_type*. Additional properties for each *airspace_type* are as follows: * CAS (Controlled Airspace)     - *name*     - *cas_class*: B, C, D, or E2     - *floor*: integer value in ft MSL     - *ceiling*: integer value in ft MSL     - *lannc*: true/false indicating whether or not authorization for this airspace may be obtained via LAANC * SUA (Special Use Airspace)     - *name*     - *sua_type*: AA &#x3D; Alert Area, MOA &#x3D; Military Operations Area, NSA &#x3D; National Security Area, PA &#x3D; Prohibited Area, RA &#x3D; Restricted Area, WA &#x3D; Warning Area     - *floor*: lower limit of the airspace     - *floor_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *floor_ref*: reference level used for the numeric floor value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *ceiling*: upper limit of the airspace     - *ceiling_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *ceiling_ref*: reference level used for the numeric ceiling value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *ceiling_ref*: reference level used for the numeric ceiling value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *schedule*: default activation days/times (other times by NOTAM) * MAA (Miscellaneous Activity Area)     - *name*     - *maa_type*: one of the following - ULTRALIGHT, PARACHUTE JUMP AREA, AEROBATIC PRACTICE, GLIDER, HANG GLIDER, SPACE LAUNCH ACTIVITY     - *use_times*: textual description of days/times when activity in the area should be expected * MTR (Military Training Route)     - *name*     - *use_times*: textual description of days/times when MTR is active/hot     - *terrain_following*: boolean value indicating whether terrain following activity occurs on the route     - *max_extent_nm*: maximum distance that aircraft can deviate from route centerline

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    AirspaceApi apiInstance = new AirspaceApi(defaultClient);
    AirspaceByDistance airspaceByDistance = new AirspaceByDistance(); // AirspaceByDistance | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      AirspaceDistanceResponse result = apiInstance.aspByDistanceUsV1AirspaceDistanceQueryPost(airspaceByDistance, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirspaceApi#aspByDistanceUsV1AirspaceDistanceQueryPost");
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
| **airspaceByDistance** | [**AirspaceByDistance**](AirspaceByDistance.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**AirspaceDistanceResponse**](AirspaceDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of GeoJSON FeatureCollections, one for each Airspace type requested. |  -  |
| **422** | Validation Error |  -  |

<a id="aspByPolyUsV1AirspacePolygonQueryPost"></a>
# **aspByPolyUsV1AirspacePolygonQueryPost**
> AirspacePolyResponse aspByPolyUsV1AirspacePolygonQueryPost(airspaceByPolygon, xApiKey)

Retrieve all requested types of airspace located within given GeoJSON Polygon.

Retrieve selected types of airspace located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2. * asptypes:  list of one or more airspace types you wish to retrieve. Allowed values are &#39;CAS&#39;, &#39;SUA&#39;, &#39;MAA&#39;, and &#39;MTR&#39;.  Successful requests return a list of GeoJSON FeatureCollections, one for each Airspace type indicated in the request. Within each feature collection, there will be a separate Feature for each Airspace instance found. All Features will include a property indicating the *airspace_type*. Additional properties for each *airspace_type* are as follows: * CAS (Controlled Airspace)     - *name*     - *cas_class*: B, C, D, or E2     - *floor*: integer value in ft MSL     - *ceiling*: integer value in ft MSL     - *lannc*: true/false indicating whether or not authorization for this airspace may be obtained via LAANC * SUA (Special Use Airspace)     - *name*     - *sua_type*: AA &#x3D; Alert Area, MOA &#x3D; Military Operations Area, NSA &#x3D; National Security Area, PA &#x3D; Prohibited Area, RA &#x3D; Restricted Area, WA &#x3D; Warning Area     - *floor*: lower limit of the airspace     - *floor_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *floor_ref*: reference level used for the numeric floor value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *ceiling*: upper limit of the airspace     - *ceiling_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *ceiling_ref*: reference level used for the numeric ceiling value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *schedule*: default activation days/times (other times by NOTAM) * MAA (Miscellaneous Activity Area)     - *name*     - *maa_type*: one of the following - ULTRALIGHT, PARACHUTE JUMP AREA, AEROBATIC PRACTICE, GLIDER, HANG GLIDER, SPACE LAUNCH ACTIVITY     - *use_times*: textual description of days/times when activity in the area should be expected * MTR (Military Training Route)     - *name*     - *use_times*: textual description of days/times when MTR is active/hot     - *terrain_following*: boolean value indicating whether terrain following activity occurs on the route     - *max_extent_nm*: maximum distance that aircraft can deviate from route centerline

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    AirspaceApi apiInstance = new AirspaceApi(defaultClient);
    AirspaceByPolygon airspaceByPolygon = new AirspaceByPolygon(); // AirspaceByPolygon | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      AirspacePolyResponse result = apiInstance.aspByPolyUsV1AirspacePolygonQueryPost(airspaceByPolygon, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirspaceApi#aspByPolyUsV1AirspacePolygonQueryPost");
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
| **airspaceByPolygon** | [**AirspaceByPolygon**](AirspaceByPolygon.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**AirspacePolyResponse**](AirspacePolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of GeoJSON FeatureCollections, one for each Airspace type requested. |  -  |
| **422** | Validation Error |  -  |

<a id="aspByRouteUsV1AirspaceRouteQueryPost"></a>
# **aspByRouteUsV1AirspaceRouteQueryPost**
> AirspaceRouteResponse aspByRouteUsV1AirspaceRouteQueryPost(airspaceByRoute, xApiKey)

Retrieve all requested types of airspace traversed by route.

Retrieve selected types of airspace traversed by route. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km. * asptypes:  list of one or more airspace types you wish to retrieve. Allowed values are &#39;CAS&#39;, &#39;SUA&#39;, &#39;MAA&#39;, and &#39;MTR&#39;.  Successful requests return a list of GeoJSON FeatureCollections, one for each Airspace type indicated in the request. Within each feature collection, there will be a separate Feature for each Airspace instance found. All Features will include a property indicating the *airspace_type*. Additional properties for each *airspace_type* are as follows: * CAS (Controlled Airspace)     - *name*     - *cas_class*: B, C, D, or E2     - *floor*: integer value in ft MSL     - *ceiling*: integer value in ft MSL     - *lannc*: true/false indicating whether or not authorization for this airspace may be obtained via LAANC * SUA (Special Use Airspace)     - *name*     - *sua_type*: AA &#x3D; Alert Area, MOA &#x3D; Military Operations Area, NSA &#x3D; National Security Area, PA &#x3D; Prohibited Area, RA &#x3D; Restricted Area, WA &#x3D; Warning Area     - *floor*: lower limit of the airspace     - *floor_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *floor_ref*: reference level used for the numeric floor value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *ceiling*: upper limit of the airspace     - *ceiling_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *ceiling_ref*: reference level used for the numeric ceiling value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *schedule*: default activation days/times (other times by NOTAM) * MAA (Miscellaneous Activity Area)     - *name*     - *maa_type*: one of the following - ULTRALIGHT, PARACHUTE JUMP AREA, AEROBATIC PRACTICE, GLIDER, HANG GLIDER, SPACE LAUNCH ACTIVITY     - *use_times*: textual description of days/times when activity in the area should be expected * MTR (Military Training Route)     - *name*     - *use_times*: textual description of days/times when MTR is active/hot     - *terrain_following*: boolean value indicating whether terrain following activity occurs on the route     - *max_extent_nm*: maximum distance that aircraft can deviate from route centerline

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    AirspaceApi apiInstance = new AirspaceApi(defaultClient);
    AirspaceByRoute airspaceByRoute = new AirspaceByRoute(); // AirspaceByRoute | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      AirspaceRouteResponse result = apiInstance.aspByRouteUsV1AirspaceRouteQueryPost(airspaceByRoute, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirspaceApi#aspByRouteUsV1AirspaceRouteQueryPost");
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
| **airspaceByRoute** | [**AirspaceByRoute**](AirspaceByRoute.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**AirspaceRouteResponse**](AirspaceRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of GeoJSON FeatureCollections, one for each Airspace type requested. |  -  |
| **422** | Validation Error |  -  |

