# SolarVps.PodsApi

All URIs are relative to *http://api.ss.solarvps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**podsGet**](PodsApi.md#podsGet) | **GET** /pods | View all your pods
[**podsPodIdActionGet**](PodsApi.md#podsPodIdActionGet) | **GET** /pods/{podId}/{action} | Perform action on a specific pod
[**podsPodIdGet**](PodsApi.md#podsPodIdGet) | **GET** /pods/{podId} | View information on a specific pod
[**podsPodIdPingGet**](PodsApi.md#podsPodIdPingGet) | **GET** /pods/{podId}/ping | Ping your specified pod



## podsGet

> podsGet()

View all your pods

Shows all your pods

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.PodsApi();
apiInstance.podsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## podsPodIdActionGet

> podsPodIdActionGet(podId, action)

Perform action on a specific pod

Allowed actions are reboot, shutdown, boot

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.PodsApi();
let podId = 3.4; // Number | Id of the pod you want to perform actions on
let action = "action_example"; // String | Action to perform on selected pod
apiInstance.podsPodIdActionGet(podId, action, (error, data, response) => {
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
 **podId** | **Number**| Id of the pod you want to perform actions on | 
 **action** | **String**| Action to perform on selected pod | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## podsPodIdGet

> podsPodIdGet(podId)

View information on a specific pod

Shows details of a specific pod. Enter 1 below to see an example

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.PodsApi();
let podId = 3.4; // Number | Id of the pod you want to perform actions on
apiInstance.podsPodIdGet(podId, (error, data, response) => {
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
 **podId** | **Number**| Id of the pod you want to perform actions on | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## podsPodIdPingGet

> podsPodIdPingGet(podId)

Ping your specified pod

Returns the ping response from your server.

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.PodsApi();
let podId = 3.4; // Number | Id of the pod you want to ping check
apiInstance.podsPodIdPingGet(podId, (error, data, response) => {
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
 **podId** | **Number**| Id of the pod you want to ping check | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

