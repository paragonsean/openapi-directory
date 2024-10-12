# UebermapsApiEndpoints.MapsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapsGet**](MapsApi.md#mapsGet) | **GET** /maps | List your own maps
[**mapsIdDelete**](MapsApi.md#mapsIdDelete) | **DELETE** /maps/{id} | Delete map
[**mapsIdGet**](MapsApi.md#mapsIdGet) | **GET** /maps/{id} | Get map
[**mapsIdPatch**](MapsApi.md#mapsIdPatch) | **PATCH** /maps/{id} | Update map
[**mapsPost**](MapsApi.md#mapsPost) | **POST** /maps | Create map
[**usersUserIdMapsGet**](MapsApi.md#usersUserIdMapsGet) | **GET** /users/{user_id}/maps | List maps for a given user



## mapsGet

> [Map] mapsGet()

List your own maps

List your own maps.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.MapsApi();
apiInstance.mapsGet((error, data, response) => {
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


## mapsIdDelete

> Map mapsIdDelete(id)

Delete map

Delete map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.MapsApi();
let id = 56; // Number | map id
apiInstance.mapsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| map id | 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsIdGet

> MapWithRelation mapsIdGet(id)

Get map

Get basic information about a map

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.MapsApi();
let id = 56; // Number | Id of map
apiInstance.mapsIdGet(id, (error, data, response) => {
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

### Return type

[**MapWithRelation**](MapWithRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsIdPatch

> Map mapsIdPatch(id, opts)

Update map

Update map. Wrap map parameters in [map]. To update the map header picture pass a base64 encoded string to [map][picture].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.MapsApi();
let id = 56; // Number | map id
let opts = {
  'map': new UebermapsApiEndpoints.MapEditable() // MapEditable | map settings attributes
};
apiInstance.mapsIdPatch(id, opts, (error, data, response) => {
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
 **id** | **Number**| map id | 
 **map** | [**MapEditable**](MapEditable.md)| map settings attributes | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mapsPost

> Map mapsPost(opts)

Create map

Create map. Wrap map parameters in [map]. To add a map header picture pass a base64 encoded string to [map][picture].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.MapsApi();
let opts = {
  'map': new UebermapsApiEndpoints.MapEditable() // MapEditable | map attributes
};
apiInstance.mapsPost(opts, (error, data, response) => {
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
 **map** | [**MapEditable**](MapEditable.md)| map attributes | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUserIdMapsGet

> [Map] usersUserIdMapsGet(userId)

List maps for a given user

List maps for a given user.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.MapsApi();
let userId = 56; // Number | Id of user
apiInstance.usersUserIdMapsGet(userId, (error, data, response) => {
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
 **userId** | **Number**| Id of user | 

### Return type

[**[Map]**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

