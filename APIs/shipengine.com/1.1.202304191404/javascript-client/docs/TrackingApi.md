# ShipEngineApi.TrackingApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTrackingLog**](TrackingApi.md#getTrackingLog) | **GET** /v1/tracking | Get Tracking Information
[**startTracking**](TrackingApi.md#startTracking) | **POST** /v1/tracking/start | Start Tracking a Package
[**stopTracking**](TrackingApi.md#stopTracking) | **POST** /v1/tracking/stop | Stop Tracking a Package



## getTrackingLog

> GetTrackingLogResponseBody getTrackingLog(opts)

Get Tracking Information

Retrieve package tracking information

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.TrackingApi();
let opts = {
  'carrierCode': "stamps_com", // String | Carrier code used to retrieve tracking information
  'trackingNumber': "9405511899223197428490" // String | The tracking number associated with a shipment
};
apiInstance.getTrackingLog(opts, (error, data, response) => {
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
 **carrierCode** | **String**| Carrier code used to retrieve tracking information | [optional] 
 **trackingNumber** | **String**| The tracking number associated with a shipment | [optional] 

### Return type

[**GetTrackingLogResponseBody**](GetTrackingLogResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startTracking

> String startTracking(opts)

Start Tracking a Package

Allows you to subscribe to tracking updates for a package. You specify the carrier_code and tracking_number of the package, and receive notifications via webhooks whenever the shipping status changes. 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.TrackingApi();
let opts = {
  'carrierCode': "stamps_com", // String | Carrier code used to retrieve tracking information
  'trackingNumber': "9405511899223197428490" // String | The tracking number associated with a shipment
};
apiInstance.startTracking(opts, (error, data, response) => {
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
 **carrierCode** | **String**| Carrier code used to retrieve tracking information | [optional] 
 **trackingNumber** | **String**| The tracking number associated with a shipment | [optional] 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## stopTracking

> String stopTracking(opts)

Stop Tracking a Package

Unsubscribe from tracking updates for a package.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.TrackingApi();
let opts = {
  'carrierCode': "stamps_com", // String | Carrier code used to retrieve tracking information
  'trackingNumber': "9405511899223197428490" // String | The tracking number associated with a shipment
};
apiInstance.stopTracking(opts, (error, data, response) => {
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
 **carrierCode** | **String**| Carrier code used to retrieve tracking information | [optional] 
 **trackingNumber** | **String**| The tracking number associated with a shipment | [optional] 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

