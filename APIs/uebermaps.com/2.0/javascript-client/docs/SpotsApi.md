# UebermapsApiEndpoints.SpotsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapsIdSpotsGet**](SpotsApi.md#mapsIdSpotsGet) | **GET** /maps/{id}/spots | List spots for a given map
[**mapsIdSpotsPost**](SpotsApi.md#mapsIdSpotsPost) | **POST** /maps/{id}/spots | Create spot
[**mapsMapIdSpotsIdGet**](SpotsApi.md#mapsMapIdSpotsIdGet) | **GET** /maps/{map_id}/spots/{id} | Get spot
[**spotsGet**](SpotsApi.md#spotsGet) | **GET** /spots | List your own spots
[**spotsIdDelete**](SpotsApi.md#spotsIdDelete) | **DELETE** /spots/{id} | Delete spot
[**spotsIdPatch**](SpotsApi.md#spotsIdPatch) | **PATCH** /spots/{id} | Update spot



## mapsIdSpotsGet

> [Spot] mapsIdSpotsGet(id, opts)

List spots for a given map

List spots for a given map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SpotsApi();
let id = 56; // Number | Id of map
let opts = {
  'order': "order_example" // String | Order of spots
};
apiInstance.mapsIdSpotsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Id of map | 
 **order** | **String**| Order of spots | [optional] 

### Return type

[**[Spot]**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsIdSpotsPost

> Spot mapsIdSpotsPost(id, spot)

Create spot

Create spot. Wrap parameters in [spot]. To add a spot picture pass a base64 encoded string to [spot][picture].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SpotsApi();
let id = 56; // Number | Id of map
let spot = new UebermapsApiEndpoints.SpotEditable(); // SpotEditable | spot attributes
apiInstance.mapsIdSpotsPost(id, spot, (error, data, response) => {
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
 **id** | **Number**| Id of map | 
 **spot** | [**SpotEditable**](SpotEditable.md)| spot attributes | 

### Return type

[**Spot**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mapsMapIdSpotsIdGet

> Spot mapsMapIdSpotsIdGet(id, mapId)

Get spot

Get basic information about a spot

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SpotsApi();
let id = 56; // Number | Id of spot
let mapId = 56; // Number | Id of map
apiInstance.mapsMapIdSpotsIdGet(id, mapId, (error, data, response) => {
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
 **id** | **Number**| Id of spot | 
 **mapId** | **Number**| Id of map | 

### Return type

[**Spot**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spotsGet

> [Spot] spotsGet(opts)

List your own spots

List your own spots.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SpotsApi();
let opts = {
  'order': "order_example" // String | Order of spots
};
apiInstance.spotsGet(opts, (error, data, response) => {
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
 **order** | **String**| Order of spots | [optional] 

### Return type

[**[Spot]**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spotsIdDelete

> Spot spotsIdDelete(id)

Delete spot

Delete spot.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SpotsApi();
let id = 56; // Number | spot id
apiInstance.spotsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| spot id | 

### Return type

[**Spot**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spotsIdPatch

> Spot spotsIdPatch(id, opts)

Update spot

Update spot. Wrap parameters in [spot]. To update the spot picture pass a base64 encoded string to [spot][picture].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SpotsApi();
let id = 56; // Number | spot id
let opts = {
  'spot': new UebermapsApiEndpoints.SpotEditable() // SpotEditable | spot attributes
};
apiInstance.spotsIdPatch(id, opts, (error, data, response) => {
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
 **id** | **Number**| spot id | 
 **spot** | [**SpotEditable**](SpotEditable.md)| spot attributes | [optional] 

### Return type

[**Spot**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

