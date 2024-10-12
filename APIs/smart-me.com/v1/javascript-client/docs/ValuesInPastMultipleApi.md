# SmartMe.ValuesInPastMultipleApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**valuesInPastMultipleGet**](ValuesInPastMultipleApi.md#valuesInPastMultipleGet) | **GET** /api/ValuesInPastMultiple/{id} | Gets multiple values of a device. This call needs a smart-me professional licence.



## valuesInPastMultipleGet

> [ValuesData] valuesInPastMultipleGet(id, startDate, endDate, interval)

Gets multiple values of a device. This call needs a smart-me professional licence.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.ValuesInPastMultipleApi();
let id = "id_example"; // String | The ID of the device
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The date when the first value should start
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The date when the last value should start
let interval = 56; // Number | The interval in minutes betwenn the values. 0 means as fast as possible. Only 1000 values can be get in one call.
apiInstance.valuesInPastMultipleGet(id, startDate, endDate, interval, (error, data, response) => {
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
 **id** | **String**| The ID of the device | 
 **startDate** | **Date**| The date when the first value should start | 
 **endDate** | **Date**| The date when the last value should start | 
 **interval** | **Number**| The interval in minutes betwenn the values. 0 means as fast as possible. Only 1000 values can be get in one call. | 

### Return type

[**[ValuesData]**](ValuesData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

