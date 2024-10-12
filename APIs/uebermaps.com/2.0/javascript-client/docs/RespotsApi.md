# UebermapsApiEndpoints.RespotsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapsIdRespotsGet**](RespotsApi.md#mapsIdRespotsGet) | **GET** /maps/{id}/respots | List respots of a map
[**mapsMapIdSpotsSpotIdRespotDelete**](RespotsApi.md#mapsMapIdSpotsSpotIdRespotDelete) | **DELETE** /maps/{map_id}/spots/{spot_id}/respot | Delete respot from map by spot id
[**respotMapsGet**](RespotsApi.md#respotMapsGet) | **GET** /respot_maps | List maps that user can respot to
[**respotsIdDelete**](RespotsApi.md#respotsIdDelete) | **DELETE** /respots/{id} | Delete respot
[**respotsIdGet**](RespotsApi.md#respotsIdGet) | **GET** /respots/{id} | Get respot
[**spotsIdRespotsPost**](RespotsApi.md#spotsIdRespotsPost) | **POST** /spots/{id}/respots | Respot a spot onto a map



## mapsIdRespotsGet

> [Respot] mapsIdRespotsGet(id)

List respots of a map

List respots of a map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.RespotsApi();
let id = 56; // Number | Map Id
apiInstance.mapsIdRespotsGet(id, (error, data, response) => {
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
 **id** | **Number**| Map Id | 

### Return type

[**[Respot]**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsMapIdSpotsSpotIdRespotDelete

> Respot mapsMapIdSpotsSpotIdRespotDelete(mapId, spotId)

Delete respot from map by spot id

Delete respot from map by spot id.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.RespotsApi();
let mapId = 56; // Number | Map Id
let spotId = 56; // Number | Spot Id
apiInstance.mapsMapIdSpotsSpotIdRespotDelete(mapId, spotId, (error, data, response) => {
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
 **mapId** | **Number**| Map Id | 
 **spotId** | **Number**| Spot Id | 

### Return type

[**Respot**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## respotMapsGet

> [Map] respotMapsGet()

List maps that user can respot to

List maps that user can respot to.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.RespotsApi();
apiInstance.respotMapsGet((error, data, response) => {
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

[**[Map]**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## respotsIdDelete

> Respot respotsIdDelete(id)

Delete respot

Delete respot.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.RespotsApi();
let id = 56; // Number | Respot Id
apiInstance.respotsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| Respot Id | 

### Return type

[**Respot**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## respotsIdGet

> Respot respotsIdGet(id)

Get respot

Get basic information about a respot

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.RespotsApi();
let id = 56; // Number | Id of respot
apiInstance.respotsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of respot | 

### Return type

[**Respot**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spotsIdRespotsPost

> Respot spotsIdRespotsPost(id, mapId)

Respot a spot onto a map

Respot a spot onto a map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.RespotsApi();
let id = 56; // Number | Spot Id
let mapId = 3.4; // Number | Map Id
apiInstance.spotsIdRespotsPost(id, mapId, (error, data, response) => {
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
 **id** | **Number**| Spot Id | 
 **mapId** | **Number**| Map Id | 

### Return type

[**Respot**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

