# SmartMe.PicoApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**picoGet**](PicoApi.md#picoGet) | **GET** /api/pico | Gets all pico charging stations for this user



## picoGet

> [Device] picoGet()

Gets all pico charging stations for this user

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.PicoApi();
apiInstance.picoGet((error, data, response) => {
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

[**[Device]**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

