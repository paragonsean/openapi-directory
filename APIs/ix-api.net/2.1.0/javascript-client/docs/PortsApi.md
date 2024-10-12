# IxApi.PortsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portsList**](PortsApi.md#portsList) | **GET** /ports | 
[**portsRead**](PortsApi.md#portsRead) | **GET** /ports/{id} | 



## portsList

> [Port] portsList(opts)



List all ports.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.PortsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'state': "state_example", // String | Filter by state
  'stateIsNot': "stateIsNot_example", // String | Filter by state__is_not
  'mediaType': "mediaType_example", // String | Filter by media_type
  'pop': "pop_example", // String | Filter by pop
  'name': "name_example", // String | Filter by name
  'externalRef': "externalRef_example", // String | Filter by external_ref
  'device': "device_example", // String | Filter by device
  'speed': "speed_example", // String | Filter by speed
  'connection': "connection_example" // String | Filter by connection
};
apiInstance.portsList(opts, (error, data, response) => {
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
 **state** | **String**| Filter by state | [optional] 
 **stateIsNot** | **String**| Filter by state__is_not | [optional] 
 **mediaType** | **String**| Filter by media_type | [optional] 
 **pop** | **String**| Filter by pop | [optional] 
 **name** | **String**| Filter by name | [optional] 
 **externalRef** | **String**| Filter by external_ref | [optional] 
 **device** | **String**| Filter by device | [optional] 
 **speed** | **String**| Filter by speed | [optional] 
 **connection** | **String**| Filter by connection | [optional] 

### Return type

[**[Port]**](Port.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## portsRead

> Port portsRead(id)



Retrieve a port.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.PortsApi();
let id = "id_example"; // String | Get by id
apiInstance.portsRead(id, (error, data, response) => {
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

[**Port**](Port.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

