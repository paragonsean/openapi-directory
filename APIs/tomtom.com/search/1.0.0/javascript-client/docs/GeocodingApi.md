# Search.GeocodingApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchVersionNumberGeocodeQueryExtGet**](GeocodingApi.md#searchVersionNumberGeocodeQueryExtGet) | **GET** /search/{versionNumber}/geocode/{query}.{ext} | Geocode
[**searchVersionNumberStructuredGeocodeExtGet**](GeocodingApi.md#searchVersionNumberStructuredGeocodeExtGet) | **GET** /search/{versionNumber}/structuredGeocode.{ext} | Structured Geocode



## searchVersionNumberGeocodeQueryExtGet

> searchVersionNumberGeocodeQueryExtGet(versionNumber, query, ext, opts)

Geocode

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.GeocodingApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let query = "4 north 2nd street san jose"; // String | Query string. Must be properly URL encoded.
let ext = "xml"; // String | Expected response format.
let opts = {
  'storeResult': false, // Boolean | If the \"storeResult\" flag is set, the query will be interpreted as a stored geocode and will be billed according to the terms of use.
  'typeahead': false, // Boolean | If the \"typeahead\" flag is set, the query will be interpreted as a partial input and the search will enter <b>predictive</b> mode.
  'limit': 10, // Number | Maximum number of search results that will be returned.
  'ofs': 0, // Number | Starting offset of the returned results within the full result set.
  'countrySet': "FR", // String | Comma separated string of country codes. This will limit the search to the specified countries.
  'lat': 37.337, // Number | Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
  'lon': -121.89, // Number | Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
  'radius': 56, // Number | If radius <b>and</b> position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
  'topLeft': "37.553,-122.453", // String | Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
  'btmRight': "37.4,-122.55", // String | Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
  'language': "language_example", // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
  'extendedPostalCodesFor': "extendedPostalCodesFor_example", // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
  'view': "'Unified'" // String | Geopolitical View.
};
apiInstance.searchVersionNumberGeocodeQueryExtGet(versionNumber, query, ext, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 2. | 
 **query** | **String**| Query string. Must be properly URL encoded. | 
 **ext** | **String**| Expected response format. | 
 **storeResult** | **Boolean**| If the \&quot;storeResult\&quot; flag is set, the query will be interpreted as a stored geocode and will be billed according to the terms of use. | [optional] [default to false]
 **typeahead** | **Boolean**| If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode. | [optional] [default to false]
 **limit** | **Number**| Maximum number of search results that will be returned. | [optional] [default to 10]
 **ofs** | **Number**| Starting offset of the returned results within the full result set. | [optional] [default to 0]
 **countrySet** | **String**| Comma separated string of country codes. This will limit the search to the specified countries. | [optional] 
 **lat** | **Number**| Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] 
 **lon** | **Number**| Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point. | [optional] 
 **radius** | **Number**| If radius &lt;b&gt;and&lt;/b&gt; position are set, the results will be constrained to the defined area. The radius parameter is specified in meters. | [optional] 
 **topLeft** | **String**| Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] 
 **btmRight** | **String**| Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] 
 **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] 
 **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **view** | **String**| Geopolitical View. | [optional] [default to &#39;Unified&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchVersionNumberStructuredGeocodeExtGet

> searchVersionNumberStructuredGeocodeExtGet(versionNumber, ext, countryCode, opts)

Structured Geocode

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.GeocodingApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let ext = "xml"; // String | Expected response format.
let countryCode = "NL"; // String | 2 or 3 letter country code (e.g.: FR, ES).
let opts = {
  'limit': 10, // Number | Maximum number of search results that will be returned.
  'ofs': 0, // Number | Starting offset of the returned results within the full result set.
  'streetNumber': "streetNumber_example", // String | The street number for the structured address.
  'streetName': "streetName_example", // String | The street name for the structured address.
  'crossStreet': "crossStreet_example", // String | The cross street name for the structured address.
  'municipality': "Amsterdam", // String | The municipality (city/town) for the structured address.
  'municipalitySubdivision': "municipalitySubdivision_example", // String | The municipality subdivision (sub/super city) for the structured address.
  'countryTertiarySubdivision': "countryTertiarySubdivision_example", // String | The named area for the structured address.
  'countrySecondarySubdivision': "countrySecondarySubdivision_example", // String | The county for the structured address.
  'countrySubdivision': "countrySubdivision_example", // String | The state or province for the structured address.
  'postalCode': "postalCode_example", // String | The zip code or postal code for the structured address.
  'language': "language_example", // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
  'extendedPostalCodesFor': "extendedPostalCodesFor_example" // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
};
apiInstance.searchVersionNumberStructuredGeocodeExtGet(versionNumber, ext, countryCode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 2. | 
 **ext** | **String**| Expected response format. | 
 **countryCode** | **String**| 2 or 3 letter country code (e.g.: FR, ES). | 
 **limit** | **Number**| Maximum number of search results that will be returned. | [optional] [default to 10]
 **ofs** | **Number**| Starting offset of the returned results within the full result set. | [optional] [default to 0]
 **streetNumber** | **String**| The street number for the structured address. | [optional] 
 **streetName** | **String**| The street name for the structured address. | [optional] 
 **crossStreet** | **String**| The cross street name for the structured address. | [optional] 
 **municipality** | **String**| The municipality (city/town) for the structured address. | [optional] 
 **municipalitySubdivision** | **String**| The municipality subdivision (sub/super city) for the structured address. | [optional] 
 **countryTertiarySubdivision** | **String**| The named area for the structured address. | [optional] 
 **countrySecondarySubdivision** | **String**| The county for the structured address. | [optional] 
 **countrySubdivision** | **String**| The state or province for the structured address. | [optional] 
 **postalCode** | **String**| The zip code or postal code for the structured address. | [optional] 
 **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] 
 **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

