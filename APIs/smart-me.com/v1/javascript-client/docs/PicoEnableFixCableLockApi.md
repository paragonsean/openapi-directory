# SmartMe.PicoEnableFixCableLockApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**picoEnableFixCableLockPost**](PicoEnableFixCableLockApi.md#picoEnableFixCableLockPost) | **POST** /api/pico/tryenablecablelock/{id} | Try to fix lock the cable of a pico. The pico must be online and a cable (without car) needs to be connected. Otherwise this will fail.



## picoEnableFixCableLockPost

> Object picoEnableFixCableLockPost(id)

Try to fix lock the cable of a pico. The pico must be online and a cable (without car) needs to be connected. Otherwise this will fail.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.PicoEnableFixCableLockApi();
let id = "id_example"; // String | The ID of the pico
apiInstance.picoEnableFixCableLockPost(id, (error, data, response) => {
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
 **id** | **String**| The ID of the pico | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

