# SmartMe.MeterValuesApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meterValuesGet**](MeterValuesApi.md#meterValuesGet) | **GET** /api/MeterValues/{id} | Gets the Values for a Meter at a given Date.               The first Value found before the given Date is returned.



## meterValuesGet

> DeviceInPast meterValuesGet(id, date)

Gets the Values for a Meter at a given Date.               The first Value found before the given Date is returned.

Gets the Values for a Meter at a given Date. The first Value found before the given Date is returned.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.MeterValuesApi();
let id = "id_example"; // String | 
let date = new Date("2013-10-20T19:20:30+01:00"); // Date | 
apiInstance.meterValuesGet(id, date, (error, data, response) => {
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
 **date** | **Date**|  | 

### Return type

[**DeviceInPast**](DeviceInPast.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

