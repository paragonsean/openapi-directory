# Traccar.DriversApi

All URIs are relative to *https://demo.traccar.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**driversGet**](DriversApi.md#driversGet) | **GET** /drivers | Fetch a list of Drivers
[**driversIdDelete**](DriversApi.md#driversIdDelete) | **DELETE** /drivers/{id} | Delete a Driver
[**driversIdPut**](DriversApi.md#driversIdPut) | **PUT** /drivers/{id} | Update a Driver
[**driversPost**](DriversApi.md#driversPost) | **POST** /drivers | Create a Driver



## driversGet

> [Driver] driversGet(opts)

Fetch a list of Drivers

Without params, it returns a list of Drivers the user has access to

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.DriversApi();
let opts = {
  'all': true, // Boolean | Can only be used by admins or managers to fetch all entities
  'userId': 56, // Number | Standard users can use this only with their own _userId_
  'deviceId': 56, // Number | Standard users can use this only with _deviceId_s, they have access to
  'groupId': 56, // Number | Standard users can use this only with _groupId_s, they have access to
  'refresh': true // Boolean | 
};
apiInstance.driversGet(opts, (error, data, response) => {
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
 **all** | **Boolean**| Can only be used by admins or managers to fetch all entities | [optional] 
 **userId** | **Number**| Standard users can use this only with their own _userId_ | [optional] 
 **deviceId** | **Number**| Standard users can use this only with _deviceId_s, they have access to | [optional] 
 **groupId** | **Number**| Standard users can use this only with _groupId_s, they have access to | [optional] 
 **refresh** | **Boolean**|  | [optional] 

### Return type

[**[Driver]**](Driver.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## driversIdDelete

> driversIdDelete(id)

Delete a Driver

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.DriversApi();
let id = 56; // Number | 
apiInstance.driversIdDelete(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## driversIdPut

> Driver driversIdPut(id, body)

Update a Driver

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.DriversApi();
let id = 56; // Number | 
let body = new Traccar.Driver(); // Driver | 
apiInstance.driversIdPut(id, body, (error, data, response) => {
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
 **id** | **Number**|  | 
 **body** | [**Driver**](Driver.md)|  | 

### Return type

[**Driver**](Driver.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driversPost

> Driver driversPost(body)

Create a Driver

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.DriversApi();
let body = new Traccar.Driver(); // Driver | 
apiInstance.driversPost(body, (error, data, response) => {
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
 **body** | [**Driver**](Driver.md)|  | 

### Return type

[**Driver**](Driver.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

