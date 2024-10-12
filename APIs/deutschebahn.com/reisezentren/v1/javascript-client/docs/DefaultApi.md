# ReisezentrenApi.DefaultApi

All URIs are relative to *https://api.deutschebahn.com/reisezentren/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reisezentrenGet**](DefaultApi.md#reisezentrenGet) | **GET** /reisezentren | Get all station infos
[**reisezentrenIdGet**](DefaultApi.md#reisezentrenIdGet) | **GET** /reisezentren/{id} | Get information about a specific station
[**reisezentrenLocLatLonDistGet**](DefaultApi.md#reisezentrenLocLatLonDistGet) | **GET** /reisezentren/loc/{lat}/{lon}/{dist} | Get stations in a given radius
[**reisezentrenLocLatLonGet**](DefaultApi.md#reisezentrenLocLatLonGet) | **GET** /reisezentren/loc/{lat}/{lon} | Get information about a station near a location



## reisezentrenGet

> [TravelCenter] reisezentrenGet(opts)

Get all station infos

Get all station infos

### Example

```javascript
import ReisezentrenApi from 'reisezentren_api';

let apiInstance = new ReisezentrenApi.DefaultApi();
let opts = {
  'name': "name_example" // String | A station name or part of it
};
apiInstance.reisezentrenGet(opts, (error, data, response) => {
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
 **name** | **String**| A station name or part of it | [optional] 

### Return type

[**[TravelCenter]**](TravelCenter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reisezentrenIdGet

> TravelCenter reisezentrenIdGet(id)

Get information about a specific station

Get information about a specific station

### Example

```javascript
import ReisezentrenApi from 'reisezentren_api';

let apiInstance = new ReisezentrenApi.DefaultApi();
let id = "id_example"; // String | Station id
apiInstance.reisezentrenIdGet(id, (error, data, response) => {
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
 **id** | **String**| Station id | 

### Return type

[**TravelCenter**](TravelCenter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## reisezentrenLocLatLonDistGet

> TravelCenter reisezentrenLocLatLonDistGet(lat, lon, dist)

Get stations in a given radius

Get stations in a given radius

### Example

```javascript
import ReisezentrenApi from 'reisezentren_api';

let apiInstance = new ReisezentrenApi.DefaultApi();
let lat = 3.4; // Number | Latitude
let lon = 3.4; // Number | Longitude
let dist = 3.4; // Number | Radius
apiInstance.reisezentrenLocLatLonDistGet(lat, lon, dist, (error, data, response) => {
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
 **lat** | **Number**| Latitude | 
 **lon** | **Number**| Longitude | 
 **dist** | **Number**| Radius | 

### Return type

[**TravelCenter**](TravelCenter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reisezentrenLocLatLonGet

> TravelCenter reisezentrenLocLatLonGet(lat, lon)

Get information about a station near a location

Get information about a station near a location

### Example

```javascript
import ReisezentrenApi from 'reisezentren_api';

let apiInstance = new ReisezentrenApi.DefaultApi();
let lat = 3.4; // Number | Latitude
let lon = 3.4; // Number | Longitude
apiInstance.reisezentrenLocLatLonGet(lat, lon, (error, data, response) => {
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
 **lat** | **Number**| Latitude | 
 **lon** | **Number**| Longitude | 

### Return type

[**TravelCenter**](TravelCenter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

