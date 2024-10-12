# CloudRfApi.CreateApi

All URIs are relative to *https://api.cloudrf.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**area**](CreateApi.md#area) | **POST** /area | Create a point-to-multipoint heatmap
[**path**](CreateApi.md#path) | **POST** /path | Point-to-point path profile analysis (Tx to Rx)
[**points**](CreateApi.md#points) | **POST** /points | Point-to-multipoint path profile analysis (Many Tx, one Rx)



## area

> area(areaRequest)

Create a point-to-multipoint heatmap

An area coverage assumes the same receiver height at all locations out to fixed radius (maximum 300km). Due to it&#39;s exhaustive processing it is the slowest of all the API calls. Speed can be improved significantly by adjusting the resolution &#39;res&#39; parameter. A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.CreateApi();
let areaRequest = new CloudRfApi.AreaRequest(); // AreaRequest | A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy.
apiInstance.area(areaRequest, (error, data, response) => {
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
 **areaRequest** | [**AreaRequest**](AreaRequest.md)| A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy. | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## path

> path(pathRequest)

Point-to-point path profile analysis (Tx to Rx)

A path profile is a single link from A to B. It is much faster than an area calculation and can be used out to 300km. A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.CreateApi();
let pathRequest = new CloudRfApi.PathRequest(); // PathRequest | A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy.
apiInstance.path(pathRequest, (error, data, response) => {
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
 **pathRequest** | [**PathRequest**](PathRequest.md)| A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy. | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## points

> points(pointsRequest)

Point-to-multipoint path profile analysis (Many Tx, one Rx)

The points function tests many transmitters and one receiver and is designed for route analysis. A minimal request needs a transmitters array of (latitude,longitude,altitude) locations, antenna, receiver and output objects defined as a minimum. Model and environment options will enhance accuracy.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.CreateApi();
let pointsRequest = new CloudRfApi.PointsRequest(); // PointsRequest | A minimal request needs a transmitters array of (latitude,longitude,altitude) locations, antenna, receiver and output objects defined as a minimum. Model and environment options will enhance accuracy.
apiInstance.points(pointsRequest, (error, data, response) => {
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
 **pointsRequest** | [**PointsRequest**](PointsRequest.md)| A minimal request needs a transmitters array of (latitude,longitude,altitude) locations, antenna, receiver and output objects defined as a minimum. Model and environment options will enhance accuracy. | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

