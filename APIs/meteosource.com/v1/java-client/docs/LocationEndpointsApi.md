# LocationEndpointsApi

All URIs are relative to */api/v1/premium*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findPlacesFindPlacesGet**](LocationEndpointsApi.md#findPlacesFindPlacesGet) | **GET** /find_places | Search for places. Complete words required. |
| [**findPlacesPrefixFindPlacesPrefixGet**](LocationEndpointsApi.md#findPlacesPrefixFindPlacesPrefixGet) | **GET** /find_places_prefix | Prefix search for places. Useful for autocomplete forms. |
| [**nearestPlaceNearestPlaceGet**](LocationEndpointsApi.md#nearestPlaceNearestPlaceGet) | **GET** /nearest_place | Returns the nearest named location for a given GPS coordinates. |


<a id="findPlacesFindPlacesGet"></a>
# **findPlacesFindPlacesGet**
> List&lt;FindPlacesModel&gt; findPlacesFindPlacesGet(text, language, key)

Search for places. Complete words required.

## Search for places  You can use this endpoint to obtain &#x60;place_id&#x60; of the location you want, to be used in &#x60;point&#x60; endpoint. The response also contains detailed information about the location, such as coordinates, timezone and the country the place belongs to.  Unlike the &#x60;/find_place_prefix&#x60; endpoint, complete words are required here. You can search for cities, mountains, lakes, countries, ZIP codes, etc. The response can contain multiple places, sorted by relevance. You can then identify the one you want by coordinates, country, or the administrative area.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1/premium");
    
    // Configure API key authorization: APIKeyHeader
    ApiKeyAuth APIKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("APIKeyHeader");
    APIKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKeyHeader.setApiKeyPrefix("Token");

    LocationEndpointsApi apiInstance = new LocationEndpointsApi(defaultClient);
    String text = "text_example"; // String | Place name or ZIP code
    Language language = Language.fromValue("cs"); // Language | The language of text summaries and place names (variable names are never translated). Available languages are:     * ``en``: English    * ``es``: Spanish    * ``fr``: French    * ``de``: German    * ``pl``: Polish    * ``pt``: Portuguese    * ``cs``: Czech 
    String key = "key_example"; // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
    try {
      List<FindPlacesModel> result = apiInstance.findPlacesFindPlacesGet(text, language, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationEndpointsApi#findPlacesFindPlacesGet");
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
| **text** | **String**| Place name or ZIP code | |
| **language** | [**Language**](.md)| The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech  | [optional] [default to en] [enum: cs, en, de, es, fr, pl, pt] |
| **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] |

### Return type

[**List&lt;FindPlacesModel&gt;**](FindPlacesModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Error in passed parameter. |  -  |
| **402** | Maximum requests per day limit exceeded. |  -  |
| **403** | API key not not specified or invalid. |  -  |
| **422** | Validation Error |  -  |
| **429** | Maximum requests per minute limit exceeded. |  -  |

<a id="findPlacesPrefixFindPlacesPrefixGet"></a>
# **findPlacesPrefixFindPlacesPrefixGet**
> List&lt;FindPlacesModel&gt; findPlacesPrefixFindPlacesPrefixGet(text, language, key)

Prefix search for places. Useful for autocomplete forms.

## Search for places by prefix  You can use this endpoint to obtain &#x60;place_id&#x60; of the location you want, to be used in &#x60;point&#x60; endpoint. The response also contains detailed information about the location, such as coordinates, timezone and the country the place belongs to.  Unlike the &#x60;/find_places&#x60; endpoint, you should only specify the prefix of the place you are looking for. This is particularly useful for autocomplete forms. You can search for cities, mountains, lakes, countries, ZIP codes, etc. The response can contain multiple places, sorted by relevance. You can then identify the one you want by coordinates, country, or the administrative area.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1/premium");
    
    // Configure API key authorization: APIKeyHeader
    ApiKeyAuth APIKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("APIKeyHeader");
    APIKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKeyHeader.setApiKeyPrefix("Token");

    LocationEndpointsApi apiInstance = new LocationEndpointsApi(defaultClient);
    String text = "text_example"; // String | Place name or ZIP code
    Language language = Language.fromValue("cs"); // Language | The language of text summaries and place names (variable names are never translated). Available languages are:     * ``en``: English    * ``es``: Spanish    * ``fr``: French    * ``de``: German    * ``pl``: Polish    * ``pt``: Portuguese    * ``cs``: Czech 
    String key = "key_example"; // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
    try {
      List<FindPlacesModel> result = apiInstance.findPlacesPrefixFindPlacesPrefixGet(text, language, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationEndpointsApi#findPlacesPrefixFindPlacesPrefixGet");
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
| **text** | **String**| Place name or ZIP code | |
| **language** | [**Language**](.md)| The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech  | [optional] [default to en] [enum: cs, en, de, es, fr, pl, pt] |
| **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] |

### Return type

[**List&lt;FindPlacesModel&gt;**](FindPlacesModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Error in passed parameter. |  -  |
| **402** | Maximum requests per day limit exceeded. |  -  |
| **403** | API key not not specified or invalid. |  -  |
| **422** | Validation Error |  -  |
| **429** | Maximum requests per minute limit exceeded. |  -  |

<a id="nearestPlaceNearestPlaceGet"></a>
# **nearestPlaceNearestPlaceGet**
> FindPlacesModel nearestPlaceNearestPlaceGet(lat, lon, language, key)

Returns the nearest named location for a given GPS coordinates.

## Search for nearest place by coordinates  You can use this endpoint to find the nearest place from given coordinates.  *Note: If you specify coordinates of a secluded place (e.g. middle of the ocean), the nearest point can be very far from the coordinates.*

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1/premium");
    
    // Configure API key authorization: APIKeyHeader
    ApiKeyAuth APIKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("APIKeyHeader");
    APIKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKeyHeader.setApiKeyPrefix("Token");

    LocationEndpointsApi apiInstance = new LocationEndpointsApi(defaultClient);
    String lat = "lat_example"; // String | Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4
    String lon = "lon_example"; // String | Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4
    Language language = Language.fromValue("cs"); // Language | The language of text summaries and place names (variable names are never translated). Available languages are:     * ``en``: English    * ``es``: Spanish    * ``fr``: French    * ``de``: German    * ``pl``: Polish    * ``pt``: Portuguese    * ``cs``: Czech 
    String key = "key_example"; // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
    try {
      FindPlacesModel result = apiInstance.nearestPlaceNearestPlaceGet(lat, lon, language, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationEndpointsApi#nearestPlaceNearestPlaceGet");
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
| **lat** | **String**| Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4 | |
| **lon** | **String**| Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4 | |
| **language** | [**Language**](.md)| The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech  | [optional] [default to en] [enum: cs, en, de, es, fr, pl, pt] |
| **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] |

### Return type

[**FindPlacesModel**](FindPlacesModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Error in passed parameter. |  -  |
| **402** | Maximum requests per day limit exceeded. |  -  |
| **403** | API key not not specified or invalid. |  -  |
| **422** | Validation Error |  -  |
| **429** | Maximum requests per minute limit exceeded. |  -  |

