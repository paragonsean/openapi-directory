# LotaData.PlacesApi

All URIs are relative to *https://api2.lotadata.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**placesGet**](PlacesApi.md#placesGet) | **GET** /places | Venues, landmarks, regions, these are all places to search.
[**placesIdGet**](PlacesApi.md#placesIdGet) | **GET** /places/{id} | Get specific place details



## placesGet

> PlacesSearchResponse placesGet(fieldset, opts)

Venues, landmarks, regions, these are all places to search.

### Example

```javascript
import LotaData from 'lota_data';
let defaultClient = LotaData.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new LotaData.PlacesApi();
let fieldset = "'context'"; // String | Return results starting at specified offset (summary, context, detail)
let opts = {
  'category': ["null"], // [String] | List of required PlaceCategory ids (Tier 1)
  '_function': ["null"], // [String] | List of required PlaceFunction ids (Tier 2)
  'ambience': ["null"], // [String] | List of required ambience ids
  'tag': ["null"], // [String] | List of required tags
  'type': "type_example", // String | Specific PlaceType to return
  'name': "name_example", // String | Match on place names
  'exact': true, // Boolean | Require an exact name match
  'capacityMin': 3.4, // Number | Min capacity at location
  'capacityMax': 3.4, // Number | Min capacity at location
  'street': "street_example", // String | Address of the place or street component of the address
  'locality': "locality_example", // String | city, town, or neighborhood of the place
  'region': "region_example", // String | region or state
  'postalCode': "postalCode_example", // String | Postal or zip code
  'country': "country_example", // String | country component of the address
  'center': "center_example", // String | latitude,longitude of the origin point
  'radius': 56, // Number | Distance from origin in meters
  'bbox': ["null"], // [String] | Corner of a bounding box (lat,lng). Requires 0 or 2 pairs
  'polygon': ["null"], // [String] | Closed custom polygon. Ordered list of lat,lng pairs
  'within': "within_example", // String | Search within specified geopolitical place id
  'offset': 56, // Number | Return results starting at specified offset
  'limit': 56 // Number | Max results to return
};
apiInstance.placesGet(fieldset, opts, (error, data, response) => {
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
 **fieldset** | **String**| Return results starting at specified offset (summary, context, detail) | [default to &#39;context&#39;]
 **category** | [**[String]**](String.md)| List of required PlaceCategory ids (Tier 1) | [optional] 
 **_function** | [**[String]**](String.md)| List of required PlaceFunction ids (Tier 2) | [optional] 
 **ambience** | [**[String]**](String.md)| List of required ambience ids | [optional] 
 **tag** | [**[String]**](String.md)| List of required tags | [optional] 
 **type** | **String**| Specific PlaceType to return | [optional] 
 **name** | **String**| Match on place names | [optional] 
 **exact** | **Boolean**| Require an exact name match | [optional] 
 **capacityMin** | **Number**| Min capacity at location | [optional] 
 **capacityMax** | **Number**| Min capacity at location | [optional] 
 **street** | **String**| Address of the place or street component of the address | [optional] 
 **locality** | **String**| city, town, or neighborhood of the place | [optional] 
 **region** | **String**| region or state | [optional] 
 **postalCode** | **String**| Postal or zip code | [optional] 
 **country** | **String**| country component of the address | [optional] 
 **center** | **String**| latitude,longitude of the origin point | [optional] 
 **radius** | **Number**| Distance from origin in meters | [optional] 
 **bbox** | [**[String]**](String.md)| Corner of a bounding box (lat,lng). Requires 0 or 2 pairs | [optional] 
 **polygon** | [**[String]**](String.md)| Closed custom polygon. Ordered list of lat,lng pairs | [optional] 
 **within** | **String**| Search within specified geopolitical place id | [optional] 
 **offset** | **Number**| Return results starting at specified offset | [optional] 
 **limit** | **Number**| Max results to return | [optional] 

### Return type

[**PlacesSearchResponse**](PlacesSearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placesIdGet

> PlaceDetail placesIdGet(id, opts)

Get specific place details

### Example

```javascript
import LotaData from 'lota_data';
let defaultClient = LotaData.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new LotaData.PlacesApi();
let id = "id_example"; // String | place @id
let opts = {
  'fieldset': "'summary'" // String | 
};
apiInstance.placesIdGet(id, opts, (error, data, response) => {
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
 **id** | **String**| place @id | 
 **fieldset** | **String**|  | [optional] [default to &#39;summary&#39;]

### Return type

[**PlaceDetail**](PlaceDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

