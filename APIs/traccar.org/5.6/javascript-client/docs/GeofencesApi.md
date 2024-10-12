# Traccar.GeofencesApi

All URIs are relative to *https://demo.traccar.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geofencesGet**](GeofencesApi.md#geofencesGet) | **GET** /geofences | Fetch a list of Geofences
[**geofencesIdDelete**](GeofencesApi.md#geofencesIdDelete) | **DELETE** /geofences/{id} | Delete a Geofence
[**geofencesIdPut**](GeofencesApi.md#geofencesIdPut) | **PUT** /geofences/{id} | Update a Geofence
[**geofencesPost**](GeofencesApi.md#geofencesPost) | **POST** /geofences | Create a Geofence



## geofencesGet

> [Geofence] geofencesGet(opts)

Fetch a list of Geofences

Without params, it returns a list of Geofences the user has access to

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.GeofencesApi();
let opts = {
  'all': true, // Boolean | Can only be used by admins or managers to fetch all entities
  'userId': 56, // Number | Standard users can use this only with their own _userId_
  'deviceId': 56, // Number | Standard users can use this only with _deviceId_s, they have access to
  'groupId': 56, // Number | Standard users can use this only with _groupId_s, they have access to
  'refresh': true // Boolean | 
};
apiInstance.geofencesGet(opts, (error, data, response) => {
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

[**[Geofence]**](Geofence.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## geofencesIdDelete

> geofencesIdDelete(id)

Delete a Geofence

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.GeofencesApi();
let id = 56; // Number | 
apiInstance.geofencesIdDelete(id, (error, data, response) => {
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


## geofencesIdPut

> Geofence geofencesIdPut(id, body)

Update a Geofence

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.GeofencesApi();
let id = 56; // Number | 
let body = new Traccar.Geofence(); // Geofence | 
apiInstance.geofencesIdPut(id, body, (error, data, response) => {
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
 **body** | [**Geofence**](Geofence.md)|  | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## geofencesPost

> Geofence geofencesPost(body)

Create a Geofence

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.GeofencesApi();
let body = new Traccar.Geofence(); // Geofence | 
apiInstance.geofencesPost(body, (error, data, response) => {
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
 **body** | [**Geofence**](Geofence.md)|  | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

