# MerakiDashboardApi.RecentApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceCameraAnalyticsRecent_2**](RecentApi.md#getDeviceCameraAnalyticsRecent_2) | **GET** /devices/{serial}/camera/analytics/recent | Returns most recent record for analytics zones



## getDeviceCameraAnalyticsRecent_2

> [Object] getDeviceCameraAnalyticsRecent_2(serial, opts)

Returns most recent record for analytics zones

Returns most recent record for analytics zones

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RecentApi();
let serial = "serial_example"; // String | 
let opts = {
  'objectType': "objectType_example" // String | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
};
apiInstance.getDeviceCameraAnalyticsRecent_2(serial, opts, (error, data, response) => {
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
 **serial** | **String**|  | 
 **objectType** | **String**| [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

