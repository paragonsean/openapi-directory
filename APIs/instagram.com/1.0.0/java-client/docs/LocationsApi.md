# LocationsApi

All URIs are relative to *https://api.instagram.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationsLocationIdGet**](LocationsApi.md#locationsLocationIdGet) | **GET** /locations/{location-id} | Get information about a location. |
| [**locationsLocationIdMediaRecentGet**](LocationsApi.md#locationsLocationIdMediaRecentGet) | **GET** /locations/{location-id}/media/recent | Get a list of recent media objects from a given location. |
| [**locationsSearchGet**](LocationsApi.md#locationsSearchGet) | **GET** /locations/search | Search for a location by geographic coordinate. |


<a id="locationsLocationIdGet"></a>
# **locationsLocationIdGet**
> LocationInfoResponse locationsLocationIdGet(locationId)

Get information about a location.

Get information about a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String locationId = "locationId_example"; // String | The location ID.
    try {
      LocationInfoResponse result = apiInstance.locationsLocationIdGet(locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsLocationIdGet");
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
| **locationId** | **String**| The location ID. | |

### Return type

[**LocationInfoResponse**](LocationInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Location information response. |  -  |

<a id="locationsLocationIdMediaRecentGet"></a>
# **locationsLocationIdMediaRecentGet**
> MediaListResponse locationsLocationIdMediaRecentGet(locationId, minTimestamp, maxTimestamp, minId, maxId)

Get a list of recent media objects from a given location.

Get a list of recent media objects from a given location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String locationId = "locationId_example"; // String | The location ID.
    Long minTimestamp = 56L; // Long | Return media after this UNIX timestamp.
    Long maxTimestamp = 56L; // Long | Return media before this UNIX timestamp.
    String minId = "minId_example"; // String | Return media before this `min_id`.
    String maxId = "maxId_example"; // String | Return media after this `max_id`.
    try {
      MediaListResponse result = apiInstance.locationsLocationIdMediaRecentGet(locationId, minTimestamp, maxTimestamp, minId, maxId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsLocationIdMediaRecentGet");
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
| **locationId** | **String**| The location ID. | |
| **minTimestamp** | **Long**| Return media after this UNIX timestamp. | [optional] |
| **maxTimestamp** | **Long**| Return media before this UNIX timestamp. | [optional] |
| **minId** | **String**| Return media before this &#x60;min_id&#x60;. | [optional] |
| **maxId** | **String**| Return media after this &#x60;max_id&#x60;. | [optional] |

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of media entries from this location. |  -  |

<a id="locationsSearchGet"></a>
# **locationsSearchGet**
> LocationSearchResponse locationsSearchGet(distance, facebookPlacesId, foursquareId, lat, lng, foursquareV2Id)

Search for a location by geographic coordinate.

Search for a location by geographic coordinate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    Integer distance = 56; // Integer | Default is 1000m (distance=1000), max distance is 5000.
    String facebookPlacesId = "facebookPlacesId_example"; // String | Returns a location mapped off of a Facebook places id. If used, a Foursquare id and `lat`, `lng` are not required.
    String foursquareId = "foursquareId_example"; // String | Returns a location mapped off of a foursquare v1 api location id. If used, you are not required to use `lat` and `lng`. Note that this method is deprecated; you should use the new foursquare IDs with V2 of their API. 
    Double lat = 3.4D; // Double | Latitude of the center search coordinate. If used, `lng` is required.
    Double lng = 3.4D; // Double | Longitude of the center search coordinate. If used, `lat` is required.
    String foursquareV2Id = "foursquareV2Id_example"; // String | Returns a location mapped off of a foursquare v2 api location id. If used, you are not required to use `lat` and `lng`. 
    try {
      LocationSearchResponse result = apiInstance.locationsSearchGet(distance, facebookPlacesId, foursquareId, lat, lng, foursquareV2Id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsSearchGet");
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
| **distance** | **Integer**| Default is 1000m (distance&#x3D;1000), max distance is 5000. | [optional] |
| **facebookPlacesId** | **String**| Returns a location mapped off of a Facebook places id. If used, a Foursquare id and &#x60;lat&#x60;, &#x60;lng&#x60; are not required. | [optional] |
| **foursquareId** | **String**| Returns a location mapped off of a foursquare v1 api location id. If used, you are not required to use &#x60;lat&#x60; and &#x60;lng&#x60;. Note that this method is deprecated; you should use the new foursquare IDs with V2 of their API.  | [optional] |
| **lat** | **Double**| Latitude of the center search coordinate. If used, &#x60;lng&#x60; is required. | [optional] |
| **lng** | **Double**| Longitude of the center search coordinate. If used, &#x60;lat&#x60; is required. | [optional] |
| **foursquareV2Id** | **String**| Returns a location mapped off of a foursquare v2 api location id. If used, you are not required to use &#x60;lat&#x60; and &#x60;lng&#x60;.  | [optional] |

### Return type

[**LocationSearchResponse**](LocationSearchResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of found locations. |  -  |

