# InteractiveDocumentationForYourPremiumPlan.LocationEndpointsApi

All URIs are relative to */api/v1/premium*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findPlacesFindPlacesGet**](LocationEndpointsApi.md#findPlacesFindPlacesGet) | **GET** /find_places | Search for places. Complete words required.
[**findPlacesPrefixFindPlacesPrefixGet**](LocationEndpointsApi.md#findPlacesPrefixFindPlacesPrefixGet) | **GET** /find_places_prefix | Prefix search for places. Useful for autocomplete forms.
[**nearestPlaceNearestPlaceGet**](LocationEndpointsApi.md#nearestPlaceNearestPlaceGet) | **GET** /nearest_place | Returns the nearest named location for a given GPS coordinates.



## findPlacesFindPlacesGet

> [FindPlacesModel] findPlacesFindPlacesGet(text, opts)

Search for places. Complete words required.

## Search for places  You can use this endpoint to obtain &#x60;place_id&#x60; of the location you want, to be used in &#x60;point&#x60; endpoint. The response also contains detailed information about the location, such as coordinates, timezone and the country the place belongs to.  Unlike the &#x60;/find_place_prefix&#x60; endpoint, complete words are required here. You can search for cities, mountains, lakes, countries, ZIP codes, etc. The response can contain multiple places, sorted by relevance. You can then identify the one you want by coordinates, country, or the administrative area.

### Example

```javascript
import InteractiveDocumentationForYourPremiumPlan from 'interactive_documentation_for_your_premium_plan';
let defaultClient = InteractiveDocumentationForYourPremiumPlan.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
let APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new InteractiveDocumentationForYourPremiumPlan.LocationEndpointsApi();
let text = "text_example"; // String | Place name or ZIP code
let opts = {
  'language': new InteractiveDocumentationForYourPremiumPlan.Language(), // Language | The language of text summaries and place names (variable names are never translated). Available languages are:     * ``en``: English    * ``es``: Spanish    * ``fr``: French    * ``de``: German    * ``pl``: Polish    * ``pt``: Portuguese    * ``cs``: Czech 
  'key': "key_example" // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
};
apiInstance.findPlacesFindPlacesGet(text, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **String**| Place name or ZIP code | 
 **language** | [**Language**](.md)| The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech  | [optional] 
 **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] 

### Return type

[**[FindPlacesModel]**](FindPlacesModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findPlacesPrefixFindPlacesPrefixGet

> [FindPlacesModel] findPlacesPrefixFindPlacesPrefixGet(text, opts)

Prefix search for places. Useful for autocomplete forms.

## Search for places by prefix  You can use this endpoint to obtain &#x60;place_id&#x60; of the location you want, to be used in &#x60;point&#x60; endpoint. The response also contains detailed information about the location, such as coordinates, timezone and the country the place belongs to.  Unlike the &#x60;/find_places&#x60; endpoint, you should only specify the prefix of the place you are looking for. This is particularly useful for autocomplete forms. You can search for cities, mountains, lakes, countries, ZIP codes, etc. The response can contain multiple places, sorted by relevance. You can then identify the one you want by coordinates, country, or the administrative area.

### Example

```javascript
import InteractiveDocumentationForYourPremiumPlan from 'interactive_documentation_for_your_premium_plan';
let defaultClient = InteractiveDocumentationForYourPremiumPlan.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
let APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new InteractiveDocumentationForYourPremiumPlan.LocationEndpointsApi();
let text = "text_example"; // String | Place name or ZIP code
let opts = {
  'language': new InteractiveDocumentationForYourPremiumPlan.Language(), // Language | The language of text summaries and place names (variable names are never translated). Available languages are:     * ``en``: English    * ``es``: Spanish    * ``fr``: French    * ``de``: German    * ``pl``: Polish    * ``pt``: Portuguese    * ``cs``: Czech 
  'key': "key_example" // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
};
apiInstance.findPlacesPrefixFindPlacesPrefixGet(text, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **String**| Place name or ZIP code | 
 **language** | [**Language**](.md)| The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech  | [optional] 
 **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] 

### Return type

[**[FindPlacesModel]**](FindPlacesModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nearestPlaceNearestPlaceGet

> FindPlacesModel nearestPlaceNearestPlaceGet(lat, lon, opts)

Returns the nearest named location for a given GPS coordinates.

## Search for nearest place by coordinates  You can use this endpoint to find the nearest place from given coordinates.  *Note: If you specify coordinates of a secluded place (e.g. middle of the ocean), the nearest point can be very far from the coordinates.*

### Example

```javascript
import InteractiveDocumentationForYourPremiumPlan from 'interactive_documentation_for_your_premium_plan';
let defaultClient = InteractiveDocumentationForYourPremiumPlan.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
let APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new InteractiveDocumentationForYourPremiumPlan.LocationEndpointsApi();
let lat = "lat_example"; // String | Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4
let lon = "lon_example"; // String | Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4
let opts = {
  'language': new InteractiveDocumentationForYourPremiumPlan.Language(), // Language | The language of text summaries and place names (variable names are never translated). Available languages are:     * ``en``: English    * ``es``: Spanish    * ``fr``: French    * ``de``: German    * ``pl``: Polish    * ``pt``: Portuguese    * ``cs``: Czech 
  'key': "key_example" // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
};
apiInstance.nearestPlaceNearestPlaceGet(lat, lon, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **String**| Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4 | 
 **lon** | **String**| Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4 | 
 **language** | [**Language**](.md)| The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech  | [optional] 
 **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] 

### Return type

[**FindPlacesModel**](FindPlacesModel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

