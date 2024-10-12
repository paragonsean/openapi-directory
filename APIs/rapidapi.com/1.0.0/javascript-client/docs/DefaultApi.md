# MoonApi.DefaultApi

All URIs are relative to *https://moon-phase.p.rapidapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAdvancedMoonPhaseData**](DefaultApi.md#getAdvancedMoonPhaseData) | **GET** /advanced | Get Advanced Moon Phase Data
[**getBasicMoonPhaseData**](DefaultApi.md#getBasicMoonPhaseData) | **GET** /basic | Get Basic Moon Phase Data
[**getEmojiOfMoonPhase**](DefaultApi.md#getEmojiOfMoonPhase) | **GET** /emoji | Get Emoji of Moon Phase
[**getLunarCalendar**](DefaultApi.md#getLunarCalendar) | **GET** /calendar | Get Lunar Calendar
[**getPlainTextMoonPhaseData**](DefaultApi.md#getPlainTextMoonPhaseData) | **GET** /plain-text | Get Plain Text Moon Phase Data



## getAdvancedMoonPhaseData

> GetAdvancedMoonPhaseData200Response getAdvancedMoonPhaseData(opts)

Get Advanced Moon Phase Data

Get Advanced Moon Phase Data

### Example

```javascript
import MoonApi from 'moon_api';

let apiInstance = new MoonApi.DefaultApi();
let opts = {
  'filters': "moon.phase_name,moon.stage,moon_phases.full_moon.next", // String | Filter data in the Advanced Moon API by specifying the desired fields using the `filters` parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details.
  'xRapidapiKey': "{{Rapidapi-Key}}" // String | 
};
apiInstance.getAdvancedMoonPhaseData(opts, (error, data, response) => {
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
 **filters** | **String**| Filter data in the Advanced Moon API by specifying the desired fields using the &#x60;filters&#x60; parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details. | [optional] 
 **xRapidapiKey** | **String**|  | [optional] 

### Return type

[**GetAdvancedMoonPhaseData200Response**](GetAdvancedMoonPhaseData200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBasicMoonPhaseData

> GetBasicMoonPhaseData200Response getBasicMoonPhaseData(opts)

Get Basic Moon Phase Data

Get Basic Moon Phase Data

### Example

```javascript
import MoonApi from 'moon_api';

let apiInstance = new MoonApi.DefaultApi();
let opts = {
  'xRapidapiKey': "{{Rapidapi-Key}}" // String | 
};
apiInstance.getBasicMoonPhaseData(opts, (error, data, response) => {
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
 **xRapidapiKey** | **String**|  | [optional] 

### Return type

[**GetBasicMoonPhaseData200Response**](GetBasicMoonPhaseData200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmojiOfMoonPhase

> getEmojiOfMoonPhase(opts)

Get Emoji of Moon Phase

Get Emoji of Moon Phase

### Example

```javascript
import MoonApi from 'moon_api';

let apiInstance = new MoonApi.DefaultApi();
let opts = {
  'xRapidapiKey': "{{Rapidapi-Key}}" // String | 
};
apiInstance.getEmojiOfMoonPhase(opts, (error, data, response) => {
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
 **xRapidapiKey** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getLunarCalendar

> getLunarCalendar(opts)

Get Lunar Calendar

Get Lunar Calendar

### Example

```javascript
import MoonApi from 'moon_api';

let apiInstance = new MoonApi.DefaultApi();
let opts = {
  'filters': "moon.phase_name,moon.stage,moon_phases.full_moon.next", // String | Filter data in the Advanced Moon API by specifying the desired fields using the `filters` parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details.
  'xRapidapiKey': "{{Rapidapi-Key}}" // String | 
};
apiInstance.getLunarCalendar(opts, (error, data, response) => {
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
 **filters** | **String**| Filter data in the Advanced Moon API by specifying the desired fields using the &#x60;filters&#x60; parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details. | [optional] 
 **xRapidapiKey** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getPlainTextMoonPhaseData

> getPlainTextMoonPhaseData(opts)

Get Plain Text Moon Phase Data

Get Plain Text Moon Phase Data

### Example

```javascript
import MoonApi from 'moon_api';

let apiInstance = new MoonApi.DefaultApi();
let opts = {
  'xRapidapiKey': "{{Rapidapi-Key}}" // String | 
};
apiInstance.getPlainTextMoonPhaseData(opts, (error, data, response) => {
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
 **xRapidapiKey** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

