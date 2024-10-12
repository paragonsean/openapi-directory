# FiltersApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchVersionNumberGeometryFilterExtGet**](FiltersApi.md#searchVersionNumberGeometryFilterExtGet) | **GET** /search/{versionNumber}/geometryFilter.{ext} | Geometry Filter |
| [**searchVersionNumberGeometryFilterExtPost**](FiltersApi.md#searchVersionNumberGeometryFilterExtPost) | **POST** /search/{versionNumber}/geometryFilter.{ext} | Geometry Filter |
| [**searchVersionNumberRoutedFilterPositionHeadingExtGet**](FiltersApi.md#searchVersionNumberRoutedFilterPositionHeadingExtGet) | **GET** /search/{versionNumber}/routedFilter/{position}/{heading}.{ext} | Routed Filter |
| [**searchVersionNumberRoutedFilterPositionHeadingExtPost**](FiltersApi.md#searchVersionNumberRoutedFilterPositionHeadingExtPost) | **POST** /search/{versionNumber}/routedFilter/{position}/{heading}.{ext} | Routed Filter |


<a id="searchVersionNumberGeometryFilterExtGet"></a>
# **searchVersionNumberGeometryFilterExtGet**
> searchVersionNumberGeometryFilterExtGet(versionNumber, ext, geometryList, poiList)

Geometry Filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String ext = "json"; // String | Expected response format.
    String geometryList = "[{\"type\":\"CIRCLE\", \"position\":\"40.80558, -73.96548\", \"radius\":100}, {\"type\":\"POLYGON\", \"vertices\":[\"37.7524152343544, -122.43576049804686\", \"37.70660472542312, -122.43301391601562\", \"37.712059855877314, -122.36434936523438\", \"37.75350561243041, -122.37396240234374\"]}]"; // String | List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON.
    String poiList = "[{\"poi\":{\"name\":\"S Restaurant Toms\"},\"address\":{\"freeformAddress\":\"2880 Broadway, New York, NY 10025\"},\"position\":{\"lat\":40.80558,\"lon\":-73.96548}},{\"poi\":{\"name\":\"Yasha Raman Corporation\"},\"address\":{\"freeformAddress\":\"940 Amsterdam Ave, New York, NY 10025\"},\"position\":{\"lat\":40.80076,\"lon\":-73.96556}}]"; // String | List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in.
    try {
      apiInstance.searchVersionNumberGeometryFilterExtGet(versionNumber, ext, geometryList, poiList);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#searchVersionNumberGeometryFilterExtGet");
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
| **versionNumber** | **Integer**| Service version number. The current value is 2. | [enum: 2] |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **geometryList** | **String**| List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON. | |
| **poiList** | **String**| List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK: the search successfully returned zero or more results. |  -  |
| **400** | Bad Request: one or more parameters were incorrectly specified. |  -  |
| **403** | Forbidden: possible causes include:   - Service requires SSL   - Not authorized   - Rate or volume limit exceeded   - Unknown referer |  -  |
| **405** | Method Not Allowed: the HTTP method (GET, POST, etc) is not supported for this request. |  -  |
| **596** | Not Found: the HTTP request method (GET, POST, etc) or path is incorrect. |  -  |
| **5XX** | An error occurred while processing the request. Please try again later. |  -  |

<a id="searchVersionNumberGeometryFilterExtPost"></a>
# **searchVersionNumberGeometryFilterExtPost**
> searchVersionNumberGeometryFilterExtPost(versionNumber, ext, searchVersionNumberGeometryFilterExtPostRequest)

Geometry Filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String ext = "json"; // String | Expected response format.
    SearchVersionNumberGeometryFilterExtPostRequest searchVersionNumberGeometryFilterExtPostRequest = new SearchVersionNumberGeometryFilterExtPostRequest(); // SearchVersionNumberGeometryFilterExtPostRequest | 
    try {
      apiInstance.searchVersionNumberGeometryFilterExtPost(versionNumber, ext, searchVersionNumberGeometryFilterExtPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#searchVersionNumberGeometryFilterExtPost");
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
| **versionNumber** | **Integer**| Service version number. The current value is 2. | [enum: 2] |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **searchVersionNumberGeometryFilterExtPostRequest** | [**SearchVersionNumberGeometryFilterExtPostRequest**](SearchVersionNumberGeometryFilterExtPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK: the search successfully returned zero or more results. |  -  |
| **400** | Bad Request: one or more parameters were incorrectly specified. |  -  |
| **403** | Forbidden: possible causes include:   - Service requires SSL   - Not authorized   - Rate or volume limit exceeded   - Unknown referer |  -  |
| **405** | Method Not Allowed: the HTTP method (GET, POST, etc) is not supported for this request. |  -  |
| **596** | Not Found: the HTTP request method (GET, POST, etc) or path is incorrect. |  -  |
| **5XX** | An error occurred while processing the request. Please try again later. |  -  |

<a id="searchVersionNumberRoutedFilterPositionHeadingExtGet"></a>
# **searchVersionNumberRoutedFilterPositionHeadingExtGet**
> searchVersionNumberRoutedFilterPositionHeadingExtGet(versionNumber, position, heading, ext, poiList, routingTimeout)

Routed Filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
    Float heading = -15.6F; // Float | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    String ext = "json"; // String | Expected response format.
    String poiList = "[{\"poi\":{\"name\":\"Cleaire Advanced Emission Controls\"},\"address\":{\"freeformAddress\":\"7220 Trade St, San Diego, CA 92121\"},\"position\":{\"lat\":\"37.83274\",\"lon\":\"-122.27631\"}}]"; // String | List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in.
    Integer routingTimeout = 4000; // Integer | Only return results that arrive from routing engine within this time limit.
    try {
      apiInstance.searchVersionNumberRoutedFilterPositionHeadingExtGet(versionNumber, position, heading, ext, poiList, routingTimeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#searchVersionNumberRoutedFilterPositionHeadingExtGet");
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
| **versionNumber** | **Integer**| Service version number. The current value is 2. | [enum: 2] |
| **position** | **String**| This is specified as a comma separated string composed of lat., lon. | |
| **heading** | **Float**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **poiList** | **String**| List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in. | |
| **routingTimeout** | **Integer**| Only return results that arrive from routing engine within this time limit. | [optional] [default to 4000] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK: the search successfully returned zero or more results. |  -  |
| **400** | Bad Request: one or more parameters were incorrectly specified. |  -  |
| **403** | Forbidden: possible causes include:   - Service requires SSL   - Not authorized   - Rate or volume limit exceeded   - Unknown referer |  -  |
| **405** | Method Not Allowed: the HTTP method (GET, POST, etc) is not supported for this request. |  -  |
| **596** | Not Found: the HTTP request method (GET, POST, etc) or path is incorrect. |  -  |
| **5XX** | An error occurred while processing the request. Please try again later. |  -  |

<a id="searchVersionNumberRoutedFilterPositionHeadingExtPost"></a>
# **searchVersionNumberRoutedFilterPositionHeadingExtPost**
> searchVersionNumberRoutedFilterPositionHeadingExtPost(versionNumber, position, heading, ext, routingTimeout, searchVersionNumberRoutedFilterPositionHeadingExtPostRequest)

Routed Filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
    Float heading = 90F; // Float | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    String ext = "json"; // String | Expected response format.
    Integer routingTimeout = 4000; // Integer | Only return results that arrive from routing engine within this time limit.
    SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest searchVersionNumberRoutedFilterPositionHeadingExtPostRequest = new SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest(); // SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest | 
    try {
      apiInstance.searchVersionNumberRoutedFilterPositionHeadingExtPost(versionNumber, position, heading, ext, routingTimeout, searchVersionNumberRoutedFilterPositionHeadingExtPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#searchVersionNumberRoutedFilterPositionHeadingExtPost");
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
| **versionNumber** | **Integer**| Service version number. The current value is 2. | [enum: 2] |
| **position** | **String**| This is specified as a comma separated string composed of lat., lon. | |
| **heading** | **Float**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **routingTimeout** | **Integer**| Only return results that arrive from routing engine within this time limit. | [optional] [default to 4000] |
| **searchVersionNumberRoutedFilterPositionHeadingExtPostRequest** | [**SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest**](SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK: the search successfully returned zero or more results. |  -  |
| **400** | Bad Request: one or more parameters were incorrectly specified. |  -  |
| **403** | Forbidden: possible causes include:   - Service requires SSL   - Not authorized   - Rate or volume limit exceeded   - Unknown referer |  -  |
| **405** | Method Not Allowed: the HTTP method (GET, POST, etc) is not supported for this request. |  -  |
| **596** | Not Found: the HTTP request method (GET, POST, etc) or path is incorrect. |  -  |
| **5XX** | An error occurred while processing the request. Please try again later. |  -  |

