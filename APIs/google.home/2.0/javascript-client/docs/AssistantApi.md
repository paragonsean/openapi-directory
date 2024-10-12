# GoogleHome.AssistantApi

All URIs are relative to *http://example.com/setup*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accessibility**](AssistantApi.md#accessibility) | **POST** /assistant/a11y_mode | Accessibility
[**alarmVolume**](AssistantApi.md#alarmVolume) | **POST** /assistant/alarms/volume | Alarm Volume
[**deleteAlarmsandTimers**](AssistantApi.md#deleteAlarmsandTimers) | **POST** /assistant/alarms/delete | Delete Alarms and Timers
[**doNotDisturb**](AssistantApi.md#doNotDisturb) | **POST** /assistant/notifications | Do Not Disturb
[**getAlarmsandTimers**](AssistantApi.md#getAlarmsandTimers) | **GET** /assistant/alarms | Get Alarms and Timers
[**setEqualizerValues**](AssistantApi.md#setEqualizerValues) | **POST** /user_eq/set_equalizer | Set Equalizer Values



## accessibility

> Getcurrentvalues accessibility(accessibilityRequest)

Accessibility

This controls Accessibility sounds. &#x60;hotword_enabled&#x60; is for &#39;Play start sound&#39; and &#x60;endpoint_enabled&#x60; is for &#39;Play end sound&#39;.   Sending an empty-body POST request returns the current values.   Either of the fields or both can be sent and new values will be saved.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.AssistantApi();
let accessibilityRequest = {"endpoint_enabled":false,"hotword_enabled":false}; // AccessibilityRequest | 
apiInstance.accessibility(accessibilityRequest, (error, data, response) => {
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
 **accessibilityRequest** | [**AccessibilityRequest**](AccessibilityRequest.md)|  | 

### Return type

[**Getcurrentvalues**](Getcurrentvalues.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## alarmVolume

> Getvolume alarmVolume(alarmVolumeRequest)

Alarm Volume

This gets and sets alarms and timers volume.   **Note:** This is not the same as normal volume.  Volume is a float number in [0, 1] where 0 is minimum and 1 is maximum.   Sending an empty body gets the volume. Sending &#x60;volume&#x60; sets the volume.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.AssistantApi();
let alarmVolumeRequest = {"volume":1}; // AlarmVolumeRequest | 
apiInstance.alarmVolume(alarmVolumeRequest, (error, data, response) => {
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
 **alarmVolumeRequest** | [**AlarmVolumeRequest**](AlarmVolumeRequest.md)|  | 

### Return type

[**Getvolume**](Getvolume.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAlarmsandTimers

> Example19 deleteAlarmsandTimers(deleteAlarmsandTimersRequest)

Delete Alarms and Timers

This deletes alarms and timers by their id.  &#x60;ids&#x60; is a list of ids to be deleted. Sending invalid id still returns a 200 OK. The &#x60;/&#x60; in the ids have to be escaped like &#x60;/&#x60;.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.AssistantApi();
let deleteAlarmsandTimersRequest = {"ids":["timer/xxx","alarm/xxx"]}; // DeleteAlarmsandTimersRequest | 
apiInstance.deleteAlarmsandTimers(deleteAlarmsandTimersRequest, (error, data, response) => {
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
 **deleteAlarmsandTimersRequest** | [**DeleteAlarmsandTimersRequest**](DeleteAlarmsandTimersRequest.md)|  | 

### Return type

[**Example19**](Example19.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## doNotDisturb

> Getcurrentstate doNotDisturb(contentType)

Do Not Disturb

This is for the Do Not Disturb option. Sending an empty-body POST returns the current value. Sending a new value changes it.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.AssistantApi();
let contentType = "application/json"; // String | 
apiInstance.doNotDisturb(contentType, (error, data, response) => {
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
 **contentType** | **String**|  | 

### Return type

[**Getcurrentstate**](Getcurrentstate.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAlarmsandTimers

> Example18 getAlarmsandTimers()

Get Alarms and Timers

This gives a list of all active alarms and timers.  Both alarms and timers have &#x60;id&#x60;s which can be used to delete them. (There is no known way of creating/deleting yet). The value of &#x60;status&#x60; have different meanings for alarms and timers (given below).  Alarms have &#x60;date_pattern&#x60; and &#x60;time_pattern&#x60; with day, month, year, hour, minute, second. &#x60;fire_time&#x60; is the same in unix time (milliseconds, not seconds).   &#x60;status&#x60; is 1 for set up and 2 for ringing.  Timers have &#x60;original_duration&#x60; is the original duration.   &#x60;status&#x60; is 1 for set up and 3 for ringing.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.AssistantApi();
apiInstance.getAlarmsandTimers((error, data, response) => {
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

[**Example18**](Example18.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setEqualizerValues

> Object setEqualizerValues(setEqualizerValuesRequest)

Set Equalizer Values

This can only set new equalizer values. To get already set values, use /setup/eureka_info.  The body is mandatory. It can either contain &#x60;low_shelf&#x60; or &#x60;high_shelf&#x60; or both.  &#x60;low_shelf.gain_db&#x60; and &#x60;high_shelf.gain_db&#x60; refer to **bass** and **treble** respectively.  Default values are 0 for both.   While the slider in the Home app only ranges from -6 to +6, they can be set to any integer like 50 or -100. These changes persist.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.AssistantApi();
let setEqualizerValuesRequest = {"high_shelf":{"gain_db":0},"low_shelf":{"gain_db":0}}; // SetEqualizerValuesRequest | 
apiInstance.setEqualizerValues(setEqualizerValuesRequest, (error, data, response) => {
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
 **setEqualizerValuesRequest** | [**SetEqualizerValuesRequest**](SetEqualizerValuesRequest.md)|  | 

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain

