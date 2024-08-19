# IxApi.PopsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**popsList**](PopsApi.md#popsList) | **GET** /pops | 
[**popsRead**](PopsApi.md#popsRead) | **GET** /pops/{id} | 



## popsList

> [PointOfPresence] popsList(opts)



List all PoPs

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.PopsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'facility': "facility_example", // String | Filter by facility
  'metroAreaNetwork': "metroAreaNetwork_example", // String | Filter by metro_area_network
  'capabilityMediaType': "capabilityMediaType_example", // String | Filter by capability_media_type
  'capabilitySpeed': 56, // Number | Filter by capability_speed
  'capabilitySpeedLt': 56, // Number | Filter by capability_speed__lt
  'capabilitySpeedLte': 56, // Number | Filter by capability_speed__lte
  'capabilitySpeedGt': 56, // Number | Filter by capability_speed__gt
  'capabilitySpeedGte': 56 // Number | Filter by capability_speed__gte
};
apiInstance.popsList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **facility** | **String**| Filter by facility | [optional] 
 **metroAreaNetwork** | **String**| Filter by metro_area_network | [optional] 
 **capabilityMediaType** | **String**| Filter by capability_media_type | [optional] 
 **capabilitySpeed** | **Number**| Filter by capability_speed | [optional] 
 **capabilitySpeedLt** | **Number**| Filter by capability_speed__lt | [optional] 
 **capabilitySpeedLte** | **Number**| Filter by capability_speed__lte | [optional] 
 **capabilitySpeedGt** | **Number**| Filter by capability_speed__gt | [optional] 
 **capabilitySpeedGte** | **Number**| Filter by capability_speed__gte | [optional] 

### Return type

[**[PointOfPresence]**](PointOfPresence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## popsRead

> PointOfPresence popsRead(id)



Get a single point of presence

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.PopsApi();
let id = "id_example"; // String | Get by id
apiInstance.popsRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**PointOfPresence**](PointOfPresence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

