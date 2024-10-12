# Traccar.PositionsApi

All URIs are relative to *https://demo.traccar.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**positionsGet**](PositionsApi.md#positionsGet) | **GET** /positions | Fetches a list of Positions



## positionsGet

> [Position] positionsGet(opts)

Fetches a list of Positions

We strongly recommend using [Traccar WebSocket API](https://www.traccar.org/traccar-api/) instead of periodically polling positions endpoint. Without any params, it returns a list of last known positions for all the user&#39;s Devices. _from_ and _to_ fields are not required with _id_.

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.PositionsApi();
let opts = {
  'deviceId': 56, // Number | _deviceId_ is optional, but requires the _from_ and _to_ parameters when used
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
  'id': 56 // Number | To fetch one or more positions. Multiple params can be passed like `id=31&id=42`
};
apiInstance.positionsGet(opts, (error, data, response) => {
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
 **deviceId** | **Number**| _deviceId_ is optional, but requires the _from_ and _to_ parameters when used | [optional] 
 **from** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | [optional] 
 **to** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | [optional] 
 **id** | **Number**| To fetch one or more positions. Multiple params can be passed like &#x60;id&#x3D;31&amp;id&#x3D;42&#x60; | [optional] 

### Return type

[**[Position]**](Position.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/gpx+xml, application/json, text/csv

