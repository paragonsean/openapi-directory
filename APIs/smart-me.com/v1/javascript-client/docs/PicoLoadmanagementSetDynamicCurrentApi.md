# SmartMe.PicoLoadmanagementSetDynamicCurrentApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**picoLoadmanagementSetDynamicCurrentPost**](PicoLoadmanagementSetDynamicCurrentApi.md#picoLoadmanagementSetDynamicCurrentPost) | **POST** /api/pico/loadmanagementgroup/current/{serial} | Sets the dynamic current of a load management group or a single station.



## picoLoadmanagementSetDynamicCurrentPost

> Object picoLoadmanagementSetDynamicCurrentPost(serial, current)

Sets the dynamic current of a load management group or a single station.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.PicoLoadmanagementSetDynamicCurrentApi();
let serial = 789; // Number | The serial number can be any pico serial in the group (e.g. 700001)
let current = 56; // Number | The dynamic current of the group (in mA)
apiInstance.picoLoadmanagementSetDynamicCurrentPost(serial, current, (error, data, response) => {
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
 **serial** | **Number**| The serial number can be any pico serial in the group (e.g. 700001) | 
 **current** | **Number**| The dynamic current of the group (in mA) | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

