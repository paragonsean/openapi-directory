# IxApi.ConnectionsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectionsList**](ConnectionsApi.md#connectionsList) | **GET** /connections | 
[**connectionsRead**](ConnectionsApi.md#connectionsRead) | **GET** /connections/{id} | 



## connectionsList

> [Connection] connectionsList(opts)



List all &#x60;connection&#x60;s.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.ConnectionsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'state': "state_example", // String | Filter by state
  'stateIsNot': "stateIsNot_example", // String | Filter by state__is_not
  'mode': "mode_example", // String | Filter by mode
  'modeIsNot': "modeIsNot_example", // String | Filter by mode__is_not
  'name': "name_example", // String | Filter by name
  'metroAreaNetwork': "metroAreaNetwork_example", // String | Filter by metro_area_network
  'pop': "pop_example", // String | Filter by pop
  'facility': "facility_example", // String | Filter by facility
  'externalRef': "externalRef_example" // String | Filter by external_ref
};
apiInstance.connectionsList(opts, (error, data, response) => {
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
 **mode** | **String**| Filter by mode | [optional] 
 **modeIsNot** | **String**| Filter by mode__is_not | [optional] 
 **name** | **String**| Filter by name | [optional] 
 **metroAreaNetwork** | **String**| Filter by metro_area_network | [optional] 
 **pop** | **String**| Filter by pop | [optional] 
 **facility** | **String**| Filter by facility | [optional] 
 **externalRef** | **String**| Filter by external_ref | [optional] 

### Return type

[**[Connection]**](Connection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionsRead

> Connection connectionsRead(id)



Read a &#x60;connection&#x60;.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.ConnectionsApi();
let id = "id_example"; // String | Get by id
apiInstance.connectionsRead(id, (error, data, response) => {
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

[**Connection**](Connection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

