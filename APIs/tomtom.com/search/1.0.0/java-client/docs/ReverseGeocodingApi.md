# ReverseGeocodingApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchVersionNumberReverseGeocodeCrossStreetPositionExtGet**](ReverseGeocodingApi.md#searchVersionNumberReverseGeocodeCrossStreetPositionExtGet) | **GET** /search/{versionNumber}/reverseGeocode/crossStreet/{position}.{ext} | Cross Street lookup |
| [**searchVersionNumberReverseGeocodePositionExtGet**](ReverseGeocodingApi.md#searchVersionNumberReverseGeocodePositionExtGet) | **GET** /search/{versionNumber}/reverseGeocode/{position}.{ext} | Reverse Geocode |


<a id="searchVersionNumberReverseGeocodeCrossStreetPositionExtGet"></a>
# **searchVersionNumberReverseGeocodeCrossStreetPositionExtGet**
> searchVersionNumberReverseGeocodeCrossStreetPositionExtGet(versionNumber, position, ext, limit, spatialKeys, heading, radius, language)

Cross Street lookup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReverseGeocodingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ReverseGeocodingApi apiInstance = new ReverseGeocodingApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
    String ext = "json"; // String | Expected response format.
    Integer limit = 1; // Integer | Maximum number of cross-streets to return.
    Boolean spatialKeys = false; // Boolean | If the \"spatialKeys\" flag is set, the response will also contain a proprietary geospatial keys for a specified location.
    Float heading = 3.4F; // Float | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    Integer radius = 10000; // Integer | The maximum distance in meters from the specified position for the reverse geocoder to consider.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    try {
      apiInstance.searchVersionNumberReverseGeocodeCrossStreetPositionExtGet(versionNumber, position, ext, limit, spatialKeys, heading, radius, language);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReverseGeocodingApi#searchVersionNumberReverseGeocodeCrossStreetPositionExtGet");
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
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **limit** | **Integer**| Maximum number of cross-streets to return. | [optional] [default to 1] |
| **spatialKeys** | **Boolean**| If the \&quot;spatialKeys\&quot; flag is set, the response will also contain a proprietary geospatial keys for a specified location. | [optional] [default to false] |
| **heading** | **Float**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | [optional] |
| **radius** | **Integer**| The maximum distance in meters from the specified position for the reverse geocoder to consider. | [optional] [default to 10000] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |

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

<a id="searchVersionNumberReverseGeocodePositionExtGet"></a>
# **searchVersionNumberReverseGeocodePositionExtGet**
> searchVersionNumberReverseGeocodePositionExtGet(versionNumber, position, ext, spatialKeys, returnSpeedLimit, heading, radius, number, returnRoadUse, roadUse, paramCallback)

Reverse Geocode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReverseGeocodingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ReverseGeocodingApi apiInstance = new ReverseGeocodingApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
    String ext = "json"; // String | Expected response format.
    Boolean spatialKeys = false; // Boolean | If the \"spatialKeys\" flag is set, the response will also contain a proprietary geospatial keys for a specified location.
    Boolean returnSpeedLimit = false; // Boolean | To enable return of the posted speed limit (where available).
    Float heading = 3.4F; // Float | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    Integer radius = 10000; // Integer | The maximum distance in meters from the specified position for the reverse geocoder to consider.
    String number = "number_example"; // String | If a number is sent in along with the request, the response may include the side of the street (Left/Right) and an offset position for that number.
    Boolean returnRoadUse = false; // Boolean | Enables return of the road use array for reverse geocodes at street level.
    String roadUse = "roadUse_example"; // String | Restricts reverse geocodes to a certain type of road use. The road use array for reverse geocodes can be one or more of: [\"LimitedAccess\", \"Arterial\", \"Terminal\", \"Ramp\", \"Rotary\", \"LocalStreet\"].
    String paramCallback = "cb"; // String | Specifies the jsonp callback method.
    try {
      apiInstance.searchVersionNumberReverseGeocodePositionExtGet(versionNumber, position, ext, spatialKeys, returnSpeedLimit, heading, radius, number, returnRoadUse, roadUse, paramCallback);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReverseGeocodingApi#searchVersionNumberReverseGeocodePositionExtGet");
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
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **spatialKeys** | **Boolean**| If the \&quot;spatialKeys\&quot; flag is set, the response will also contain a proprietary geospatial keys for a specified location. | [optional] [default to false] |
| **returnSpeedLimit** | **Boolean**| To enable return of the posted speed limit (where available). | [optional] [default to false] |
| **heading** | **Float**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | [optional] |
| **radius** | **Integer**| The maximum distance in meters from the specified position for the reverse geocoder to consider. | [optional] [default to 10000] |
| **number** | **String**| If a number is sent in along with the request, the response may include the side of the street (Left/Right) and an offset position for that number. | [optional] |
| **returnRoadUse** | **Boolean**| Enables return of the road use array for reverse geocodes at street level. | [optional] [default to false] |
| **roadUse** | **String**| Restricts reverse geocodes to a certain type of road use. The road use array for reverse geocodes can be one or more of: [\&quot;LimitedAccess\&quot;, \&quot;Arterial\&quot;, \&quot;Terminal\&quot;, \&quot;Ramp\&quot;, \&quot;Rotary\&quot;, \&quot;LocalStreet\&quot;]. | [optional] |
| **paramCallback** | **String**| Specifies the jsonp callback method. | [optional] [default to cb] |

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

