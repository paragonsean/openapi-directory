# AerodromesApi

All URIs are relative to *https://dflight-api.ljaero.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aerodromesByDistanceUsV1AerodromesDistanceQueryPost**](AerodromesApi.md#aerodromesByDistanceUsV1AerodromesDistanceQueryPost) | **POST** /us/v1/aerodromes/distance-query | Retrieve aerodromes within given distance of location. |
| [**aerodromesByPolyUsV1AerodromesPolygonQueryPost**](AerodromesApi.md#aerodromesByPolyUsV1AerodromesPolygonQueryPost) | **POST** /us/v1/aerodromes/polygon-query | Retrieve aerodromes located within given area. |
| [**aerodromesByRouteUsV1AerodromesRouteQueryPost**](AerodromesApi.md#aerodromesByRouteUsV1AerodromesRouteQueryPost) | **POST** /us/v1/aerodromes/route-query | Retrieve aerodromes found along a route. |


<a id="aerodromesByDistanceUsV1AerodromesDistanceQueryPost"></a>
# **aerodromesByDistanceUsV1AerodromesDistanceQueryPost**
> AerodromeDistanceResponse aerodromesByDistanceUsV1AerodromesDistanceQueryPost(aerodromesByDistance, xApiKey)

Retrieve aerodromes within given distance of location.

Retrieve aerodromes within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)  Successful requests return a GeoJSON FeatureCollection, with a separate Feature for each Aerodrome found. All Features will include properties for the facility name, ident, type, and operational status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AerodromesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    AerodromesApi apiInstance = new AerodromesApi(defaultClient);
    AerodromesByDistance aerodromesByDistance = new AerodromesByDistance(); // AerodromesByDistance | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      AerodromeDistanceResponse result = apiInstance.aerodromesByDistanceUsV1AerodromesDistanceQueryPost(aerodromesByDistance, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AerodromesApi#aerodromesByDistanceUsV1AerodromesDistanceQueryPost");
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
| **aerodromesByDistance** | [**AerodromesByDistance**](AerodromesByDistance.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**AerodromeDistanceResponse**](AerodromeDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each aerodrome found. |  -  |
| **422** | Validation Error |  -  |

<a id="aerodromesByPolyUsV1AerodromesPolygonQueryPost"></a>
# **aerodromesByPolyUsV1AerodromesPolygonQueryPost**
> AerodromePolyResponse aerodromesByPolyUsV1AerodromesPolygonQueryPost(aerodromesByPolygon, xApiKey)

Retrieve aerodromes located within given area.

Retrieve aerodromes located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.  Successful requests return a GeoJSON FeatureCollection, with a separate Feature for each Aerodrome found. All Features will include properties for the facility name, ident, type, and operational status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AerodromesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    AerodromesApi apiInstance = new AerodromesApi(defaultClient);
    AerodromesByPolygon aerodromesByPolygon = new AerodromesByPolygon(); // AerodromesByPolygon | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      AerodromePolyResponse result = apiInstance.aerodromesByPolyUsV1AerodromesPolygonQueryPost(aerodromesByPolygon, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AerodromesApi#aerodromesByPolyUsV1AerodromesPolygonQueryPost");
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
| **aerodromesByPolygon** | [**AerodromesByPolygon**](AerodromesByPolygon.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**AerodromePolyResponse**](AerodromePolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each aerodrome found. |  -  |
| **422** | Validation Error |  -  |

<a id="aerodromesByRouteUsV1AerodromesRouteQueryPost"></a>
# **aerodromesByRouteUsV1AerodromesRouteQueryPost**
> AerodromeRouteResponse aerodromesByRouteUsV1AerodromesRouteQueryPost(aerodromesByRoute, xApiKey)

Retrieve aerodromes found along a route.

Retrieve aerodromes found along a route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.  Successful requests return a GeoJSON FeatureCollection, with a separate Feature for each Aerodrome found. All Features will include properties for the facility name, ident, type, and operational status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AerodromesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    AerodromesApi apiInstance = new AerodromesApi(defaultClient);
    AerodromesByRoute aerodromesByRoute = new AerodromesByRoute(); // AerodromesByRoute | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      AerodromeRouteResponse result = apiInstance.aerodromesByRouteUsV1AerodromesRouteQueryPost(aerodromesByRoute, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AerodromesApi#aerodromesByRouteUsV1AerodromesRouteQueryPost");
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
| **aerodromesByRoute** | [**AerodromesByRoute**](AerodromesByRoute.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**AerodromeRouteResponse**](AerodromeRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each aerodrome found. |  -  |
| **422** | Validation Error |  -  |

