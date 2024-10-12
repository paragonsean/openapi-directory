# DisruptionsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disruptionsGetAllDisruptions**](DisruptionsApi.md#disruptionsGetAllDisruptions) | **GET** /v3/disruptions | View all disruptions for all route types |
| [**disruptionsGetDisruptionById**](DisruptionsApi.md#disruptionsGetDisruptionById) | **GET** /v3/disruptions/{disruption_id} | View a specific disruption |
| [**disruptionsGetDisruptionModes**](DisruptionsApi.md#disruptionsGetDisruptionModes) | **GET** /v3/disruptions/modes | Get all disruption modes |
| [**disruptionsGetDisruptionsByRoute**](DisruptionsApi.md#disruptionsGetDisruptionsByRoute) | **GET** /v3/disruptions/route/{route_id} | View all disruptions for a particular route |
| [**disruptionsGetDisruptionsByRouteAndStop**](DisruptionsApi.md#disruptionsGetDisruptionsByRouteAndStop) | **GET** /v3/disruptions/route/{route_id}/stop/{stop_id} | View all disruptions for a particular route and stop |
| [**disruptionsGetDisruptionsByStop**](DisruptionsApi.md#disruptionsGetDisruptionsByStop) | **GET** /v3/disruptions/stop/{stop_id} | View all disruptions for a particular stop |


<a id="disruptionsGetAllDisruptions"></a>
# **disruptionsGetAllDisruptions**
> V3DisruptionsResponse disruptionsGetAllDisruptions(routeTypes, disruptionModes, disruptionStatus, token, devid, signature)

View all disruptions for all route types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisruptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    DisruptionsApi apiInstance = new DisruptionsApi(defaultClient);
    List<Integer> routeTypes = Arrays.asList(); // List<Integer> | Filter by route_type; values returned via RouteTypes API
    List<Integer> disruptionModes = Arrays.asList(); // List<Integer> | Filter by disruption_mode; values returned via v3/disruptions/modes API
    String disruptionStatus = "current"; // String | Filter by status of disruption
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3DisruptionsResponse result = apiInstance.disruptionsGetAllDisruptions(routeTypes, disruptionModes, disruptionStatus, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisruptionsApi#disruptionsGetAllDisruptions");
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
| **disruptionModes** | [**List&lt;Integer&gt;**](Integer.md)| Filter by disruption_mode; values returned via v3/disruptions/modes API | [optional] [enum: 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 100] |
| **disruptionStatus** | **String**| Filter by status of disruption | [optional] [enum: current, planned] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3DisruptionsResponse**](V3DisruptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All disruption information for all route types. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="disruptionsGetDisruptionById"></a>
# **disruptionsGetDisruptionById**
> V3DisruptionResponse disruptionsGetDisruptionById(disruptionId, token, devid, signature)

View a specific disruption

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisruptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    DisruptionsApi apiInstance = new DisruptionsApi(defaultClient);
    Long disruptionId = 56L; // Long | Identifier of disruption; values returned by Disruptions API - /v3/disruptions OR /v3/disruptions/route/{route_id}
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3DisruptionResponse result = apiInstance.disruptionsGetDisruptionById(disruptionId, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisruptionsApi#disruptionsGetDisruptionById");
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
| **disruptionId** | **Long**| Identifier of disruption; values returned by Disruptions API - /v3/disruptions OR /v3/disruptions/route/{route_id} | |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3DisruptionResponse**](V3DisruptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disruption information for the specified disruption ID. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="disruptionsGetDisruptionModes"></a>
# **disruptionsGetDisruptionModes**
> V3DisruptionModesResponse disruptionsGetDisruptionModes(token, devid, signature)

Get all disruption modes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisruptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    DisruptionsApi apiInstance = new DisruptionsApi(defaultClient);
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3DisruptionModesResponse result = apiInstance.disruptionsGetDisruptionModes(token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisruptionsApi#disruptionsGetDisruptionModes");
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
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3DisruptionModesResponse**](V3DisruptionModesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disruption specific modes |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="disruptionsGetDisruptionsByRoute"></a>
# **disruptionsGetDisruptionsByRoute**
> V3DisruptionsResponse disruptionsGetDisruptionsByRoute(routeId, disruptionStatus, token, devid, signature)

View all disruptions for a particular route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisruptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    DisruptionsApi apiInstance = new DisruptionsApi(defaultClient);
    Integer routeId = 56; // Integer | Identifier of route; values returned by Routes API - v3/routes
    String disruptionStatus = "current"; // String | Filter by status of disruption
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3DisruptionsResponse result = apiInstance.disruptionsGetDisruptionsByRoute(routeId, disruptionStatus, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisruptionsApi#disruptionsGetDisruptionsByRoute");
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
| **routeId** | **Integer**| Identifier of route; values returned by Routes API - v3/routes | |
| **disruptionStatus** | **String**| Filter by status of disruption | [optional] [enum: current, planned] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3DisruptionsResponse**](V3DisruptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All disruption information (if any exists) for the specified route. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="disruptionsGetDisruptionsByRouteAndStop"></a>
# **disruptionsGetDisruptionsByRouteAndStop**
> V3DisruptionsResponse disruptionsGetDisruptionsByRouteAndStop(routeId, stopId, disruptionStatus, token, devid, signature)

View all disruptions for a particular route and stop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisruptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    DisruptionsApi apiInstance = new DisruptionsApi(defaultClient);
    Integer routeId = 56; // Integer | Identifier of route; values returned by Routes API - v3/routes
    Integer stopId = 56; // Integer | Identifier of stop; values returned by Stops API - v3/stops
    String disruptionStatus = "current"; // String | Filter by status of disruption
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3DisruptionsResponse result = apiInstance.disruptionsGetDisruptionsByRouteAndStop(routeId, stopId, disruptionStatus, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisruptionsApi#disruptionsGetDisruptionsByRouteAndStop");
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
| **routeId** | **Integer**| Identifier of route; values returned by Routes API - v3/routes | |
| **stopId** | **Integer**| Identifier of stop; values returned by Stops API - v3/stops | |
| **disruptionStatus** | **String**| Filter by status of disruption | [optional] [enum: current, planned] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3DisruptionsResponse**](V3DisruptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All disruption information (if any exists) for the specified route and stop. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="disruptionsGetDisruptionsByStop"></a>
# **disruptionsGetDisruptionsByStop**
> V3DisruptionsResponse disruptionsGetDisruptionsByStop(stopId, disruptionStatus, token, devid, signature)

View all disruptions for a particular stop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisruptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    DisruptionsApi apiInstance = new DisruptionsApi(defaultClient);
    Integer stopId = 56; // Integer | Identifier of stop; values returned by Stops API - v3/stops
    String disruptionStatus = "current"; // String | Filter by status of disruption
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3DisruptionsResponse result = apiInstance.disruptionsGetDisruptionsByStop(stopId, disruptionStatus, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisruptionsApi#disruptionsGetDisruptionsByStop");
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
| **stopId** | **Integer**| Identifier of stop; values returned by Stops API - v3/stops | |
| **disruptionStatus** | **String**| Filter by status of disruption | [optional] [enum: current, planned] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3DisruptionsResponse**](V3DisruptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All disruption information (if any exists) for the specified stop. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

