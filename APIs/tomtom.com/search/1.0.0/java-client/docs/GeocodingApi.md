# GeocodingApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchVersionNumberGeocodeQueryExtGet**](GeocodingApi.md#searchVersionNumberGeocodeQueryExtGet) | **GET** /search/{versionNumber}/geocode/{query}.{ext} | Geocode |
| [**searchVersionNumberStructuredGeocodeExtGet**](GeocodingApi.md#searchVersionNumberStructuredGeocodeExtGet) | **GET** /search/{versionNumber}/structuredGeocode.{ext} | Structured Geocode |


<a id="searchVersionNumberGeocodeQueryExtGet"></a>
# **searchVersionNumberGeocodeQueryExtGet**
> searchVersionNumberGeocodeQueryExtGet(versionNumber, query, ext, storeResult, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, extendedPostalCodesFor, view)

Geocode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeocodingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GeocodingApi apiInstance = new GeocodingApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String query = "4 north 2nd street san jose"; // String | Query string. Must be properly URL encoded.
    String ext = "json"; // String | Expected response format.
    Boolean storeResult = false; // Boolean | If the \"storeResult\" flag is set, the query will be interpreted as a stored geocode and will be billed according to the terms of use.
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
      apiInstance.searchVersionNumberGeocodeQueryExtGet(versionNumber, query, ext, storeResult, typeahead, limit, ofs, countrySet, lat, lon, radius, topLeft, btmRight, language, extendedPostalCodesFor, view);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeocodingApi#searchVersionNumberGeocodeQueryExtGet");
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
| **storeResult** | **Boolean**| If the \&quot;storeResult\&quot; flag is set, the query will be interpreted as a stored geocode and will be billed according to the terms of use. | [optional] [default to false] |
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

<a id="searchVersionNumberStructuredGeocodeExtGet"></a>
# **searchVersionNumberStructuredGeocodeExtGet**
> searchVersionNumberStructuredGeocodeExtGet(versionNumber, ext, countryCode, limit, ofs, streetNumber, streetName, crossStreet, municipality, municipalitySubdivision, countryTertiarySubdivision, countrySecondarySubdivision, countrySubdivision, postalCode, language, extendedPostalCodesFor)

Structured Geocode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeocodingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GeocodingApi apiInstance = new GeocodingApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String ext = "json"; // String | Expected response format.
    String countryCode = "NL"; // String | 2 or 3 letter country code (e.g.: FR, ES).
    Integer limit = 10; // Integer | Maximum number of search results that will be returned.
    Integer ofs = 0; // Integer | Starting offset of the returned results within the full result set.
    String streetNumber = "streetNumber_example"; // String | The street number for the structured address.
    String streetName = "streetName_example"; // String | The street name for the structured address.
    String crossStreet = "crossStreet_example"; // String | The cross street name for the structured address.
    String municipality = "Amsterdam"; // String | The municipality (city/town) for the structured address.
    String municipalitySubdivision = "municipalitySubdivision_example"; // String | The municipality subdivision (sub/super city) for the structured address.
    String countryTertiarySubdivision = "countryTertiarySubdivision_example"; // String | The named area for the structured address.
    String countrySecondarySubdivision = "countrySecondarySubdivision_example"; // String | The county for the structured address.
    String countrySubdivision = "countrySubdivision_example"; // String | The state or province for the structured address.
    String postalCode = "postalCode_example"; // String | The zip code or postal code for the structured address.
    String language = "language_example"; // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
    String extendedPostalCodesFor = "extendedPostalCodesFor_example"; // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
    try {
      apiInstance.searchVersionNumberStructuredGeocodeExtGet(versionNumber, ext, countryCode, limit, ofs, streetNumber, streetName, crossStreet, municipality, municipalitySubdivision, countryTertiarySubdivision, countrySecondarySubdivision, countrySubdivision, postalCode, language, extendedPostalCodesFor);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeocodingApi#searchVersionNumberStructuredGeocodeExtGet");
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
| **countryCode** | **String**| 2 or 3 letter country code (e.g.: FR, ES). | |
| **limit** | **Integer**| Maximum number of search results that will be returned. | [optional] [default to 10] |
| **ofs** | **Integer**| Starting offset of the returned results within the full result set. | [optional] [default to 0] |
| **streetNumber** | **String**| The street number for the structured address. | [optional] |
| **streetName** | **String**| The street name for the structured address. | [optional] |
| **crossStreet** | **String**| The cross street name for the structured address. | [optional] |
| **municipality** | **String**| The municipality (city/town) for the structured address. | [optional] |
| **municipalitySubdivision** | **String**| The municipality subdivision (sub/super city) for the structured address. | [optional] |
| **countryTertiarySubdivision** | **String**| The named area for the structured address. | [optional] |
| **countrySecondarySubdivision** | **String**| The county for the structured address. | [optional] |
| **countrySubdivision** | **String**| The state or province for the structured address. | [optional] |
| **postalCode** | **String**| The zip code or postal code for the structured address. | [optional] |
| **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] |
| **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] |

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

