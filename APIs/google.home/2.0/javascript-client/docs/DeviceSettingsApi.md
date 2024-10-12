# GoogleHome.DeviceSettingsApi

All URIs are relative to *http://example.com/setup*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nightModesettings**](DeviceSettingsApi.md#nightModesettings) | **POST** /assistant/set_night_mode_params | Night Mode settings
[**rebootandFactoryReset**](DeviceSettingsApi.md#rebootandFactoryReset) | **POST** /reboot | Reboot and Factory Reset
[**setEurekaInfo**](DeviceSettingsApi.md#setEurekaInfo) | **POST** /set_eureka_info | Set Eureka Info



## nightModesettings

> Example17 nightModesettings(nightModesettingsRequest)

Night Mode settings

This sets night mode options.   To view currently set values, use /setup/eureka_info.   If &#x60;enabled&#x60; is set to false, night mode is disabled and the other values do not matter.   &#x60;led_brightness&#x60; and &#x60;volume&#x60; refer to the maximum LED Brightness and Volume that is set during night mode.   &#x60;demo_to_user&#x60; is always set to &#x60;true&#x60; so change in values will be visible in realtime (like brightness).   &#x60;windows&#x60;: A combination of &#x60;length_hours&#x60; and &#x60;start_hour&#x60; is used to define start and end times for night mode. In this example, night mode starts at 10 PM (22) and ends at 6 AM (8 hours later). &#x60;windows.days&#x60; is an array of days of week when night mode will be enabled. Example: 0-&gt;Sunday, 1-&gt; Monday, ..., 6-&gt;Saturday.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.DeviceSettingsApi();
let nightModesettingsRequest = {"demo_to_user":true,"do_not_disturb":true,"enabled":false,"led_brightness":0.44999998807907104,"volume":0.46000000834465027,"windows":[{"days":[0,1,2,3,4,5,6],"length_hours":8,"start_hour":22}]}; // NightModesettingsRequest | 
apiInstance.nightModesettings(nightModesettingsRequest, (error, data, response) => {
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
 **nightModesettingsRequest** | [**NightModesettingsRequest**](NightModesettingsRequest.md)|  | 

### Return type

[**Example17**](Example17.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rebootandFactoryReset

> Object rebootandFactoryReset(rebootandFactoryResetRequest)

Reboot and Factory Reset

This can simply reboot the device (&#x60;params: \&quot;now\&quot;&#x60;) or factory reset the device (&#x60;params: \&quot;fdr\&quot;&#x60;).

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.DeviceSettingsApi();
let rebootandFactoryResetRequest = {"params":"now"}; // RebootandFactoryResetRequest | 
apiInstance.rebootandFactoryReset(rebootandFactoryResetRequest, (error, data, response) => {
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
 **rebootandFactoryResetRequest** | [**RebootandFactoryResetRequest**](RebootandFactoryResetRequest.md)|  | 

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## setEurekaInfo

> Object setEurekaInfo(setEurekaInfoRequest)

Set Eureka Info

This can set custom values to some options.  Only fields to be modified need to be sent, not all. The example has some modifiable fields.  TODO: List all modifiable fields.  Sending non-existant fields will still return a 200 OK, but they are not saved.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.DeviceSettingsApi();
let setEurekaInfoRequest = {"name":"Living Room","opt_in":{"opencast":true,"preview_channel":true,"remote_ducking":true,"stats":true},"settings":{"control_notifications":2}}; // SetEurekaInfoRequest | 
apiInstance.setEurekaInfo(setEurekaInfoRequest, (error, data, response) => {
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
 **setEurekaInfoRequest** | [**SetEurekaInfoRequest**](SetEurekaInfoRequest.md)|  | 

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain

