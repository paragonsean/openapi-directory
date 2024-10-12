# BungieNetApi.DefaultApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAvailableLocales**](DefaultApi.md#getAvailableLocales) | **GET** /GetAvailableLocales/ | 
[**getCommonSettings**](DefaultApi.md#getCommonSettings) | **GET** /Settings/ | 
[**getGlobalAlerts**](DefaultApi.md#getGlobalAlerts) | **GET** /GlobalAlerts/ | 
[**getUserSystemOverrides**](DefaultApi.md#getUserSystemOverrides) | **GET** /UserSystemOverrides/ | 



## getAvailableLocales

> GetAvailableLocales200Response getAvailableLocales()



List of available localization cultures

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.DefaultApi();
apiInstance.getAvailableLocales((error, data, response) => {
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

[**GetAvailableLocales200Response**](GetAvailableLocales200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getCommonSettings

> GetCommonSettings200Response getCommonSettings()



Get the common settings used by the Bungie.Net environment.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.DefaultApi();
apiInstance.getCommonSettings((error, data, response) => {
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

[**GetCommonSettings200Response**](GetCommonSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGlobalAlerts

> GetGlobalAlerts200Response getGlobalAlerts(opts)



Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.DefaultApi();
let opts = {
  'includestreaming': true // Boolean | Determines whether Streaming Alerts are included in results
};
apiInstance.getGlobalAlerts(opts, (error, data, response) => {
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
 **includestreaming** | **Boolean**| Determines whether Streaming Alerts are included in results | [optional] 

### Return type

[**GetGlobalAlerts200Response**](GetGlobalAlerts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getUserSystemOverrides

> GetUserSystemOverrides200Response getUserSystemOverrides()



Get the user-specific system overrides that should be respected alongside common systems.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.DefaultApi();
apiInstance.getUserSystemOverrides((error, data, response) => {
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

[**GetUserSystemOverrides200Response**](GetUserSystemOverrides200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

