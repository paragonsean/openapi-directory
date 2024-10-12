# RestrictedPublicVenuesApi

All URIs are relative to *https://dflight-api.ljaero.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**venByDistanceUsV1VenuesDistanceQueryPost**](RestrictedPublicVenuesApi.md#venByDistanceUsV1VenuesDistanceQueryPost) | **POST** /us/v1/venues/distance-query | Retrieve all restricted public venues located within given distance of location. |
| [**venByPolyUsV1VenuesPolygonQueryPost**](RestrictedPublicVenuesApi.md#venByPolyUsV1VenuesPolygonQueryPost) | **POST** /us/v1/venues/polygon-query | Retrieve all restricted public venues located within given GeoJSON Polygon. |
| [**venByRouteUsV1VenuesRouteQueryPost**](RestrictedPublicVenuesApi.md#venByRouteUsV1VenuesRouteQueryPost) | **POST** /us/v1/venues/route-query | Retrieve all restricted public venues traversed by route. |


<a id="venByDistanceUsV1VenuesDistanceQueryPost"></a>
# **venByDistanceUsV1VenuesDistanceQueryPost**
> VenueDistanceResponse venByDistanceUsV1VenuesDistanceQueryPost(venuesByDistance, xApiKey)

Retrieve all restricted public venues located within given distance of location.

Retrieve venues existing within given distance from a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestrictedPublicVenuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    RestrictedPublicVenuesApi apiInstance = new RestrictedPublicVenuesApi(defaultClient);
    VenuesByDistance venuesByDistance = new VenuesByDistance(); // VenuesByDistance | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      VenueDistanceResponse result = apiInstance.venByDistanceUsV1VenuesDistanceQueryPost(venuesByDistance, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestrictedPublicVenuesApi#venByDistanceUsV1VenuesDistanceQueryPost");
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
| **venuesByDistance** | [**VenuesByDistance**](VenuesByDistance.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**VenueDistanceResponse**](VenueDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each venue found. |  -  |
| **422** | Validation Error |  -  |

<a id="venByPolyUsV1VenuesPolygonQueryPost"></a>
# **venByPolyUsV1VenuesPolygonQueryPost**
> VenuePolyResponse venByPolyUsV1VenuesPolygonQueryPost(venuesByPolygon, xApiKey)

Retrieve all restricted public venues located within given GeoJSON Polygon.

Retrieve all restricted public venues located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestrictedPublicVenuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    RestrictedPublicVenuesApi apiInstance = new RestrictedPublicVenuesApi(defaultClient);
    VenuesByPolygon venuesByPolygon = new VenuesByPolygon(); // VenuesByPolygon | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      VenuePolyResponse result = apiInstance.venByPolyUsV1VenuesPolygonQueryPost(venuesByPolygon, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestrictedPublicVenuesApi#venByPolyUsV1VenuesPolygonQueryPost");
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
| **venuesByPolygon** | [**VenuesByPolygon**](VenuesByPolygon.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**VenuePolyResponse**](VenuePolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each venue found. |  -  |
| **422** | Validation Error |  -  |

<a id="venByRouteUsV1VenuesRouteQueryPost"></a>
# **venByRouteUsV1VenuesRouteQueryPost**
> VenueRouteResponse venByRouteUsV1VenuesRouteQueryPost(venuesByRoute, xApiKey)

Retrieve all restricted public venues traversed by route.

Retrieve all restricted public venues intersected by route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestrictedPublicVenuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    RestrictedPublicVenuesApi apiInstance = new RestrictedPublicVenuesApi(defaultClient);
    VenuesByRoute venuesByRoute = new VenuesByRoute(); // VenuesByRoute | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      VenueRouteResponse result = apiInstance.venByRouteUsV1VenuesRouteQueryPost(venuesByRoute, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestrictedPublicVenuesApi#venByRouteUsV1VenuesRouteQueryPost");
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
| **venuesByRoute** | [**VenuesByRoute**](VenuesByRoute.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**VenueRouteResponse**](VenueRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection, one Feature for each venue found. |  -  |
| **422** | Validation Error |  -  |

