# TransportForLondonUnifiedApi.PlaceApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**placeGet**](PlaceApi.md#placeGet) | **GET** /Place/{id} | Gets the place with the given id.
[**placeGetAt**](PlaceApi.md#placeGetAt) | **GET** /Place/{type}/At/{Lat}/{Lon} | Gets any places of the given type whose geography intersects the given latitude and longitude. In practice this means the Place              must be polygonal e.g. a BoroughBoundary.
[**placeGetByGeo**](PlaceApi.md#placeGetByGeo) | **GET** /Place | Gets the places that lie within a geographic region. The geographic region of interest can either be specified              by using a lat/lon geo-point and a radius in metres to return places within the locus defined by the lat/lon of              its centre or alternatively, by the use of a bounding box defined by the lat/lon of its north-west and south-east corners.              Optionally filters on type and can strip properties for a smaller payload.
[**placeGetByType**](PlaceApi.md#placeGetByType) | **GET** /Place/Type/{types} | Gets all places of a given type
[**placeGetOverlay**](PlaceApi.md#placeGetOverlay) | **GET** /Place/{type}/overlay/{z}/{Lat}/{Lon}/{width}/{height} | Gets the place overlay for a given set of co-ordinates and a given width/height.
[**placeGetStreetsByPostCode**](PlaceApi.md#placeGetStreetsByPostCode) | **GET** /Place/Address/Streets/{Postcode} | Gets the set of streets associated with a post code.
[**placeMetaCategories**](PlaceApi.md#placeMetaCategories) | **GET** /Place/Meta/Categories | Gets a list of all of the available place property categories and keys.
[**placeMetaPlaceTypes**](PlaceApi.md#placeMetaPlaceTypes) | **GET** /Place/Meta/PlaceTypes | Gets a list of the available types of Place.
[**placeSearch**](PlaceApi.md#placeSearch) | **GET** /Place/Search | Gets all places that matches the given query



## placeGet

> [TflApiPresentationEntitiesPlace] placeGet(id, opts)

Gets the place with the given id.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.PlaceApi();
let id = "id_example"; // String | The id of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their ids
let opts = {
  'includeChildren': true // Boolean | Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned
};
apiInstance.placeGet(id, opts, (error, data, response) => {
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
 **id** | **String**| The id of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their ids | 
 **includeChildren** | **Boolean**| Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned | [optional] 

### Return type

[**[TflApiPresentationEntitiesPlace]**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## placeGetAt

> Object placeGetAt(type, lat, lon, locationLat, locationLon, lat2, lon2)

Gets any places of the given type whose geography intersects the given latitude and longitude. In practice this means the Place              must be polygonal e.g. a BoroughBoundary.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.PlaceApi();
let type = ["null"]; // [String] | The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint)
let lat = "lat_example"; // String | 
let lon = "lon_example"; // String | 
let locationLat = 3.4; // Number | 
let locationLon = 3.4; // Number | 
let lat2 = "lat_example"; // String | Automatically added
let lon2 = "lon_example"; // String | Automatically added
apiInstance.placeGetAt(type, lat, lon, locationLat, locationLon, lat2, lon2, (error, data, response) => {
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
 **type** | [**[String]**](String.md)| The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint) | 
 **lat** | **String**|  | 
 **lon** | **String**|  | 
 **locationLat** | **Number**|  | 
 **locationLon** | **Number**|  | 
 **lat2** | **String**| Automatically added | 
 **lon2** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## placeGetByGeo

> [TflApiPresentationEntitiesStopPoint] placeGetByGeo(opts)

Gets the places that lie within a geographic region. The geographic region of interest can either be specified              by using a lat/lon geo-point and a radius in metres to return places within the locus defined by the lat/lon of              its centre or alternatively, by the use of a bounding box defined by the lat/lon of its north-west and south-east corners.              Optionally filters on type and can strip properties for a smaller payload.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.PlaceApi();
let opts = {
  'radius': 3.4, // Number | The radius of the bounding circle in metres when only lat/lon are specified.
  'categories': ["null"], // [String] | An optional list of comma separated property categories to return in the Place's property bag. If null or empty, all categories of property are returned. Pass the keyword \"none\" to return no properties (a valid list of categories can be obtained from the /Place/Meta/categories endpoint)
  'includeChildren': true, // Boolean | Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned
  'type': ["null"], // [String] | Place types to filter on, or null to return all types
  'activeOnly': true, // Boolean | An optional parameter to limit the results to active records only (Currently only the 'VariableMessageSign' place type is supported)
  'numberOfPlacesToReturn': 56, // Number | If specified, limits the number of returned places equal to the given value
  'placeGeoSwLat': 3.4, // Number | 
  'placeGeoSwLon': 3.4, // Number | 
  'placeGeoNeLat': 3.4, // Number | 
  'placeGeoNeLon': 3.4, // Number | 
  'placeGeoLat': 3.4, // Number | 
  'placeGeoLon': 3.4 // Number | 
};
apiInstance.placeGetByGeo(opts, (error, data, response) => {
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
 **radius** | **Number**| The radius of the bounding circle in metres when only lat/lon are specified. | [optional] 
 **categories** | [**[String]**](String.md)| An optional list of comma separated property categories to return in the Place&#39;s property bag. If null or empty, all categories of property are returned. Pass the keyword \&quot;none\&quot; to return no properties (a valid list of categories can be obtained from the /Place/Meta/categories endpoint) | [optional] 
 **includeChildren** | **Boolean**| Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned | [optional] 
 **type** | [**[String]**](String.md)| Place types to filter on, or null to return all types | [optional] 
 **activeOnly** | **Boolean**| An optional parameter to limit the results to active records only (Currently only the &#39;VariableMessageSign&#39; place type is supported) | [optional] 
 **numberOfPlacesToReturn** | **Number**| If specified, limits the number of returned places equal to the given value | [optional] 
 **placeGeoSwLat** | **Number**|  | [optional] 
 **placeGeoSwLon** | **Number**|  | [optional] 
 **placeGeoNeLat** | **Number**|  | [optional] 
 **placeGeoNeLon** | **Number**|  | [optional] 
 **placeGeoLat** | **Number**|  | [optional] 
 **placeGeoLon** | **Number**|  | [optional] 

### Return type

[**[TflApiPresentationEntitiesStopPoint]**](TflApiPresentationEntitiesStopPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## placeGetByType

> [TflApiPresentationEntitiesPlace] placeGetByType(types, opts)

Gets all places of a given type

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.PlaceApi();
let types = ["null"]; // [String] | A comma-separated list of the types to return. Max. approx 12 types.              A valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint.
let opts = {
  'activeOnly': true // Boolean | An optional parameter to limit the results to active records only (Currently only the 'VariableMessageSign' place type is supported)
};
apiInstance.placeGetByType(types, opts, (error, data, response) => {
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
 **types** | [**[String]**](String.md)| A comma-separated list of the types to return. Max. approx 12 types.              A valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint. | 
 **activeOnly** | **Boolean**| An optional parameter to limit the results to active records only (Currently only the &#39;VariableMessageSign&#39; place type is supported) | [optional] 

### Return type

[**[TflApiPresentationEntitiesPlace]**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## placeGetOverlay

> Object placeGetOverlay(z, type, width, height, lat, lon, locationLat, locationLon, lat2, lon2)

Gets the place overlay for a given set of co-ordinates and a given width/height.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.PlaceApi();
let z = 56; // Number | The zoom level
let type = ["null"]; // [String] | The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint)
let width = 56; // Number | The width of the requested overlay.
let height = 56; // Number | The height of the requested overlay.
let lat = "lat_example"; // String | 
let lon = "lon_example"; // String | 
let locationLat = 3.4; // Number | 
let locationLon = 3.4; // Number | 
let lat2 = "lat_example"; // String | Automatically added
let lon2 = "lon_example"; // String | Automatically added
apiInstance.placeGetOverlay(z, type, width, height, lat, lon, locationLat, locationLon, lat2, lon2, (error, data, response) => {
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
 **z** | **Number**| The zoom level | 
 **type** | [**[String]**](String.md)| The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint) | 
 **width** | **Number**| The width of the requested overlay. | 
 **height** | **Number**| The height of the requested overlay. | 
 **lat** | **String**|  | 
 **lon** | **String**|  | 
 **locationLat** | **Number**|  | 
 **locationLon** | **Number**|  | 
 **lat2** | **String**| Automatically added | 
 **lon2** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## placeGetStreetsByPostCode

> Object placeGetStreetsByPostCode(postcode, postcode2, opts)

Gets the set of streets associated with a post code.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.PlaceApi();
let postcode = "postcode_example"; // String | 
let postcode2 = "postcode_example"; // String | Automatically added
let opts = {
  'postcodeInputPostcode': "postcodeInputPostcode_example" // String | 
};
apiInstance.placeGetStreetsByPostCode(postcode, postcode2, opts, (error, data, response) => {
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
 **postcode** | **String**|  | 
 **postcode2** | **String**| Automatically added | 
 **postcodeInputPostcode** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## placeMetaCategories

> [TflApiPresentationEntitiesPlaceCategory] placeMetaCategories()

Gets a list of all of the available place property categories and keys.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.PlaceApi();
apiInstance.placeMetaCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TflApiPresentationEntitiesPlaceCategory]**](TflApiPresentationEntitiesPlaceCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## placeMetaPlaceTypes

> [TflApiPresentationEntitiesPlaceCategory] placeMetaPlaceTypes()

Gets a list of the available types of Place.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.PlaceApi();
apiInstance.placeMetaPlaceTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TflApiPresentationEntitiesPlaceCategory]**](TflApiPresentationEntitiesPlaceCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## placeSearch

> [TflApiPresentationEntitiesPlace] placeSearch(name, opts)

Gets all places that matches the given query

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.PlaceApi();
let name = "name_example"; // String | The name of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their names.
let opts = {
  'types': ["null"] // [String] | A comma-separated list of the types to return. Max. approx 12 types.
};
apiInstance.placeSearch(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their names. | 
 **types** | [**[String]**](String.md)| A comma-separated list of the types to return. Max. approx 12 types. | [optional] 

### Return type

[**[TflApiPresentationEntitiesPlace]**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

