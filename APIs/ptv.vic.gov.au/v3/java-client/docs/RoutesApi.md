# RoutesApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**routesOneOrMoreRoutes**](RoutesApi.md#routesOneOrMoreRoutes) | **GET** /v3/routes | View route names and numbers for all routes |
| [**routesRouteFromId**](RoutesApi.md#routesRouteFromId) | **GET** /v3/routes/{route_id} | View route name and number for specific route ID |


<a id="routesOneOrMoreRoutes"></a>
# **routesOneOrMoreRoutes**
> V3RouteResponse routesOneOrMoreRoutes(routeTypes, routeName, token, devid, signature)

View route names and numbers for all routes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    RoutesApi apiInstance = new RoutesApi(defaultClient);
    List<Integer> routeTypes = Arrays.asList(); // List<Integer> | Filter by route_type; values returned via RouteTypes API
    String routeName = "routeName_example"; // String | Filter by name  of route (accepts partial route name matches)
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3RouteResponse result = apiInstance.routesOneOrMoreRoutes(routeTypes, routeName, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutesApi#routesOneOrMoreRoutes");
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
| **routeTypes** | [**List&lt;Integer&gt;**](Integer.md)| Filter by route_type; values returned via RouteTypes API | [optional] [enum: 0, 1, 2, 3, 4] |
| **routeName** | **String**| Filter by name  of route (accepts partial route name matches) | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3RouteResponse**](V3RouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Route names and numbers for all routes of all route types. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="routesRouteFromId"></a>
# **routesRouteFromId**
> V3RouteResponse routesRouteFromId(routeId, includeGeopath, geopathUtc, token, devid, signature)

View route name and number for specific route ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    RoutesApi apiInstance = new RoutesApi(defaultClient);
    Integer routeId = 56; // Integer | Identifier of route; values returned by Departures, Directions and Disruptions APIs
    Boolean includeGeopath = true; // Boolean | Indicates kif geopath data will be returned (default = false)
    OffsetDateTime geopathUtc = OffsetDateTime.now(); // OffsetDateTime | Filter geopaths by date (ISO 8601 UTC format) (default = current date)
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3RouteResponse result = apiInstance.routesRouteFromId(routeId, includeGeopath, geopathUtc, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutesApi#routesRouteFromId");
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
| **routeId** | **Integer**| Identifier of route; values returned by Departures, Directions and Disruptions APIs | |
| **includeGeopath** | **Boolean**| Indicates kif geopath data will be returned (default &#x3D; false) | [optional] |
| **geopathUtc** | **OffsetDateTime**| Filter geopaths by date (ISO 8601 UTC format) (default &#x3D; current date) | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3RouteResponse**](V3RouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The route name and number for the specified route ID. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

