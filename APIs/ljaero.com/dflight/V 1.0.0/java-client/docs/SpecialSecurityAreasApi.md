# SpecialSecurityAreasApi

All URIs are relative to *https://dflight-api.ljaero.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ssaByDistanceUsV1SsaDistanceQueryPost**](SpecialSecurityAreasApi.md#ssaByDistanceUsV1SsaDistanceQueryPost) | **POST** /us/v1/ssa/distance-query | Retrieve all special security areas located within given distance of location. |
| [**ssaByPolyUsV1SsaPolygonQueryPost**](SpecialSecurityAreasApi.md#ssaByPolyUsV1SsaPolygonQueryPost) | **POST** /us/v1/ssa/polygon-query | Retrieve all special security areas located within given GeoJSON Polygon. |
| [**ssaByRouteUsV1SsaRouteQueryPost**](SpecialSecurityAreasApi.md#ssaByRouteUsV1SsaRouteQueryPost) | **POST** /us/v1/ssa/route-query | Retrieve all special security areas traversed by route. |


<a id="ssaByDistanceUsV1SsaDistanceQueryPost"></a>
# **ssaByDistanceUsV1SsaDistanceQueryPost**
> SSADistanceResponse ssaByDistanceUsV1SsaDistanceQueryPost(ssAByDistance, xApiKey)

Retrieve all special security areas located within given distance of location.

Retrieve special security areas existing within given distance from a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecialSecurityAreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    SpecialSecurityAreasApi apiInstance = new SpecialSecurityAreasApi(defaultClient);
    SSAByDistance ssAByDistance = new SSAByDistance(); // SSAByDistance | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      SSADistanceResponse result = apiInstance.ssaByDistanceUsV1SsaDistanceQueryPost(ssAByDistance, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecialSecurityAreasApi#ssaByDistanceUsV1SsaDistanceQueryPost");
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
| **ssAByDistance** | [**SSAByDistance**](SSAByDistance.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**SSADistanceResponse**](SSADistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each area found. |  -  |
| **422** | Validation Error |  -  |

<a id="ssaByPolyUsV1SsaPolygonQueryPost"></a>
# **ssaByPolyUsV1SsaPolygonQueryPost**
> SSAPolyResponse ssaByPolyUsV1SsaPolygonQueryPost(ssAByPolygon, xApiKey)

Retrieve all special security areas located within given GeoJSON Polygon.

Retrieve all special security areas located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecialSecurityAreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    SpecialSecurityAreasApi apiInstance = new SpecialSecurityAreasApi(defaultClient);
    SSAByPolygon ssAByPolygon = new SSAByPolygon(); // SSAByPolygon | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      SSAPolyResponse result = apiInstance.ssaByPolyUsV1SsaPolygonQueryPost(ssAByPolygon, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecialSecurityAreasApi#ssaByPolyUsV1SsaPolygonQueryPost");
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
| **ssAByPolygon** | [**SSAByPolygon**](SSAByPolygon.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**SSAPolyResponse**](SSAPolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each area found. |  -  |
| **422** | Validation Error |  -  |

<a id="ssaByRouteUsV1SsaRouteQueryPost"></a>
# **ssaByRouteUsV1SsaRouteQueryPost**
> SSARouteResponse ssaByRouteUsV1SsaRouteQueryPost(ssAByRoute, xApiKey)

Retrieve all special security areas traversed by route.

Retrieve all special security areas intersected by route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecialSecurityAreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    SpecialSecurityAreasApi apiInstance = new SpecialSecurityAreasApi(defaultClient);
    SSAByRoute ssAByRoute = new SSAByRoute(); // SSAByRoute | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      SSARouteResponse result = apiInstance.ssaByRouteUsV1SsaRouteQueryPost(ssAByRoute, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecialSecurityAreasApi#ssaByRouteUsV1SsaRouteQueryPost");
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
| **ssAByRoute** | [**SSAByRoute**](SSAByRoute.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**SSARouteResponse**](SSARouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each area found. |  -  |
| **422** | Validation Error |  -  |

