# SmartMe.RegisterForRealtimeApiApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registerForRealtimeApiDelete**](RegisterForRealtimeApiApi.md#registerForRealtimeApiDelete) | **DELETE** /api/RegisterForRealtimeApi/{id} | Deletes a realtime API registration.
[**registerForRealtimeApiGet**](RegisterForRealtimeApiApi.md#registerForRealtimeApiGet) | **GET** /api/RegisterForRealtimeApi | Gets all registrations for the Realtime API.
[**registerForRealtimeApiPost**](RegisterForRealtimeApiApi.md#registerForRealtimeApiPost) | **POST** /api/RegisterForRealtimeApi | Creates a new registration for the realtime API. The Realtime API sends you the data of the registred devices as soon as we have them on the cloud.               More Information about the realtime API: https://www.smart-me.com/Description/api/realtimeapi.aspx



## registerForRealtimeApiDelete

> registerForRealtimeApiDelete(id)

Deletes a realtime API registration.

Deletes a realtime API registration.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.RegisterForRealtimeApiApi();
let id = "id_example"; // String | The ID of the realtime API registration
apiInstance.registerForRealtimeApiDelete(id, (error, data, response) => {
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
 **id** | **String**| The ID of the realtime API registration | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## registerForRealtimeApiGet

> [RegisterRealtimeApiData] registerForRealtimeApiGet()

Gets all registrations for the Realtime API.

Gets all registrations for the Realtime API.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.RegisterForRealtimeApiApi();
apiInstance.registerForRealtimeApiGet((error, data, response) => {
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

[**[RegisterRealtimeApiData]**](RegisterRealtimeApiData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## registerForRealtimeApiPost

> registerForRealtimeApiPost(registerRealtimeApiData)

Creates a new registration for the realtime API. The Realtime API sends you the data of the registred devices as soon as we have them on the cloud.               More Information about the realtime API: https://www.smart-me.com/Description/api/realtimeapi.aspx

Creates a new registration for the realtime API. The Realtime API sends you the data of the registred devices as soon as we have them on the cloud. More Information about the realtime API: https://www.smart-me.com/Description/api/realtimeapi.aspx

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.RegisterForRealtimeApiApi();
let registerRealtimeApiData = new SmartMe.RegisterRealtimeApiData(); // RegisterRealtimeApiData | 
apiInstance.registerForRealtimeApiPost(registerRealtimeApiData, (error, data, response) => {
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
 **registerRealtimeApiData** | [**RegisterRealtimeApiData**](RegisterRealtimeApiData.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

