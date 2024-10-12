# InterzoidGetGlobalTimeApi.CurrentGlobalTimeApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getglobaltime**](CurrentGlobalTimeApi.md#getglobaltime) | **GET** /getglobaltime | Gets the current time for a global locale



## getglobaltime

> Getglobaltime200Response getglobaltime(license, locale)

Gets the current time for a global locale

Gets the current time for a global locale (city, state, region, or country such as Chicago, London, Paris, Seoul, Spain, Buenos Aires, Hawaii, Moscow, Tokyo, Hanoi, etc.)

### Example

```javascript
import InterzoidGetGlobalTimeApi from 'interzoid_get_global_time_api';

let apiInstance = new InterzoidGetGlobalTimeApi.CurrentGlobalTimeApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let locale = "locale_example"; // String | Geographic locale to get the current time for
apiInstance.getglobaltime(license, locale, (error, data, response) => {
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
 **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | 
 **locale** | **String**| Geographic locale to get the current time for | 

### Return type

[**Getglobaltime200Response**](Getglobaltime200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

