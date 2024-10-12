# RubrikRestApi.BlackoutWindowApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBlackoutWindowStatus**](BlackoutWindowApi.md#getBlackoutWindowStatus) | **GET** /blackout_window | Get current status of global blackout window
[**toggleBlackoutWindow**](BlackoutWindowApi.md#toggleBlackoutWindow) | **PATCH** /blackout_window | Starts or stops the global blackout window in local Rubrik cluster



## getBlackoutWindowStatus

> GlobalBlackoutWindowStatus getBlackoutWindowStatus()

Get current status of global blackout window

Determine whether global blackout window is currently active.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.BlackoutWindowApi();
apiInstance.getBlackoutWindowStatus((error, data, response) => {
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

[**GlobalBlackoutWindowStatus**](GlobalBlackoutWindowStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## toggleBlackoutWindow

> GlobalBlackoutWindowStatus toggleBlackoutWindow(globalBlackoutWindowStatus)

Starts or stops the global blackout window in local Rubrik cluster

Returns whether or not the system is in a blackout window.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.BlackoutWindowApi();
let globalBlackoutWindowStatus = new RubrikRestApi.GlobalBlackoutWindowStatus(); // GlobalBlackoutWindowStatus | Whether to start or stop the global blackout window.
apiInstance.toggleBlackoutWindow(globalBlackoutWindowStatus, (error, data, response) => {
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
 **globalBlackoutWindowStatus** | [**GlobalBlackoutWindowStatus**](GlobalBlackoutWindowStatus.md)| Whether to start or stop the global blackout window. | 

### Return type

[**GlobalBlackoutWindowStatus**](GlobalBlackoutWindowStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

