# FlightRestrictionsApi

All URIs are relative to *https://dflight-api.ljaero.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tfrByDistanceUsV1RestrictionsDistanceQueryPost**](FlightRestrictionsApi.md#tfrByDistanceUsV1RestrictionsDistanceQueryPost) | **POST** /us/v1/restrictions/distance-query | Retrieve flight restrictions applicable within given distance of location. |
| [**tfrByPolyUsV1RestrictionsPolygonQueryPost**](FlightRestrictionsApi.md#tfrByPolyUsV1RestrictionsPolygonQueryPost) | **POST** /us/v1/restrictions/polygon-query | Retrieve flight restrictions applicable within given area. |
| [**tfrByRouteUsV1RestrictionsRouteQueryPost**](FlightRestrictionsApi.md#tfrByRouteUsV1RestrictionsRouteQueryPost) | **POST** /us/v1/restrictions/route-query | Retrieve flight restrictions applicable along route. |


<a id="tfrByDistanceUsV1RestrictionsDistanceQueryPost"></a>
# **tfrByDistanceUsV1RestrictionsDistanceQueryPost**
> NOTAMsDistanceResponse tfrByDistanceUsV1RestrictionsDistanceQueryPost(noTAMsByDistance, xApiKey)

Retrieve flight restrictions applicable within given distance of location.

Retrieve Flight Restrictions applicable within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlightRestrictionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    FlightRestrictionsApi apiInstance = new FlightRestrictionsApi(defaultClient);
    NOTAMsByDistance noTAMsByDistance = new NOTAMsByDistance(); // NOTAMsByDistance | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      NOTAMsDistanceResponse result = apiInstance.tfrByDistanceUsV1RestrictionsDistanceQueryPost(noTAMsByDistance, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlightRestrictionsApi#tfrByDistanceUsV1RestrictionsDistanceQueryPost");
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
| **noTAMsByDistance** | [**NOTAMsByDistance**](NOTAMsByDistance.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**NOTAMsDistanceResponse**](NOTAMsDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each restriction. |  -  |
| **422** | Validation Error |  -  |

<a id="tfrByPolyUsV1RestrictionsPolygonQueryPost"></a>
# **tfrByPolyUsV1RestrictionsPolygonQueryPost**
> NOTAMsPolyResponse tfrByPolyUsV1RestrictionsPolygonQueryPost(noTAMsByPolygon, xApiKey)

Retrieve flight restrictions applicable within given area.

Retrieve Flight Restrictions located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlightRestrictionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    FlightRestrictionsApi apiInstance = new FlightRestrictionsApi(defaultClient);
    NOTAMsByPolygon noTAMsByPolygon = new NOTAMsByPolygon(); // NOTAMsByPolygon | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      NOTAMsPolyResponse result = apiInstance.tfrByPolyUsV1RestrictionsPolygonQueryPost(noTAMsByPolygon, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlightRestrictionsApi#tfrByPolyUsV1RestrictionsPolygonQueryPost");
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
| **noTAMsByPolygon** | [**NOTAMsByPolygon**](NOTAMsByPolygon.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**NOTAMsPolyResponse**](NOTAMsPolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each restriction. |  -  |
| **422** | Validation Error |  -  |

<a id="tfrByRouteUsV1RestrictionsRouteQueryPost"></a>
# **tfrByRouteUsV1RestrictionsRouteQueryPost**
> NOTAMsRouteResponse tfrByRouteUsV1RestrictionsRouteQueryPost(noTAMsByRoute, xApiKey)

Retrieve flight restrictions applicable along route.

Retrieve Flight Restrictions applicable along your route. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlightRestrictionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    FlightRestrictionsApi apiInstance = new FlightRestrictionsApi(defaultClient);
    NOTAMsByRoute noTAMsByRoute = new NOTAMsByRoute(); // NOTAMsByRoute | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      NOTAMsRouteResponse result = apiInstance.tfrByRouteUsV1RestrictionsRouteQueryPost(noTAMsByRoute, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlightRestrictionsApi#tfrByRouteUsV1RestrictionsRouteQueryPost");
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
| **noTAMsByRoute** | [**NOTAMsByRoute**](NOTAMsByRoute.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**NOTAMsRouteResponse**](NOTAMsRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each restriction. |  -  |
| **422** | Validation Error |  -  |

