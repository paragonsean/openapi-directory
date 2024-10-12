# Search.SearchApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchVersionNumberCSCategoryExtGet**](SearchApi.md#searchVersionNumberCSCategoryExtGet) | **GET** /search/{versionNumber}/cS/{category}.{ext} | Low Bandwith Category Search
[**searchVersionNumberCategorySearchQueryExtGet**](SearchApi.md#searchVersionNumberCategorySearchQueryExtGet) | **GET** /search/{versionNumber}/categorySearch/{query}.{ext} | Category Search
[**searchVersionNumberGeometrySearchQueryExtGet**](SearchApi.md#searchVersionNumberGeometrySearchQueryExtGet) | **GET** /search/{versionNumber}/geometrySearch/{query}.{ext} | Geometry Search
[**searchVersionNumberGeometrySearchQueryExtPost**](SearchApi.md#searchVersionNumberGeometrySearchQueryExtPost) | **POST** /search/{versionNumber}/geometrySearch/{query}.{ext} | Geometry Search
[**searchVersionNumberNearbySearchExtGet**](SearchApi.md#searchVersionNumberNearbySearchExtGet) | **GET** /search/{versionNumber}/nearbySearch/.{ext} | Nearby Search
[**searchVersionNumberPoiSearchQueryExtGet**](SearchApi.md#searchVersionNumberPoiSearchQueryExtGet) | **GET** /search/{versionNumber}/poiSearch/{query}.{ext} | Points of Interest Search
[**searchVersionNumberRoutedSearchQueryPositionHeadingExtGet**](SearchApi.md#searchVersionNumberRoutedSearchQueryPositionHeadingExtGet) | **GET** /search/{versionNumber}/routedSearch/{query}/{position}/{heading}.{ext} | Routed Search
[**searchVersionNumberSQueryExtGet**](SearchApi.md#searchVersionNumberSQueryExtGet) | **GET** /search/{versionNumber}/s/{query}.{ext} | Low bandwith Search
[**searchVersionNumberSearchAlongRouteQueryExtPost**](SearchApi.md#searchVersionNumberSearchAlongRouteQueryExtPost) | **POST** /search/{versionNumber}/searchAlongRoute/{query}.{ext} | Along Route Search
[**searchVersionNumberSearchQueryExtGet**](SearchApi.md#searchVersionNumberSearchQueryExtGet) | **GET** /search/{versionNumber}/search/{query}.{ext} | Fuzzy Search



## searchVersionNumberCSCategoryExtGet

> searchVersionNumberCSCategoryExtGet(versionNumber, category, ext, opts)

Low Bandwith Category Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let category = "pizza"; // String | Query string. Must be properly URL encoded.
let ext = "xml"; // String | Expected response format.
let opts = {
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
  'idxSet': "POI", // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
  'view': "'Unified'" // String | Geopolitical View.
};
apiInstance.searchVersionNumberCSCategoryExtGet(versionNumber, category, ext, opts, (error, data, response) => {
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
 **category** | **String**| Query string. Must be properly URL encoded. | 
 **ext** | **String**| Expected response format. | 
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
 **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **view** | **String**| Geopolitical View. | [optional] [default to &#39;Unified&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchVersionNumberCategorySearchQueryExtGet

> searchVersionNumberCategorySearchQueryExtGet(versionNumber, query, ext, opts)

Category Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let query = "pizza"; // String | Query string. Must be properly URL encoded.
let ext = "xml"; // String | Expected response format.
let opts = {
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
apiInstance.searchVersionNumberCategorySearchQueryExtGet(versionNumber, query, ext, opts, (error, data, response) => {
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


## searchVersionNumberGeometrySearchQueryExtGet

> searchVersionNumberGeometrySearchQueryExtGet(versionNumber, query, ext, opts)

Geometry Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let query = "pizza"; // String | Query string. Must be properly URL encoded.
let ext = "xml"; // String | Expected response format.
let opts = {
  'geometryList': "[{\"type\":\"POLYGON\", \"vertices\":[\"37.7524152343544, -122.43576049804686\", \"37.70660472542312, -122.43301391601562\", \"37.712059855877314, -122.36434936523438\", \"37.75350561243041, -122.37396240234374\"]}, {\"type\":\"CIRCLE\", \"position\":\"37.71205, -121.36434\", \"radius\":6000}, {\"type\":\"CIRCLE\", \"position\":\"37.31205, -121.36434\", \"radius\":1000}]", // String | List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON.
  'limit': 10, // Number | Maximum number of search results that will be returned.
  'language': "language_example", // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
  'extendedPostalCodesFor': "extendedPostalCodesFor_example", // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
  'idxSet': "POI" // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
};
apiInstance.searchVersionNumberGeometrySearchQueryExtGet(versionNumber, query, ext, opts, (error, data, response) => {
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
 **geometryList** | **String**| List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON. | [optional] 
 **limit** | **Number**| Maximum number of search results that will be returned. | [optional] [default to 10]
 **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] 
 **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchVersionNumberGeometrySearchQueryExtPost

> searchVersionNumberGeometrySearchQueryExtPost(versionNumber, query, ext, opts)

Geometry Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let query = "pizza"; // String | Query string. Must be properly URL encoded.
let ext = "xml"; // String | Expected response format.
let opts = {
  'limit': 10, // Number | Maximum number of search results that will be returned.
  'language': "language_example", // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
  'extendedPostalCodesFor': "extendedPostalCodesFor_example", // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
  'idxSet': "POI", // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
  'searchVersionNumberGeometrySearchQueryExtPostRequest': new Search.SearchVersionNumberGeometrySearchQueryExtPostRequest() // SearchVersionNumberGeometrySearchQueryExtPostRequest | 
};
apiInstance.searchVersionNumberGeometrySearchQueryExtPost(versionNumber, query, ext, opts, (error, data, response) => {
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
 **limit** | **Number**| Maximum number of search results that will be returned. | [optional] [default to 10]
 **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] 
 **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **searchVersionNumberGeometrySearchQueryExtPostRequest** | [**SearchVersionNumberGeometrySearchQueryExtPostRequest**](SearchVersionNumberGeometrySearchQueryExtPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## searchVersionNumberNearbySearchExtGet

> searchVersionNumberNearbySearchExtGet(versionNumber, ext, lat, lon, opts)

Nearby Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let ext = "xml"; // String | Expected response format.
let lat = 37.337; // Number | Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point.
let lon = -121.89; // Number | Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point.
let opts = {
  'limit': 10, // Number | Maximum number of search results that will be returned.
  'ofs': 0, // Number | Starting offset of the returned results within the full result set.
  'countrySet': "FR", // String | Comma separated string of country codes. This will limit the search to the specified countries.
  'radius': 10000, // Number | If radius and position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
  'topLeft': "37.553,-122.453", // String | Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon.
  'btmRight': "37.4,-122.55", // String | Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon.
  'language': "language_example", // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
  'extendedPostalCodesFor': "extendedPostalCodesFor_example", // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
  'minFuzzyLevel': 1, // Number | Minimum fuzziness level to be used.
  'maxFuzzyLevel': 2, // Number | Maximum fuzziness level to be used.
  'idxSet': "POI", // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
  'view': "'Unified'" // String | Geopolitical View.
};
apiInstance.searchVersionNumberNearbySearchExtGet(versionNumber, ext, lat, lon, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude where results should be biased. NOTE: supplying a lat/lon without a radius will return search results biased to that point. | 
 **lon** | **Number**| Longitude where results should be biased NOTE: supplying a lat/lon without a radius will return search results biased to that point. | 
 **limit** | **Number**| Maximum number of search results that will be returned. | [optional] [default to 10]
 **ofs** | **Number**| Starting offset of the returned results within the full result set. | [optional] [default to 0]
 **countrySet** | **String**| Comma separated string of country codes. This will limit the search to the specified countries. | [optional] 
 **radius** | **Number**| If radius and position are set, the results will be constrained to the defined area. The radius parameter is specified in meters. | [optional] [default to 10000]
 **topLeft** | **String**| Top left position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] 
 **btmRight** | **String**| Bottom right position of the bounding box. This is specified as a comma separated string composed of lat., lon. | [optional] 
 **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] 
 **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **minFuzzyLevel** | **Number**| Minimum fuzziness level to be used. | [optional] [default to 1]
 **maxFuzzyLevel** | **Number**| Maximum fuzziness level to be used. | [optional] [default to 2]
 **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **view** | **String**| Geopolitical View. | [optional] [default to &#39;Unified&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchVersionNumberPoiSearchQueryExtGet

> searchVersionNumberPoiSearchQueryExtGet(versionNumber, query, ext, opts)

Points of Interest Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let query = "pizza"; // String | Query string. Must be properly URL encoded.
let ext = "xml"; // String | Expected response format.
let opts = {
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
apiInstance.searchVersionNumberPoiSearchQueryExtGet(versionNumber, query, ext, opts, (error, data, response) => {
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


## searchVersionNumberRoutedSearchQueryPositionHeadingExtGet

> searchVersionNumberRoutedSearchQueryPositionHeadingExtGet(versionNumber, query, position, heading, ext, opts)

Routed Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let query = "gas"; // String | Query string. Must be properly URL encoded.
let position = "37.8328,-122.27669"; // String | This is specified as a comma separated string composed of lat., lon.
let heading = 90; // Number | The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
let ext = "xml"; // String | Expected response format.
let opts = {
  'typeahead': false, // Boolean | If the \"typeahead\" flag is set, the query will be interpreted as a partial input and the search will enter <b>predictive</b> mode.
  'limit': 10, // Number | Maximum number of search results that will be returned.
  'multiplier': 2, // Number | Multiplies the limit by N to gather more candidate POIs, which will then be sorted by drive distance, returning only the top candidates according to the limit.
  'routingTimeout': 4000, // Number | Only return results that arrive from routing engine within this time limit.
  'language': "language_example", // String | Language in which search results should be returned. Should be one of <a href=\"/search-api/search-api-documentation/supported-languages\">supported IETF language tags</a>, case insensitive.
  'extendedPostalCodesFor': "extendedPostalCodesFor_example", // String | Indexes for which extended postal codes should be included in the results. Available indexes are:   - <b>Addr</b> = Address ranges   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of Interest   - <b>Str</b> = Streets   - <b>XStr</b> = Cross Streets (intersections)
  'idxSet': "POI" // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
};
apiInstance.searchVersionNumberRoutedSearchQueryPositionHeadingExtGet(versionNumber, query, position, heading, ext, opts, (error, data, response) => {
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
 **position** | **String**| This is specified as a comma separated string composed of lat., lon. | 
 **heading** | **Number**| The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.) | 
 **ext** | **String**| Expected response format. | 
 **typeahead** | **Boolean**| If the \&quot;typeahead\&quot; flag is set, the query will be interpreted as a partial input and the search will enter &lt;b&gt;predictive&lt;/b&gt; mode. | [optional] [default to false]
 **limit** | **Number**| Maximum number of search results that will be returned. | [optional] [default to 10]
 **multiplier** | **Number**| Multiplies the limit by N to gather more candidate POIs, which will then be sorted by drive distance, returning only the top candidates according to the limit. | [optional] [default to 2]
 **routingTimeout** | **Number**| Only return results that arrive from routing engine within this time limit. | [optional] [default to 4000]
 **language** | **String**| Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive. | [optional] 
 **extendedPostalCodesFor** | **String**| Indexes for which extended postal codes should be included in the results. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address ranges   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of Interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;XStr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchVersionNumberSQueryExtGet

> searchVersionNumberSQueryExtGet(versionNumber, query, ext, opts)

Low bandwith Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let query = "pizza"; // String | Query string. Must be properly URL encoded.
let ext = "xml"; // String | Expected response format.
let opts = {
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
  'idxSet': "POI", // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
  'view': "'Unified'" // String | Geopolitical View.
};
apiInstance.searchVersionNumberSQueryExtGet(versionNumber, query, ext, opts, (error, data, response) => {
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
 **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **view** | **String**| Geopolitical View. | [optional] [default to &#39;Unified&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchVersionNumberSearchAlongRouteQueryExtPost

> searchVersionNumberSearchAlongRouteQueryExtPost(versionNumber, query, ext, maxDetourTime, opts)

Along Route Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let query = "pizza"; // String | Query string. Must be properly URL encoded.
let ext = "xml"; // String | Expected response format.
let maxDetourTime = 1200; // Number | Maximum detour time
let opts = {
  'limit': 10, // Number | Maximum number of search results that will be returned.
  'searchVersionNumberSearchAlongRouteQueryExtPostRequest': new Search.SearchVersionNumberSearchAlongRouteQueryExtPostRequest() // SearchVersionNumberSearchAlongRouteQueryExtPostRequest | 
};
apiInstance.searchVersionNumberSearchAlongRouteQueryExtPost(versionNumber, query, ext, maxDetourTime, opts, (error, data, response) => {
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
 **maxDetourTime** | **Number**| Maximum detour time | 
 **limit** | **Number**| Maximum number of search results that will be returned. | [optional] [default to 10]
 **searchVersionNumberSearchAlongRouteQueryExtPostRequest** | [**SearchVersionNumberSearchAlongRouteQueryExtPostRequest**](SearchVersionNumberSearchAlongRouteQueryExtPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## searchVersionNumberSearchQueryExtGet

> searchVersionNumberSearchQueryExtGet(versionNumber, query, ext, opts)

Fuzzy Search

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.SearchApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let query = "pizza"; // String | Query string. Must be properly URL encoded.  To perform a reverse geocode, the user can provide latitude and longitude coordinates directly in the query. More information can be found <a href=\"/search-api/search-api-documentation-search/fuzzy-search#AdditionalInfo\">here</a>.
let ext = "xml"; // String | Expected response format.
let opts = {
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
  'minFuzzyLevel': 1, // Number | Minimum fuzziness level to be used.
  'maxFuzzyLevel': 2, // Number | Maximum fuzziness level to be used.
  'idxSet': "POI", // String | A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - <b>Addr</b> = Address range interpolation (when there is no PAD)   - <b>Geo</b> = Geographies   - <b>PAD</b> = Point Addresses   - <b>POI</b> = Points of interest   - <b>Str</b> = Streets   - <b>Xstr</b> = Cross Streets (intersections)
  'view': "'Unified'" // String | Geopolitical View.
};
apiInstance.searchVersionNumberSearchQueryExtGet(versionNumber, query, ext, opts, (error, data, response) => {
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
 **query** | **String**| Query string. Must be properly URL encoded.  To perform a reverse geocode, the user can provide latitude and longitude coordinates directly in the query. More information can be found &lt;a href&#x3D;\&quot;/search-api/search-api-documentation-search/fuzzy-search#AdditionalInfo\&quot;&gt;here&lt;/a&gt;. | 
 **ext** | **String**| Expected response format. | 
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
 **minFuzzyLevel** | **Number**| Minimum fuzziness level to be used. | [optional] [default to 1]
 **maxFuzzyLevel** | **Number**| Maximum fuzziness level to be used. | [optional] [default to 2]
 **idxSet** | **String**| A comma separated list of indexes which should be utilized for the search. Item order does not matter. Available indexes are:   - &lt;b&gt;Addr&lt;/b&gt; &#x3D; Address range interpolation (when there is no PAD)   - &lt;b&gt;Geo&lt;/b&gt; &#x3D; Geographies   - &lt;b&gt;PAD&lt;/b&gt; &#x3D; Point Addresses   - &lt;b&gt;POI&lt;/b&gt; &#x3D; Points of interest   - &lt;b&gt;Str&lt;/b&gt; &#x3D; Streets   - &lt;b&gt;Xstr&lt;/b&gt; &#x3D; Cross Streets (intersections) | [optional] 
 **view** | **String**| Geopolitical View. | [optional] [default to &#39;Unified&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

