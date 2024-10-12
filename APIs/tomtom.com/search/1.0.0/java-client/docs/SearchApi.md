# SearchApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchVersionNumberCSCategoryExtGet**](SearchApi.md#searchVersionNumberCSCategoryExtGet) | **GET** /search/{versionNumber}/cS/{category}.{ext} | Low Bandwith Category Search |
| [**searchVersionNumberCategorySearchQueryExtGet**](SearchApi.md#searchVersionNumberCategorySearchQueryExtGet) | **GET** /search/{versionNumber}/categorySearch/{query}.{ext} | Category Search |
| [**searchVersionNumberGeometrySearchQueryExtGet**](SearchApi.md#searchVersionNumberGeometrySearchQueryExtGet) | **GET** /search/{versionNumber}/geometrySearch/{query}.{ext} | Geometry Search |
| [**searchVersionNumberGeometrySearchQueryExtPost**](SearchApi.md#searchVersionNumberGeometrySearchQueryExtPost) | **POST** /search/{versionNumber}/geometrySearch/{query}.{ext} | Geometry Search |
| [**searchVersionNumberNearbySearchExtGet**](SearchApi.md#searchVersionNumberNearbySearchExtGet) | **GET** /search/{versionNumber}/nearbySearch/.{ext} | Nearby Search |
| [**searchVersionNumberPoiSearchQueryExtGet**](SearchApi.md#searchVersionNumberPoiSearchQueryExtGet) | **GET** /search/{versionNumber}/poiSearch/{query}.{ext} | Points of Interest Search |
| [**searchVersionNumberRoutedSearchQueryPositionHeadingExtGet**](SearchApi.md#searchVersionNumberRoutedSearchQueryPositionHeadingExtGet) | **GET** /search/{versionNumber}/routedSearch/{query}/{position}/{heading}.{ext} | Routed Search |
| [**searchVersionNumberSQueryExtGet**](SearchApi.md#searchVersionNumberSQueryExtGet) | **GET** /search/{versionNumber}/s/{query}.{ext} | Low bandwith Search |
| [**searchVersionNumberSearchAlongRouteQueryExtPost**](SearchApi.md#searchVersionNumberSearchAlongRouteQueryExtPost) | **POST** /search/{versionNumber}/searchAlongRoute/{query}.{ext} | Along Route Search |
| [**searchVersionNumberSearchQueryExtGet**](SearchApi.md#searchVersionNumberSearchQueryExtGet) | **GET** /search/{versionNumber}/search/{query}.{ext} | Fuzzy Search |


<a id="searchVersionNumberCSCategoryExtGet"></a>
# **searchVersionNumberCSCategoryExtGet**
> searchVersionNumberCSCategoryExtGet(versionNumber, category, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, idxSet, view)

Low Bandwith Category Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String category = "pizza"; // String | Query string. Must be properly URL encoded.
    String ext = "json"; // String | Expected response format.
    Boolean typeahead = false; // Boolean | If the \"typeahead\" flag is set, the query will be interpreted as a partial input and the search will enter <b>predictive</b> mode.
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    Integer ofs = 0; // Integer | Starting offset of the returned results within the full result set.
    String countrySet = "FR"; // String | Comma separated string of country codes. This will limit the search to the specified countries.
    Float lat = 37.337F; // Float | Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Float lon = -121.89F; // Float | Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Integer radius = 56; // Integer | If radius <b>and</b> position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
    String topLeft = "37.553,-122.453"; // String | Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String btmRight = "37.4,-122.55"; // String | Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String idxSet = "POI"; // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
    String view = "Unified"; // String | Geopolitical View.
    try {
      apiInstance.searchVersionNumberCSCategoryExtGet(versionNumber, category, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, idxSet, view);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberCSCategoryExtGet");
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
| **category** | **String**| Query string. Must be properly URL encoded. | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **typeahead** | **Boolean**| If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode. | [optional] [default to false] |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **ofs** | **Integer**| Starting offset of the returned results within the full result set. | [optional] [default to 0] |
| **countrySet** | **String**| Comma separated string of country codes. This will limit the search to the specified countries. | [optional] |
| **lat** | **Float**| Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **lon** | **Float**| Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **radius** | **Integer**| If radius &lt;b&gt;and&lt;/b&gt; position are set, the results will be constrained to the defined area. The radius parameter is specified in meters. | [optional] |
| **topLeft** | **String**| Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **btmRight** | **String**| Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **view** | **String**| Geopolitical View. | [optional] [default to Unified] [enum: Unified, IN, PK, IL, MA] |

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

<a id="searchVersionNumberCategorySearchQueryExtGet"></a>
# **searchVersionNumberCategorySearchQueryExtGet**
> searchVersionNumberCategorySearchQueryExtGet(versionNumber, query, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, extendedPostalCodesFor, view)

Category Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String query = "pizza"; // String | Query string. Must be properly URL encoded.
    String ext = "json"; // String | Expected response format.
    Boolean typeahead = false; // Boolean | If the \"typeahead\" flag is set, the query will be interpreted as a partial input and the search will enter <b>predictive</b> mode.
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    Integer ofs = 0; // Integer | Starting offset of the returned results within the full result set.
    String countrySet = "FR"; // String | Comma separated string of country codes. This will limit the search to the specified countries.
    Float lat = 37.337F; // Float | Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Float lon = -121.89F; // Float | Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Integer radius = 56; // Integer | If radius <b>and</b> position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
    String topLeft = "37.553,-122.453"; // String | Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String btmRight = "37.4,-122.55"; // String | Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String extendedPostalCodesFor = "extendedPostalCodesFor_example"; // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
    String view = "Unified"; // String | Geopolitical View.
    try {
      apiInstance.searchVersionNumberCategorySearchQueryExtGet(versionNumber, query, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, extendedPostalCodesFor, view);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberCategorySearchQueryExtGet");
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
| **query** | **String**| Query string. Must be properly URL encoded. | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **typeahead** | **Boolean**| If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode. | [optional] [default to false] |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **ofs** | **Integer**| Starting offset of the returned results within the full result set. | [optional] [default to 0] |
| **countrySet** | **String**| Comma separated string of country codes. This will limit the search to the specified countries. | [optional] |
| **lat** | **Float**| Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **lon** | **Float**| Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **radius** | **Integer**| If radius &lt;b&gt;and&lt;/b&gt; position are set, the results will be constrained to the defined area. The radius parameter is specified in meters. | [optional] |
| **topLeft** | **String**| Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **btmRight** | **String**| Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **view** | **String**| Geopolitical View. | [optional] [default to Unified] [enum: Unified, IN, PK, IL, MA] |

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

<a id="searchVersionNumberGeometrySearchQueryExtGet"></a>
# **searchVersionNumberGeometrySearchQueryExtGet**
> searchVersionNumberGeometrySearchQueryExtGet(versionNumber, query, ext, geometryList, limit, language, extendedPostalCodesFor, idxSet)

Geometry Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String query = "pizza"; // String | Query string. Must be properly URL encoded.
    String ext = "json"; // String | Expected response format.
    String geometryList = "[{\"type\":\"POLYGON\", \"vertices\":[\"37.7524152343544, -122.43576049804686\", \"37.70660472542312, -122.43301391601562\", \"37.712059855877314, -122.36434936523438\", \"37.75350561243041, -122.37396240234374\"]}, {\"type\":\"CIRCLE\", \"position\":\"37.71205, -121.36434\", \"radius\":6000}, {\"type\":\"CIRCLE\", \"position\":\"37.31205, -121.36434\", \"radius\":1000}]"; // String | List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON.
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String extendedPostalCodesFor = "extendedPostalCodesFor_example"; // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
    String idxSet = "POI"; // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
    try {
      apiInstance.searchVersionNumberGeometrySearchQueryExtGet(versionNumber, query, ext, geometryList, limit, language, extendedPostalCodesFor, idxSet);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberGeometrySearchQueryExtGet");
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
| **query** | **String**| Query string. Must be properly URL encoded. | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **geometryList** | **String**| List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON. | [optional] |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |

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

<a id="searchVersionNumberGeometrySearchQueryExtPost"></a>
# **searchVersionNumberGeometrySearchQueryExtPost**
> searchVersionNumberGeometrySearchQueryExtPost(versionNumber, query, ext, limit, language, extendedPostalCodesFor, idxSet, searchVersionNumberGeometrySearchQueryExtPostRequest)

Geometry Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String query = "pizza"; // String | Query string. Must be properly URL encoded.
    String ext = "json"; // String | Expected response format.
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String extendedPostalCodesFor = "extendedPostalCodesFor_example"; // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
    String idxSet = "POI"; // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
    SearchVersionNumberGeometrySearchQueryExtPostRequest searchVersionNumberGeometrySearchQueryExtPostRequest = new SearchVersionNumberGeometrySearchQueryExtPostRequest(); // SearchVersionNumberGeometrySearchQueryExtPostRequest | 
    try {
      apiInstance.searchVersionNumberGeometrySearchQueryExtPost(versionNumber, query, ext, limit, language, extendedPostalCodesFor, idxSet, searchVersionNumberGeometrySearchQueryExtPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberGeometrySearchQueryExtPost");
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
| **query** | **String**| Query string. Must be properly URL encoded. | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **searchVersionNumberGeometrySearchQueryExtPostRequest** | [**SearchVersionNumberGeometrySearchQueryExtPostRequest**](SearchVersionNumberGeometrySearchQueryExtPostRequest.md)|  | [optional] |

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

<a id="searchVersionNumberNearbySearchExtGet"></a>
# **searchVersionNumberNearbySearchExtGet**
> searchVersionNumberNearbySearchExtGet(versionNumber, ext, lat, lon, limit, ofs, countrySet, radius, topLeft, btmRight, language, extendedPostalCodesFor, minFuzzyLevel, maxFuzzyLevel, idxSet, view)

Nearby Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String ext = "json"; // String | Expected response format.
    Float lat = 37.337F; // Float | Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Float lon = -121.89F; // Float | Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    Integer ofs = 0; // Integer | Starting offset of the returned results within the full result set.
    String countrySet = "FR"; // String | Comma separated string of country codes. This will limit the search to the specified countries.
    Integer radius = 10000; // Integer | If radius and position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
    String topLeft = "37.553,-122.453"; // String | Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String btmRight = "37.4,-122.55"; // String | Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String extendedPostalCodesFor = "extendedPostalCodesFor_example"; // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
    Integer minFuzzyLevel = 1; // Integer | Minimum fuzziness level to be used.
    Integer maxFuzzyLevel = 2; // Integer | Maximum fuzziness level to be used.
    String idxSet = "POI"; // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
    String view = "Unified"; // String | Geopolitical View.
    try {
      apiInstance.searchVersionNumberNearbySearchExtGet(versionNumber, ext, lat, lon, limit, ofs, countrySet, radius, topLeft, btmRight, language, extendedPostalCodesFor, minFuzzyLevel, maxFuzzyLevel, idxSet, view);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberNearbySearchExtGet");
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
| **lat** | **Float**| Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point. | |
| **lon** | **Float**| Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point. | |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **ofs** | **Integer**| Starting offset of the returned results within the full result set. | [optional] [default to 0] |
| **countrySet** | **String**| Comma separated string of country codes. This will limit the search to the specified countries. | [optional] |
| **radius** | **Integer**| If radius and position are set, the results will be constrained to the defined area. The radius parameter is specified in meters. | [optional] [default to 10000] |
| **topLeft** | **String**| Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **btmRight** | **String**| Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **minFuzzyLevel** | **Integer**| Minimum fuzziness level to be used. | [optional] [default to 1] |
| **maxFuzzyLevel** | **Integer**| Maximum fuzziness level to be used. | [optional] [default to 2] |
| **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **view** | **String**| Geopolitical View. | [optional] [default to Unified] [enum: Unified, IN, PK, IL, MA] |

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

<a id="searchVersionNumberPoiSearchQueryExtGet"></a>
# **searchVersionNumberPoiSearchQueryExtGet**
> searchVersionNumberPoiSearchQueryExtGet(versionNumber, query, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, extendedPostalCodesFor, view)

Points of Interest Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String query = "pizza"; // String | Query string. Must be properly URL encoded.
    String ext = "json"; // String | Expected response format.
    Boolean typeahead = false; // Boolean | If the \"typeahead\" flag is set, the query will be interpreted as a partial input and the search will enter <b>predictive</b> mode.
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    Integer ofs = 0; // Integer | Starting offset of the returned results within the full result set.
    String countrySet = "FR"; // String | Comma separated string of country codes. This will limit the search to the specified countries.
    Float lat = 37.337F; // Float | Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Float lon = -121.89F; // Float | Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Integer radius = 56; // Integer | If radius <b>and</b> position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
    String topLeft = "37.553,-122.453"; // String | Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String btmRight = "37.4,-122.55"; // String | Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String extendedPostalCodesFor = "extendedPostalCodesFor_example"; // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
    String view = "Unified"; // String | Geopolitical View.
    try {
      apiInstance.searchVersionNumberPoiSearchQueryExtGet(versionNumber, query, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, extendedPostalCodesFor, view);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberPoiSearchQueryExtGet");
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
| **query** | **String**| Query string. Must be properly URL encoded. | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **typeahead** | **Boolean**| If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode. | [optional] [default to false] |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **ofs** | **Integer**| Starting offset of the returned results within the full result set. | [optional] [default to 0] |
| **countrySet** | **String**| Comma separated string of country codes. This will limit the search to the specified countries. | [optional] |
| **lat** | **Float**| Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **lon** | **Float**| Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **radius** | **Integer**| If radius &lt;b&gt;and&lt;/b&gt; position are set, the results will be constrained to the defined area. The radius parameter is specified in meters. | [optional] |
| **topLeft** | **String**| Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **btmRight** | **String**| Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **view** | **String**| Geopolitical View. | [optional] [default to Unified] [enum: Unified, IN, PK, IL, MA] |

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

<a id="searchVersionNumberRoutedSearchQueryPositionHeadingExtGet"></a>
# **searchVersionNumberRoutedSearchQueryPositionHeadingExtGet**
> searchVersionNumberRoutedSearchQueryPositionHeadingExtGet(versionNumber, query, position, heading, ext, typeahead, limit, multiplier, routingTimeout, language, extendedPostalCodesFor, idxSet)

Routed Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String query = "gas"; // String | Query string. Must be properly URL encoded.
    String position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
    Float heading = 90F; // Float | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    String ext = "json"; // String | Expected response format.
    Boolean typeahead = false; // Boolean | If the \"typeahead\" flag is set, the query will be interpreted as a partial input and the search will enter <b>predictive</b> mode.
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    Integer multiplier = 2; // Integer | Multiplies the limit by N to gather more candidate POIs, which will then be sorted by drive distance, returning only the top candidates according to the limit.
    Integer routingTimeout = 4000; // Integer | Only return results that arrive from routing engine within this time limit.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String extendedPostalCodesFor = "extendedPostalCodesFor_example"; // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
    String idxSet = "POI"; // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
    try {
      apiInstance.searchVersionNumberRoutedSearchQueryPositionHeadingExtGet(versionNumber, query, position, heading, ext, typeahead, limit, multiplier, routingTimeout, language, extendedPostalCodesFor, idxSet);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberRoutedSearchQueryPositionHeadingExtGet");
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
| **query** | **String**| Query string. Must be properly URL encoded. | |
| **position** | **String**| This is specified as a comma separated string composed of lat., lon. | |
| **heading** | **Float**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **typeahead** | **Boolean**| If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode. | [optional] [default to false] |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **multiplier** | **Integer**| Multiplies the limit by N to gather more candidate POIs, which will then be sorted by drive distance, returning only the top candidates according to the limit. | [optional] [default to 2] |
| **routingTimeout** | **Integer**| Only return results that arrive from routing engine within this time limit. | [optional] [default to 4000] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |

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

<a id="searchVersionNumberSQueryExtGet"></a>
# **searchVersionNumberSQueryExtGet**
> searchVersionNumberSQueryExtGet(versionNumber, query, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, idxSet, view)

Low bandwith Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String query = "pizza"; // String | Query string. Must be properly URL encoded.
    String ext = "json"; // String | Expected response format.
    Boolean typeahead = false; // Boolean | If the \"typeahead\" flag is set, the query will be interpreted as a partial input and the search will enter <b>predictive</b> mode.
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    Integer ofs = 0; // Integer | Starting offset of the returned results within the full result set.
    String countrySet = "FR"; // String | Comma separated string of country codes. This will limit the search to the specified countries.
    Float lat = 37.337F; // Float | Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Float lon = -121.89F; // Float | Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Integer radius = 56; // Integer | If radius <b>and</b> position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
    String topLeft = "37.553,-122.453"; // String | Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String btmRight = "37.4,-122.55"; // String | Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String idxSet = "POI"; // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
    String view = "Unified"; // String | Geopolitical View.
    try {
      apiInstance.searchVersionNumberSQueryExtGet(versionNumber, query, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, idxSet, view);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberSQueryExtGet");
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
| **query** | **String**| Query string. Must be properly URL encoded. | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **typeahead** | **Boolean**| If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode. | [optional] [default to false] |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **ofs** | **Integer**| Starting offset of the returned results within the full result set. | [optional] [default to 0] |
| **countrySet** | **String**| Comma separated string of country codes. This will limit the search to the specified countries. | [optional] |
| **lat** | **Float**| Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **lon** | **Float**| Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **radius** | **Integer**| If radius &lt;b&gt;and&lt;/b&gt; position are set, the results will be constrained to the defined area. The radius parameter is specified in meters. | [optional] |
| **topLeft** | **String**| Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **btmRight** | **String**| Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **view** | **String**| Geopolitical View. | [optional] [default to Unified] [enum: Unified, IN, PK, IL, MA] |

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

<a id="searchVersionNumberSearchAlongRouteQueryExtPost"></a>
# **searchVersionNumberSearchAlongRouteQueryExtPost**
> searchVersionNumberSearchAlongRouteQueryExtPost(versionNumber, query, ext, maxDetourTime, limit, searchVersionNumberSearchAlongRouteQueryExtPostRequest)

Along Route Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String query = "pizza"; // String | Query string. Must be properly URL encoded.
    String ext = "json"; // String | Expected response format.
    Integer maxDetourTime = 1200; // Integer | Maximum detour time
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    SearchVersionNumberSearchAlongRouteQueryExtPostRequest searchVersionNumberSearchAlongRouteQueryExtPostRequest = new SearchVersionNumberSearchAlongRouteQueryExtPostRequest(); // SearchVersionNumberSearchAlongRouteQueryExtPostRequest | 
    try {
      apiInstance.searchVersionNumberSearchAlongRouteQueryExtPost(versionNumber, query, ext, maxDetourTime, limit, searchVersionNumberSearchAlongRouteQueryExtPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberSearchAlongRouteQueryExtPost");
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
| **query** | **String**| Query string. Must be properly URL encoded. | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **maxDetourTime** | **Integer**| Maximum detour time | |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **searchVersionNumberSearchAlongRouteQueryExtPostRequest** | [**SearchVersionNumberSearchAlongRouteQueryExtPostRequest**](SearchVersionNumberSearchAlongRouteQueryExtPostRequest.md)|  | [optional] |

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

<a id="searchVersionNumberSearchQueryExtGet"></a>
# **searchVersionNumberSearchQueryExtGet**
> searchVersionNumberSearchQueryExtGet(versionNumber, query, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, extendedPostalCodesFor, minFuzzyLevel, maxFuzzyLevel, idxSet, view)

Fuzzy Search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String query = "pizza"; // String | Query string. Must be properly URL encoded.  To perform a reverse geocode, the user can provide latitude and longitude coordinates directly in the query. More information can be found <a href=\"/search-api/search-api-documentation-search/fuzzy-search#AdditionalInfo\">here</a>.
    String ext = "json"; // String | Expected response format.
    Boolean typeahead = false; // Boolean | If the \"typeahead\" flag is set, the query will be interpreted as a partial input and the search will enter <b>predictive</b> mode.
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    Integer ofs = 0; // Integer | Starting offset of the returned results within the full result set.
    String countrySet = "FR"; // String | Comma separated string of country codes. This will limit the search to the specified countries.
    Float lat = 37.337F; // Float | Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Float lon = -121.89F; // Float | Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
    Integer radius = 56; // Integer | If radius <b>and</b> position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
    String topLeft = "37.553,-122.453"; // String | Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String btmRight = "37.4,-122.55"; // String | Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String extendedPostalCodesFor = "extendedPostalCodesFor_example"; // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
    Integer minFuzzyLevel = 1; // Integer | Minimum fuzziness level to be used.
    Integer maxFuzzyLevel = 2; // Integer | Maximum fuzziness level to be used.
    String idxSet = "POI"; // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
    String view = "Unified"; // String | Geopolitical View.
    try {
      apiInstance.searchVersionNumberSearchQueryExtGet(versionNumber, query, ext, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, extendedPostalCodesFor, minFuzzyLevel, maxFuzzyLevel, idxSet, view);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVersionNumberSearchQueryExtGet");
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
| **query** | **String**| Query string. Must be properly URL encoded.  To perform a reverse geocode, the user can provide latitude and longitude coordinates directly in the query. More information can be found &lt;a href&#x3D;\&quot;/search-api/search-api-documentation-search/fuzzy-search#AdditionalInfo\&quot;&gt;here&lt;/a&gt;. | |
| **ext** | **String**| Expected response format. | [enum: json, jsonp, js, xml] |
| **typeahead** | **Boolean**| If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode. | [optional] [default to false] |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **ofs** | **Integer**| Starting offset of the returned results within the full result set. | [optional] [default to 0] |
| **countrySet** | **String**| Comma separated string of country codes. This will limit the search to the specified countries. | [optional] |
| **lat** | **Float**| Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **lon** | **Float**| Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] |
| **radius** | **Integer**| If radius &lt;b&gt;and&lt;/b&gt; position are set, the results will be constrained to the defined area. The radius parameter is specified in meters. | [optional] |
| **topLeft** | **String**| Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **btmRight** | **String**| Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **minFuzzyLevel** | **Integer**| Minimum fuzziness level to be used. | [optional] [default to 1] |
| **maxFuzzyLevel** | **Integer**| Maximum fuzziness level to be used. | [optional] [default to 2] |
| **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |
| **view** | **String**| Geopolitical View. | [optional] [default to Unified] [enum: Unified, IN, PK, IL, MA] |

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

