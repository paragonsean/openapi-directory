# IxApi.DevicesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicesList**](DevicesApi.md#devicesList) | **GET** /devices | 
[**devicesRead**](DevicesApi.md#devicesRead) | **GET** /devices/{id} | 



## devicesList

> [Device] devicesList(opts)



List available devices

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.DevicesApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'name': "name_example", // String | Filter by name
  'capabilityMediaType': "capabilityMediaType_example", // String | Filter by capability_media_type
  'capabilitySpeed': 56, // Number | Filter by capability_speed
  'capabilitySpeedLt': 56, // Number | Filter by capability_speed__lt
  'capabilitySpeedLte': 56, // Number | Filter by capability_speed__lte
  'capabilitySpeedGt': 56, // Number | Filter by capability_speed__gt
  'capabilitySpeedGte': 56, // Number | Filter by capability_speed__gte
  'facility': "facility_example", // String | Filter by facility
  'pop': "pop_example", // String | Filter by pop
  'metroAreaNetwork': "metroAreaNetwork_example" // String | Filter by metro_area_network
};
apiInstance.devicesList(opts, (error, data, response) => {
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
 **name** | **String**| Filter by name | [optional] 
 **capabilityMediaType** | **String**| Filter by capability_media_type | [optional] 
 **capabilitySpeed** | **Number**| Filter by capability_speed | [optional] 
 **capabilitySpeedLt** | **Number**| Filter by capability_speed__lt | [optional] 
 **capabilitySpeedLte** | **Number**| Filter by capability_speed__lte | [optional] 
 **capabilitySpeedGt** | **Number**| Filter by capability_speed__gt | [optional] 
 **capabilitySpeedGte** | **Number**| Filter by capability_speed__gte | [optional] 
 **facility** | **String**| Filter by facility | [optional] 
 **pop** | **String**| Filter by pop | [optional] 
 **metroAreaNetwork** | **String**| Filter by metro_area_network | [optional] 

### Return type

[**[Device]**](Device.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesRead

> Device devicesRead(id)



Get a specific device identified by id

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.DevicesApi();
let id = "id_example"; // String | Get by id
apiInstance.devicesRead(id, (error, data, response) => {
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

[**Device**](Device.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

