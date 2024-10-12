# SmartMe.PicoSettingsApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**picoSettingsGet**](PicoSettingsApi.md#picoSettingsGet) | **GET** /api/pico/settings/{id} | GET: api/pico/settings                            Returns the settings of a pico charging station.



## picoSettingsGet

> PicoSettingsDto picoSettingsGet(id)

GET: api/pico/settings                            Returns the settings of a pico charging station.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.PicoSettingsApi();
let id = "id_example"; // String | 
apiInstance.picoSettingsGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**PicoSettingsDto**](PicoSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

