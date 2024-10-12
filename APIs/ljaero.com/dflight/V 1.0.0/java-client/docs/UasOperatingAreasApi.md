# UasOperatingAreasApi

All URIs are relative to *https://dflight-api.ljaero.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uoaByDistanceUsV1UoaDistanceQueryPost**](UasOperatingAreasApi.md#uoaByDistanceUsV1UoaDistanceQueryPost) | **POST** /us/v1/uoa/distance-query | Retrieve UAS Operating Areas (UOAs) found within given distance of location. |
| [**uoaByPolyUsV1UoaPolygonQueryPost**](UasOperatingAreasApi.md#uoaByPolyUsV1UoaPolygonQueryPost) | **POST** /us/v1/uoa/polygon-query | Retrieve UAS Operating Areas (UOAs) found within given area. |
| [**uoaByRouteUsV1UoaRouteQueryPost**](UasOperatingAreasApi.md#uoaByRouteUsV1UoaRouteQueryPost) | **POST** /us/v1/uoa/route-query | Retrieve UAS Operating Areas (UOAs) found along route. |


<a id="uoaByDistanceUsV1UoaDistanceQueryPost"></a>
# **uoaByDistanceUsV1UoaDistanceQueryPost**
> UOAsDistanceResponse uoaByDistanceUsV1UoaDistanceQueryPost(uoAsByDistance, xApiKey)

Retrieve UAS Operating Areas (UOAs) found within given distance of location.

Retrieve UAS Operating Areas (UOAs) found within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UasOperatingAreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    UasOperatingAreasApi apiInstance = new UasOperatingAreasApi(defaultClient);
    UOAsByDistance uoAsByDistance = new UOAsByDistance(); // UOAsByDistance | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      UOAsDistanceResponse result = apiInstance.uoaByDistanceUsV1UoaDistanceQueryPost(uoAsByDistance, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UasOperatingAreasApi#uoaByDistanceUsV1UoaDistanceQueryPost");
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
| **uoAsByDistance** | [**UOAsByDistance**](UOAsByDistance.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**UOAsDistanceResponse**](UOAsDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each UOA. |  -  |
| **422** | Validation Error |  -  |

<a id="uoaByPolyUsV1UoaPolygonQueryPost"></a>
# **uoaByPolyUsV1UoaPolygonQueryPost**
> UOAsPolyResponse uoaByPolyUsV1UoaPolygonQueryPost(uoAsByPolygon, xApiKey)

Retrieve UAS Operating Areas (UOAs) found within given area.

Retrieve UAS Operating Areas (UOAs) found within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UasOperatingAreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    UasOperatingAreasApi apiInstance = new UasOperatingAreasApi(defaultClient);
    UOAsByPolygon uoAsByPolygon = new UOAsByPolygon(); // UOAsByPolygon | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      UOAsPolyResponse result = apiInstance.uoaByPolyUsV1UoaPolygonQueryPost(uoAsByPolygon, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UasOperatingAreasApi#uoaByPolyUsV1UoaPolygonQueryPost");
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
| **uoAsByPolygon** | [**UOAsByPolygon**](UOAsByPolygon.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**UOAsPolyResponse**](UOAsPolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each UOA. |  -  |
| **422** | Validation Error |  -  |

<a id="uoaByRouteUsV1UoaRouteQueryPost"></a>
# **uoaByRouteUsV1UoaRouteQueryPost**
> UOAsRouteResponse uoaByRouteUsV1UoaRouteQueryPost(uoAsByRoute, xApiKey)

Retrieve UAS Operating Areas (UOAs) found along route.

Retrieve UAS Operating Areas (UOAs) found along your route. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UasOperatingAreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    UasOperatingAreasApi apiInstance = new UasOperatingAreasApi(defaultClient);
    UOAsByRoute uoAsByRoute = new UOAsByRoute(); // UOAsByRoute | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      UOAsRouteResponse result = apiInstance.uoaByRouteUsV1UoaRouteQueryPost(uoAsByRoute, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UasOperatingAreasApi#uoaByRouteUsV1UoaRouteQueryPost");
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
| **uoAsByRoute** | [**UOAsByRoute**](UOAsByRoute.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**UOAsRouteResponse**](UOAsRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each UOA. |  -  |
| **422** | Validation Error |  -  |

